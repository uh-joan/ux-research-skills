"""
H11: Traceability Audit
Measures quote density across JTBD and persona files.
Quote density = verbatim quotes per content section (## heading).
"""

import re
from pathlib import Path
from collections import defaultdict

BASE = Path(__file__).parent.parent.parent.parent.parent  # repo root

PROJECTS = ['DI&A', 'CPI', 'CDDI', 'Fusion', 'PT', 'MASS', 'MT360', 'KAI', 'OFFX']

STEPS = {
    'jtbd':     {'dir': 'jtbd',           'ext': '.md'},
    'personas': {'dir': 'personas',        'ext': '.md'},
    'scenarios':{'dir': 'scenarios',       'ext': '.md'},
    'ai-opps':  {'dir': 'ai-opportunities','ext': '.md'},
}

EXCLUDE = re.compile(r'overview|template|readme|status|batch|clustering', re.IGNORECASE)

# ── Quote detection ──────────────────────────────────────────────────────────

def count_quotes(text: str) -> int:
    """Count distinct verbatim quote instances in a markdown file."""
    quotes = 0
    for line in text.splitlines():
        stripped = line.strip()
        # Blockquote lines: > "..." or plain > text
        if stripped.startswith('>') and len(stripped) > 5:
            quotes += 1
            continue
        # Inline quotes: "capitalized phrase of ≥20 chars"
        inline = re.findall(r'"([A-Z][^"]{19,})"', stripped)
        quotes += len(inline)
    return quotes

def count_sections(text: str) -> int:
    """Count ## or ### headings (content sections)."""
    return len(re.findall(r'^#{2,3} ', text, re.MULTILINE))

def quote_density(text: str) -> float:
    """Quotes per section. Returns raw quote count if no sections found."""
    q = count_quotes(text)
    s = max(count_sections(text), 1)
    return round(q / s, 2)

# ── Per-file audit ───────────────────────────────────────────────────────────

def audit_files(project: str, step: str) -> list[dict]:
    step_cfg = STEPS[step]
    d = BASE / project / step_cfg['dir']
    if not d.exists():
        return []
    results = []
    for f in sorted(d.glob(f"*{step_cfg['ext']}")):
        if EXCLUDE.search(f.name):
            continue
        text = f.read_text(encoding='utf-8', errors='ignore')
        q = count_quotes(text)
        s = count_sections(text)
        dens = round(q / max(s, 1), 2)
        results.append({
            'project': project,
            'step': step,
            'file': f.name,
            'quotes': q,
            'sections': s,
            'density': dens,
            'flag': dens < 0.3,  # low traceability threshold
        })
    return results

# ── Project-level pipeline completeness ─────────────────────────────────────

PROJECT_EXPECTED = {
    'personas':  (3, 6),   # (min_ok, max_expected)
    'scenarios': (1, 3),
    'ai-opps':   (1, 2),
}

def project_completeness(project: str) -> dict:
    txn_count = len(list((BASE / project / 'transcripts').glob('*'))) if (BASE / project / 'transcripts').exists() else 0
    row = {'project': project, 'transcripts': txn_count}
    for step, (min_ok, _) in PROJECT_EXPECTED.items():
        step_cfg = STEPS[step]
        d = BASE / project / step_cfg['dir']
        if not d.exists():
            count = 0
        else:
            count = len([f for f in d.glob(f"*{step_cfg['ext']}") if not EXCLUDE.search(f.name)])
        status = '✅' if count >= min_ok else ('⚠️' if count > 0 else '❌')
        row[step] = f"{status} {count}"
    return row

# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    all_records = []
    for proj in PROJECTS:
        for step in STEPS:
            all_records.extend(audit_files(proj, step))

    # ── Quote density summary by project + step ──────────────────────────────
    print("\n=== QUOTE DENSITY BY PROJECT (avg quotes/section) ===")
    print(f"{'Project':<10} {'JTBD':>8} {'Personas':>10} {'Scenarios':>10} {'AI-Opps':>10}  Files  Low%")
    print("-" * 65)

    by_proj_step = defaultdict(list)
    for r in all_records:
        by_proj_step[(r['project'], r['step'])].append(r['density'])

    project_summaries = {}
    for proj in PROJECTS:
        jtbd_d   = by_proj_step.get((proj, 'jtbd'), [])
        pers_d   = by_proj_step.get((proj, 'personas'), [])
        scen_d   = by_proj_step.get((proj, 'scenarios'), [])
        ai_d     = by_proj_step.get((proj, 'ai-opps'), [])
        all_d    = jtbd_d + pers_d + scen_d + ai_d
        low_pct  = round(100 * sum(1 for r in all_records if r['project'] == proj and r['flag']) / max(len(all_d), 1))

        def fmt(lst): return f"{sum(lst)/len(lst):.2f}" if lst else "—"
        print(f"{proj:<10} {fmt(jtbd_d):>8} {fmt(pers_d):>10} {fmt(scen_d):>10} {fmt(ai_d):>10}  {len(all_d):>4}  {low_pct:>3}%")
        project_summaries[proj] = {
            'jtbd': sum(jtbd_d)/len(jtbd_d) if jtbd_d else None,
            'personas': sum(pers_d)/len(pers_d) if pers_d else None,
            'n_files': len(all_d),
            'low_pct': low_pct,
        }

    # ── Low-traceability files ───────────────────────────────────────────────
    flagged = [r for r in all_records if r['flag']]
    print(f"\n=== LOW-TRACEABILITY FILES (density < 0.30) — {len(flagged)} files ===")
    if flagged:
        print(f"{'Project':<10} {'Step':<12} {'File':<50} {'Density':>8}")
        print("-" * 85)
        for r in sorted(flagged, key=lambda x: x['density']):
            print(f"{r['project']:<10} {r['step']:<12} {r['file']:<50} {r['density']:>8.2f}")
    else:
        print("None found.")

    # ── Project-level pipeline completeness (corrected) ─────────────────────
    print("\n=== PIPELINE COMPLETENESS (project-level denominators) ===")
    print(f"{'Project':<10} {'TXN':>5} {'Personas':>12} {'Scenarios':>12} {'AI-Opps':>12}")
    print("-" * 55)
    for proj in PROJECTS:
        row = project_completeness(proj)
        print(f"{row['project']:<10} {row['transcripts']:>5} {row['personas']:>12} {row['scenarios']:>12} {row['ai-opps']:>12}")

    # ── Overall stats ────────────────────────────────────────────────────────
    total = len(all_records)
    flagged_n = len(flagged)
    avg_jtbd = [r['density'] for r in all_records if r['step'] == 'jtbd']
    avg_pers = [r['density'] for r in all_records if r['step'] == 'personas']
    print(f"\n=== SUMMARY ===")
    print(f"Total files audited: {total}")
    print(f"Low-traceability (<0.30): {flagged_n} ({round(100*flagged_n/max(total,1))}%)")
    print(f"Avg JTBD quote density: {sum(avg_jtbd)/len(avg_jtbd):.2f}" if avg_jtbd else "No JTBD files")
    print(f"Avg persona quote density: {sum(avg_pers)/len(avg_pers):.2f}" if avg_pers else "No persona files")

if __name__ == '__main__':
    main()
