---
name: Empathy Clustering
description: Discover emotional pain clusters across all empathy maps in a project using semantic embeddings (sentence-transformers → UMAP → HDBSCAN). Produces a clustering-analysis.md with named clusters, universality ratings, design implications, and a prioritised opportunity table.
agent: agent
tools:
  - codebase
  - editFiles
  - runCommands
---

You are a UX researcher running semantic clustering on empathy map FEELS entries.

## Your Task

Cluster the emotional patterns across all empathy maps in a project to identify universal vs. niche pain themes.

**Usage:**
- `Run empathy clustering for CCI`
- `Run empathy clustering across all projects`

**Prerequisites:** Python packages installed — `pip install sentence-transformers hdbscan umap-learn scikit-learn pandas numpy`

---

## Algorithm

**sentence-transformers all-MiniLM-L6-v2 → UMAP(15 dimensions) → HDBSCAN**

This combination was validated in H1 experiment (2026-04-27): 661 FEELS entries, 104 empathy maps, 14 clusters, 12% noise. PCA produced 49% noise by comparison.

---

## Step 1: Discover empathy maps

```python
from pathlib import Path
project = "CCI"  # or iterate all projects
maps = sorted(Path(f"{project}/empathy-maps").glob("empathy-map-*.md"))
print(f"Found {len(maps)} empathy maps")
```

## Step 2: Extract FEELS entries

Two format variants exist across projects:

**Format A** (most projects): `- **😰 Emotion** description text`
**Format B** (MASS project): `- **emoji Name:** description text`

```python
import re

def extract_feels(path, participant_name):
    content = Path(path).read_text(encoding='utf-8', errors='ignore')
    
    # Position-based extraction (avoids regex collapse bug with ### subsections)
    feels_hdr = re.search(
        r'##\s*(?:💭\s*)?(?:\d+\.)?\s*FEELS[^\n]*\n',
        content, re.IGNORECASE
    )
    if not feels_hdr:
        return []
    
    start = feels_hdr.end()
    next_sec = re.search(r'\n## ', content[start:])
    feels_text = content[start : start + (next_sec.start() if next_sec else len(content[start:]))]
    
    entries = []
    SKIP = re.compile(
        r'^(?:dominant emotion|emotional trajectory|evidence:|impact:|emotion:|'
        r'emotional arc|overall|summary|primary emotion|key emotion)',
        re.IGNORECASE
    )
    
    for line in feels_text.split('\n'):
        s = line.strip()
        
        # Format A: - **Emotion** description
        m = re.match(r'^(?:[-*]\s+)?\*\*([^\*:]+)\*\*\s+(.+)', s)
        if m and not SKIP.match(m.group(1)):
            emotion = re.sub(r'^[\U0001F000-\U0001FFFF\U00002600-\U000027FF☀-➿\s]+', '', m.group(1)).strip()
            text = f"{emotion}: {m.group(2).strip()}" if emotion else m.group(2).strip()
            if len(text) > 20:
                entries.append({'participant': participant_name, 'emotion': emotion, 'text': text})
            continue
        
        # Format B: - **emoji Name:** description
        m2 = re.match(r'^[-*]\s+\*\*([^\*]+):\*\*\s+(.+)', s)
        if m2 and not SKIP.match(m2.group(1)):
            emotion = re.sub(r'^[\U0001F000-\U0001FFFF\U00002600-\U000027FF☀-➿\s]+', '', m2.group(1)).strip()
            text = f"{emotion}: {m2.group(2).strip()}" if emotion else m2.group(2).strip()
            if len(text) > 20:
                entries.append({'participant': participant_name, 'emotion': emotion, 'text': text})
    
    return entries
```

## Step 3: Embed and cluster

```python
from sentence_transformers import SentenceTransformer
import umap.umap_ as umap_module
import hdbscan
import numpy as np

# Collect all entries
all_entries = []
for map_path in maps:
    name = map_path.stem.replace('empathy-map-', '')
    all_entries.extend(extract_feels(map_path, name))

print(f"Total FEELS entries extracted: {len(all_entries)}")

# Embed
model = SentenceTransformer('all-MiniLM-L6-v2')
texts = [e['text'] for e in all_entries]
embeddings = model.encode(texts, show_progress_bar=True, batch_size=64)

# UMAP
reducer = umap_module.UMAP(n_components=15, random_state=42, n_neighbors=15, min_dist=0.0)
embeddings_reduced = reducer.fit_transform(embeddings)

# HDBSCAN — try multiple configs, pick best (4–14 clusters, <45% noise)
best_labels, best_config = None, {}
best_score = -1
for min_cluster_size in [5, 8, 12, 15]:
    for min_samples in [3, 5]:
        clusterer = hdbscan.HDBSCAN(
            min_cluster_size=min_cluster_size, min_samples=min_samples,
            metric='euclidean', cluster_selection_method='eom'
        )
        labels = clusterer.fit_predict(embeddings_reduced)
        n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
        noise_pct = (labels == -1).sum() / len(labels)
        if 4 <= n_clusters <= 14 and noise_pct < 0.45:
            score = n_clusters * (1 - noise_pct)
            if score > best_score:
                best_score, best_labels = score, labels.copy()
                best_config = {'min_cluster_size': min_cluster_size, 'min_samples': min_samples,
                               'n_clusters': n_clusters, 'noise_pct': round(noise_pct, 3)}

print(f"Best config: {best_config}")
```

## Step 4: Name and describe clusters

For each cluster:
1. Find the 5 entries closest to the centroid (most representative)
2. Identify dominant emotions and pain themes
3. Name the cluster: `[Emotion] [Pain Theme]` (e.g., "Expert Confidence Under Deadline Pressure")
4. Count unique participants — compute universality:
   - **Universal:** >40% of cohort (for single-project: 9+ of 21)
   - **Common:** 24–40% of cohort
   - **Niche:** <24% of cohort

## Step 5: Write clustering-analysis.md

Save to `[project]/empathy-maps/clustering-analysis.md`.

```markdown
# Empathy Map Clustering Analysis — [PROJECT]
**Generated by empathy-clustering**
**Method:** sentence-transformers all-MiniLM-L6-v2 → UMAP(15d) → HDBSCAN (min_cluster_size=[N], min_samples=[N])
**Participants:** [N] empathy maps analysed
**Total FEELS entries:** [N] (avg [N] per map, range [N]–[N])
**Date:** [TODAY]

---

## Executive Summary

[N] distinct emotional clusters found across [N] users. [N] are universal patterns (9+ participants, >40% of cohort); [N] are common; [N] are niche.

**Dominant pattern: [Cluster 1 Name]** ([N] entries, [N] users) — [one-sentence insight]

**Second dominant pattern: [Cluster 2 Name]** ([N] entries, [N] users) — [one-sentence insight]

**Noise:** [N] entries ([N]%) — [brief explanation of what the noise consists of]

---

## Clusters

### Cluster 1: [Name] (n=[N] entries, [N] users)
**Universality:** [Universal/Common/Niche] — [N]/[total] users ([N]%)
**Dominant emotions:** [list]
**Users:** [participant-name, participant-name, ...]
**Defining entries:**
- "[Entry closest to centroid 1]"
- "[Entry 2]"
- "[Entry 3]"
**Platform implication:** [What this cluster means for product/design — actionable]

---

[Repeat for all clusters]

---

## Noise Points (n=[N], [N]%)

[Description of what noise entries contain — typically researcher-relationship moments, highly idiosyncratic reactions]

---

## Validation Notes

- **Coverage**: [N]% — [N] of [N] empathy maps contributed entries
- **Cluster names** are grounded in centroid entries and dominant emotion labels
- **No meta-text captured**: SKIP filter correctly excluded "Dominant Emotion:" and "Emotional Trajectory:" lines

---

## Top Design Opportunities by Cluster Weight

| Priority | Cluster | Users | Opportunity |
|---|---|---|---|
| 1 | [Name] | [N] | [Opportunity] |
| 2 | [Name] | [N] | [Opportunity] |
[continue for top 8]

---

**Methodology:** sentence-transformers all-MiniLM-L6-v2 → UMAP(15d, n_neighbors=15, min_dist=0) → HDBSCAN (min_cluster_size=[N], min_samples=[N], EOM selection)
```

---

## Troubleshooting

| Problem | Fix |
|---|---|
| Too many noise points (>40%) | Reduce `min_cluster_size` to 5; reduce `min_samples` to 2 |
| Too few clusters (<4) | Reduce `min_cluster_size`; try `cluster_selection_method='leaf'` |
| `import umap` fails | Use `import umap.umap_ as umap_module` not `import umap` |
| MASS project missing entries | MASS uses Format B with ### subsection headers — ensure Format B regex is active |
| <80% coverage | Check FEELS header format — new templates may use different header text |
