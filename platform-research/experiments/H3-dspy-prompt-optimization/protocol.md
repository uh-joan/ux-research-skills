# Experiment H3: DSPy-Inspired Prompt Quality Analysis

**Hypothesis:** The 400+ existing skill outputs contain measurable quality variance. Analyzing
this variance reveals specific prompt weaknesses that can be fixed with targeted instruction
improvements — without requiring full DSPy compilation.

**Prediction:**
- At least 2 skill prompts have measurable quality variance across projects (high-quality
  vs low-quality outputs on the same task)
- The variance correlates with specific prompt instructions that are ambiguous or missing
- Proposed prompt improvements are concrete (specific instruction rewrites, not vague advice)

**Status:** PROTOCOL LOCKED — 2026-04-27

---

## Design

### Quality Metrics per Skill

**Empathy maps (empathy-map-generator):**
- `feels_count` — number of FEELS entries (target: 8-15 per map)
- `emotion_diversity` — unique emotion labels / total entries
- `description_depth` — avg word count of FEELS descriptions (target: 10-20 words)
- `says_quote_density` — entries with actual quotes vs paraphrases
- `format_compliance` — uses `- **emoji Emotion** description` format

**Personas (persona-generator):**
- `quote_density` — quotes per persona (target: 5+)
- `section_completeness` — all 6 NNG sections present
- `pain_specificity` — pain points with quantification vs generic

**JTBD (jtbd-analyzer):**
- `statement_count` — number of JTBD statements
- `circumstance_detail` — "when I..." clauses with context richness
- `outcome_measurability` — outcomes with success criteria vs vague

### Analysis Approach

1. Parse all existing outputs and compute quality metrics per file
2. Compute per-project means and variance
3. Identify outliers (files >1.5 IQR below median)
4. Read low-quality outliers to identify root causes
5. Trace root causes to specific prompt instructions
6. Write improved instruction text

### Success Criteria

| Criterion | Success |
|-----------|---------|
| Quality metrics computed | For all 3 skills across all projects |
| Variance identified | At least 2 skills show significant (>30%) variance |
| Root causes found | At least 3 specific prompt weaknesses identified |
| Improvements written | Concrete instruction rewrites for each weakness |
