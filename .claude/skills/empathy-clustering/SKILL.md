---
name: empathy-clustering
description: Automatically cluster FEELS quadrant entries from empathy maps using semantic embeddings (UMAP + HDBSCAN) to reveal universal pain patterns across users and product domains. Use when you want to find cross-user emotional patterns, generate a clustering-analysis.md for a project, identify universal vs. product-specific pains, or replace manual empathy clustering with automated analysis. Replaces the manual clustering-analysis.md workflow.
version: 1.0.0
author: researcher_ux platform research
tags: [Empathy Maps, Semantic Clustering, UMAP, HDBSCAN, Cross-Project Analysis, Pain Patterns]
dependencies: [sentence-transformers, hdbscan, umap-learn, scikit-learn, pandas, numpy]
---

# Empathy Clustering Skill

Automatically discovers emotional pain clusters across empathy maps using semantic embeddings. This replaces the manual clustering-analysis.md workflow that previously existed only for DI&A.

**Research origin:** Validated by H1 experiment (2026-04-27) — 661 FEELS entries across 104 empathy maps, 14 clusters found, 11 universal across 5+ product domains, 12% noise (vs. 49% with PCA).

## When to Use This Skill

- After creating 3+ empathy maps for a project and wanting cross-user patterns
- When starting cross-project synthesis (feed outputs to `cross-project-synthesizer`)
- When stakeholders ask "what do users universally feel frustrated by?"
- To replace or validate manual clustering done in a single project

**Do NOT use this skill when:**
- You only have 1-2 empathy maps (too few for meaningful clustering)
- You want per-user emotional analysis (use `empathy-map-generator` output directly)

---

## Trigger Modes

### Single-Project Mode
```
/empathy-clustering DI&A
/empathy-clustering CPI
```
Clusters all empathy maps in `[PROJECT]/empathy-maps/`. Outputs `[PROJECT]/empathy-maps/clustering-analysis.md`.

### Cross-Project Mode
```
/empathy-clustering
/empathy-clustering all
```
Clusters across all discovered projects. Outputs:
- `[PROJECT]/empathy-maps/clustering-analysis.md` per project (project-specific view)
- `cross-project-synthesis/empathy-cluster-taxonomy.md` (universal cluster definitions)

---

## Setup

Install required Python packages once:

```bash
pip install sentence-transformers hdbscan umap-learn scikit-learn pandas numpy
```

These are available in the `platform-research/experiments/H1-semantic-clustering/code/run_clustering.py` reference implementation.

---

## Execution Workflow

### Step 0: Discover Projects

If cross-project mode:
```python
from pathlib import Path
base = Path('.')
projects = [d.name for d in base.iterdir()
            if d.is_dir() and (d / 'empathy-maps').exists()
            and not d.name.startswith('.')]
print(f"Found projects: {projects}")
```

### Step 1: Extract FEELS Entries

The FEELS section has two format variants:

**Format A** (most projects — DI&A, CPI, CDDI, Fusion, PT, MT360, KAI, OFFX):
```
- **😰 Emotion** description text
```

**Format B** (MASS — subsection headers + bold labels with colon):
```
### Sub-heading
- **emoji Name:** description text
```

Use this extraction regex:
```python
import re

def extract_feels_entries(path):
    content = Path(path).read_text(encoding='utf-8', errors='ignore')
    
    # Find FEELS section — position-based extraction avoids regex \Z collapse bug
    # (non-greedy (.*?)(?=\n##|\Z) collapses to 0 chars when FEELS has ### subsections)
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
                entries.append({'emotion': emotion, 'text': text})
            continue
        
        # Format B: - **emoji Name:** description
        m2 = re.match(r'^[-*]\s+\*\*([^\*]+):\*\*\s+(.+)', s)
        if m2 and not SKIP.match(m2.group(1)):
            emotion = re.sub(r'^[\U0001F000-\U0001FFFF\U00002600-\U000027FF☀-➿\s]+', '', m2.group(1)).strip()
            text = f"{emotion}: {m2.group(2).strip()}" if emotion else m2.group(2).strip()
            if len(text) > 20:
                entries.append({'emotion': emotion, 'text': text})
    
    return entries
```

### Step 2: Embed with sentence-transformers

```python
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')
texts = [e['text'] for e in all_entries]
embeddings = model.encode(texts, show_progress_bar=True, batch_size=64)
```

**Why `all-MiniLM-L6-v2`:** Fastest model with strong semantic quality. H1 validation showed it recovers manual clusters from DI&A with high fidelity.

### Step 3: UMAP → HDBSCAN

```python
import umap.umap_ as umap_module
import hdbscan

# UMAP reduction (CRITICAL: dramatically reduces noise vs. PCA)
reducer = umap_module.UMAP(n_components=15, random_state=42, n_neighbors=15, min_dist=0.0)
embeddings_reduced = reducer.fit_transform(embeddings)

# HDBSCAN — try multiple configs, pick best
best_labels, best_config = None, {}
best_score = -1
for min_cluster_size in [8, 12, 15, 20]:
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
```

**Expected:** 8-15 clusters, 10-20% noise for a full cross-project run.

### Step 4: Name Clusters

For each cluster, synthesize a name from the top entries (those closest to the cluster centroid):
- Identify the dominant emotion words
- Identify the dominant pain theme from descriptions
- Generate a 3-5 word name: `[Emotion] [Pain Theme]` (e.g., "Data Fragmentation Fatigue")

**Universality categories:**
- Universal: 5+ projects (>55% of total)
- Common: 3-4 projects
- Niche: 1-2 projects (likely product-specific)

### Step 5: Write clustering-analysis.md

Output format (mirrors DI&A manual clustering-analysis.md):

```markdown
# Empathy Map Clustering Analysis — [PROJECT]
**Generated by empathy-clustering skill (automated)**
**Method:** sentence-transformers all-MiniLM-L6-v2 → UMAP(15d) → HDBSCAN
**Participants:** N empathy maps analyzed
**Date:** [DATE]

## Executive Summary
[N] distinct emotional clusters found across [N] users. [N] are universal patterns.
Dominant pattern: [CLUSTER NAME] ([N] users, [N]% of entries).

## Clusters

### Cluster 1: [Name] (n=[N] entries, [N] users)
**Universality:** [Universal/Common/Niche]
**Dominant emotions:** [list]
**Defining entries:**
- [entry 1]
- [entry 2]
- [entry 3]
**Products where present:** [list]
**Platform implication:** [what this means for product/design]

[repeat for each cluster]

## Noise Points (n=[N], [N]%)
[Brief description of what the noise contains — often edge cases or mixed signals]

## Validation Notes
[If DI&A: compare to manual clustering-analysis.md]
[Note any format variants that reduced extraction coverage]
```

---

## Output Quality Checks

After generating clustering-analysis.md, verify:

✅ **Coverage**: At least 80% of empathy maps contributed entries
✅ **Cluster names** are intelligible (not "cluster of frustrated/uncertain entries")
✅ **No meta-text captured** (no "Dominant Emotion:" or "Emotional Trajectory:" lines)
✅ **DI&A validation** (if running on DI&A): compare top clusters to manual analysis

If DI&A coverage is <60%, check FEELS section format — new empathy map templates may have format changes.

---

## Performance Benchmarks (from H1 validation)

| Configuration | Entries | Clusters | Noise | Runtime |
|---|---|---|---|---|
| Cross-project (9 products, 104 maps) | 661 | 14 | 12% | ~3 min (CPU) |
| Single-project DI&A (21 maps) | ~137 | 5-8 | ~15% | <1 min |
| Single-project MASS (3 maps) | ~20 | 3-5 | ~30% | <30s |

**Minimum viable:** 3 empathy maps / ~15 FEELS entries. Below this, clustering is unreliable.

---

## Troubleshooting

**Too many noise points (>40%)**
→ Reduce `min_cluster_size` to 5-8
→ Reduce `min_samples` to 2
→ Check extraction: may be missing entries due to format variant

**Too few clusters (<3)**
→ Reduce `min_cluster_size`
→ Try `cluster_selection_method='leaf'` instead of `'eom'`

**MASS project missing entries**
→ MASS empathy maps use Format B with subsection headers
→ Ensure Format B regex is active in extraction code

**Import errors for umap**
→ Use `import umap.umap_ as umap_module` (not `import umap`)

---

## Integration with Other Skills

This skill **reads from:**
- `[PROJECT]/empathy-maps/*.md` (output of `empathy-map-generator`)

This skill **feeds into:**
- `cross-project-synthesizer` — provides universal cluster taxonomy as input
- `persona-generator` — clustering pre-segments users for persona creation
- `ai-opportunity-analyzer` — cluster membership can weight opportunity scoring (see H8)

---

## Reference Implementation

Full validated implementation: `platform-research/experiments/H1-semantic-clustering/code/run_clustering.py`

This script was the H1 experiment prototype. The SKILL.md describes the same algorithm in prompt form.
