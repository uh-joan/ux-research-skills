# H14 Protocol: Independent Universality Replication

**Status:** IN PROGRESS  
**Date:** 2026-04-27  
**Hypothesis slug:** universality-replication

---

## Hypothesis

H1 identified 11 "universal" clusters by running global clustering on all 661 FEELS entries mixed together from 9 products. This is susceptible to bias: global clustering may find themes that span products not because users independently experience them, but because the global mixture artificially pulls entries toward common geometric regions.

H13 produced independent per-project clusters for all 9 products. H14 tests whether H1's universal clusters replicate through independent per-project detection — a stronger test of genuine universality.

**If a cluster theme appears independently in 7/9 products' own clustering, it is truly universal. If it appears in <4/9, the H1 claim was inflated by global mixing.**

## Prediction

1. H1's top universal clusters (AI Ambivalence, Data Fragmentation, Manual Correction) will replicate in ≥6/9 products independently.
2. Some of H1's 11 "universal" clusters will fail to replicate (appear in <4 products independently) — exposing them as global-mixing artifacts.
3. The product-count ordering from H1 is preserved in independent replication (high-count clusters stay high, low-count clusters drop).

## Method

1. **Embed all H1 cluster labels** using sentence-transformers
2. **Embed all H13 per-project cluster summaries** (emotion labels + sample entries)
3. **For each project × H1 cluster pair**: compute cosine similarity between per-project cluster embeddings and H1 cluster centroids
4. **Assign**: per-project cluster → nearest H1 cluster if similarity ≥ 0.35
5. **Count**: how many products independently detect each H1 cluster
6. **Compare**: independent count vs. H1's reported count

## Confirmatory if

- Top 5 H1 clusters replicate in ≥6/9 products independently
- Rank correlation between H1 count and independent count ≥ 0.7

## Disconfirmatory if

- Multiple H1 "universal" clusters (≥3) replicate in <4/9 products
- Rank correlation < 0.5
