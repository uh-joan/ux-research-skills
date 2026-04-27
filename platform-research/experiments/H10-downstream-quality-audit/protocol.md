# H10 Protocol: Downstream Quality Audit

**Status:** Running  
**Date:** 2026-04-27  
**Hypothesis:** Projects that skip individual per-transcript JTBD files produce lower-quality consolidated outputs (cross-persona synthesis, AI opportunities) than projects with complete individual file coverage.

---

## Background

H2 pipeline audit found "Fusion: 0 JTBD files." On re-examination, Fusion has `jtbd-cross-persona-synthesis.md` but no individual per-transcript files. This means someone synthesised across 21 interviews without the intermediate per-transcript step. KAI has only a `personas-overview` file with no individual persona profiles.

The question: does this shortcut produce worse outputs?

## Prediction

- Fusion's cross-persona JTBD will contain more generic, low-specificity insights than DI&A's (which has 26 individual files feeding it)
- Measurable signal: claim-to-quote ratio, specificity of job statements, number of distinct jobs identified
- Prediction: Fusion cross-persona JTBD has <50% the quote density of DI&A cross-persona JTBD

## Method

### Comparison pairs

| Project | Individual files | Consolidated output | 
|---|---|---|
| DI&A | 26 JTBD files | cross-persona JTBD (if exists) |
| Fusion | 0 individual | jtbd-cross-persona-synthesis.md |
| CPI | 11 JTBD files | cross-persona JTBD (if exists) |
| KAI | 6 JTBD files | personas-overview-2026-04-23.md |

### Quality metrics

For JTBD files:
- **Quote density**: quotes per job statement (verbatim user quotes)
- **Job specificity**: are jobs named with context ("When preparing quarterly forecasts...") or generic ("When I need data...")
- **n_jobs**: number of distinct jobs identified
- **Participant tracing**: can individual jobs be traced back to specific participants

For persona files:
- **Quote density**: quotes per persona section
- **Participant count**: how many participants mapped to each persona
- **Behavioral specificity**: are behaviors described with concrete actions or generic categories

### Scoring rubric (1-5 per dimension)

| Score | Quote density | Job specificity |
|---|---|---|
| 5 | >1 quote per job | "When [specific trigger + context]..." |
| 3 | ~0.5 quotes per job | Some context, some generic |
| 1 | <0.1 quotes per job | "When I need to..." only |

## Files to read

1. `Fusion/jtbd/jtbd-cross-persona-synthesis.md`
2. `DI&A/jtbd/cross-persona-*.md` (if exists) or a sample of individual JTBD files
3. `KAI/personas/personas-overview-2026-04-23.md`
4. `DI&A/personas/*.md` or `CPI/personas/*.md` (comparison baseline)

## Outcome types

- **CONFIRMATORY**: Fusion synthesis significantly lower quality → individual files matter
- **DISCONFIRMATORY**: Fusion synthesis comparable quality → shortcut is valid
- **MIXED**: Quality gap exists but for different reasons than hypothesised
