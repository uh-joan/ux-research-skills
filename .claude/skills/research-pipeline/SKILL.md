---
name: research-pipeline
description: Auto-detects which UX research pipeline steps are missing for a project (or all projects) and runs them in sequence. Use when you want to fill pipeline gaps without manually triggering each skill, when new transcripts arrive and the downstream steps haven't been run, or when you want a completion audit across all projects. Replaces the manual skill-by-skill triggering workflow.
version: 1.0.0
author: researcher_ux platform research
tags: [Pipeline, Automation, Gap Detection, Orchestration, Empathy Maps, Personas, JTBD, AI Opportunities, Scenarios]
---

# Research Pipeline Skill

Auto-detects missing outputs and runs pipeline steps in sequence. Eliminates manual trigger friction.

**Research origin:** Validated by H2 experiment (2026-04-27) — 298-file gap found across 9 projects; scenario mapping is the universal bottleneck (only 13 files across all projects vs. ~45 expected).

## Trigger Modes

```
/research-pipeline                    → Audit all projects, show completion matrix
/research-pipeline DI&A               → Run missing steps for DI&A
/research-pipeline DI&A --dry-run     → Show what would run, don't execute
/research-pipeline all                → Fill all gaps across all projects (confirm first)
```

---

## Execution Workflow

### Step 0: Run Pipeline Audit

Always start by checking what's missing. Run this Python script (or manually inspect):

```python
from pathlib import Path

BASE = Path('.')
STEPS = {
    'transcripts': {'dir': 'transcripts', 'extensions': ['.md', '.txt', '.docx', '.vtt']},
    'empathy-maps': {'dir': 'empathy-maps', 'extensions': ['.md'], 'exclude': ['overview', 'clustering', 'template']},
    'journey': {'dir': 'journey', 'extensions': ['.md'], 'exclude': ['overview', 'template']},
    'personas': {'dir': 'personas', 'extensions': ['.md'], 'exclude': ['overview', 'template', 'summary']},
    'jtbd': {'dir': 'jtbd', 'extensions': ['.md'], 'exclude': ['overview', 'template', 'cross-persona', 'summary']},
    'ai-opportunities': {'dir': 'ai-opportunities', 'extensions': ['.md'], 'exclude': ['overview', 'template']},
    'scenarios': {'dir': 'scenarios', 'extensions': ['.md'], 'exclude': ['overview', 'template', 'summary']},
}

def count_files(d, step_config):
    path = d / step_config['dir']
    if not path.exists(): return 0
    return sum(1 for ext in step_config['extensions']
               for f in path.glob(f'*{ext}')
               if not any(ex in f.stem.lower() for ex in step_config.get('exclude', [])))

# Check single project
project = Path('DI&A')  # or Path(project_name)
n_tx = count_files(project, STEPS['transcripts'])
for step, cfg in STEPS.items():
    if step == 'transcripts': continue
    n = count_files(project, cfg)
    pct = n / n_tx if n_tx else 0
    status = '✅' if pct >= 0.8 else ('⚠️' if pct > 0 else '❌')
    print(f"  {status} {step}: {n}/{n_tx} ({pct:.0%})")
```

### Step 1: Determine Missing Steps

Pipeline steps in dependency order:
```
transcripts → empathy-maps → journey → personas → jtbd → ai-opportunities → scenarios
```

Each step requires the previous step to be ≥80% complete before running.

**Step completion rules (corrected for output type):**
- `empathy-maps`: complete if ≥80% of transcripts have an empathy map
- `journey`: complete if there are journey maps for each discovered persona
- `personas`: complete if ≥3 persona files exist
- `jtbd`: complete if JTBD files exist for each persona
- `ai-opportunities`: complete if at least 1 consolidated assessment exists
- `scenarios`: complete if ≥3 scenario files exist

### Step 2: Run Missing Steps In Order

For each missing step, invoke the corresponding skill:

| Pipeline Step | Skill to Invoke | Notes |
|--------------|----------------|-------|
| empathy-maps | `/empathy-map-generator [project]` | Run once per transcript |
| journey | `/user-journey [project]` | Requires personas to exist |
| personas | `/persona-generator [project]` | Synthesizes from empathy maps |
| jtbd | `/jtbd-analyzer [project]` | Requires personas |
| ai-opportunities | `/ai-opportunity-analyzer [project]` | Requires JTBD |
| scenarios | `/scenario-mapper [project]` | Requires JTBD clusters |

**Critical:** Always run in dependency order. Don't skip steps.

### Step 3: Report Completion

After running all steps, output a summary:
```
[project] pipeline completion:
  empathy-maps: ✅ 21/21 (100%)
  journey: ✅ 25/21 (119%)
  personas: ✅ 6/21 → now 6/6 per persona
  jtbd: ✅ 25/21 (119%)
  ai-opportunities: ✅ 1/1 (100%)
  scenarios: ⚠️ 3/~15 (20%) — run /scenario-mapper again for remaining JTBD clusters
```

---

## Known Gaps (from H2 audit, 2026-04-27)

| Project | Priority Gap | Skill to Run |
|---------|-------------|-------------|
| Fusion | JTBD completely missing (0 files) | `/jtbd-analyzer Fusion` → `/ai-opportunity-analyzer Fusion` |
| KAI | Personas missing (0 files), empathy incomplete | `/empathy-map-generator KAI` (5 missing) → `/persona-generator KAI` |
| All 9 | Scenarios severely under-generated (13 total, ~45 expected) | `/scenario-mapper [project]` for each |
| CDDI, DI&A, MT360 | AI opportunity assessment not generated | `/ai-opportunity-analyzer [project]` |

---

## Integration with Other Skills

This skill **reads from:**
- `[PROJECT]/transcripts/` (source of truth for project size)
- All pipeline output directories

This skill **feeds into:**
- All downstream skills (personas, JTBD, AI-opps, scenarios) — it's the orchestrator
- `empathy-clustering` — better inputs = better clustering
- `cross-project-synthesizer` — only useful when all projects are at JTBD+ step

---

## Performance Benchmarks (from H2 experiment)

| Metric | Value |
|--------|-------|
| Projects audited | 9 |
| Total transcripts | 106 |
| Gap identified | ~50-60 meaningful missing files |
| Audit script runtime | < 1 second |
| Scenario gap (universal) | 13 existing / ~45 expected |

---

## Reference Implementation

Pipeline status script: `platform-research/experiments/H2-pipeline-automation/code/pipeline_status.py`

Run anytime to get current completion status across all projects.
