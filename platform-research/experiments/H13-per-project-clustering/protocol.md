# H13 Protocol: Per-Project Empathy Clustering

**Status:** IN PROGRESS  
**Date:** 2026-04-27  
**Hypothesis slug:** per-project-clustering

---

## Hypothesis

H1 produced a global cross-project cluster taxonomy from 661 FEELS entries across all 9 products. H9 validated the clustering skill on DI&A (21 maps, single project). H13 extends this: per-project clustering reveals project-specific emotional patterns that are invisible in the global view, because global clustering averages out local signal.

## Prediction

1. Every project with ≥5 empathy maps produces 3-8 meaningful clusters at <20% noise.
2. 60-80% of per-project cluster themes match the 11 global H1 clusters (universal patterns visible at project level).
3. Each project produces ≥1 cluster with no equivalent in the global taxonomy (project-specific emotional pattern — local signal that global clustering smoothed away).
4. Smaller projects (MASS=3 maps, KAI=5, MT360=6) have fewer clusters (3-4) vs. richer projects (DI&A=21, Fusion=21, CDDI=20).

## Method

1. **Reuse H9 pipeline** — sentence-transformers/all-MiniLM-L6-v2 → UMAP → HDBSCAN
2. **Adaptive params** — scale `min_cluster_size` with project size: 3-5 maps → mcs=3; 6-10 maps → mcs=5; 11+ maps → mcs=8
3. **Run on 8 remaining projects** — CPI, CDDI, Fusion, PT, MASS, MT360, KAI, OFFX
4. **Output** — per-project clustering-analysis-automated.md in each project's empathy-maps/ dir
5. **Comparative analysis** — tabulate cluster counts, noise rates, and theme overlap with H1 taxonomy

## Confirmatory if

- ≥6 of 8 projects produce 3+ clusters at <20% noise
- ≥1 project-specific cluster not in H1 taxonomy found for ≥4 projects

## Disconfirmatory if

- Most per-project clusters are just subsets of H1 clusters with nothing new
- Small projects (MASS, KAI) produce only noise (no stable clusters)
