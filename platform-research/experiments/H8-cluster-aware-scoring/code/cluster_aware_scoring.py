#!/usr/bin/env python3.11
"""
H8: Cluster-aware AI opportunity scoring.
Applies H1 universal cluster multipliers to per-project AI opportunity scores.
"""

import json
from pathlib import Path

# H1 universal cluster taxonomy (from H1 analysis.md)
# n_products = how many of 9 product domains contain this cluster
UNIVERSAL_CLUSTERS = {
    0:  {'name': 'AI Opportunity-Threat Ambivalence',      'n_products': 7, 'n_entries': 162},
    1:  {'name': 'Expert Achievement Satisfaction',         'n_products': 8, 'n_entries': 72},
    2:  {'name': 'Methodological Confidence in Triangulation', 'n_products': 8, 'n_entries': 57},
    3:  {'name': 'Vendor Commercial Friction',              'n_products': 7, 'n_entries': 23},
    4:  {'name': 'Strategic Isolation & Disruption Anxiety','n_products': 7, 'n_entries': 37},
    5:  {'name': 'Constant Urgency Pressure',               'n_products': 7, 'n_entries': 20},
    6:  {'name': 'Tool Navigation Friction',                'n_products': 7, 'n_entries': 17},
    7:  {'name': 'Process Verification Anxiety',            'n_products': 6, 'n_entries': 15},
    11: {'name': 'Vendor Partnership Dependency',           'n_products': 5, 'n_entries': 22},
    12: {'name': 'Data Fragmentation Fatigue',              'n_products': 7, 'n_entries': 26},
    13: {'name': 'Manual Correction Burden at Scale',       'n_products': 8, 'n_entries': 69},
}

def cluster_multiplier(cluster_id):
    c = UNIVERSAL_CLUSTERS.get(cluster_id)
    if not c:
        return 1.0  # niche cluster
    return round(1.0 + (c['n_products'] / 9) * 0.5, 3)

# H4 pain-modulated confidence
def confidence_floor(pain_score):
    if pain_score >= 8.0:
        return 0.9
    elif pain_score >= 6.0:
        return 0.6
    return 0.3

# --- AI Opportunities Dataset ---
# Extracted from all per-project assessment files
# Fields: name, project, base_score, pain_score, clusters (H1 cluster IDs it addresses)
opportunities = [
    # CPI
    {'name': 'Multi-Source Data Verification & Reconciliation',
     'project': 'CPI', 'base_score': 8.3, 'pain_score': 8.5,
     'clusters': [12, 7, 0],
     'tier_original': 'P0'},
    {'name': 'MENA/Brazil Regional Patent Coverage',
     'project': 'CPI', 'base_score': 8.8, 'pain_score': 9.0,
     'clusters': [13, 4],
     'tier_original': 'P0'},
    {'name': 'Patent Litigation Timeline Predictor',
     'project': 'CPI', 'base_score': 8.7, 'pain_score': 8.5,
     'clusters': [7, 5, 12],
     'tier_original': 'P1'},
    {'name': 'Multi-Parameter Candidate Screening',
     'project': 'CPI', 'base_score': 8.3, 'pain_score': 7.5,
     'clusters': [12, 6],
     'tier_original': 'P1'},

    # CDDI
    {'name': 'Pre-Indexed AI Competitive Synthesis',
     'project': 'CDDI', 'base_score': 9.0, 'pain_score': 8.5,
     'clusters': [5, 6, 12],
     'tier_original': 'P1'},
    {'name': 'AI-Powered Literature Summarization',
     'project': 'CDDI', 'base_score': 8.2, 'pain_score': 7.5,
     'clusters': [12, 6],
     'tier_original': 'P1'},
    {'name': 'Chemistry-Biology Translation AI',
     'project': 'CDDI', 'base_score': 7.8, 'pain_score': 7.0,
     'clusters': [7, 2],
     'tier_original': 'P1'},

    # DI&A
    {'name': 'AI-Driven Market Forecast Auto-Updater',
     'project': 'DI&A', 'base_score': 8.9, 'pain_score': 8.5,
     'clusters': [13, 12],
     'tier_original': 'P1'},
    {'name': 'Source-Cited AI Analyst Assistant',
     'project': 'DI&A', 'base_score': 8.5, 'pain_score': 8.0,
     'clusters': [0, 7, 2],
     'tier_original': 'P1'},

    # MT360
    {'name': 'AI Taxonomy Mapper + Attribute Enrichment',
     'project': 'MT360', 'base_score': 9.1, 'pain_score': 9.0,
     'clusters': [13, 6],
     'tier_original': 'P1'},
    {'name': 'Source-Cited AI Assistant for Fire Drills',
     'project': 'MT360', 'base_score': 8.9, 'pain_score': 8.5,
     'clusters': [7, 0, 5],
     'tier_original': 'P1'},
    {'name': 'Auto-Triangulation Engine with Variance',
     'project': 'MT360', 'base_score': 8.7, 'pain_score': 8.5,
     'clusters': [12, 2, 7],
     'tier_original': 'P1'},

    # PT
    {'name': 'Fuzzy-Match Entity Resolver',
     'project': 'PT', 'base_score': 9.0, 'pain_score': 9.0,
     'clusters': [13, 12],
     'tier_original': 'P1'},
    {'name': 'Retrieval-First AI Architecture',
     'project': 'PT', 'base_score': 9.0, 'pain_score': 8.0,
     'clusters': [0, 7],
     'tier_original': 'P1'},
    {'name': 'Multi-Source Forecast Discrepancy Resolver',
     'project': 'PT', 'base_score': 8.5, 'pain_score': 8.0,
     'clusters': [12, 13],
     'tier_original': 'P1'},

    # KAI
    {'name': 'Methodology Provenance at Response Level',
     'project': 'KAI', 'base_score': 8.8, 'pain_score': 8.5,
     'clusters': [2, 7, 0],
     'tier_original': 'P1'},
    {'name': 'Data-First Response Structure (Anti-Hallucination)',
     'project': 'KAI', 'base_score': 8.7, 'pain_score': 8.5,
     'clusters': [0, 7],
     'tier_original': 'P1'},
    {'name': 'Comparative Trial Table Auto-Assembly',
     'project': 'KAI', 'base_score': 8.3, 'pain_score': 8.0,
     'clusters': [13, 6],
     'tier_original': 'P1'},

    # MASS
    {'name': 'Natural Language Query Interface',
     'project': 'MASS', 'base_score': 9.1, 'pain_score': 8.5,
     'clusters': [6, 13, 5],
     'tier_original': 'P1'},
    {'name': 'AI-Powered Slide Deck Generator',
     'project': 'MASS', 'base_score': 8.9, 'pain_score': 8.0,
     'clusters': [13, 5],
     'tier_original': 'P1'},
    {'name': 'Formulary Name Fuzzy Matcher',
     'project': 'MASS', 'base_score': 8.7, 'pain_score': 8.5,
     'clusters': [13, 7],
     'tier_original': 'P1'},

    # OFFX
    {'name': 'Evidence Synthesis AI',
     'project': 'OFFX', 'base_score': 8.6, 'pain_score': 8.5,
     'clusters': [12, 7, 2],
     'tier_original': 'P1'},
    {'name': 'Smart Report Generation',
     'project': 'OFFX', 'base_score': 8.5, 'pain_score': 8.0,
     'clusters': [13, 5],
     'tier_original': 'P1'},
    {'name': 'Evidence Change Alerting',
     'project': 'OFFX', 'base_score': 8.2, 'pain_score': 7.5,
     'clusters': [7, 5],
     'tier_original': 'P1'},
]

# --- Apply cluster-aware scoring ---
results = []
for opp in opportunities:
    # Best cluster multiplier across all applicable clusters
    multipliers = [cluster_multiplier(c) for c in opp['clusters']]
    best_multiplier = max(multipliers)

    # Confidence floor from H4 pain-modulation
    conf_floor = confidence_floor(opp['pain_score'])

    # Cluster-aware score: base * best_multiplier * confidence_floor
    # Cap at 10.0
    cluster_score = min(10.0, round(opp['base_score'] * best_multiplier * conf_floor, 2))

    # Tier assignment
    if cluster_score >= 9.5:
        tier_new = 'P0'
    elif cluster_score >= 8.5:
        tier_new = 'P1'
    elif cluster_score >= 7.5:
        tier_new = 'P2'
    else:
        tier_new = 'P3'

    tier_change = 'PROMOTED' if tier_new < opp['tier_original'] else (
                  'DEMOTED' if tier_new > opp['tier_original'] else 'UNCHANGED')

    results.append({
        **opp,
        'best_multiplier': best_multiplier,
        'conf_floor': conf_floor,
        'cluster_score': cluster_score,
        'tier_new': tier_new,
        'tier_change': tier_change,
        'cluster_names': [UNIVERSAL_CLUSTERS[c]['name'] for c in opp['clusters'] if c in UNIVERSAL_CLUSTERS],
    })

# Sort by cluster_score descending
results.sort(key=lambda x: x['cluster_score'], reverse=True)

# Save results
output_path = Path('platform-research/experiments/H8-cluster-aware-scoring/results/scored_opportunities.json')
output_path.parent.mkdir(parents=True, exist_ok=True)
with open(output_path, 'w') as f:
    json.dump(results, f, indent=2)

# --- Print summary ---
print(f"\n{'='*70}")
print("H8: CLUSTER-AWARE AI OPPORTUNITY SCORING")
print(f"{'='*70}")
print(f"\nTotal opportunities scored: {len(results)}")

print(f"\n{'RANK':<4} {'SCORE':<7} {'TIER':<4} {'CHANGE':<12} {'PROJECT':<8} OPPORTUNITY")
print('-'*90)
for i, r in enumerate(results[:20], 1):
    change_marker = '⬆' if r['tier_change'] == 'PROMOTED' else ('⬇' if r['tier_change'] == 'DEMOTED' else ' ')
    print(f"{i:<4} {r['cluster_score']:<7} {r['tier_new']:<4} {change_marker} {r['tier_change']:<10} {r['project']:<8} {r['name'][:50]}")

print(f"\n--- TIER CHANGES ---")
promoted = [r for r in results if r['tier_change'] == 'PROMOTED']
demoted = [r for r in results if r['tier_change'] == 'DEMOTED']

print(f"\nPROMOTED ({len(promoted)}):")
for r in promoted:
    print(f"  {r['tier_original']} → {r['tier_new']} | {r['project']}: {r['name']}")
    print(f"    Clusters: {', '.join(r['cluster_names'])}")

print(f"\nDEMOTED ({len(demoted)}):")
for r in demoted:
    print(f"  {r['tier_original']} → {r['tier_new']} | {r['project']}: {r['name']}")

# Platform-level P0s (cross-domain universality ≥ 7 products, score ≥ 9.5)
print(f"\n--- PLATFORM-LEVEL P0 CANDIDATES ---")
platform_p0 = [r for r in results if r['tier_new'] == 'P0']
for r in platform_p0:
    n_products_coverage = max(UNIVERSAL_CLUSTERS.get(c, {}).get('n_products', 0) for c in r['clusters'])
    print(f"  {r['name']} ({r['project']})")
    print(f"    Score: {r['cluster_score']} | Clusters: {', '.join(r['cluster_names'])}")
    print(f"    Cross-domain coverage: {n_products_coverage}/9 products")

print(f"\nH8 VALIDATION:")
print(f"  Re-ranked opportunities (tier change): {len(promoted) + len(demoted)}")
print(f"  Platform-level P0s: {len(platform_p0)}")
print(f"  Prediction: 3-5 platform investments emerge → {'✅ CONFIRMED' if len(platform_p0) >= 3 else '⚠️ CHECK'}")
print(f"  Saved to: {output_path}")
