# Experiment H9: Empathy Clustering Skill

**Hypothesis:** Productizing the H1 pipeline as a SKILL.md + implementation enables automatic
cross-domain FEELS clustering for any project with 3+ interviews.

**Prediction:** New skill produces clustering-analysis.md in <10 minutes for any project with 3+ empathy maps.

**Status:** PROTOCOL LOCKED — 2026-04-27

---

## What This Ships

A new `.claude/skills/empathy-clustering/SKILL.md` that:
1. Triggers on `/empathy-clustering [project]` or `/empathy-clustering` (auto-discovers all projects)
2. Runs the H1 UMAP+HDBSCAN pipeline
3. Outputs `[project]/empathy-maps/clustering-analysis.md` — equivalent to DI&A's manual version
4. Also includes the platform-level cluster naming with cross-domain universality scores

## Success Criteria

| Criterion | Success |
|-----------|---------|
| Single-project mode | Runs on one project in <10 minutes |
| Cross-project mode | Runs on all 9 projects, finds universal clusters |
| Output format | Matches DI&A's manual clustering-analysis.md structure |
| Quality | Names are intelligible; clusters match manual DI&A validation |
