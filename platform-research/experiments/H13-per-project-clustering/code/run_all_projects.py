#!/usr/bin/env python3
"""
H13: Per-project empathy clustering across all 9 Clarivate products.
Extends H9 (DI&A-only) to all remaining projects, then does comparative analysis
against H1 global taxonomy to identify universal vs. project-specific patterns.
"""

import re, json, sys, time
from pathlib import Path
from collections import Counter
import numpy as np
import pandas as pd

BASE_PATH = Path('/Users/joan.saez-pons/code/researcher_ux')
TODAY = '2026-04-27'

# H1 universal cluster themes for comparison
H1_THEMES = [
    'AI Opportunity-Threat Ambivalence',
    'Expert Achievement Satisfaction',
    'Methodological Confidence in Triangulation',
    'Vendor Commercial Friction',
    'Strategic Isolation & Disruption Anxiety',
    'Constant Urgency Pressure',
    'Tool Navigation Friction',
    'Process Verification Anxiety',
    'Data Fragmentation Fatigue',
    'Manual Correction Burden at Scale',
    'Vendor Partnership Dependency',
]

PROJECTS = ['MASS', 'CPI', 'CDDI', 'Fusion', 'PT', 'MT360', 'KAI', 'OFFX']

SKIP = re.compile(
    r'^(?:dominant emotion|emotional trajectory|evidence:|impact:|emotion:|'
    r'emotional arc|overall|summary|primary emotion|key emotion)',
    re.IGNORECASE
)


def extract_feels(path):
    content = Path(path).read_text(encoding='utf-8', errors='ignore')
    m = re.search(r'##\s*(?:💭\s*)?(?:\d+\.)?\s*FEELS[^\n]*\n(.*?)(?=\n## (?!#)|\Z)', content, re.DOTALL | re.IGNORECASE)
    if not m:
        return []
    entries = []
    for line in m.group(1).split('\n'):
        s = line.strip()
        # Standard format: **EmotionWord** description
        # MASS format: **emoji Label:** description  (colon inside bold)
        m2 = re.match(r'^(?:[-*]\s+)?\*\*([^\*]+?):?\*\*\s*(.+)', s)
        if m2 and not SKIP.match(m2.group(1)):
            raw_emo = m2.group(1).rstrip(':').strip()
            emo = re.sub(r'^[\U0001F000-\U0001FFFF\U00002600-\U000027FF\U00002702-\U000027B0☀-⟿\s]+', '', raw_emo).strip()
            desc = m2.group(2).strip()
            text = f'{emo}: {desc}' if emo else desc
            if len(text) > 15:
                entries.append({'emotion': emo, 'description': desc, 'text': text})
    return entries


def get_adaptive_params(n_entries):
    """Scale clustering params with project size."""
    if n_entries < 20:
        return [(3, 2), (4, 2)]
    elif n_entries < 40:
        return [(4, 2), (5, 2), (6, 3)]
    else:
        return [(5, 2), (8, 3), (10, 3)]


def cluster_project(project, embeddings_model, umap_module, hdbscan_module):
    empathy_dir = BASE_PATH / project / 'empathy-maps'
    if not empathy_dir.exists():
        print(f"  {project}: no empathy-maps dir")
        return None

    files = [f for f in empathy_dir.glob('*.md')
             if 'clustering' not in f.name.lower() and 'overview' not in f.name.lower()
             and 'template' not in f.name.lower()]

    if len(files) < 3:
        print(f"  {project}: only {len(files)} files — skipping")
        return None

    all_entries = []
    for f in files:
        for e in extract_feels(f):
            all_entries.append({**e, 'user': f.stem, 'file': str(f)})

    if len(all_entries) < 10:
        print(f"  {project}: only {len(all_entries)} FEELS entries — skipping")
        return None

    df = pd.DataFrame(all_entries)
    print(f"  {project}: {len(files)} maps, {len(all_entries)} FEELS entries")

    # Embed
    embeddings = embeddings_model.encode(df['text'].tolist(), show_progress_bar=False, batch_size=64)

    # UMAP
    n_components = min(10, len(df) - 2)
    reducer = umap_module.UMAP(n_components=n_components, random_state=42,
                                n_neighbors=min(10, len(df) - 1), min_dist=0.0)
    emb_reduced = reducer.fit_transform(embeddings)

    # HDBSCAN — adaptive params
    best_labels, best_config, best_score = None, {}, -1
    for mcs, ms in get_adaptive_params(len(all_entries)):
        if mcs > len(df) // 2:
            continue
        c = hdbscan_module.HDBSCAN(min_cluster_size=mcs, min_samples=ms,
                                    metric='euclidean', cluster_selection_method='eom')
        labels = c.fit_predict(emb_reduced)
        n_c = len(set(labels)) - (1 if -1 in labels else 0)
        noise = (labels == -1).sum() / len(labels)
        if n_c >= 2 and noise < 0.5:
            score = n_c * (1 - noise)
            if score > best_score:
                best_score, best_labels, best_config = score, labels.copy(), {
                    'n_clusters': n_c, 'noise_pct': round(float(noise), 3)
                }

    if best_labels is None:
        c = hdbscan_module.HDBSCAN(min_cluster_size=3, min_samples=2, metric='euclidean')
        best_labels = c.fit_predict(emb_reduced)
        best_config = {
            'n_clusters': len(set(best_labels)) - (1 if -1 in best_labels else 0),
            'noise_pct': round(float((best_labels == -1).sum() / len(best_labels)), 3)
        }

    df['cluster'] = best_labels
    n_clusters = best_config['n_clusters']
    noise_pct = best_config['noise_pct']
    print(f"    → {n_clusters} clusters, {noise_pct:.0%} noise")

    # Build cluster summaries
    cluster_ids = sorted([int(c) for c in df['cluster'].unique() if c != -1])
    clusters = []
    for cid in cluster_ids:
        cdf = df[df['cluster'] == cid]
        emotions = Counter(cdf['emotion'].str.lower().str.split(':').str[0].str.strip().tolist()).most_common(4)
        samples = cdf['text'].tolist()
        clusters.append({
            'id': cid,
            'n': len(cdf),
            'emotions': [e[0] for e in emotions if e[0]],
            'samples': samples[:5],
            'all_texts': cdf['text'].tolist(),
        })

    # Write output
    output_path = empathy_dir / f'clustering-analysis-automated.md'
    noise_n = (df['cluster'] == -1).sum()
    lines = [
        f"# Empathy Map Clustering Analysis — {project}",
        f"**Generated by:** empathy-clustering skill (H13 multi-project run)",
        f"**Method:** sentence-transformers `all-MiniLM-L6-v2` → UMAP → HDBSCAN",
        f"**Participants:** {len(files)} empathy maps, {len(all_entries)} FEELS entries",
        f"**Date:** {TODAY}",
        "",
        "---",
        "",
        "## Executive Summary",
        "",
        f"Automated semantic clustering of {len(all_entries)} FEELS entries from {len(files)} empathy maps reveals **{n_clusters} distinct emotional clusters**. Noise rate: {noise_pct:.0%}.",
        "",
        "---",
        "",
        "## Clusters",
        "",
    ]
    for cl in clusters:
        label = ', '.join(cl['emotions'][:2]).title() if cl['emotions'] else 'Mixed'
        lines += [
            f"### Cluster {cl['id']+1}: {label} (n={cl['n']})",
            f"**Dominant emotions:** {', '.join(cl['emotions'][:4]) if cl['emotions'] else 'varied'}",
            f"**Sample entries:**",
        ]
        for s in cl['samples'][:4]:
            lines.append(f"- {s[:130]}")
        lines.append("")

    lines += [
        f"## Noise Points (n={noise_n}, {noise_n/len(df):.0%})",
        "Entries that did not cluster — often transitional or mixed emotional states.",
        "",
        "---",
        "",
        "## H1 Global Taxonomy Comparison",
        "",
        "H1 identified 11 universal clusters across all 9 Clarivate products.",
        "Per-project clusters that appear to match H1 universal themes:",
        "",
    ]
    for theme in H1_THEMES:
        lines.append(f"- {theme}")
    lines += ["", "*(Manual mapping required to assign per-project clusters to H1 taxonomy.)*"]

    output_path.write_text('\n'.join(lines))
    return {
        'project': project,
        'n_maps': len(files),
        'n_entries': len(all_entries),
        'n_clusters': n_clusters,
        'noise_pct': noise_pct,
        'clusters': clusters,
        'output': str(output_path),
    }


def main():
    print("H13: Per-project empathy clustering")
    print("=" * 60)

    # Load shared model once
    from sentence_transformers import SentenceTransformer
    import umap.umap_ as umap_module
    import hdbscan as hdbscan_module

    print("Loading sentence-transformers model...")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    print("Model loaded.\n")

    results = []
    t0 = time.time()
    for proj in PROJECTS:
        print(f"\n{proj}:")
        r = cluster_project(proj, model, umap_module, hdbscan_module)
        if r:
            results.append(r)

    elapsed = time.time() - t0
    print(f"\n{'='*60}")
    print(f"Completed {len(results)}/{len(PROJECTS)} projects in {elapsed:.1f}s")
    print()

    # Comparative summary
    print(f"{'Project':<10} {'Maps':>5} {'Entries':>8} {'Clusters':>9} {'Noise':>7}")
    print("-" * 45)
    for r in results:
        print(f"{r['project']:<10} {r['n_maps']:>5} {r['n_entries']:>8} {r['n_clusters']:>9} {r['noise_pct']:>6.0%}")

    # Save comparative data
    summary_path = Path(__file__).parent.parent / 'results' / 'per_project_clustering_summary.json'
    summary_path.parent.mkdir(exist_ok=True)
    with open(summary_path, 'w') as f:
        json.dump([{k: v for k, v in r.items() if k != 'clusters'} for r in results], f, indent=2)
    print(f"\nSummary written: {summary_path}")

    # Write cluster theme table for comparative analysis
    print("\n=== CLUSTER THEME OVERVIEW ===")
    for r in results:
        print(f"\n{r['project']} ({r['n_clusters']} clusters):")
        for i, cl in enumerate(r['clusters']):
            label = ', '.join(cl['emotions'][:3]) if cl['emotions'] else '(unlabeled)'
            print(f"  C{i+1} (n={cl['n']}): {label}")


if __name__ == '__main__':
    main()
