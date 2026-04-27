#!/usr/bin/env python3.11
"""
H4: Confidence Propagation in AI Opportunity Scoring

Tests whether weighting AI opportunities by JTBD source confidence (N interviews)
reclassifies 25-35% of Priority 1 assessments.
"""

import json
import re
from pathlib import Path

TOTAL_INTERVIEWS = 10

# ---------------------------------------------------------------------------
# CPI JTBD job clusters with frequency data (from jtbd-cross-persona-analysis.md)
# ---------------------------------------------------------------------------
JTBD_CLUSTERS = [
    {"id": 1, "name": "Freedom-to-Operate Patent Clearance", "n_users": 8, "confidence_label": "Very High"},
    {"id": 2, "name": "Market Opportunity Identification & Candidate Selection", "n_users": 5, "confidence_label": "Very High"},
    {"id": 3, "name": "Pricing Intelligence & Financial Modeling", "n_users": 4, "confidence_label": "High"},
    {"id": 4, "name": "MENA/Regional Market Intelligence Gaps", "n_users": 3, "confidence_label": "Very High"},
    {"id": 5, "name": "Competitive Intelligence & Litigation Tracking", "n_users": 5, "confidence_label": "High"},
    {"id": 6, "name": "Cross-Functional Stakeholder Synthesis & Reporting", "n_users": 5, "confidence_label": "High"},
    {"id": 7, "name": "API Manufacturer Intelligence & Sourcing Validation", "n_users": 6, "confidence_label": "High"},
]

# ---------------------------------------------------------------------------
# CPI AI opportunities with original scores (from ai-opportunity-assessment)
# Mapped to their primary JTBD cluster
# Scores are the original (non-empathy-adjusted) assessments
# ---------------------------------------------------------------------------
AI_OPPORTUNITIES = [
    # Format: name, original_score, original_priority, primary_jtbd_cluster, n_source_users
    # (n_source_users = interviews mentioning this specific opportunity, from cross-persona analysis)
    {"name": "Patent Litigation Timeline Predictor", "score": 8.7, "priority": 1, "jtbd_cluster": 1, "n_source_users": 8},
    {"name": "Multi-Parameter Candidate Screening Agent", "score": 8.3, "priority": 1, "jtbd_cluster": 2, "n_source_users": 5},
    {"name": "Plain-Language Litigation Summarizer", "score": 8.0, "priority": 1, "jtbd_cluster": 1, "n_source_users": 8},
    {"name": "Jurisdiction-Specific Patent Status Tracker", "score": 7.7, "priority": 1, "jtbd_cluster": 4, "n_source_users": 3},
    {"name": "Automated Historical Trend Analyzer", "score": 7.3, "priority": 1, "jtbd_cluster": 5, "n_source_users": 5},
    {"name": "MENA/Brazil Regional Coverage Expander", "score": 8.8, "priority": "P0-post-empathy", "jtbd_cluster": 4, "n_source_users": 3},
    {"name": "Multi-Source Data Verification & Reconciliation", "score": 8.3, "priority": "P0-post-empathy", "jtbd_cluster": 2, "n_source_users": 10},
    {"name": "FTO Analysis Workflow Automation", "score": 7.8, "priority": 2, "jtbd_cluster": 1, "n_source_users": 8},
    {"name": "Biosimilar Comparability Evidence Package Generator", "score": 7.5, "priority": 2, "jtbd_cluster": 1, "n_source_users": 4},
    {"name": "API Manufacturer Due Diligence Automator", "score": 7.2, "priority": 2, "jtbd_cluster": 7, "n_source_users": 6},
    {"name": "Market Entry Timeline Optimizer", "score": 7.0, "priority": 2, "jtbd_cluster": 2, "n_source_users": 5},
    {"name": "Competitive Landscape Intelligence Dashboard", "score": 6.8, "priority": 2, "jtbd_cluster": 5, "n_source_users": 5},
    {"name": "Cross-Functional Reporting Automation", "score": 6.5, "priority": 2, "jtbd_cluster": 6, "n_source_users": 4},
    {"name": "Patent Claims Semantic Similarity Analyzer", "score": 6.3, "priority": 3, "jtbd_cluster": 1, "n_source_users": 4},
    {"name": "Pricing Strategy Optimizer", "score": 6.0, "priority": 3, "jtbd_cluster": 3, "n_source_users": 4},
    {"name": "Regulatory Submission Timeline Predictor", "score": 5.8, "priority": 3, "jtbd_cluster": 1, "n_source_users": 3},
    {"name": "KOL/Expert Network Mapper", "score": 5.5, "priority": 3, "jtbd_cluster": 6, "n_source_users": 2},
]

# ---------------------------------------------------------------------------
# Confidence factor formula
# ---------------------------------------------------------------------------

def confidence_factor(n_users, total=TOTAL_INTERVIEWS):
    """
    Normalizes so that ≥50% coverage = 1.0 (no penalty).
    Coverage below 50% gets proportionally discounted.
    Floor at 0.3 to preserve real low-coverage signals.
    """
    raw = (n_users / total) / 0.5  # 5/10 → 1.0, 3/10 → 0.6, 1/10 → 0.2
    return max(0.3, min(1.0, raw))

# Apply confidence weighting
print(f"\n{'='*70}")
print(f"H4: CONFIDENCE PROPAGATION ANALYSIS — CPI ({TOTAL_INTERVIEWS} interviews)")
print(f"{'='*70}")

print(f"\nConfidence factors by source count:")
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    cf = confidence_factor(n)
    bar = '█' * int(cf * 20)
    print(f"  {n:2d}/10 users → cf={cf:.2f}  {bar}")

results = []
for opp in AI_OPPORTUNITIES:
    cf = confidence_factor(opp["n_source_users"])
    adjusted_score = opp["score"] * cf
    # Reclassify based on adjusted score
    if adjusted_score >= 7.5:
        new_priority = 1
    elif adjusted_score >= 6.5:
        new_priority = 2
    elif adjusted_score >= 5.5:
        new_priority = 3
    else:
        new_priority = 4

    original_p = opp["priority"]
    original_numeric = 1 if original_p in [1, "P0-post-empathy"] else (2 if original_p == 2 else 3)

    changed = new_priority != original_numeric
    direction = ""
    if changed:
        if new_priority > original_numeric:
            direction = f"↓ DEMOTED to P{new_priority}"
        else:
            direction = f"↑ PROMOTED to P{new_priority}"

    results.append({
        **opp,
        "confidence_factor": round(cf, 2),
        "adjusted_score": round(adjusted_score, 2),
        "original_priority_numeric": original_numeric,
        "new_priority": new_priority,
        "changed": changed,
        "direction": direction,
    })

# ---------------------------------------------------------------------------
# Results
# ---------------------------------------------------------------------------
print(f"\n{'='*70}")
print(f"OPPORTUNITY SCORING: BEFORE vs. AFTER CONFIDENCE WEIGHTING")
print(f"{'='*70}")
print(f"{'Opportunity':<45} {'Orig':>6} {'Src':>4} {'CF':>5} {'Adj':>6} {'Result'}")
print(f"{'-'*45} {'-'*6} {'-'*4} {'-'*5} {'-'*6} {'-'*25}")

for r in sorted(results, key=lambda x: x['adjusted_score'], reverse=True):
    flag = " ⚠️" if r["changed"] else ""
    print(f"{r['name']:<45} {r['score']:>5.1f}  {r['n_source_users']:>2}/10  {r['confidence_factor']:>4.2f}  {r['adjusted_score']:>5.2f}  {r['direction'] or 'unchanged'}{flag}")

# Summary statistics
p1_original = [r for r in results if r["original_priority_numeric"] == 1]
p1_demoted = [r for r in p1_original if r["changed"] and r["new_priority"] > 1]
p2_promoted = [r for r in results if r["original_priority_numeric"] == 2 and r["changed"] and r["new_priority"] < 2]
all_changed = [r for r in results if r["changed"]]

print(f"\n{'='*70}")
print(f"SUMMARY")
print(f"{'='*70}")
print(f"Total opportunities analyzed: {len(results)}")
print(f"Original P1 count: {len(p1_original)}")
print(f"P1 demoted by confidence: {len(p1_demoted)} ({len(p1_demoted)/len(p1_original):.0%})")
print(f"P2 promoted by confidence: {len(p2_promoted)}")
print(f"Total changed: {len(all_changed)} ({len(all_changed)/len(results):.0%})")

print(f"\nDEMOTED from P1:")
for r in p1_demoted:
    print(f"  - {r['name']}: {r['n_source_users']}/10 users, CF={r['confidence_factor']}, "
          f"{r['score']:.1f} → {r['adjusted_score']:.2f} (P{r['new_priority']})")

print(f"\nHIGH-CONFIDENCE P1 (confirmed):")
for r in results:
    if r["original_priority_numeric"] == 1 and not r["changed"]:
        print(f"  ✓ {r['name']}: {r['n_source_users']}/10 users, CF={r['confidence_factor']}, score={r['adjusted_score']:.2f}")

# ---------------------------------------------------------------------------
# Prediction check
# ---------------------------------------------------------------------------
print(f"\n{'='*70}")
print(f"PREDICTION CHECK")
print(f"{'='*70}")
p1_reclassification_pct = len(p1_demoted) / len(p1_original) if p1_original else 0
prediction_met = 0.25 <= p1_reclassification_pct <= 0.35
print(f"Predicted: 25-35% of P1 reclassified → Actual: {p1_reclassification_pct:.0%}")
print(f"Prediction matched: {prediction_met}")
print(f"\nNote: Original P1 includes 2 post-empathy P0 upgrades. If those are excluded,")
original_p1_strict = [r for r in results if r["priority"] == 1]
p1_strict_demoted = [r for r in original_p1_strict if r["changed"] and r["new_priority"] > 1]
p1_strict_pct = len(p1_strict_demoted) / len(original_p1_strict) if original_p1_strict else 0
print(f"strict-P1 reclassification: {p1_strict_pct:.0%} ({len(p1_strict_demoted)}/{len(original_p1_strict)})")

# ---------------------------------------------------------------------------
# Save results
# ---------------------------------------------------------------------------
output_dir = Path('/Users/joan.saez-pons/code/researcher_ux/platform-research/experiments/H4-confidence-propagation/results')
output_dir.mkdir(exist_ok=True)

with open(output_dir / 'confidence_propagation_results.json', 'w') as f:
    json.dump({
        "hypothesis": "H4",
        "dataset": "CPI",
        "total_interviews": TOTAL_INTERVIEWS,
        "opportunities": results,
        "summary": {
            "total_opportunities": len(results),
            "p1_count_original": len(p1_original),
            "p1_demoted": len(p1_demoted),
            "p1_demotion_rate": round(p1_reclassification_pct, 3),
            "prediction_met": prediction_met,
            "total_reclassified": len(all_changed),
            "reclassification_rate": round(len(all_changed)/len(results), 3),
        }
    }, f, indent=2)

print(f"\nResults saved to {output_dir}")
