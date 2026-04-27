"""
H12: Scenario Depth Root-Cause Analysis
Compares JTBD job count vs scenario count per project to determine
whether the depth gap is data-limited or prompt-limited.
"""

import re
from pathlib import Path
from collections import defaultdict

BASE = Path(__file__).parent.parent.parent.parent.parent  # repo root

PROJECTS = ['DI&A', 'CPI', 'CDDI', 'Fusion', 'PT', 'MASS', 'MT360', 'KAI', 'OFFX']

EXCLUDE = re.compile(r'template|readme|status|batch|clustering', re.IGNORECASE)

# ── JTBD job counter ─────────────────────────────────────────────────────────

JOB_PATTERNS = [
    re.compile(r'^#{1,3} Job[\s\d:]', re.MULTILINE),         # ## Job 1: ...
    re.compile(r'^\*\*Job.*?:\*\*', re.MULTILINE),            # **Job Title:**
    re.compile(r'^- \*\*Job Statement', re.MULTILINE),        # - **Job Statement
    re.compile(r'^## JTBD[\s\d]+', re.MULTILINE),             # ## JTBD 1
    re.compile(r'When .{5,80}, I want to .{5,80}, so I can', re.IGNORECASE),  # job statement inline
]

CONFIDENCE_PATTERNS = [
    re.compile(r'confidence.*?high', re.IGNORECASE),
    re.compile(r'high.*?confidence', re.IGNORECASE),
    re.compile(r'confidence.*?medium', re.IGNORECASE),
    re.compile(r'n=\d+', re.IGNORECASE),
]

def count_jtbd_jobs(text: str) -> int:
    """Count distinct JTBD job entries. Use the most specific pattern that fires."""
    # Try structural headings first (most reliable)
    heading_matches = len(re.findall(r'^#{1,3}\s+(?:Job|JTBD)\s*\d+', text, re.MULTILINE))
    if heading_matches >= 2:
        return heading_matches

    # Try inline job statements
    inline = len(re.findall(r'When .{5,80}I want to .{5,80}so I can', text, re.IGNORECASE))
    if inline >= 2:
        return inline

    # Fallback: count bold job headers
    bold = len(re.findall(r'\*\*(?:Job|JTBD)[^*]+\*\*', text, re.IGNORECASE))
    return max(heading_matches, inline, bold)


def audit_project_jtbd(project: str) -> dict:
    d = BASE / project / 'jtbd'
    if not d.exists():
        return {'project': project, 'jtbd_files': 0, 'total_jobs': 0, 'jobs_per_file': 0.0}

    files = [f for f in sorted(d.glob('*.md')) if not EXCLUDE.search(f.name)]
    total_jobs = 0
    file_details = []
    for f in files:
        text = f.read_text(encoding='utf-8', errors='ignore')
        jobs = count_jtbd_jobs(text)
        total_jobs += jobs
        file_details.append({'file': f.name, 'jobs': jobs})

    return {
        'project': project,
        'jtbd_files': len(files),
        'total_jobs': total_jobs,
        'jobs_per_file': round(total_jobs / max(len(files), 1), 1),
        'file_details': file_details,
    }


def audit_project_scenarios(project: str) -> dict:
    d = BASE / project / 'scenarios'
    if not d.exists():
        return {'project': project, 'scenario_files': 0, 'total_scenarios': 0}

    files = [f for f in sorted(d.glob('*.md')) if not EXCLUDE.search(f.name)]
    total_scenarios = 0
    for f in files:
        text = f.read_text(encoding='utf-8', errors='ignore')
        # Count distinct scenario sections
        n = len(re.findall(r'^#{1,3}\s+Scenario\s+\d+', text, re.MULTILINE))
        if n == 0:
            # Fallback: count H2 headings as proxy
            n = max(len(re.findall(r'^## ', text, re.MULTILINE)) - 2, 1)
        total_scenarios += n

    return {
        'project': project,
        'scenario_files': len(files),
        'total_scenarios': total_scenarios,
    }


def main():
    print("\n=== H12: SCENARIO DEPTH ROOT-CAUSE ANALYSIS ===\n")
    print(f"{'Project':<10} {'JTBD Files':>12} {'Jobs Total':>12} {'Scen Files':>12} {'Scen Count':>12}  {'Ratio':>7}  Assessment")
    print("-" * 90)

    confirmatory = 0
    disconfirmatory = 0

    for proj in PROJECTS:
        j = audit_project_jtbd(proj)
        s = audit_project_scenarios(proj)

        jobs = j['total_jobs']
        scens = s['total_scenarios']
        scen_files = s['scenario_files']
        ratio = round(jobs / max(scens, 1), 1)

        # Assessment logic
        if jobs >= 5 and scen_files == 1 and scens <= 3:
            assessment = "⚠️  prompt-limited"
            confirmatory += 1
        elif jobs <= 3:
            assessment = "ℹ️  data-limited"
            disconfirmatory += 1
        elif scens >= 4:
            assessment = "✅ good depth"
        else:
            assessment = "〰  borderline"

        print(f"{proj:<10} {j['jtbd_files']:>12} {jobs:>12} {scen_files:>12} {scens:>12}  {ratio:>7}  {assessment}")

    print(f"\n{'─'*90}")
    print(f"Confirmatory (prompt-limited): {confirmatory} projects")
    print(f"Disconfirmatory (data-limited): {disconfirmatory} projects")
    print(f"\n{'─'*90}")

    # Per-project JTBD file breakdown for depth check
    print("\n=== JTBD JOB COUNTS PER FILE (spot-check) ===")
    for proj in ['DI&A', 'CPI', 'PT', 'MASS']:
        j = audit_project_jtbd(proj)
        print(f"\n{proj} — {j['jtbd_files']} JTBD files, {j['total_jobs']} total jobs:")
        for fd in j.get('file_details', []):
            print(f"  {fd['file']:<55} {fd['jobs']:>3} jobs")


if __name__ == '__main__':
    main()
