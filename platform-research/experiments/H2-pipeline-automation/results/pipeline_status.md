# Pipeline Status Audit — H2

**Date:** 2026-04-27  
**Script:** `code/pipeline_status.py`  
**Projects:** 9 (CDDI, CPI, DI&A, Fusion, KAI, MASS, MT360, OFFX, PT)  
**Total transcripts:** 106

---

## Completion Matrix

| Project | TXN | Empathy Maps | Journey | Personas | JTBD | AI-Opps | Scenarios |
|---------|-----|-------------|---------|---------|------|---------|-----------|
| CDDI | 17 | ✅ 118% | ✅ 129% | ⚠️ 35% | ✅ 106% | ⚠️ 6% | ⚠️ 24% |
| CPI | 10 | ✅ 100% | ✅ 140% | ⚠️ 50% | ✅ 100% | ⚠️ 30% | ⚠️ 20% |
| DI&A | 21 | ✅ 100% | ✅ 119% | ⚠️ 29% | ✅ 119% | ⚠️ 5% | ⚠️ 5% |
| Fusion | 21 | ✅ 100% | ✅ 100% | ⚠️ 19% | ❌ 0% | ❌ 0% | ⚠️ 5% |
| KAI | 10 | ⚠️ 50% | ⚠️ 50% | ❌ 0% | ⚠️ 50% | ⚠️ 10% | ⚠️ 10% |
| MASS | 3 | ✅ 100% | ✅ 100% | ✅ 100% | ✅ 100% | ⚠️ 33% | ⚠️ 33% |
| MT360 | 5 | ✅ 120% | ✅ 120% | ⚠️ 60% | ⚠️ 60% | ⚠️ 20% | ⚠️ 20% |
| OFFX | 12 | ✅ 100% | ✅ 100% | ⚠️ 33% | ✅ 100% | ⚠️ 8% | ⚠️ 8% |
| PT | 7 | ✅ 100% | ✅ 100% | ⚠️ 57% | ✅ 100% | ⚠️ 14% | ⚠️ 14% |

Note: >100% = additional analyses beyond per-transcript (e.g. DI&A has 21 transcripts but 25 JTBD files — multi-persona, supplementary).

---

## Corrected Gap Analysis

The per-transcript baseline is misleading for steps that produce consolidated outputs. Corrected expected counts:

| Step | Expected per project | True gap |
|------|---------------------|---------|
| Empathy maps | 1 per transcript | **KAI missing 5 maps** |
| Journey maps | 1 per persona (3-5) | **KAI missing 5 journeys** |
| Personas | 3-5 per project | Most projects have 3-6 ✅ (except Fusion 4, KAI 0) |
| JTBD | 1 per persona | **Fusion: 0/21 — ENTIRE step missing** |
| AI opportunities | 1 per project | **5/9 projects have 1 file; CDDI, DI&A, Fusion, MT360 gap** |
| Scenarios | 3-5 per project | **All 9 projects severely under-generated** |

---

## Critical Gaps (by priority)

### P0: Fusion — JTBD and AI-Opportunities completely missing
- 21 empathy maps done, 21 journey maps done, 4 personas done → pipeline stalled at JTBD
- Impact: the entire Fusion AI opportunity roadmap doesn't exist

### P1: Scenario Mapping — 80-90% gap confirmed
- Total: 13 scenario files across 9 projects
- Expected: ~35-45 (3-5 per project)
- Gap: 22-32 missing scenario maps
- This confirms the bootstrap finding: scenarios are the most consistently under-generated output
- Root cause: scenario mapper requires the most manual setup per JTBD cluster

### P2: Personas incomplete in 7/9 projects
- Personas are often created before empathy maps (CPI sequence violation noted in findings)
- MASS (3 transcripts → 3 personas ✅) is the only correct ratio
- Fusion (21 transcripts → 4 personas), KAI (10 transcripts → 0 personas)

### P3: AI opportunity assessments — 4/9 projects incomplete
- CDDI, DI&A, Fusion, MT360 are missing consolidated AI opportunity assessments
- Note: these projects DO have JTBD analysis — the opportunity step wasn't triggered

---

## Root Causes

1. **Manual trigger friction** — Each skill requires explicit invocation; no auto-continuation between steps
2. **Scenario mapper setup** — Requires JTBD cluster data as input + more manual curation than other steps
3. **Pipeline sequence violations** — CPI: personas created before empathy maps; KAI: JTBD before empathy maps complete
4. **Project complexity vs. small projects** — MASS (3 transcripts) is 100% complete; DI&A (21 transcripts) is severely incomplete

---

## H2 Solution Design

### pipeline-runner SKILL.md (to be created)

When invoked as `/research-pipeline [project]`:
1. Run this audit script to detect which steps are missing
2. For each missing step (in order), display what will be run and ask for confirmation
3. Run the appropriate skill for the missing step
4. Report completion

**Minimum viable implementation:** The audit script IS already the core of the solution.
The SKILL.md wraps it with: (a) detection, (b) ordered execution, (c) progress tracking.

### Priority Order for Manual Gaps

Based on this audit, if someone runs `/research-pipeline` for each project, the correct execution order is:

```
Fusion: /jtbd-analyzer → /ai-opportunity-analyzer → /scenario-mapper
KAI: (complete empathy + journey first) → /persona-generator → /jtbd-analyzer → /ai-opportunity-analyzer → /scenario-mapper  
All projects: /scenario-mapper (universal gap)
```

---

## Impact

- **298 files** are the measurable gap across 9 projects (per-transcript baseline)
- **Corrected meaningful gap:** ~50-60 files (JTBD for Fusion + AI-opps for 4 projects + scenarios for all)
- The pipeline-runner SKILL.md would close this gap with a single command per project
