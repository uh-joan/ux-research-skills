#!/usr/bin/env python3.11
"""
H2: Pipeline status audit.
Scans all 9 projects and reports completion % per pipeline step.
"""

from pathlib import Path
import json, re

BASE = Path('/Users/joan.saez-pons/code/researcher_ux')

STEPS = {
    'transcripts': {'dir': 'transcripts', 'extensions': ['.md', '.txt', '.docx', '.vtt']},
    'empathy-maps': {'dir': 'empathy-maps', 'extensions': ['.md'], 'exclude': ['overview', 'clustering', 'template']},
    'journey': {'dir': 'journey', 'extensions': ['.md'], 'exclude': ['overview', 'template']},
    'personas': {'dir': 'personas', 'extensions': ['.md'], 'exclude': ['overview', 'template', 'summary']},
    'jtbd': {'dir': 'jtbd', 'extensions': ['.md'], 'exclude': ['overview', 'template', 'cross-persona', 'summary']},
    'ai-opportunities': {'dir': 'ai-opportunities', 'extensions': ['.md'], 'exclude': ['overview', 'template']},
    'scenarios': {'dir': 'scenarios', 'extensions': ['.md'], 'exclude': ['overview', 'template', 'summary']},
}

def count_files(project_dir, step_config):
    d = project_dir / step_config['dir']
    if not d.exists():
        return 0
    excludes = step_config.get('exclude', [])
    count = 0
    for ext in step_config['extensions']:
        for f in d.glob(f'*{ext}'):
            if not any(ex in f.stem.lower() for ex in excludes):
                count += 1
    return count

# Discover projects
projects = []
for d in sorted(BASE.iterdir()):
    if d.is_dir() and not d.name.startswith('.') and not d.name.startswith('platform') and (d / 'transcripts').exists():
        projects.append(d)

print(f"Found {len(projects)} projects with transcripts")
print()

results = {}
for proj in projects:
    n_transcripts = count_files(proj, STEPS['transcripts'])
    if n_transcripts == 0:
        continue

    row = {'n_transcripts': n_transcripts, 'steps': {}}
    for step_name, step_config in STEPS.items():
        if step_name == 'transcripts':
            continue
        n = count_files(proj, step_config)
        pct = round(n / n_transcripts, 2) if n_transcripts > 0 else 0
        row['steps'][step_name] = {'n': n, 'pct': pct, 'complete': pct >= 0.8}

    results[proj.name] = row

# Print completion matrix
STEP_NAMES = ['empathy-maps', 'journey', 'personas', 'jtbd', 'ai-opportunities', 'scenarios']
col_w = 14

header = f"{'Project':<12} {'TXN':>4} " + " ".join(f"{s[:col_w]:>{col_w}}" for s in STEP_NAMES)
print(header)
print('-' * len(header))

for proj_name, row in results.items():
    cols = [f"{proj_name:<12}", f"{row['n_transcripts']:>4}"]
    for step in STEP_NAMES:
        d = row['steps'].get(step, {'n': 0, 'pct': 0, 'complete': False})
        pct_str = f"{d['pct']:.0%}"
        flag = '✅' if d['complete'] else ('⚠️' if d['pct'] > 0 else '❌')
        cols.append(f"{flag} {pct_str:>4} ({d['n']:>2})".rjust(col_w))
    print(" ".join(cols))

print()

# Summary stats
total_transcripts = sum(r['n_transcripts'] for r in results.values())
print(f"SUMMARY:")
print(f"  Total transcripts: {total_transcripts} across {len(results)} projects")
print()
for step in STEP_NAMES:
    total_expected = sum(r['n_transcripts'] for r in results.values())
    total_actual = sum(r['steps'].get(step, {}).get('n', 0) for r in results.values())
    n_complete_projects = sum(1 for r in results.values() if r['steps'].get(step, {}).get('complete', False))
    pct = round(total_actual / total_expected, 2) if total_expected else 0
    print(f"  {step:<20} {total_actual:>3}/{total_expected} files ({pct:.0%}) — {n_complete_projects}/{len(results)} projects complete")

print()

# Gap report
print("GAPS (steps with <80% coverage):")
gaps = []
for proj_name, row in results.items():
    for step in STEP_NAMES:
        d = row['steps'].get(step, {'n': 0, 'pct': 0})
        if d['pct'] < 0.8:
            gaps.append({
                'project': proj_name,
                'step': step,
                'have': d['n'],
                'need': row['n_transcripts'],
                'missing': row['n_transcripts'] - d['n'],
                'pct': d['pct'],
            })

for g in sorted(gaps, key=lambda x: x['missing'], reverse=True):
    print(f"  {g['project']:<12} {g['step']:<20} missing {g['missing']:>2} files ({g['pct']:.0%} complete)")

print(f"\n  Total gap: {sum(g['missing'] for g in gaps)} files across {len(set(g['project'] for g in gaps))} projects")

# Save results
out = BASE / 'platform-research/experiments/H2-pipeline-automation/results/pipeline_status.json'
out.parent.mkdir(parents=True, exist_ok=True)
with open(out, 'w') as f:
    json.dump({'projects': results, 'gaps': gaps}, f, indent=2)

print(f"\nSaved: {out}")
