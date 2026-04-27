# Findings: researcher_ux Platform Improvement Research

**Research Question:** How can the researcher_ux UX research skills platform be improved in algorithms, workflow automation, quality, and capability gaps?

**Status:** Bootstrap complete. 7 hypotheses formed. First experiment in progress.

**Last Updated:** 2026-04-27

---

## Current Understanding

### What the Platform Does Well

The core pipeline (empathy map → user journey → persona → JTBD → AI opportunities) is **production-grade and validated**. Evidence:
- 53 interviews processed across 9 Clarivate product domains
- 400+ markdown deliverables created
- Time savings of 85-95% vs. manual research (4-6 weeks → 1-2 days)
- Multi-dimensional user understanding: SAYS (verbatim) + THINKS (inferred) + DOES (behavioral) + FEELS (emotional with intensity)
- Full traceability: every insight linked to source quotes
- Validated methodology: Nielsen Norman Group + Clayton Christensen JTBD

Key validated insights from production:
- **Pain intensity ≠ frequency**: MENA regional data gaps (pain 9.0/10, only 30% reach) correctly elevated to P0 priority in CPI
- **Vendor credibility gap as moat**: 7/9 DI&A users prefer "vendor-backed AI" (Clarivate/DRG) over generic LLMs — validated differentiation strategy
- **Empathy-first prioritization works**: FEELS quadrant pain intensity + frequency-weighted scoring surfaces non-obvious high-value opportunities

### What is Broken or Missing

**Critical gaps (impact: HIGH):**

1. **Scenario mapping output gap** — 80-90% of expected outputs not generated
   - Only 1-2 scenario files per project; design teams need 10-15 per project to fill a backlog
   - Root cause: skill exists but requires high-quality JTBD input AND design team feedback loop not established
   - Fix: validate scenario-mapper with a real design workshop; iterate on output format

2. **Pain-point matrix absent everywhere** — 1 file across 9 projects
   - The skill exists, the input data exists (400+ empathy maps + journey maps), but the skill requires manual extraction
   - Fix: refactor pain-point-matrix skill to auto-read from existing files (H7)

3. **Cross-interview analysis is manual and inconsistent**
   - Clustering is done ad-hoc (DI&A has clustering-analysis.md created manually; CPI does not)
   - No systematic detection of patterns across all 53 interviews
   - Fix: semantic clustering skill (H1) + cross-project meta-analysis (H5)

4. **Figma visual deliverables blocked** — 35+ journey maps lack visual counterparts
   - journey-figma-creator has a node ID staleness bug that causes failures on multi-step execution
   - Fix: enforce single-subagent execution protocol (H6)

**Important opportunities (impact: MEDIUM):**

5. **Confidence propagation missing** — JTBD jobs with single-user evidence feed directly into Priority 1 AI opportunity scores
   - DI&A job "find missing data for underrepresented populations" (1/9 users) scored as Priority 2 opportunity
   - CPI: some P1 opportunities may be inflated by low-sample JTBD jobs
   - Fix: confidence weighting in ai-opportunity-analyzer (H4)

6. **No pipeline automation** — each skill manually triggered, costing hours of coordination
   - A CrewAI or LangGraph orchestration of empathy → persona → JTBD would run in 2-4 hours unattended
   - Fix: multi-agent pipeline (H2)

7. **Prompt quality not optimized** — current skill prompts are hand-written, not data-driven
   - 400+ outputs exist as potential training signal for DSPy optimization
   - Fix: prompt optimization experiment (H3)

---

## Patterns and Insights

### Pattern 1: The "Outer Loop" is the Missing Layer
The platform does the inner loop (per-interview analysis) excellently but lacks the outer loop (cross-interview synthesis). This exactly mirrors the Orchestra autoresearch two-loop gap — the system collects deep per-interview data but has no mechanism to step back and synthesize patterns across all 53 interviews. Every improvement opportunity in the HIGH impact tier is an outer loop problem.

### Pattern 2: The Output Gap is Concentration-Dependent
The deepest outputs exist in DI&A (most complete, best methodology applied) and CPI (richest data). For 7 other projects, the pipeline stops after empathy + journey + JTBD and never produces scenarios, pain matrices, or AI opportunities. The gap isn't skill capability — it's skill adoption. The scenario-mapper and pain-matrix need to be easier to trigger and require less manual input.

### Pattern 3: Existing Data is Massively Underutilized
400+ files across 9 domains represent a gold mine of cross-project insights:
- Are the same persona archetypes appearing in CPI, DI&A, and CDDI?
- Is "data fragmentation" a universal Clarivate pain point across all products?
- Do the same AI opportunities (semantic synthesis, multi-source triangulation) appear across multiple product domains?
None of these questions can currently be answered without manual review.

### Pattern 4: The Trust + Explainability Signal is Universal
Across DI&A (9 users), CPI (10 users), and CDDI (8 users), the #1 blocker for AI adoption is the same: **trust and explainability**. Users want vendor-backed AI with audit trails, not generic ChatGPT responses. This cross-domain signal has not been synthesized — it's buried in individual project analyses.

---

## Lessons and Constraints

1. **Skills are adopted when they're easy to trigger** — scenario-mapper generates excellent output but requires perfect JTBD input + explicit triggering. The harder a skill is to run, the less it gets used.

2. **Workflow sequence violations compound** — CPI personas were created before empathy maps (workflow violation). This propagated through the entire pipeline: personas lack empathy clustering analysis, JTBD lacks pain intensity grounding. Sequence enforcement is not optional.

3. **Manual clustering is the bottleneck** — DI&A clustering-analysis.md took significant manual effort and is the single best artifact in the entire repo. But it only exists for one project. Every project needs this and can't get it at scale without automation.

4. **Node ID staleness is a hard constraint in Figma** — the journey-figma-creator failure mode is well-documented (node IDs go stale across multiple `figma_execute` calls). The fix must be architectural (single execution), not a retry loop.

---

## Open Questions

1. **H1: Will semantic clustering find meaningful patterns or just noise?** — DI&A clustering found 4 clean behavioral clusters from 9 users. Will the signal hold at 53 users across 9 domains, or will domain-specific variation drown the pattern?

2. **H5: Are cross-domain patterns actionable?** — If we find "data triangulation pain" in 7/9 product domains, what does Clarivate do with that? The finding has different implications for each product team. How do we make the meta-analysis output product-team-actionable?

3. **H2: What's the right orchestration granularity?** — Should the pipeline automation run all 4 skills at project level (all transcripts → all empathy maps → all personas), or per-transcript (transcript → empathy → journey → individual JTBD, then aggregate)? The latter preserves traceability but is more complex.

4. **H3: Is DSPy overhead worth it?** — With 400+ outputs as training signal, DSPy prompt optimization could be powerful. But rewriting skill prompts from optimized DSPy output requires careful adaptation. Is the quality improvement large enough to justify the complexity?

5. **Is the 85-95% time savings claim still accurate?** — The claim is in the README but no explicit timing data is tracked per project. Adding timing instrumentation to skills would validate this claim and identify which stages are still slow.

---

## Research Trajectory

| Exp # | Hypothesis | Status | Result |
|-------|-----------|--------|--------|
| — | Bootstrap | ✅ Complete | 7 hypotheses formed |
| E1 | H1: Semantic Clustering | 🔄 In Progress | — |
