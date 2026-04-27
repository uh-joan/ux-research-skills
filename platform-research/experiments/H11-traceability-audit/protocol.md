# H11 Protocol: Traceability Audit

**Status:** Running  
**Date:** 2026-04-27  
**Hypothesis:** Source proximity (quote traceability to original transcripts) varies significantly across JTBD and persona files. Files citing journey maps or producing zero quotes are identifiable via a quote-density scan.

## Background

H10 found that file count is the wrong pipeline quality metric — source proximity is right. Fusion JTBD cites journey maps, not transcripts. The question: how widespread is this pattern? Are other projects also generating low-traceability downstream files?

## Prediction

- ≥2 projects besides Fusion will have JTBD or persona files with <0.5 quotes per section
- The quote density distribution will be bimodal: high-quality projects (DI&A, CPI) vs. low-quality (CDDI, Fusion, KAI)
- Fixing pipeline_status.py to use project-level denominators will change coverage % for personas/scenarios/ai-opps substantially

## Deliverables

1. **`quote_density_audit.py`** — scans all JTBD and persona .md files, counts verbatim quotes (lines starting with `>` or enclosed in `"..."`) per file, produces per-project summary
2. **Fixed `pipeline_status.py`** — adds project-level mode: for personas/scenarios/ai-opps, expected = 1-5 per project, not per transcript
3. **Analysis** — quote density distribution, low-traceability files flagged, corrected pipeline completeness table

## Method

### Quote detection heuristics
- Blockquote lines: `> "..."` or `> text`
- Inline quotes: text matching `"[A-Z][^"]{20,}"` (capitalized, ≥20 chars)
- Count per file, normalise by section count (headers starting with `##` or `###`)

### Project-level pipeline fix
- Consolidated outputs (personas, scenarios, ai-opps): expected = project-specific constant
  - personas: 3-5 (flag if 0 or 1)
  - scenarios: 1-3 (flag if 0)
  - ai-opportunities: 1 (flag if 0)
