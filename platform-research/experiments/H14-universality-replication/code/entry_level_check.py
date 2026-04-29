#!/usr/bin/env python3
"""
H14b: Entry-level universality replication.
For each project, extract actual FEELS entries and compute cosine similarity
to each H1 cluster description. If ANY entry exceeds the threshold, the project
independently 'has' that H1 cluster.

This is more robust than label-level comparison (H14a) because entries contain
the actual content (activities + emotions), not just emotion words.
"""

import re, json
from pathlib import Path
import numpy as np

BASE = Path('/Users/joan.saez-pons/code/researcher_ux')

H1_CLUSTERS = [
    {'id': 0, 'name': 'AI Opportunity-Threat Ambivalence', 'h1_products': 7,
     'description': 'AI tools promising but untrustworthy. Fear of skill atrophy. Hope for automation combined with anxiety about displacement. Excited about AI AND worried it replaces jobs. Cannot verify AI methodology.'},
    {'id': 1, 'name': 'Expert Achievement Satisfaction', 'h1_products': 8,
     'description': 'Pride in expertise and deep domain knowledge. Satisfaction from completing complex analysis. Energized by strategic impact. Fulfilled when work succeeds. Recognition valued.'},
    {'id': 2, 'name': 'Methodological Confidence in Triangulation', 'h1_products': 8,
     'description': 'Trusts own process when rigorous. Confidence from cross-validation across multiple sources. Methodological pride. Strategic thinking clarity. Analytical certainty.'},
    {'id': 3, 'name': 'Vendor Commercial Friction', 'h1_products': 7,
     'description': 'Frustrated by vendor pricing. Hopeful for vendor innovation. Consulting cost burden. Appreciation for Clarivate or other vendors mixed with frustration at tool limitations and data gaps.'},
    {'id': 4, 'name': 'Strategic Isolation & Disruption Anxiety', 'h1_products': 7,
     'description': 'Anxious about being the only person with this knowledge. Solo operator pressure. Fear of organizational irrelevance. AI displacement anxiety. CI function isolation.'},
    {'id': 5, 'name': 'Constant Urgency Pressure', 'h1_products': 7,
     'description': 'Deliver everything yesterday. Deadline pressure. Stretched thin across multiple simultaneous demands. Launch mode stress. Time poverty. Wary but focused under constant pressure.'},
    {'id': 6, 'name': 'Tool Navigation Friction', 'h1_products': 7,
     'description': 'Frustrated by slow tools and cumbersome interfaces. Too many clicks. Hunting and pecking. Platform usability problems. Workflow interrupted by tool limitations and navigation lag.'},
    {'id': 7, 'name': 'Process Verification Anxiety', 'h1_products': 6,
     'description': 'Need to double-check and verify every AI output. Cannot trust automated results. Accuracy stakes are high. Compliance verification burden. Worried about errors in high-stakes decisions.'},
    {'id': 8, 'name': 'Data Fragmentation Fatigue', 'h1_products': 7,
     'description': 'Manually piecing data from multiple fragmented sources. Data silos across IQVIA, DRG, Clarivate, Excel. Triangulation burden. Frustrated by lack of unified data layer. Multiple vendor portals.'},
    {'id': 9, 'name': 'Manual Correction Burden at Scale', 'h1_products': 8,
     'description': 'Correcting data across markets manually. Formulary name mapping burden. Payer ID mismatch reconciliation. Data cleaning at scale. Half-day Excel manipulation sessions. Overwhelmed by manual correction volume.'},
    {'id': 10, 'name': 'Vendor Partnership Dependency', 'h1_products': 5,
     'description': 'Collaborative but vulnerable to vendor deprecation. Appreciation for vendor relationship combined with dependency anxiety. Hoping vendor will innovate. Consulting reliance.'},
]

PROJECTS = ['DI&A', 'CPI', 'CDDI', 'Fusion', 'PT', 'MASS', 'MT360', 'KAI', 'OFFX']

SKIP = re.compile(
    r'^(?:dominant emotion|emotional trajectory|evidence:|impact:|emotion:|'
    r'emotional arc|overall|summary|primary emotion|key emotion)',
    re.IGNORECASE
)


def extract_feels(path):
    content = Path(path).read_text(encoding='utf-8', errors='ignore')
    m = re.search(r'##\s*(?:💭\s*)?(?:\d+\.)?\s*FEELS[^\n]*\n', content, re.IGNORECASE)
    if not m:
        return []
    start = m.end()
    next_sec = re.search(r'\n## (?!#)', content[start:])
    feels_text = content[start: start + (next_sec.start() if next_sec else len(content[start:]))]
    entries = []
    for line in feels_text.split('\n'):
        s = line.strip()
        # Format A: **Emotion** description
        m2 = re.match(r'^(?:[-*]\s+)?\*\*([^\*:]+)\*\*\s+(.+)', s)
        if m2 and not SKIP.match(m2.group(1)):
            emo = re.sub(r'^[\U0001F000-\U0001FFFF\U00002600-\U000027FF\U00002702-\U000027B0\s]+', '', m2.group(1)).strip()
            text = f"{emo}: {m2.group(2).strip()}" if emo else m2.group(2).strip()
            if len(text) > 15:
                entries.append(text)
            continue
        # Format B: **emoji Label:** description  (MASS format)
        m3 = re.match(r'^[-*]\s+\*\*([^\*]+):\*\*\s+(.+)', s)
        if m3 and not SKIP.match(m3.group(1)):
            raw = m3.group(1).rstrip(':').strip()
            emo = re.sub(r'^[\U0001F000-\U0001FFFF\U00002600-\U000027FF\U00002702-\U000027B0\s]+', '', raw).strip()
            text = f"{emo}: {m3.group(2).strip()}" if emo else m3.group(2).strip()
            if len(text) > 15:
                entries.append(text)
    return entries


def main():
    from sentence_transformers import SentenceTransformer
    from scipy.spatial.distance import cosine
    from scipy.stats import spearmanr

    print("H14b: Entry-Level Universality Replication")
    print("=" * 65)

    model = SentenceTransformer('all-MiniLM-L6-v2')

    # Embed H1 cluster descriptions
    h1_texts = [c['description'] for c in H1_CLUSTERS]
    h1_embeddings = model.encode(h1_texts, show_progress_bar=False)
    print(f"Encoded {len(H1_CLUSTERS)} H1 cluster descriptions.\n")

    # Extract all FEELS entries per project
    THRESHOLD = 0.45  # entry must be at least this similar to H1 cluster
    MIN_ENTRIES_MATCHING = 2  # need ≥2 entries above threshold to count project

    project_entries = {}
    for proj in PROJECTS:
        empathy_dir = BASE / proj / 'empathy-maps'
        if not empathy_dir.exists():
            project_entries[proj] = []
            continue
        files = [f for f in empathy_dir.glob('*.md')
                 if 'clustering' not in f.name.lower() and 'overview' not in f.name.lower()
                 and 'template' not in f.name.lower()]
        all_entries = []
        for f in files:
            all_entries.extend(extract_feels(f))
        project_entries[proj] = all_entries
        print(f"  {proj}: {len(files)} maps, {len(all_entries)} FEELS entries")

    print()

    # For each project × H1 cluster: count entries above similarity threshold
    h1_detected_projects = {c['id']: set() for c in H1_CLUSTERS}
    project_h1_matches = {proj: {c['id']: 0 for c in H1_CLUSTERS} for proj in PROJECTS}

    for proj, entries in project_entries.items():
        if not entries:
            continue
        entry_embeddings = model.encode(entries, show_progress_bar=False, batch_size=64)
        for j, h1c in enumerate(H1_CLUSTERS):
            matching = sum(
                1 for emb in entry_embeddings
                if (1 - cosine(emb, h1_embeddings[j])) >= THRESHOLD
            )
            project_h1_matches[proj][h1c['id']] = matching
            if matching >= MIN_ENTRIES_MATCHING:
                h1_detected_projects[h1c['id']].add(proj)

    # ── Per-project detection heatmap ─────────────────────────────────────────
    print("=== DETECTION HEATMAP (entries matching each H1 cluster per project) ===")
    cluster_names = [c['name'][:30] for c in H1_CLUSTERS]
    header = f"{'Project':<10} " + " ".join(f"{i:>3}" for i in range(11))
    print(header)
    print("-" * (10 + 11 * 4))
    for proj in PROJECTS:
        row = f"{proj:<10} "
        for c in H1_CLUSTERS:
            n = project_h1_matches[proj][c['id']]
            row += f"{n:>3} " if n > 0 else "  . "
        print(row)
    print(f"\nH1 cluster legend:")
    for i, c in enumerate(H1_CLUSTERS):
        print(f"  {i}: {c['name']}")

    # ── Universality replication table ────────────────────────────────────────
    print(f"\n\n=== UNIVERSALITY REPLICATION (threshold={THRESHOLD}, min_entries={MIN_ENTRIES_MATCHING}) ===")
    print(f"{'H1 Cluster':<42} {'H1':>4} {'Indep':>6}  {'Δ':>4}  Verdict")
    print("-" * 70)

    verdicts = []
    for c in sorted(H1_CLUSTERS, key=lambda x: -x['h1_products']):
        ind = len(h1_detected_projects[c['id']])
        delta = ind - c['h1_products']
        if ind >= c['h1_products'] - 1:
            v = '✅ REPLICATES'
        elif ind >= c['h1_products'] - 2:
            v = '⚠️  PARTIAL'
        else:
            v = '❌ FAILS'
        projects_str = ', '.join(sorted(h1_detected_projects[c['id']]))
        print(f"{c['name']:<42} {c['h1_products']:>4}/9 {ind:>5}/9  {delta:>+4}  {v}")
        print(f"  Detected in: {projects_str or '(none)'}")
        verdicts.append({'cluster': c['name'], 'h1': c['h1_products'], 'replicated': ind, 'delta': delta})

    # Rank correlation
    h1_counts = [c['h1_products'] for c in H1_CLUSTERS]
    ind_counts = [len(h1_detected_projects[c['id']]) for c in H1_CLUSTERS]
    rho, p = spearmanr(h1_counts, ind_counts)
    print(f"\nSpearman rank correlation: ρ={rho:.3f}, p={p:.3f}")

    replicates = sum(1 for c in H1_CLUSTERS if len(h1_detected_projects[c['id']]) >= c['h1_products'] - 1)
    fails = sum(1 for c in H1_CLUSTERS if len(h1_detected_projects[c['id']]) < c['h1_products'] - 2)

    print(f"\n=== SUMMARY ===")
    print(f"Clusters that replicate independently (≤1 product short): {replicates}/11")
    print(f"Clusters that fail replication (>2 products short): {fails}/11")
    print(f"Spearman ρ = {rho:.3f} (p={p:.3f})")

    # Save
    out = {
        'threshold': THRESHOLD, 'min_entries': MIN_ENTRIES_MATCHING,
        'rank_correlation': {'rho': round(rho, 3), 'p': round(p, 3)},
        'results': [{
            'cluster': c['name'],
            'h1_claim': c['h1_products'],
            'independent_count': len(h1_detected_projects[c['id']]),
            'projects': sorted(h1_detected_projects[c['id']]),
        } for c in H1_CLUSTERS],
    }
    out_path = Path(__file__).parent.parent / 'results' / 'entry_level_replication.json'
    out_path.parent.mkdir(exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2))
    print(f"\nResults saved: {out_path}")


if __name__ == '__main__':
    main()
