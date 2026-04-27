# Experiment H2: Pipeline Automation

**Hypothesis:** A pipeline-runner skill that auto-detects missing steps and triggers them in sequence would eliminate the manual trigger friction that causes 80-90% of expected outputs to be missing.

**Prediction:** A pipeline-runner can:
1. Detect which of the 5 pipeline steps (empathy → journey → persona → JTBD → AI-opps) are missing per project
2. Report a completion audit across all 9 projects
3. Provide a single-command `/research-pipeline [project]` that fills all gaps in order

**Status:** PROTOCOL LOCKED — 2026-04-27

---

## Design

### Pipeline Steps (in order)

1. **empathy-maps** — one `.md` per interview transcript
2. **journey** — user journey maps per persona
3. **personas** — persona synthesis from empathy maps
4. **jtbd** — Jobs-to-Be-Done analysis from personas
5. **ai-opportunities** — AI opportunity assessment from JTBD
6. **scenarios** — scenario maps (currently 80-90% missing)

### Gap Detection Algorithm

For each project:
```
completion_status = {
    step: (n_files_present / n_transcripts)
    for step in pipeline_steps
}
```

A step is "complete" if ≥ 80% of expected outputs exist.
Expected outputs for each step = number of interview transcripts.

### Deliverables

1. `code/pipeline_status.py` — audit script: runs across all 9 projects, prints completion matrix
2. `results/pipeline_status.md` — completion audit output
3. `.claude/skills/research-pipeline/SKILL.md` — the pipeline runner skill (new skill)

### Success Criteria

| Criterion | Success |
|-----------|---------|
| Status audit | Produces completion matrix for all 9 projects |
| Gap detection accurate | Correctly identifies which steps have <80% output coverage |
| pipeline-runner SKILL.md | Callable as /research-pipeline [project] |
| Scenario gap quantified | Exact count of missing scenario maps identified |
