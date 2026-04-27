#!/usr/bin/env python3.11
"""
H3: Prompt quality analysis across all empathy maps.
Computes quality metrics and identifies prompt weaknesses.
"""

import re, json, statistics
from pathlib import Path
from collections import defaultdict

BASE = Path('/Users/joan.saez-pons/code/researcher_ux')

SKIP = re.compile(
    r'^(?:dominant emotion|emotional trajectory|evidence:|impact:|emotion:|'
    r'emotional arc|overall|summary|primary emotion|key emotion)',
    re.IGNORECASE
)

# ── Quality metric functions ──────────────────────────────────────────────────

def analyze_empathy_map(path):
    text = path.read_text(encoding='utf-8', errors='ignore')
    metrics = {}

    # FEELS section — use position-based extraction to avoid regex \Z collapse bug
    feels_hdr = re.search(r'##\s*(?:💭\s*)?(?:\d+\.)?\s*FEELS[^\n]*\n', text, re.IGNORECASE)
    if feels_hdr:
        start = feels_hdr.end()
        next_sec = re.search(r'\n## ', text[start:])
        feels_text = text[start : start + (next_sec.start() if next_sec else len(text[start:]))]
    if feels_hdr:
        entries = []
        for line in feels_text.split('\n'):
            s = line.strip()
            # Format A
            ma = re.match(r'^(?:[-*]\s+)?\*\*([^\*:]+)\*\*\s+(.+)', s)
            if ma and not SKIP.match(ma.group(1)):
                emo = re.sub(r'^[\U0001F000-\U0001FFFF\U00002600-\U000027FF☀-➿\s]+', '', ma.group(1)).strip()
                desc = ma.group(2).strip()
                if len(desc) > 5:
                    entries.append({'emotion': emo, 'description': desc})
            # Format B
            mb = re.match(r'^[-*]\s+\*\*([^\*]+):\*\*\s+(.+)', s)
            if mb and not SKIP.match(mb.group(1)):
                emo = re.sub(r'^[\U0001F000-\U0001FFFF\U00002600-\U000027FF☀-➿\s]+', '', mb.group(1)).strip()
                desc = mb.group(2).strip()
                if len(desc) > 5:
                    entries.append({'emotion': emo, 'description': desc})

        metrics['feels_count'] = len(entries)
        unique_emotions = set(e['emotion'].lower()[:20] for e in entries if e['emotion'])
        metrics['emotion_diversity'] = len(unique_emotions) / max(len(entries), 1)
        if entries:
            word_counts = [len(e['description'].split()) for e in entries]
            metrics['avg_description_words'] = round(statistics.mean(word_counts), 1)
            metrics['min_description_words'] = min(word_counts)
        else:
            metrics['avg_description_words'] = 0
            metrics['min_description_words'] = 0
    if not feels_hdr:
        metrics['feels_count'] = 0
        metrics['emotion_diversity'] = 0
        metrics['avg_description_words'] = 0
        metrics['min_description_words'] = 0

    # SAYS section — quote density (lines with " or quotation marks)
    says_hdr = re.search(r'##\s*(?:💬\s*)?(?:\d+\.)?\s*SAYS[^\n]*\n', text, re.IGNORECASE)
    if says_hdr:
        s_start = says_hdr.end()
        s_next = re.search(r'\n## ', text[s_start:])
        says_content = text[s_start : s_start + (s_next.start() if s_next else len(text[s_start:]))]
        says_lines = [l.strip() for l in says_content.split('\n') if l.strip().startswith(('-', '*', '>'))]
        quoted = sum(1 for l in says_lines if '"' in l or '“' in l or '”' in l or "'" in l)
        metrics['says_lines'] = len(says_lines)
        metrics['quote_density'] = round(quoted / max(len(says_lines), 1), 2)
    else:
        metrics['says_lines'] = 0
        metrics['quote_density'] = 0

    # Format compliance — correct bold+emoji pattern
    format_a = len(re.findall(r'\*\*[\U0001F000-\U0001FFFF\U00002600-\U000027FF☀-➿]', text))
    metrics['emoji_bold_count'] = format_a

    # Overall section completeness
    sections = ['SAYS', 'THINKS', 'DOES', 'FEELS']
    present = sum(1 for s in sections if re.search(rf'##.*{s}', text, re.IGNORECASE))
    metrics['sections_complete'] = present
    metrics['has_all_sections'] = present == 4

    # File size as proxy for depth
    metrics['word_count'] = len(text.split())

    return metrics


def quality_score(m):
    """Composite quality score 0-10."""
    score = 0
    # FEELS richness (0-4 pts)
    score += min(4, m['feels_count'] / 4)
    # Emotion diversity (0-2 pts)
    score += m['emotion_diversity'] * 2
    # Description depth (0-2 pts)
    score += min(2, m['avg_description_words'] / 10)
    # Quote density in SAYS (0-1 pt)
    score += m['quote_density']
    # Section completeness (0-1 pt)
    score += m['sections_complete'] / 4
    return round(score, 2)


# ── Scan all projects ─────────────────────────────────────────────────────────

EXCLUDE = ['overview', 'clustering', 'template', 'automated']
all_results = {}

projects = [d for d in sorted(BASE.iterdir())
            if d.is_dir() and not d.name.startswith('.') and (d / 'empathy-maps').exists()]

for proj in projects:
    emp_dir = proj / 'empathy-maps'
    files = [f for f in emp_dir.glob('*.md')
             if not any(ex in f.stem.lower() for ex in EXCLUDE)]
    if not files:
        continue

    proj_results = []
    for f in files:
        m = analyze_empathy_map(f)
        m['file'] = f.name
        m['project'] = proj.name
        m['quality_score'] = quality_score(m)
        proj_results.append(m)

    all_results[proj.name] = proj_results


# ── Print summary ─────────────────────────────────────────────────────────────

print(f"\n{'='*70}")
print("H3: EMPATHY MAP QUALITY ANALYSIS")
print(f"{'='*70}")

print(f"\n{'Project':<10} {'Maps':>5} {'Avg FEELS':>10} {'Avg Words':>10} {'Avg Q':>8} {'Min Q':>7} {'Format':>8}")
print('-'*60)

all_scores = []
project_summaries = {}
for proj_name, results in all_results.items():
    scores = [r['quality_score'] for r in results]
    feels = [r['feels_count'] for r in results]
    words = [r['avg_description_words'] for r in results]
    fmt = [r['emoji_bold_count'] for r in results]
    all_scores.extend(scores)
    project_summaries[proj_name] = {
        'n': len(results),
        'avg_quality': round(statistics.mean(scores), 2),
        'min_quality': round(min(scores), 2),
        'avg_feels': round(statistics.mean(feels), 1),
        'avg_words': round(statistics.mean(words), 1),
        'avg_format': round(statistics.mean(fmt), 1),
        'results': results,
    }
    print(f"{proj_name:<10} {len(results):>5} {statistics.mean(feels):>10.1f} {statistics.mean(words):>10.1f} "
          f"{statistics.mean(scores):>8.2f} {min(scores):>7.2f} {statistics.mean(fmt):>8.1f}")

print(f"\nOverall: {len(all_scores)} maps, avg quality {statistics.mean(all_scores):.2f}, "
      f"std {statistics.stdev(all_scores):.2f}")

# ── Identify outliers ─────────────────────────────────────────────────────────

print(f"\n{'='*50}")
print("LOW-QUALITY OUTLIERS (quality < 3.0)")
print(f"{'='*50}")

low_quality = []
for proj_name, results in all_results.items():
    for r in results:
        if r['quality_score'] < 3.0:
            low_quality.append(r)
            print(f"\n  [{proj_name}] {r['file']}")
            print(f"    Quality: {r['quality_score']} | FEELS: {r['feels_count']} | "
                  f"Avg words: {r['avg_description_words']} | Sections: {r['sections_complete']}/4")
            print(f"    Quote density: {r['quote_density']} | Emoji-bold: {r['emoji_bold_count']}")

if not low_quality:
    print("  None found (all maps score ≥ 3.0)")

# ── Variance analysis ─────────────────────────────────────────────────────────

print(f"\n{'='*50}")
print("QUALITY VARIANCE BY METRIC")
print(f"{'='*50}")

all_flat = [r for results in all_results.values() for r in results]
metrics_to_check = ['feels_count', 'emotion_diversity', 'avg_description_words', 'quote_density']

for metric in metrics_to_check:
    vals = [r[metric] for r in all_flat]
    if vals:
        mean = statistics.mean(vals)
        std = statistics.stdev(vals) if len(vals) > 1 else 0
        cv = std / mean if mean > 0 else 0
        low_pct = sum(1 for v in vals if v < mean * 0.5) / len(vals)
        print(f"\n  {metric}:")
        print(f"    Mean: {mean:.2f} | Std: {std:.2f} | CV: {cv:.0%} | "
              f"Maps <50% mean: {low_pct:.0%}")

# ── Project-level weaknesses ──────────────────────────────────────────────────

print(f"\n{'='*50}")
print("PROMPT WEAKNESS DIAGNOSIS")
print(f"{'='*50}")

weaknesses = []

for proj_name, summary in project_summaries.items():
    issues = []
    if summary['avg_feels'] < 6:
        issues.append(f"Low FEELS count ({summary['avg_feels']:.1f} avg) — prompt doesn't require minimum entries")
    if summary['avg_words'] < 8:
        issues.append(f"Thin descriptions ({summary['avg_words']:.1f} words avg) — prompt allows one-word emotions")
    if summary['avg_format'] < 2:
        issues.append(f"Poor emoji format ({summary['avg_format']:.1f} emoji-bold avg) — format instruction unclear")
    if summary['n'] > 0:
        low_section = sum(1 for r in summary['results'] if not r['has_all_sections'])
        if low_section > 0:
            issues.append(f"{low_section}/{summary['n']} maps missing sections — section headers not enforced")

    if issues:
        print(f"\n  [{proj_name}]")
        for issue in issues:
            print(f"    ⚠️  {issue}")
        weaknesses.extend(issues)

if not weaknesses:
    print("  No systematic weaknesses detected — output quality is consistent")

# ── Save results ──────────────────────────────────────────────────────────────

out = BASE / 'platform-research/experiments/H3-dspy-prompt-optimization/results/quality_analysis.json'
serializable = {
    proj: [
        {k: v for k, v in r.items() if k != 'results'}
        for r in results
    ]
    for proj, results in all_results.items()
}
with open(out, 'w') as f:
    json.dump({'maps': serializable, 'summaries': {
        k: {kk: vv for kk, vv in v.items() if kk != 'results'}
        for k, v in project_summaries.items()
    }}, f, indent=2)

print(f"\nSaved: {out}")
print(f"\nH3 STATUS: {len(all_flat)} maps analyzed, {len(low_quality)} low-quality outliers, {len(weaknesses)} weaknesses found")
