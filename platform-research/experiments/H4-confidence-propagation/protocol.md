# Experiment H4: Confidence Propagation in AI Opportunity Scoring

**Hypothesis:** Adding a confidence weighting layer to ai-opportunity-analyzer that discounts JTBD jobs from single-source transcripts would reduce false Priority 1 assessments.

**Prediction:** Applying confidence weighting to CPI's 17 opportunities would reclassify 25-35% from Priority 1, giving a more defensible roadmap.

**Status:** PROTOCOL LOCKED — 2026-04-27

---

## What This Tests

The ai-opportunity-analyzer currently scores opportunities based on user needs (pain severity, frequency, reach) + business value + technical feasibility. However, it doesn't account for **source confidence** — how many distinct interviews mention the underlying JTBD job.

A JTBD job mentioned by 1/10 users feeds directly into the same scoring pipeline as one mentioned by 8/10 users. This creates false confidence in low-evidence opportunities.

**Specific Question:** If we weight the "User Needs" dimension by interview_count/total_interviews, how many CPI Priority 1 opportunities get reclassified?

## Method

1. Extract JTBD job statements from CPI cross-persona analysis with frequency counts
2. Map each CPI AI opportunity to its underlying JTBD job(s)
3. Compute confidence score = N_interviews / total_interviews
4. Compute adjusted score = original_score × confidence_factor
5. Compare P1/P2/P3 assignments before vs. after

## Confidence Factor Formula

```
confidence_factor = min(1.0, (n_interviews / total_interviews) / 0.5)
# Normalizes so that 50%+ coverage = no penalty (factor = 1.0)
# Coverage below 50% gets proportionally discounted
# Floor at 0.3 to prevent complete elimination of real signals
confidence_factor = max(0.3, confidence_factor)
```

## Success Criteria

| Criterion | Success |
|-----------|---------|
| JTBD extracted with frequency counts | Coverage ≥80% of current P1 opportunities |
| P1 reclassifications | 25-35% of current P1 demoted |
| Defensibility | Reclassified opportunities have n_interviews ≤ 2/10 |

## Expected Outcome

If confirmed: Update ai-opportunity-analyzer SKILL.md to include confidence propagation step.
If disconfirmed: Current scoring is already adequate OR the issue is pain intensity not source count.
