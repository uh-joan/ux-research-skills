# H6 Protocol: Figma Creator Hardening

**Status:** Running  
**Date:** 2026-04-27  
**Hypothesis:** The node ID staleness bug in journey-figma-creator can be permanently fixed via architectural constraint (single execution), and the fix can be verified through code audit of the skill artifacts.

---

## Hypothesis

Node ID staleness in `journey-figma-creator` is a hard constraint of the Figma plugin API: node references do not persist across `figma_execute` calls. A retry loop does not fix this — only single-execution architecture does.

**Prediction:**
- The existing skill artifacts (SKILL.md, implementation.js, LESSONS_LEARNED.md) already encode the architectural fix
- A code audit will find ≥80% of failure modes documented and addressed
- ≤2 remaining unaddressed edge cases will be found

## What This Is NOT

- This is NOT a live Figma execution test (requires Desktop Bridge plugin, not available in this session)
- This is NOT about fixing a new bug — the fix exists
- This IS a completeness audit of the hardening that was already applied

## Audit Targets

1. **SKILL.md** — Does it prevent future multi-call mistakes with clear warnings?
2. **implementation.js** — Does the reference code enforce single-execution?
3. **LESSONS_LEARNED.md** — Are all failure modes documented?
4. **Cross-consistency** — Are the three files consistent with each other?

## Method

1. Read all 4 skill files (SKILL.md, implementation.js, LESSONS_LEARNED.md, QUICK_REFERENCE.md)
2. For each documented failure mode in LESSONS_LEARNED.md, check it's also addressed in SKILL.md
3. For each SKILL.md directive, check implementation.js embodies it in code
4. Identify any gaps between docs and implementation
5. Apply any remaining fixes

## Success Criteria

- SKILL.md has prominent single-execution warning (not buried)
- implementation.js enforces Section → Frame hierarchy (no floating nodes)
- All 5 failure modes in LESSONS_LEARNED.md reflected in SKILL.md guidance
- Any remaining gaps closed in this experiment
