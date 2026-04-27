#!/usr/bin/env python3.11
"""
H1: Semantic Clustering of FEELS quadrant entries across all 53 interviews.
Fixed version: handles all 3 empathy map format variants, UMAP reduction, clean JSON output.

Prediction: 5-8 universal pain clusters spanning multiple product domains.
"""

import os
import re
import json
import numpy as np
import pandas as pd
from pathlib import Path
from collections import Counter

BASE_PATH = Path('/Users/joan.saez-pons/code/researcher_ux')
PROJECT_DIRS = ['DI&A', 'CPI', 'CDDI', 'Fusion', 'PT', 'MT360', 'KAI', 'MASS', 'OFFX']

# Lines to skip — they are summaries, not individual emotional states
SKIP_PATTERNS = re.compile(
    r'^(?:dominant emotion|emotional trajectory|evidence:|impact:|emotion:|'
    r'emotional arc|overall|summary|primary emotion|key emotion)',
    re.IGNORECASE
)


def extract_feels_entries(path):
    """Extract emotional state entries from empathy map FEELS section.

    Handles three formats:
      Format A: - **Emotion** description (most DI&A, CPI, CDDI, Fusion)
      Format B: - **emoji Name:** description (MASS, some OFFX)
      Format C: ### Sub-heading / - **Evidence:** / - **Emotion:** text (MASS theodore)
    """
    content = Path(path).read_text(encoding='utf-8', errors='ignore')

    # Find FEELS section
    feels_match = re.search(
        r'##\s*(?:💭\s*)?(?:\d+\.)?\s*FEELS[^\n]*\n(.*?)(?=\n##|\Z)',
        content, re.DOTALL | re.IGNORECASE
    )
    if not feels_match:
        return []

    feels_text = feels_match.group(1)
    entries = []

    current_subheading = None

    for line in feels_text.split('\n'):
        line_stripped = line.strip()

        # Track sub-headings (e.g. ### Frustrations & Pain)
        if re.match(r'^###\s+', line_stripped):
            current_subheading = re.sub(r'^###\s+', '', line_stripped).strip()
            continue

        # Skip summary/meta lines
        if SKIP_PATTERNS.match(line_stripped.lstrip('*- ')):
            continue

        # Format A: - **Emotion** description or **Emotion** description
        m = re.match(r'^(?:[-*]\s+)?\*\*([^\*:]+)\*\*\s+(.+)', line_stripped)
        if m:
            emotion_part = m.group(1).strip()
            description = m.group(2).strip()
            # Skip if this looks like a meta-label
            if SKIP_PATTERNS.match(emotion_part):
                continue
            # Remove leading emoji chars from emotion_part
            emotion_word = re.sub(
                r'^[\U0001F000-\U0001FFFF\U00002600-\U000027FF☀-➿\s]+',
                '', emotion_part
            ).strip()
            full_text = f"{emotion_word}: {description}" if emotion_word else description
            if len(full_text) > 20:
                entries.append({
                    'emotion': emotion_word or current_subheading or 'unknown',
                    'description': description,
                    'text': full_text,
                    'subheading': current_subheading,
                })
            continue

        # Format B: - **emoji Name:** description (with trailing colon in bold)
        m2 = re.match(r'^[-*]\s+\*\*([^\*]+):\*\*\s+(.+)', line_stripped)
        if m2:
            emotion_part = m2.group(1).strip()
            description = m2.group(2).strip()
            if SKIP_PATTERNS.match(emotion_part):
                continue
            emotion_word = re.sub(
                r'^[\U0001F000-\U0001FFFF\U00002600-\U000027FF☀-➿\s]+',
                '', emotion_part
            ).strip()
            full_text = f"{emotion_word}: {description}" if emotion_word else description
            if len(full_text) > 20:
                entries.append({
                    'emotion': emotion_word or current_subheading or 'unknown',
                    'description': description,
                    'text': full_text,
                    'subheading': current_subheading,
                })

    return entries


all_entries = []
project_user_counts = {}

for project in PROJECT_DIRS:
    empathy_dir = BASE_PATH / project / 'empathy-maps'
    if not empathy_dir.exists():
        continue
    files = [f for f in empathy_dir.glob('*.md')
             if 'clustering' not in f.name.lower()
             and 'overview' not in f.name.lower()
             and 'README' not in f.name]
    project_user_counts[project] = len(files)
    for empathy_file in files:
        user = empathy_file.stem
        entries = extract_feels_entries(empathy_file)
        for e in entries:
            all_entries.append({
                'text': e['text'],
                'emotion': e['emotion'],
                'description': e['description'],
                'subheading': e.get('subheading', ''),
                'project': project,
                'user': user,
                'file': str(empathy_file),
            })

print(f"\n{'='*60}")
print(f"STEP 1: DATA EXTRACTION")
print(f"{'='*60}")
print(f"Total FEELS entries: {len(all_entries)}")
print(f"Empathy maps per project: {project_user_counts}")
print(f"Total empathy maps: {sum(project_user_counts.values())}")

df = pd.DataFrame(all_entries)
print(f"\nEntries per project:")
print(df['project'].value_counts().to_string())

# Sanity check
assert len(all_entries) >= 150, f"Only {len(all_entries)} entries — extraction issue!"

# ---------------------------------------------------------------------------
# Step 2: Embed
# ---------------------------------------------------------------------------
print(f"\n{'='*60}")
print(f"STEP 2: EMBEDDING")
print(f"{'='*60}")

from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')
texts = df['text'].tolist()
print(f"Embedding {len(texts)} entries...")
embeddings = model.encode(texts, show_progress_bar=True, batch_size=64)
embeddings = embeddings.astype(np.float32)
print(f"Embeddings shape: {embeddings.shape}")

# ---------------------------------------------------------------------------
# Step 3: UMAP reduction → HDBSCAN
# ---------------------------------------------------------------------------
print(f"\n{'='*60}")
print(f"STEP 3: UMAP + HDBSCAN CLUSTERING")
print(f"{'='*60}")

try:
    import umap.umap_ as umap_module
    reducer = umap_module.UMAP(n_components=15, random_state=42, n_neighbors=15, min_dist=0.0)
    embeddings_2d = reducer.fit_transform(embeddings)
    print(f"UMAP reduced to shape: {embeddings_2d.shape}")
    use_umap = True
except ImportError:
    print("UMAP not installed — falling back to PCA")
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import normalize
    embeddings_norm = normalize(embeddings)
    n_components = min(50, len(embeddings) - 1)
    pca = PCA(n_components=n_components, random_state=42)
    embeddings_2d = pca.fit_transform(embeddings_norm)
    print(f"PCA explained variance ({n_components} components): {pca.explained_variance_ratio_.sum():.1%}")
    use_umap = False

import hdbscan

best_labels = None
best_score = -1
best_config = {}

for min_cluster_size in [8, 12, 15, 20]:
    for min_samples in [3, 5]:
        clusterer = hdbscan.HDBSCAN(
            min_cluster_size=min_cluster_size,
            min_samples=min_samples,
            metric='euclidean',
            cluster_selection_method='eom'
        )
        labels = clusterer.fit_predict(embeddings_2d)
        n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
        n_noise = int((labels == -1).sum())
        noise_pct = n_noise / len(labels)

        if 4 <= n_clusters <= 14 and noise_pct < 0.45:
            score = n_clusters * (1 - noise_pct)
            if score > best_score:
                best_score = score
                best_labels = labels.copy()
                best_config = {
                    'min_cluster_size': int(min_cluster_size),
                    'min_samples': int(min_samples),
                    'n_clusters': int(n_clusters),
                    'n_noise': int(n_noise),
                    'noise_pct': float(noise_pct),
                    'use_umap': use_umap,
                }

if best_labels is None:
    clusterer = hdbscan.HDBSCAN(min_cluster_size=10, min_samples=3, metric='euclidean')
    best_labels = clusterer.fit_predict(embeddings_2d)
    best_config = {
        'min_cluster_size': 10, 'min_samples': 3,
        'n_clusters': int(len(set(best_labels)) - (1 if -1 in best_labels else 0)),
        'n_noise': int((best_labels == -1).sum()),
        'noise_pct': float((best_labels == -1).sum() / len(best_labels)),
        'use_umap': use_umap,
    }

print(f"\nBest config: {best_config}")
df['cluster'] = best_labels

# ---------------------------------------------------------------------------
# Step 4: Cluster analysis
# ---------------------------------------------------------------------------
print(f"\n{'='*60}")
print(f"STEP 4: CLUSTER ANALYSIS")
print(f"{'='*60}")

cluster_ids = sorted([int(c) for c in df['cluster'].unique() if c != -1])
cluster_summaries = []

for cid in cluster_ids:
    cluster_df = df[df['cluster'] == cid]
    emotions = Counter(cluster_df['emotion'].str.lower().str.split().str[0].tolist()).most_common(5)
    top_descriptions = cluster_df['description'].tolist()[:10]
    project_dist = cluster_df['project'].value_counts().to_dict()
    n_projects = len(project_dist)
    universality = n_projects / len(PROJECT_DIRS)

    summary = {
        'cluster_id': cid,
        'size': int(len(cluster_df)),
        'n_projects': int(n_projects),
        'universality': float(universality),
        'projects': {k: int(v) for k, v in project_dist.items()},
        'top_emotions': [(e, int(c)) for e, c in emotions],
        'sample_descriptions': top_descriptions[:5],
    }
    cluster_summaries.append(summary)

    print(f"\nCluster {cid} (n={len(cluster_df)}, {n_projects}/9 projects, {universality:.0%}):")
    print(f"  Projects: {list(project_dist.keys())}")
    print(f"  Top emotions: {[e[0] for e in emotions[:3]]}")
    print(f"  Samples:")
    for desc in top_descriptions[:3]:
        print(f"    - {str(desc)[:110]}")

noise_df = df[df['cluster'] == -1]
print(f"\nNoise: {len(noise_df)} ({len(noise_df)/len(df):.0%})")

# ---------------------------------------------------------------------------
# Step 5: Universal clusters
# ---------------------------------------------------------------------------
print(f"\n{'='*60}")
print(f"STEP 5: UNIVERSAL CLUSTERS")
print(f"{'='*60}")

universal = [s for s in cluster_summaries if s['n_projects'] >= 5]
common = [s for s in cluster_summaries if 3 <= s['n_projects'] < 5]
niche = [s for s in cluster_summaries if s['n_projects'] < 3]

print(f"Universal (5+ projects): {len(universal)} → {[s['cluster_id'] for s in universal]}")
print(f"Common (3-4 projects):   {len(common)}")
print(f"Niche (<3 projects):     {len(niche)}")

for s in universal:
    print(f"\n  Cluster {s['cluster_id']} ({s['size']} entries, {s['n_projects']}/9 projects):")
    print(f"    Projects: {list(s['projects'].keys())}")
    print(f"    Emotions: {[e[0] for e in s['top_emotions'][:3]]}")
    for d in s['sample_descriptions'][:2]:
        print(f"    - {str(d)[:100]}")

# ---------------------------------------------------------------------------
# Step 6: DI&A validation
# ---------------------------------------------------------------------------
print(f"\n{'='*60}")
print(f"STEP 6: DI&A VALIDATION")
print(f"{'='*60}")
print("Known manual clusters: 1) Data triangulation burden  2) Epistemic uncertainty")
print("                        3) Cross-functional friction  4) AI trust/credibility")

dia_entries = df[df['project'] == 'DI&A']
print(f"\nDI&A: {len(dia_entries)} entries across clusters:")
print(dia_entries.groupby('cluster').size().sort_values(ascending=False).to_string())

# ---------------------------------------------------------------------------
# Save
# ---------------------------------------------------------------------------
output_dir = Path('/Users/joan.saez-pons/code/researcher_ux/platform-research/experiments/H1-semantic-clustering/results')
output_dir.mkdir(exist_ok=True)
data_dir = Path('/Users/joan.saez-pons/code/researcher_ux/platform-research/data')

df.to_csv(output_dir / 'all_entries_clustered.csv', index=False)
df.to_csv(data_dir / 'H1_feels_entries_clustered.csv', index=False)

with open(output_dir / 'cluster_summaries.json', 'w') as f:
    json.dump(cluster_summaries, f, indent=2)

prediction_met = 5 <= best_config['n_clusters'] <= 8
metrics = {
    'n_entries': int(len(df)),
    'n_projects': int(len(df['project'].unique())),
    'n_empathy_maps': int(sum(project_user_counts.values())),
    'clustering_config': best_config,
    'n_universal_clusters': int(len(universal)),
    'n_common_clusters': int(len(common)),
    'n_niche_clusters': int(len(niche)),
    'universal_cluster_ids': [int(s['cluster_id']) for s in universal],
    'prediction_5_8_clusters': bool(prediction_met),
    'prediction_spans_domains': bool(len(universal) >= 3),
    'success_extraction': bool(len(df) >= 200),
    'success_clustering': bool(4 <= best_config['n_clusters'] <= 15),
    'success_cross_domain': bool(len(universal) >= 3),
}

with open(output_dir / 'metrics.json', 'w') as f:
    json.dump(metrics, f, indent=2)

print(f"\n{'='*60}")
print(f"RESULTS SUMMARY")
print(f"{'='*60}")
print(f"Entries: {len(df)} (success criterion: ≥200)")
print(f"Clusters: {best_config['n_clusters']} (predicted: 5-8)")
print(f"Universal clusters (5+ domains): {len(universal)} (predicted: ≥3)")
print(f"Noise: {best_config['noise_pct']:.0%}")
print(f"Prediction matched (5-8 clusters): {prediction_met}")
print(f"Cross-domain prediction met: {len(universal) >= 3}")
print(f"Results: {output_dir}")
