# Findings: researcher_ux Platform Improvement Research

**Research Question:** How can the researcher_ux UX research skills platform be improved in algorithms, workflow automation, quality, and capability gaps?

**Status:** 11 hypotheses shipped (H1-H11). Active — new hypotheses forming from outer loop.

**Last Updated:** 2026-04-27

---

## Current Understanding

### What the Platform Does Well

The core pipeline (empathy map → user journey → persona → JTBD → AI opportunities) is **production-grade and validated**. Evidence:
- 104 empathy maps processed across 9 Clarivate product domains
- 400+ markdown deliverables created
- Time savings of 85-95% vs. manual research (4-6 weeks → 1-2 days)
- Full traceability: every insight linked to source quotes
- Validated methodology: Nielsen Norman Group + Clayton Christensen JTBD

### What is Broken or Missing

**Critical gaps (impact: HIGH):**

1. **Scenario mapping output gap** — 80-90% confirmed by H2 audit (13 files / ~45 expected). /research-pipeline skill addresses this.
2. **Pain-point matrix** — fixed via auto-discovery mode (H7 shipped)
3. **Cross-interview analysis** — addressed by semantic clustering (H1) + synthesizer (H5) + clustering skill (H9)
4. **Figma visual deliverables** — 35+ journey maps lack visual counterparts. journey-figma-creator skill exists and is hardened (H6 shipped). Generating the 35+ maps is execution work, not research.

**Resolved opportunities:**

5. **Confidence propagation** — pain-modulated weighting now algorithmic (H4 result)
6. **Pipeline automation** — /research-pipeline SKILL.md detects gaps and runs missing steps in sequence (H2 shipped)
7. **Cross-domain AI roadmap** — 3 platform capabilities identified from cluster-aware scoring (H8 shipped)

**Resolved — hardening complete:**

8. **Figma node ID staleness** — Code audit (H6) confirms fix is complete: single-execution architectural pattern enforced in SKILL.md, LESSONS_LEARNED.md, and implementation.js. 3 documentation gaps closed: Task tool prompt now references QUICK_REFERENCE.md + gold standard JS; screenshot width table added to execution steps; Template Mode gets staleness warning.

**Remaining (deliberate descope):**

9. **Prompt optimization via DSPy** — 400+ empathy maps as training signal. Skipped: H3 analysis shows CV=69% is prompt-driven but the 3 targeted text improvements already close the gap without DSPy's engineering investment.

---

## Patterns and Insights

### Pattern 1: The "Outer Loop" is the Missing Layer [UNCHANGED]
The platform does the per-interview inner loop excellently but lacks the cross-interview synthesis outer loop. Every HIGH-impact improvement is an outer loop problem. **Now being addressed by H1 + H5 + H8 + H9.**

### Pattern 2: Pain Signals are Universal Across Clarivate Products [NEW — H1 RESULT]

**The strongest finding from H1:** 11 of 14 emotional pain clusters span 5+ of 9 product domains. User emotional experiences are MORE SIMILAR across Clarivate products than different. This was invisible at per-project scope.

The 11 universal clusters:
1. **AI Opportunity-Threat Ambivalence** (n=162, 7/9 products) — users excited about AI AND anxious about displacement
2. **Expert Achievement Satisfaction** (n=72, 8/9 products) — the emotional target state when work succeeds
3. **Methodological Confidence in Triangulation** (n=57, 8/9 products) — trusts their own process when rigorous
4. **Vendor Commercial Friction** (n=23, 7/9 products) — frustrated by pricing, hopeful for innovation
5. **Strategic Isolation & Disruption Anxiety** (n=37, 7/9 products) — anxious about CI function isolation, AI displacement
6. **Constant Urgency Pressure** (n=20, 7/9 products) — "deliver everything yesterday" organizational culture
7. **Tool Navigation Friction** (n=17, 7/9 products) — frustrated by navigation lag, slow tools
8. **Process Verification Anxiety** (n=15, 6/9 products) — concerned about manual verification steps
9. **Data Fragmentation Fatigue** (n=26, 7/9 products) — manually piecing data from multiple sources
10. **Manual Correction Burden at Scale** (n=69, 8/9 products) — correcting data across 60-80 markets
11. **Vendor Partnership Dependency** (n=22, 5/9 products) — collaborative but vulnerable to deprecation

**Platform implication:** These 11 clusters ARE the Clarivate user emotional taxonomy. Any AI feature addressing Clusters 9+12+13 (data fragmentation/correction) or Cluster 0 (AI ambivalence) addresses universal platform pain.

### Pattern 4 (NEW — H8 RESULT): Per-Product AI Roadmaps Systematically Undervalue Platform Investments

**H8 applied H1 cluster taxonomy as cross-domain weights to 24 AI opportunities** across 8 products. Result: 22 of 24 re-ranked; 4 demoted to P3. The ceiling effect (20 opportunities all score 10.0) is the finding: when you account for cross-domain universality, almost every P1 touching a universal cluster (6+ products) deserves P0 consideration.

**The 3 platform capability themes that emerge:**

1. **Data Synthesis & Reconciliation** (8/9 products, Clusters 12+13) — Cross-source entity resolution, fuzzy matching, variance detection. Every product independently building this. Should be platform infrastructure with per-product adapters. MVP: PT's Fuzzy-Match Entity Resolver as shared service.

2. **Trust / Retrieval-First AI Infrastructure** (7-8/9 products, Clusters 0+2+7) — Source citation, methodology provenance, hallucination prevention. Per-product RAG builds are duplicated effort. Should be a shared RAG framework that all AI features run on top of. MVP: PT's Retrieval-First AI Architecture as platform-wide standard.

3. **NL Workflow Automation** (7/9 products, Clusters 5+6+13) — Natural language query → synthesized report. Reduces 60-90 min workflows to 5-10 min universally. MVP: MASS's NL Query Interface generalized as platform capability.

**The 4 demoted items** (Multi-Parameter Candidate Screening, Literature Summarization, Chemistry-Biology AI, Evidence Change Alerting) are product-specific investments that should NOT receive shared platform resources.

**Strategic implication:** The AI roadmap should be organized by H1 cluster, not by product. Products that share the same universal pain cluster should co-invest in a shared capability rather than each building their own.

### Pattern 7: Quote Starvation Cascades Through Synthesis Skills [NEW — H11 RESULT]

H11 audited 148 files across 9 projects for verbatim quote density (quotes/section). Only 3 files fell below threshold (2%), but those 3 revealed a structural skill design gap.

**PT paradox:** PT has the highest JTBD quote density (3.66 avg) but the two lowest-density downstream files — AI opportunities (0.03) and scenarios (0.19). The analyst extracted well; the synthesis skills did not pull quotes forward.

**Root cause:** `ai-opportunity-analyzer` and `scenario-mapper` synthesise from JTBD job statements but do not require embedding verbatim quotes from upstream JTBD files. Unless the researcher manually copies quotes, downstream files are structurally quote-sparse.

**Fix shipped:** Quality gate added to both skills — each opportunity and each scenario must contain ≥1 verbatim blockquote pulled from JTBD files or transcripts. The gate requirement reads upstream if the scenario file lacks quotes.

**Practical rule:** Quote density alone does not reveal traceability problems when intermediate synthesis layers exist. The cascade is invisible until you compare density across pipeline stages for the same project.

---

### Pattern 6: Source Proximity, Not File Count, Predicts Research Quality [NEW — H10 RESULT]

H10 compared Fusion's cross-persona JTBD synthesis (no individual files) vs. DI&A's per-transcript JTBD files, and KAI's consolidated personas overview vs. individual persona files.

**Finding:** A single consolidated file with direct transcript quotes (KAI personas) is quality-equivalent to individual per-transcript files. What degrades quality is not consolidation but **citation chain length**: Fusion's JTBD cites journey map line numbers (transcript → journey → JTBD) instead of transcript quotes directly (transcript → JTBD). Traceability weakens with each intermediate hop.

**The rule:** Any output format is acceptable *if* verbatim quotes trace directly to transcripts. Consolidated files save time and are not lower quality. Journey-map-as-source is the anti-pattern.

**Practical implication:** The pipeline completeness metrics from H2 were wrong. Correct figures: AI opportunities 89% complete (8/9 projects), scenarios 100% presence (depth gap, not presence gap). Fusion is the only genuine hole (0 AI opportunities, JTBD lacks transcript quotes).

### Pattern 3: Pain Intensity × Source Confidence is the Right Scoring Dimension [NEW — H4 RESULT]

H4 revealed that blind frequency-based confidence weighting breaks high-stakes, low-frequency signals:
- **MENA/Brazil Coverage** (9.0/10 pain, 3/10 users): correctly a P0 — blind confidence weighting would demote to P4
- **Jurisdiction Tracker** (5/10 pain, 3/10 users): correctly a P2/3 — confidence weighting correctly demotes

**The rule:** Pain intensity modulates the confidence penalty. High pain (≥8/10) → protect signal regardless of frequency. The CPI empathy re-scoring intuitively got this right; H4 makes it algorithmic.

This generalizes: **signal reliability = confidence_factor(pain_intensity, n_interviews)**, not confidence_factor(n_interviews) alone.

### Pattern 4: The Trust + Explainability Signal is Universal [UNCHANGED]
Across DI&A, CPI, CDDI — the #1 AI adoption blocker is trust and explainability. Cluster 0 (AI Ambivalence) in H1 confirms this at platform scale (162 entries, 7/9 products). **This is now quantified, not just observed.**

### Pattern 5: The Output Gap is Concentration-Dependent [UNCHANGED]
DI&A (most complete) and CPI (richest data) are the reference implementations. 7 other projects stop at empathy + journey + JTBD. The bottleneck is not skill capability — it's friction at each trigger point. Automation (H2) + auto-discovery (H7, H9) addresses this.

---

## Lessons and Constraints

1. **Skills are adopted when they're easy to trigger** — auto-discovery mode (H7) is the right design pattern.

2. **Workflow sequence violations compound** — CPI personas were created before empathy maps; this error propagated through the entire pipeline. Sequence enforcement is not optional.

3. **Manual clustering is the bottleneck — now solved** — DI&A clustering-analysis.md is the best artifact in the entire repo. H9 shipped: `/empathy-clustering [project]` runs in <10 seconds and recovers all manual themes plus additional emotional nuances. Any project with 3+ empathy maps can now get clustering.

4. **Node ID staleness is a hard constraint in Figma** — the fix must be architectural (single execution), not a retry loop.

5. **Prediction magnitude is often off, direction is usually right** — H1 predicted 5-8 clusters, found 14. H4 predicted 25-35% reclassification, found 43%. Both directionally correct but the platform is MORE interesting than predicted.

6. **UMAP dramatically outperforms PCA for text embedding clustering** — 49% noise → 12% noise. Always use UMAP for semantic clustering of empathy/qualitative data.

---

## Open Questions

1. **Pipeline orchestration granularity** — Per-transcript vs. per-project for /research-pipeline. Per-transcript preserves traceability; per-project is simpler. Decision left to implementation phase.

2. **Timing validation** — Is the 85-95% time savings claim still accurate? No explicit timing data tracked per project. Would require a controlled comparison study.

3. **Scenario depth gap** — H10 corrects H2: all 9 projects have ≥1 scenario file (presence = 100%). The gap is depth: most have 1 consolidated map where 3-5 would give richer coverage. This is an execution priority, not a missing-skill problem.

4. **Pipeline completeness was mismeasured** (H10) — H2's "9% AI opps, 12% scenarios" used per-transcript denominators for project-level outputs. Corrected: AI opportunities 89% complete (8/9 projects), scenarios 100% presence. Only Fusion is missing AI opportunities (no JTBD to feed it).

---

## Research Trajectory

| Exp | Hypothesis | Status | Key Result |
|-----|-----------|--------|-----------|
| — | Bootstrap | ✅ Done | 7 hypotheses formed |
| H5 | Cross-project synthesizer | ✅ Shipped | Skill created |
| H7 | Pain-matrix autogen | ✅ Shipped | Auto-discovery mode added |
| H1 | Semantic clustering | ✅ Shipped | 11 universal clusters, 14 total, 12% noise |
| H4 | Confidence propagation | ✅ Shipped | Pain-modulated confidence is correct design |
| H9 | Empathy-clustering skill | ✅ Shipped | 8 clusters, 4% noise, <10s — all DI&A themes recovered |
| H8 | Cluster-aware scoring | ✅ Shipped | 3 platform capability themes — per-product P1s systematically undervalue universal investments |
| H2 | Pipeline automation | ✅ Shipped | /research-pipeline skill + audit — scenario gap confirmed (13/~45 files), Fusion JTBD=0 |
| H3 | Prompt optimization | ✅ Shipped | FEELS quality CV=69% — prompt-driven not data-driven; 3 improvements + bug fix shipped |
| H6 | Figma hardening | ✅ Shipped | Code audit — all 5 failure modes covered; 3 documentation gaps closed in SKILL.md |
| H10 | Downstream quality audit | ✅ Shipped | File count wrong metric; source proximity right metric. Pipeline was mismeasured — AI opps 89% complete, scenarios 100% presence |
| H11 | Traceability audit | ✅ Shipped | 148 files, 2% low-density. Quote starvation cascade: PT JTBD→AI opps drops 3.66→0.03. Quality gate added to ai-opportunity-analyzer + scenario-mapper |
