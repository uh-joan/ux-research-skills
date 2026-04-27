# Experiment H7: Pain-Point Matrix Auto-Generation

**Hypothesis:** Refactoring pain-point-matrix to auto-read from existing empathy maps + journey maps (rather than requiring manual input) would fill the biggest current output gap across all 9 projects.

**Prediction:** Updated skill would produce complete pain matrices for all 9 projects using 400+ existing files as inputs.

**Status:** PROTOCOL LOCKED — 2026-04-27

---

## The Gap

Current state:
- pain-point-matrix skill exists with full SKILL.md
- Only 1 pain matrix file exists across all 9 projects (CPI only)
- Root cause: skill expects manually compiled pain list as input; users don't want to do this extraction step
- The data EXISTS — empathy map FEELS quadrants + journey map pain-point sections

## Fix Design

### Current SKILL.md trigger pattern:
```
/pain-point-matrix [domain] [pain-list-or-manual-input]
```

### New SKILL.md trigger pattern:
```
/pain-point-matrix [domain]
```
The skill should:
1. Auto-detect domain folder
2. Scan all `[domain]/empathy-maps/*.md` → extract FEELS quadrant items
3. Scan all `[domain]/journey/*.md` → extract Pain Points sections from each phase
4. Scan `[domain]/jtbd/*.md` → extract switching triggers (proxy for pain intensity)
5. Deduplicate and merge (same pain mentioned in empathy map + journey map = same row)
6. Auto-score severity (from FEELS intensity ratings: 🔴=high, 🟡=medium, 🟢=low) 
7. Auto-score frequency (from JTBD frequency labels: "daily" > "weekly" > "monthly")
8. Plot the 2×2 matrix and generate prioritized roadmap

### Parsing patterns to implement

**From empathy maps (FEELS section):**
```
- 🔴 Overwhelmed by data volume (8/10) — feeling: anxious
  → Pain: "Data volume overwhelm", Severity: 8, Frequency: needs journey data
```

**From journey maps (Pain Points per phase):**
```
| Phase | Pain Point | Severity | Frequency |
|-------|-----------|----------|-----------|
| Data Collection | Manual triangulation across 5 vendors | 9/10 | daily |
```

**From JTBD (switching triggers):**
```
Switching Triggers:
- ⏰ Time: "If I could eliminate the 3-hour manual consolidation..." → Frequency: high
- 🎯 Quality: "If data gaps for ultra-rare diseases were filled..." → Severity: 8/10
```

## Validation

Test on DI&A first:
- 9 empathy maps + 9 journey maps + 9 JTBD files → should auto-generate pain matrix
- Compare to DI&A's manually known top pains (data triangulation 9.2/10, vendor gaps 8.8/10)
- Check: does auto-extraction match manual ranking?

## SKILL.md Changes Required

1. Add auto-discovery section: "scan empathy-maps/ and journey/ folders"
2. Add extraction logic description with file format examples
3. Add deduplication instruction: "merge pains mentioned in 3+ sources as high-confidence"
4. Add confidence scoring: "n/9 sources" labeling for each pain point
5. Keep manual override: user can still provide explicit pain list if auto-discovery fails

## Success Criteria

| Criterion | Success | Failure |
|-----------|---------|---------|
| Auto-discovery | DI&A pain matrix generated without manual input | Requires manual list |
| Top pain accuracy | Top 3 pains match known DI&A ranking | Wrong order or different pains |
| Coverage | All 9 projects get matrices after skill update | Only projects with complete data |
| Confidence labels | Each pain shows source count "n/9 users" | No source attribution |

## Estimated Effort

- SKILL.md update: 2-3 hours
- Validation on DI&A: 30 min
- Rollout to all 9 projects: skill auto-runs once updated

## Impact

Directly fills the biggest output gap: 0 pain matrices across 8 projects → 9 matrices immediately after skill update. No new interviews needed — all input data already exists.
