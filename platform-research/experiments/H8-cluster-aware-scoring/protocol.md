# Experiment H8: Cluster-Aware AI Opportunity Scoring

**Hypothesis:** Using H1 universal cluster taxonomy as weights in ai-opportunity-analyzer scoring
would produce a more strategically defensible cross-domain AI roadmap.

**Prediction:** Rerunning cross-project AI opportunity scoring with cluster-aware weights surfaces
3-5 platform-level AI investments distinct from current per-product P1 lists, specifically:
- Data Fragmentation (Cluster 12, 7/9 products) should surface a cross-source synthesis tool
- Manual Correction Burden (Cluster 13, 8/9 products) should surface a market data auto-correction tool
- AI Ambivalence (Cluster 0, 7/9 products) should surface trust/explainability infrastructure
- At least 1 P1 in current per-product lists should be demoted when cross-domain prevalence weighting applied

**Status:** PROTOCOL LOCKED — 2026-04-27

---

## Design

### Cluster Universality Multipliers

From H1 results, map each universal cluster to a score multiplier based on cross-domain prevalence:

| Cluster | Name | Products | Multiplier |
|---------|------|----------|-----------|
| 0 | AI Opportunity-Threat Ambivalence | 7/9 | 1.4 |
| 1 | Expert Achievement Satisfaction | 8/9 | 1.45 |
| 2 | Methodological Confidence | 8/9 | 1.45 |
| 3 | Vendor Commercial Friction | 7/9 | 1.35 |
| 4 | Strategic Isolation & Disruption Anxiety | 7/9 | 1.35 |
| 5 | Constant Urgency Pressure | 7/9 | 1.35 |
| 6 | Tool Navigation Friction | 7/9 | 1.30 |
| 7 | Process Verification Anxiety | 6/9 | 1.25 |
| 12 | Data Fragmentation Fatigue | 7/9 | 1.35 |
| 13 | Manual Correction Burden at Scale | 8/9 | 1.45 |
| 11 | Vendor Partnership Dependency | 5/9 | 1.20 |
| Niche | <5 products | 1-4 | 1.00 |

Multiplier formula: `1.0 + (n_products / 9) * 0.5`

### Mapping AI Opportunities to Clusters

For each AI opportunity in the cross-project synthesis, identify which H1 universal cluster(s) it addresses.
Apply the highest applicable multiplier to the existing composite score.

Then apply H4's pain-modulation rule: for opportunities addressing pain ≥ 8/10, set confidence_floor = 0.9.

### Data Source

Pull from `cross-project-synthesis/ai-opportunity-ranking.md` (the cross-domain opportunity list).
If it doesn't exist or is insufficient, use per-project JTBD AI opportunity lists and aggregate.

### Success Criteria

- At least 3 opportunities re-ranked relative to current P1 lists
- At least 1 new "platform-level" P0/P1 emerges that is NOT already a P1 in any single product
- The final ranking is explainable: "this is P0 because it addresses a pain shared by 8/9 products"

---

## What to Measure

1. **Re-ranking magnitude**: How many opportunities change tier (P1→P0, P2→P1, etc.)?
2. **New platform-level P0/P1s**: How many appear only when cross-domain weighting is applied?
3. **Demotion rate**: How many per-product P1s fall to P2+ when their cluster is niche (1-2 products)?
4. **Alignment with H1 universal clusters**: Does the final ranking match intuition from the cluster taxonomy?
