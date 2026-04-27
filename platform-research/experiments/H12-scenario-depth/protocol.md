# H12 Protocol: Scenario Depth Root-Cause Analysis

**Status:** IN PROGRESS  
**Date:** 2026-04-27  
**Hypothesis slug:** scenario-depth

---

## Hypothesis

The scenario depth gap (8 of 9 projects have exactly 1 consolidated scenario file instead of 3-5) is caused by the scenario-mapper skill prompt, not by insufficient JTBD data. Projects have enough high-confidence JTBD jobs to generate 3-5 distinct scenarios, but the skill defaults to a single consolidated output.

## Prediction

Counting high-confidence JTBD jobs across projects will show ≥5 distinct jobs per project (enough inputs to generate 5 scenarios). The scenario files will show <50% utilization of available JTBD jobs. The skill prompt says "8-15 scenarios" in the FAQ but the step-by-step workflow does not enforce minimum scenario count, so researchers stop at 1.

## Method

1. **Count JTBD jobs per project** — parse JTBD analysis files to count high-confidence job statements (`## Job` or `**Job:**` headings + confidence indicators)
2. **Count scenarios per project** — re-run the pipeline completeness audit focusing on scenario count
3. **Compare JTBD-to-scenario ratio** — if ratio > 3:1, the bottleneck is skill execution, not data
4. **Check skill prompt** — does the scenario-mapper's workflow section enforce a minimum scenario count?

## Confirmatory if

- ≥6 of 9 projects have JTBD job count ≥5 AND scenario count = 1
- JTBD-to-scenario ratio ≥ 5:1 across most projects

## Disconfirmatory if

- Projects with 1 scenario file also have ≤3 high-confidence JTBD jobs (data-limited, not prompt-limited)

## Proposed Fix (if confirmatory)

Add to scenario-mapper SKILL.md Phase 2: "Generate 1 scenario per unique high-confidence JTBD job. Minimum 3 scenarios for any project with ≥5 jobs. Do not consolidate all jobs into one scenario — that produces a scenario map, not a set of scenarios."
