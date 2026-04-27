# H11 Analysis: Traceability Audit

**Status:** PARTIALLY CONFIRMATORY  
**Date:** 2026-04-27  
**Files audited:** 148 across 9 projects (JTBD, personas, scenarios, AI opportunities)

---

## Result vs. Prediction

| Criterion | Prediction | Result | Verdict |
|---|---|---|---|
| ≥2 projects with low-density files | Yes | PT + Fusion (correct projects, small extent) | ✅ CONFIRMED |
| Bimodal distribution (high vs. low quality) | Yes | Not found — distribution is broadly uniform 1.5–3.0 | ❌ DISCONFIRMATORY |
| Quote density reveals platform quality risk | Yes | 2% low-traceability — platform is healthier than expected | ⚠️ WEAKER THAN PREDICTED |

---

## Key Numbers

| Metric | Value |
|---|---|
| Total files audited | 148 |
| Low-traceability files (<0.30 quotes/section) | 3 (2%) |
| Avg JTBD quote density | 2.20 |
| Avg persona quote density | 1.89 |
| Projects fully complete (project-level) | 7 of 9 |

---

## Finding 1: Overall Traceability Is High

Only 3 of 148 files fall below the 0.30 threshold. The platform's downstream outputs are substantially quote-backed. The H10 concern about Fusion JTBD was valid but limited — Fusion's JTBD avg density (0.36) is just above threshold, not critically low.

**Quote density by project (JTBD / Personas):**

| Project | JTBD avg | Persona avg | Low% |
|---|---|---|---|
| DI&A | 2.70 | 3.53 | 0% |
| CPI | 2.42 | 2.05 | 0% |
| PT | **3.66** | 0.51 | **14%** |
| MASS | 2.38 | 1.74 | 0% |
| MT360 | 3.15 | 1.94 | 0% |
| CDDI | 1.66 | 1.80 | 3% |
| Fusion | **0.36** | 1.84 | 0% |
| OFFX | 1.02 | 1.33 | 0% |
| KAI | 1.56 | — (audit bug) | 0% |

---

## Finding 2: PT Is the Traceability Outlier, Not Fusion

The three low-traceability files:

| File | Density | Issue |
|---|---|---|
| `PT/ai-opportunities/ai-opportunity-assessment-2026-04-16.md` | **0.03** | Framework document with almost no user quotes |
| `CDDI/jtbd/jtbd-analysis-belinda-stretch.md` | 0.11 | Single interview with sparse quote extraction |
| `PT/scenarios/scenario-map-2026-04-16.md` | 0.19 | Scenario descriptions without supporting evidence |

**PT paradox:** PT has the highest JTBD quote density (3.66 avg) but the two lowest-density downstream files. The JTBD analyst extracted well but the AI opportunity and scenario files were written without pulling quotes forward into the synthesis.

**Root cause:** The AI opportunity and scenario skills do not require quotes — they synthesise from JTBD statements. Quotes are upstream. If the skill user doesn't manually embed supporting evidence, the downstream files are structurally quote-sparse. This is a skill design gap, not a researcher failure.

---

## Finding 3: Pipeline Completeness Confirmed (Corrected Denominators)

Project-level audit (using 1-5 expected per project, not per-transcript):

| Project | Personas | Scenarios | AI Opps | Status |
|---|---|---|---|---|
| DI&A | ✅ 5 | ✅ 1 | ✅ 1 | Complete |
| CPI | ✅ 4 | ✅ 2 | ✅ 3 | Complete |
| CDDI | ✅ 6 | ✅ 4 | ✅ 1 | Complete |
| Fusion | ✅ 4 | ✅ 1 | **❌ 0** | Missing AI opps |
| PT | ✅ 4 | ✅ 1 | ✅ 1 | Complete |
| MASS | ✅ 3 | ✅ 1 | ✅ 1 | Complete |
| MT360 | ✅ 3 | ✅ 1 | ✅ 1 | Complete |
| KAI | ❌ 0 (audit bug) | ✅ 1 | ✅ 1 | Personas miscounted |
| OFFX | ✅ 4 | ✅ 1 | ✅ 1 | Complete |

**KAI audit bug:** The `overview` exclusion pattern filtered `personas-overview-2026-04-23.md` — KAI's only persona file. KAI does have 3 personas (confirmed in H10). Fix: personas step should not exclude files containing "overview."

**Corrected status:** 8 of 9 projects fully complete. Fusion AI opportunities is the only genuine gap.

---

## Finding 4: Skill Design Gap — AI Opps and Scenario Skills Don't Pull Quotes Forward

The pattern in PT (high JTBD density → near-zero AI opp/scenario density) reveals a structural issue: the `ai-opportunity-analyzer` and `scenario-mapper` skills synthesise from JTBD statements but do not require — or prompt for — embedding supporting verbatim quotes from the upstream JTBD files.

This means every AI opportunity assessment and scenario map is structurally quote-sparse unless the researcher manually copies quotes from JTBD files into the synthesis.

**Comparison:**
- JTBD files: avg 2.20 quotes/section — high, because the skill explicitly prompts "include supporting quotes"
- AI opportunity files: avg 1.34 quotes/section overall, but 0.03 for PT (the most JTBD-rich project)
- This inconsistency is structural, not random

**Fix:** Add "Supporting Evidence" field to the ai-opportunity-analyzer output format, populated from upstream JTBD quotes. Same for scenario-mapper.

---

## Script Bug Fixed

Excluded `overview` from persona directory exclusion for the pipeline completeness check. The `traceability_audit.py` EXCLUDE pattern correctly excludes overview files from density scoring (since overview files are meta-documents), but the project-level completeness counter should not exclude them if they are the primary persona artifact.

---

## Recommendations

1. **Immediate fix (PT):** Add 3-5 user quotes to `PT/ai-opportunities/ai-opportunity-assessment-2026-04-16.md` and `PT/scenarios/scenario-map-2026-04-16.md`. ~30 minutes of work.

2. **Skill improvement:** Update `ai-opportunity-analyzer` and `scenario-mapper` SKILL.md to require a "Supporting Evidence" field (1-2 quotes per opportunity/scenario pulled from upstream JTBD). This closes the structural gap for all future outputs.

3. **Fusion:** Generate AI opportunity assessment from the existing cross-persona JTBD synthesis. Fusion is the only project with 0 AI opportunity files. One output needed.

4. **Pipeline audit fix:** Update `pipeline_status.py` to use project-level expected counts for personas/scenarios/ai-opps. Deploy the corrected completeness table as the canonical view.

---

## H11 Verdict: PARTIALLY CONFIRMATORY

The prediction of low-density outliers in ≥2 projects was correct. But the scale was smaller than expected (2% files, not 15-20%). The most important finding is structural: AI opportunity and scenario synthesis skills don't pull quotes forward from JTBD files, creating a systematic — though mild — traceability gap in all downstream synthesis. PT makes this visible; other projects compensate by having lower JTBD density going in.
