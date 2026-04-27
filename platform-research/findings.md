# Findings: researcher_ux Platform Improvement Research

**Research Question:** How can the researcher_ux UX research skills platform be improved in algorithms, workflow automation, quality, and capability gaps?

**Status:** 6 hypotheses shipped (H1, H4, H5, H7, H8, H9). Outer loop synthesis complete. H2 is next.

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

1. **Scenario mapping output gap** — 80-90% of expected outputs not generated (unchanged)
2. **Pain-point matrix** — now fixable via auto-discovery mode (H7 shipped)
3. **Cross-interview analysis** — now addressable via semantic clustering (H1 shipped) + synthesizer (H5 shipped)
4. **Figma visual deliverables** — 35+ journey maps lack visual counterparts (H6 not started)

**Important opportunities (impact: MEDIUM):**

5. **Confidence propagation** — needs pain-modulated weighting, not blind frequency weighting (H4 result)
6. **Pipeline automation** — CrewAI/LangGraph for empathy → persona → JTBD (H2 not started)
7. **Prompt optimization** — DSPy with 400+ outputs as training signal (H3 not started)

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

1. **H8: Do universal clusters change the cross-domain AI opportunity rankings?** — High priority. If data fragmentation (Cluster 12) appears in 7/9 products, cross-source synthesis tools should score much higher than per-product P1 assessments suggest.

2. **H8: Cluster-aware AI opportunity scoring** — now the highest priority. If Manual Correction Burden (8/9 products) and Data Fragmentation (7/9 products) are universal, AI features targeting these should score much higher than per-product P1 lists suggest.

3. **H2: What's the right orchestration granularity for the pipeline?** — Per-transcript vs. per-project. The former preserves traceability, the latter is simpler to orchestrate.

4. **Timing validation:** Is the 85-95% time savings claim still accurate? No explicit timing data tracked per project.

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
| H2 | Pipeline automation | ⏳ Pending | CrewAI/LangGraph orchestration |
| H3 | DSPy optimization | ⏳ Pending | Prompt optimization from 400+ examples |
| H6 | Figma hardening | ⏳ Pending | node ID staleness fix |
