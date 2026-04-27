# Experiment H1: Semantic Clustering of Interview Quotes

**Hypothesis:** Semantic vector embeddings over interview quotes would enable automated cross-interview pattern detection, surfacing universal pain clusters invisible at per-project scope.

**Prediction:** Clustering FEELS quadrant entries from all 53 interviews using sentence-transformers would surface 5-8 universal pain clusters spanning multiple product domains.

**Status:** PROTOCOL LOCKED (before results) — 2026-04-27

---

## What This Tests

Currently, clustering is done manually per-project (only DI&A has clustering-analysis.md). This experiment tests whether automated semantic clustering of the FEELS quadrant across ALL 53 interviews can:
1. Reproduce the manual clusters (validate the approach)
2. Discover cross-domain patterns not visible at per-project scope
3. Run in minutes rather than hours

## Why This Matters

- 53 interviews across 9 Clarivate products represent a unique dataset
- No current mechanism to ask "What pain is universal across all Clarivate research users?"
- If H1 succeeds, it enables a new `cross-project-synthesizer` skill (H5)
- If patterns are found, it directly informs Clarivate platform-level product strategy

## Method

### Step 1: Extract FEELS Quadrant Data
Parse all empathy map files to extract the FEELS section.

```python
import os
import re
from pathlib import Path

def extract_feels_entries(empathy_map_path):
    """Extract all FEELS entries from an empathy map markdown file."""
    content = Path(empathy_map_path).read_text()
    
    # Find FEELS section
    feels_match = re.search(
        r'##?\s*(?:4\.)?\s*FEELS.*?\n(.*?)(?=##|\Z)',
        content, re.DOTALL | re.IGNORECASE
    )
    if not feels_match:
        return []
    
    feels_text = feels_match.group(1)
    
    # Extract bullet items
    entries = []
    for line in feels_text.split('\n'):
        line = line.strip()
        if line.startswith(('- ', '* ', '• ')) and len(line) > 10:
            # Strip intensity markers like 🔴 8/10 etc.
            entry = re.sub(r'[🔴🟡🟢⚡]\s*\d+/10\s*', '', line[2:]).strip()
            entries.append(entry)
    
    return entries

# Collect from all projects
project_dirs = ['DI&A', 'CPI', 'CDDI', 'Fusion', 'PT', 'MT360', 'KAI', 'MASS', 'OFFX']
base_path = Path('/Users/joan.saez-pons/code/researcher_ux')

all_entries = []  # list of {text, project, user, file}

for project in project_dirs:
    empathy_dir = base_path / project / 'empathy-maps'
    if not empathy_dir.exists():
        continue
    for empathy_file in empathy_dir.glob('*.md'):
        if 'clustering' in empathy_file.name or 'overview' in empathy_file.name:
            continue
        user = empathy_file.stem.replace('empathy-map-', '').replace('-empathy-map', '')
        entries = extract_feels_entries(empathy_file)
        for e in entries:
            all_entries.append({
                'text': e,
                'project': project,
                'user': user,
                'file': str(empathy_file)
            })

print(f"Extracted {len(all_entries)} FEELS entries from {len(set(e['project'] for e in all_entries))} projects")
```

### Step 2: Embed with sentence-transformers

```python
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')
texts = [e['text'] for e in all_entries]
embeddings = model.encode(texts, show_progress_bar=True)

print(f"Embeddings shape: {embeddings.shape}")  # Expected: (N, 384)
```

### Step 3: Cluster with HDBSCAN

```python
import hdbscan
from sklearn.decomposition import PCA

# Reduce dimensions first for better clustering
pca = PCA(n_components=50)
embeddings_reduced = pca.fit_transform(embeddings)

clusterer = hdbscan.HDBSCAN(
    min_cluster_size=5,   # At least 5 entries per cluster
    min_samples=2,
    metric='euclidean'
)
cluster_labels = clusterer.fit_predict(embeddings_reduced)

n_clusters = len(set(cluster_labels)) - (1 if -1 in cluster_labels else 0)
n_noise = (cluster_labels == -1).sum()
print(f"Clusters: {n_clusters}, Noise points: {n_noise}/{len(cluster_labels)}")
```

### Step 4: Validate Against Known Clusters

Compare discovered clusters to DI&A's manual clustering-analysis.md:
- DI&A found 4 clusters: Data Triangulation Pain, Vendor Data Gaps, Forecasting Uncertainty, Cross-Functional Communication
- Expected: H1 clusters should encompass these or be more specific subsets

### Step 5: Name Clusters with LLM

For each cluster, use Claude to generate a descriptive name from the top 10 representative entries (those closest to cluster centroid).

### Step 6: Analyze Cross-Domain Distribution

```python
import pandas as pd

results_df = pd.DataFrame(all_entries)
results_df['cluster'] = cluster_labels

# Per cluster: which projects contribute?
cluster_distribution = results_df.groupby(['cluster', 'project']).size().unstack(fill_value=0)
print(cluster_distribution)

# Universal clusters: those appearing in 5+ projects
universal_clusters = cluster_distribution[
    (cluster_distribution > 0).sum(axis=1) >= 5
].index
print(f"Universal clusters (5+ projects): {list(universal_clusters)}")
```

## Success Criteria

| Criterion | Success | Failure |
|-----------|---------|---------|
| Extraction | All 53 empathy maps parsed, >200 FEELS entries extracted | <150 entries (file format issues) |
| Clustering | 5-10 meaningful clusters found | <3 clusters or >15 noisy clusters |
| DI&A validation | Known DI&A clusters recovered | Cannot match manual clusters |
| Cross-domain | 3+ clusters span 5+ product domains | All clusters are domain-specific |
| LLM naming | Cluster names are intelligible and useful | Names are vague or contradictory |

## Expected Outcome

**If confirmed:** Build a new `empathy-clustering` skill that runs automatically after empathy maps are created, producing a `clustering-analysis.md` for any project with 4+ interviews.

**If disconfirmed:** 
- If domain-specific noise dominates: try FEELS + THINKS combined, or normalize for domain vocabulary
- If clusters are too broad: try fine-grained clustering with lower min_cluster_size

## Dependencies

- `pip install sentence-transformers hdbscan scikit-learn pandas`
- All empathy map files accessible at standard paths
- FEELS section format relatively consistent across projects

## Estimated Time

- Data extraction + validation: 30 min
- Embedding + clustering: 10 min (CPU)
- Analysis + visualization: 30 min
- LLM naming pass: 15 min
- Total: ~90 min to first results
