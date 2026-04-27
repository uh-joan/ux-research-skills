# H10 Analysis: Downstream Quality Audit

**Status:** MIXED RESULT  
**Date:** 2026-04-27  
**Comparisons:** Fusion cross-persona JTBD vs. DI&A individual JTBD · KAI personas overview vs. individual persona baseline

---

## Result vs. Prediction

| Criterion | Prediction | Result | Verdict |
|-----------|-----------|--------|---------|
| Fusion JTBD lower quality than DI&A | Yes — <50% quote density | Specificity comparable; traceability weaker | ⚡ MIXED |
| Individual files → better quality | Yes | Wrong dimension: specificity is similar; source proximity is the gap | ⚡ MIXED |
| KAI overview lower quality | Yes | KAI overview is high quality — shortcut works | ❌ DISCONFIRMATORY |

The hypothesis was framed around the wrong dimension. The gap is not **specificity** — it is **source proximity**.

---

## Finding 1: Fusion JTBD — Good Jobs, Weak Traceability

Fusion's `jtbd-cross-persona-synthesis.md` contains 46 distinct, well-formed JTBD statements across 4 personas. Job quality by format:

✅ **Format quality**: All jobs follow "When/I want to/So I can" correctly  
✅ **Specificity**: Jobs name concrete triggers ("when DRG doesn't cover 20+ countries"), concrete outcomes ("deliver global market segmentation without being limited by vendor coverage")  
✅ **Frequency / pain / current solution**: All present per job  
⚠️ **Source citations**: Journey map line numbers, not transcript quotes — e.g., "Sources: Abhishek (user-journey-abhishek-mehendale.md:411-413)"  
❌ **Verbatim quotes**: None embedded within job statements  
❌ **13 of 21 interviews "inferred"**: Header states "8 with explicit JTBD sections, 13 inferred" — 62% were inferred from journey maps rather than extracted from transcripts  

**Comparison — DI&A individual JTBD (Abhishek example):**
- 4+ verbatim quotes per job, directly from transcript
- Job dimensions (functional/emotional/social)
- Switching triggers (ranked order)
- Cross-participant validation flag
- Confidence rating per job

**Assessment:** Fusion jobs are usable for roadmap prioritisation. They fail the traceability standard: citations are to journey maps (one layer removed from transcripts), not to interviews directly. If a stakeholder challenges a job statement, the researcher must trace: JTBD → journey map → transcript. DI&A allows JTBD → transcript directly.

**The actual gap:** source proximity, not job quality.

---

## Finding 2: KAI Personas Overview — Shortcut That Works

KAI's `personas-overview-2026-04-23.md` is a consolidated file containing all 3 personas. Quality assessment:

✅ **Verbatim quotes per persona** (2+ direct transcript quotes each)  
✅ **Participant mapping** (specific participants named per persona)  
✅ **AI maturity spectrum** (additional dimension not always in individual files)  
✅ **Goals, motivations, tools, pain points** — all present  
✅ **Traceability**: quotes are direct — "We want to know very quickly: how many patients are eligible..." — Florian  

**Assessment:** Comparable to individual persona files from CPI/DI&A. The consolidated format does not reduce quality here because verbatim quotes were preserved from transcripts directly, not passed through an intermediate artifact.

**Why the KAI shortcut works:** the researcher maintained direct transcript-to-persona traceability within the consolidated file. No intermediate artifact (journey map) was inserted between transcript and output.

---

## The Actual Rule: Source Proximity Matters, File Count Does Not

| Pattern | Example | Quote traceability | Quality verdict |
|---|---|---|---|
| Per-transcript → individual file → synthesis | DI&A JTBD | Transcript → file direct | ✅ Best |
| Per-transcript → consolidated file (quotes kept) | KAI personas | Transcript → file direct | ✅ Equivalent |
| Journey maps → cross-persona synthesis (quotes absent) | Fusion JTBD | Journey map line refs | ⚠️ Usable, not ideal |
| Journey maps → synthesis with quotes inferred | (hypothetical) | No direct trace | ❌ Unacceptable |

**The rule:** traceability degrades when an intermediate artifact (journey map, persona) becomes the citation source instead of the original transcript. File count is irrelevant — a single well-traced consolidated file is equivalent to individual files.

---

## Finding 3: Pipeline Completeness Was Mismeasured

The H2 audit used per-transcript denominators for all steps. On re-examination:

| Step | H2 reported | Actual (project level) | Interpretation |
|---|---|---|---|
| AI opportunities | 9% | 8 of 9 projects have ≥1 file | **89% complete** — only Fusion missing |
| Scenarios | 12% | 9 of 9 projects have ≥1 file | **100% presence** — depth varies |
| Personas | 33% | 8 of 9 projects have 3-5 profiles | **~90% complete** — KAI is outlier |

The scenario and AI opportunity "gap" from H2 was a measurement artefact. Projects were correctly generating 1 consolidated file per project (appropriate), not one per transcript. Only **Fusion's 0 AI opportunity files** and **KAI's depth** are genuine gaps.

**Correcting the record:** findings.md previously stated "universal 80% scenario gap." This should be corrected — there is a **scenario depth gap** (1 scenario map where 3-5 would be richer) but not a presence gap.

---

## Recommendations

1. **The shortcut is acceptable if quotes stay direct.** Researchers generating consolidated JTBD or persona files do not need individual per-transcript files, *as long as* verbatim quotes come from original interviews, not from journey maps.

2. **Fusion JTBD needs a quote pass.** The 46 jobs are usable but each job statement should have at least 1 verbatim quote attached. This is a 1-hour edit, not a re-research.

3. **Correct pipeline completeness metrics.** AI opportunities are 89% complete, scenarios have presence in all 9 projects. The `pipeline_status.py` script needs a project-level mode for consolidated outputs.

4. **Scenario depth, not scenario presence, is the real gap.** Most projects have 1 scenario map; richer coverage would have 3-5. Worth flagging in research-state as an execution priority.

---

## H10 Verdict: MIXED — File Count Is Wrong Metric; Source Proximity Is Right Metric

The original hypothesis ("individual files → better quality") was measuring the wrong thing. The finding that matters:

> **Traceability degrades when intermediate artifacts become citation sources. File count is irrelevant. A single consolidated file with direct transcript quotes is equivalent to individual files.**

This changes the pipeline completeness picture significantly: the platform is more complete than H2 suggested, and the primary quality risk is not missing files but citation chains that pass through journey maps rather than going directly to transcripts.
