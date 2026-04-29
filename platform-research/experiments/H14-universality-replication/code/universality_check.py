#!/usr/bin/env python3
"""
H14: Independent Universality Replication
Tests whether H1's 11 universal clusters replicate through per-project
independent detection (H13 outputs) via embedding similarity.
"""

import re, json
from pathlib import Path
import numpy as np

BASE = Path('/Users/joan.saez-pons/code/researcher_ux')

# ── H1 Universal Cluster Descriptions ────────────────────────────────────────
H1_CLUSTERS = [
    {
        'id': 0, 'name': 'AI Opportunity-Threat Ambivalence',
        'h1_products': 7,
        'description': (
            'Users excited about AI AND anxious about displacement. '
            'AI tools promising but untrustworthy. Fear of skill atrophy. '
            'Hope for automation combined with anxiety about job relevance.'
        )
    },
    {
        'id': 1, 'name': 'Expert Achievement Satisfaction',
        'h1_products': 8,
        'description': (
            'Emotional target state when work succeeds. Pride in expertise. '
            'Satisfaction from completing complex analysis. Energized by impact. '
            'Recognition of deep domain knowledge.'
        )
    },
    {
        'id': 2, 'name': 'Methodological Confidence in Triangulation',
        'h1_products': 8,
        'description': (
            'Trusts their own process when rigorous. Confidence from cross-validation. '
            'Methodological pride. Strategic thinking. Analytical certainty from multiple sources.'
        )
    },
    {
        'id': 3, 'name': 'Vendor Commercial Friction',
        'h1_products': 7,
        'description': (
            'Frustrated by pricing, hopeful for innovation. Vendor lock-in anxiety. '
            'Dependency on external data providers. Consulting cost burden. '
            'Appreciation for vendor support mixed with frustration at limitations.'
        )
    },
    {
        'id': 4, 'name': 'Strategic Isolation & Disruption Anxiety',
        'h1_products': 7,
        'description': (
            'Anxious about CI function isolation. AI displacement fear. '
            'Solo operator pressure. Being the only person with this knowledge. '
            'Fear of organizational irrelevance.'
        )
    },
    {
        'id': 5, 'name': 'Constant Urgency Pressure',
        'h1_products': 7,
        'description': (
            'Deliver everything yesterday organizational culture. Deadline pressure. '
            'Stretched thin. Launch mode stress. Multiple simultaneous demands. '
            'Time poverty. Wary focused under pressure.'
        )
    },
    {
        'id': 6, 'name': 'Tool Navigation Friction',
        'h1_products': 7,
        'description': (
            'Frustrated by navigation lag, slow tools, cumbersome interfaces. '
            'Hunting and pecking. Too many clicks. Platform usability frustration. '
            'Workflow interruption from tool limitations.'
        )
    },
    {
        'id': 7, 'name': 'Process Verification Anxiety',
        'h1_products': 6,
        'description': (
            'Concerned about manual verification steps. Need to double-check AI outputs. '
            'Accuracy stakes are high. Cannot trust automated results without review. '
            'Compliance verification burden.'
        )
    },
    {
        'id': 8, 'name': 'Data Fragmentation Fatigue',
        'h1_products': 7,
        'description': (
            'Manually piecing data from multiple sources. Fragmented vendor landscape. '
            'Data silos. Triangulation burden across IQVIA, DRG, Clarivate. '
            'Frustrated by lack of unified data layer.'
        )
    },
    {
        'id': 9, 'name': 'Manual Correction Burden at Scale',
        'h1_products': 8,
        'description': (
            'Correcting data across 60-80 markets. Manual reconciliation. '
            'Formulary name mapping. Payer ID mismatch. Data cleaning at scale. '
            'Half-day Excel sessions. Overwhelmed by manual work volume.'
        )
    },
    {
        'id': 10, 'name': 'Vendor Partnership Dependency',
        'h1_products': 5,
        'description': (
            'Collaborative but vulnerable to vendor deprecation. '
            'Appreciation for vendor relationship mixed with dependency anxiety. '
            'Consulting reliance. Hoping vendor will innovate to solve problems.'
        )
    },
]

# ── H13 Per-Project Cluster Themes (from run output) ─────────────────────────
# Format: {project: [(cluster_label, n_entries, [sample_emotions])]}
H13_CLUSTERS = {
    'DI&A': [  # From H9
        ('Data triangulation burden, fragmented sources, frustrated', 20, ['frustrated', 'overwhelmed']),
        ('AI trust anxiety, credibility concerns, explainability', 18, ['uncertain', 'anxious']),
        ('Cross-functional communication friction, orchestration', 15, ['pressured', 'collaborative']),
        ('Expert achievement, satisfaction, methodological confidence', 25, ['confident', 'satisfied']),
        ('Deadline pressure, urgency, stretched thin', 22, ['pressured', 'focused']),
        ('Data quality verification, manual checking anxiety', 12, ['anxious', 'vigilant']),
        ('Strategic impact, excited, energized', 15, ['excited', 'energized']),
        ('Vendor dependency, tool navigation frustration', 10, ['frustrated', 'constrained']),
    ],
    'CPI': [
        ('frustrated, uncertain, anxious about data and verification', 32, ['frustrated', 'uncertain', 'anxious']),
        ('confident, pressured, uncertain about methodology', 6, ['confident', 'pressured', 'uncertain']),
        ('pressured, satisfied, confident in process', 30, ['pressured', 'satisfied', 'confident']),
        ('strategic, pressured, accomplished', 11, ['strategic', 'pressured', 'accomplished']),
    ],
    'CDDI': [
        ('energized, excited, satisfied from research work', 20, ['energized', 'excited', 'satisfied']),
        ('thoughtful, anxious, frustrated about process', 12, ['thoughtful', 'anxious', 'frustrated']),
        ('frustrated, overwhelmed, resigned with manual burden', 11, ['frustrated', 'overwhelmed', 'resigned']),
        ('pressured, focused, analytical under deadline', 8, ['pressured', 'focused', 'analytical']),
        ('confident, frustrated, proud in expertise', 9, ['confident', 'frustrated', 'proud']),
        ('confident, uncertain, challenged methodologically', 13, ['confident', 'uncertain', 'challenged']),
        ('frustrated, pragmatic, responsible about quality', 19, ['frustrated', 'pragmatic', 'responsible']),
    ],
    'Fusion': [
        ('skeptical, curious, frustrated with tools', 8, ['skeptical', 'curious', 'frustrated']),
        ('appreciative, curious, frustrated with vendor', 6, ['appreciative', 'curious', 'frustrated']),
        ('frustrated, exasperated, overwhelmed by manual work', 14, ['frustrated', 'exasperated', 'overwhelmed']),
        ('exasperated, grateful, uncertain about AI outputs', 6, ['exasperated', 'grateful', 'uncertain']),
        ('frustrated, curious, appreciative mixed feelings', 5, ['frustrated', 'curious', 'appreciative']),
        ('confident, uncertain, pragmatic about method', 10, ['confident', 'uncertain', 'pragmatic']),
        ('uncertain, proud, strategic in analysis', 12, ['uncertain', 'proud', 'strategic']),
        ('frustrated, skeptical, impatient with process', 6, ['frustrated', 'skeptical', 'impatient']),
        ('overwhelmed, concerned about accuracy stakes', 9, ['overwhelmed', 'concerned']),
        ('curious, excited, hopeful about AI potential', 15, ['curious', 'excited', 'hopeful']),
        ('enthusiastic, excited, ambitious about innovation', 8, ['enthusiastic', 'excited', 'ambitious']),
        ('cautious, skeptical, curious about AI trust', 6, ['cautious', 'skeptical', 'curious']),
        ('pragmatic, overwhelmed, cautious about scale', 10, ['pragmatic', 'overwhelmed', 'cautious']),
    ],
    'PT': [
        ('confident, hopeful, constrained by resources', 9, ['confident', 'hopeful', 'constrained']),
        ('stretched thin, wary, focused under urgency', 20, ['stretched thin', 'wary', 'focused']),
        ('collaborative, generous, pragmatic solidarity', 9, ['collaborative', 'pragmatic']),
        ('frustrated, resigned, mildly frustrated with limitations', 11, ['frustrated', 'resigned']),
    ],
    'MASS': [
        ('efficiency drive, manual process inefficiency frustration', 5, ['frustrated', 'efficiency-focused']),
        ('emotional mixed states', 5, ['varied']),
        ('consulting dependency burden, vendor appreciation', 6, ['dependent', 'appreciative']),
        ('AI adoption excitement, data storytelling mastery', 12, ['excited', 'proud', 'hopeful']),
        ('formulary name mapping, update lag anxiety, workflow pain', 10, ['frustrated', 'anxious']),
        ('strategic impact, responsible, quality-driven', 9, ['responsible', 'strategic']),
        ('solo operator pressure, overwhelmed', 8, ['stressed', 'overwhelmed']),
        ('data reconciliation confusion, verification anxiety', 11, ['confused', 'anxious']),
        ('AI slide creation pride, translating complexity mastery', 13, ['proud', 'satisfied']),
    ],
    'MT360': [
        ('confident, curious, skeptical about methods and tools', 24, ['confident', 'curious', 'skeptical']),
        ('pragmatic, demanding, results-focused', 6, ['pragmatic', 'demanding']),
        ('frustrated, concerned, skeptical about data quality', 11, ['frustrated', 'concerned', 'skeptical']),
    ],
    'KAI': [
        ('vigilant, enthusiastic, pragmatic regulatory watchfulness', 8, ['vigilant', 'enthusiastic', 'pragmatic']),
        ('confident, frustrated, curious about process', 15, ['confident', 'frustrated', 'curious']),
        ('unsatisfied, curious, frustrated with current tools', 8, ['unsatisfied', 'curious', 'frustrated']),
    ],
    'OFFX': [
        ('confident, humbled, critical about quality and limitations', 16, ['confident', 'humbled', 'critical']),
        ('purposeful, intellectually engaged, intellectually energized', 18, ['purposeful', 'engaged', 'energized']),
        ('pressured, knowledgeable, constrained by resources', 16, ['pressured', 'knowledgeable', 'constrained']),
    ],
}

PROJECTS = list(H13_CLUSTERS.keys())


def build_cluster_text(label, emotions):
    """Build a rich text description for embedding."""
    return f"{label}. Emotional states: {', '.join(emotions)}."


def main():
    from sentence_transformers import SentenceTransformer
    from scipy.spatial.distance import cosine

    print("H14: Independent Universality Replication")
    print("=" * 60)

    model = SentenceTransformer('all-MiniLM-L6-v2')

    # Embed H1 cluster descriptions
    h1_texts = [f"{c['name']}. {c['description']}" for c in H1_CLUSTERS]
    h1_embeddings = model.encode(h1_texts, show_progress_bar=False)

    # For each project, embed per-project clusters and find best H1 match
    SIMILARITY_THRESHOLD = 0.35
    h1_independent_count = {c['id']: set() for c in H1_CLUSTERS}
    h1_best_similarities = {c['id']: [] for c in H1_CLUSTERS}

    project_assignments = {}
    for proj, clusters in H13_CLUSTERS.items():
        proj_texts = [build_cluster_text(label, emotions) for label, n, emotions in clusters]
        proj_embeddings = model.encode(proj_texts, show_progress_bar=False)

        assignments = []
        for i, (label, n, emotions) in enumerate(clusters):
            # Cosine similarity to each H1 cluster
            sims = [1 - cosine(proj_embeddings[i], h1_embeddings[j]) for j in range(len(H1_CLUSTERS))]
            best_h1_idx = int(np.argmax(sims))
            best_sim = sims[best_h1_idx]

            if best_sim >= SIMILARITY_THRESHOLD:
                h1_id = H1_CLUSTERS[best_h1_idx]['id']
                h1_independent_count[h1_id].add(proj)
                h1_best_similarities[h1_id].append(best_sim)
                assignments.append((label[:50], H1_CLUSTERS[best_h1_idx]['name'], round(best_sim, 3)))
            else:
                assignments.append((label[:50], 'NO MATCH (project-specific)', round(best_sim, 3)))

        project_assignments[proj] = assignments

    # ── Per-project assignment table ─────────────────────────────────────────
    print("\n=== PER-PROJECT CLUSTER → H1 MAPPING ===")
    for proj in PROJECTS:
        print(f"\n{proj}:")
        for local_label, h1_name, sim in project_assignments[proj]:
            marker = '✅' if h1_name != 'NO MATCH (project-specific)' else '🆕'
            print(f"  {marker} ({sim:.2f}) {local_label[:45]:<45} → {h1_name[:40]}")

    # ── Universality replication table ───────────────────────────────────────
    print("\n\n=== H1 CLUSTER REPLICATION (independent per-project detection) ===")
    print(f"{'H1 Cluster':<42} {'H1 Claim':>9} {'Replicated':>10}  {'Δ':>4}  {'Verdict'}")
    print("-" * 85)

    verdicts = []
    for c in sorted(H1_CLUSTERS, key=lambda x: -x['h1_products']):
        ind_count = len(h1_independent_count[c['id']])
        delta = ind_count - c['h1_products']
        if ind_count >= c['h1_products'] - 1:
            verdict = '✅ REPLICATES'
        elif ind_count >= c['h1_products'] - 2:
            verdict = '⚠️  PARTIAL'
        else:
            verdict = '❌ FAILS'
        print(f"{c['name']:<42} {c['h1_products']:>9}/9 {ind_count:>9}/9  {delta:>+4}  {verdict}")
        verdicts.append({'cluster': c['name'], 'h1': c['h1_products'], 'replicated': ind_count, 'delta': delta})

    # ── Rank correlation ─────────────────────────────────────────────────────
    from scipy.stats import spearmanr
    h1_ranks = [c['h1_products'] for c in H1_CLUSTERS]
    ind_ranks = [len(h1_independent_count[c['id']]) for c in H1_CLUSTERS]
    rho, p = spearmanr(h1_ranks, ind_ranks)
    print(f"\nSpearman rank correlation (H1 count vs. independent count): ρ={rho:.3f}, p={p:.3f}")

    # ── Summary ──────────────────────────────────────────────────────────────
    replicates = sum(1 for v in verdicts if '✅' in v.get('cluster', '') or (v['replicated'] >= v['h1'] - 1))
    # Recount properly
    replicates = sum(1 for c in H1_CLUSTERS if len(h1_independent_count[c['id']]) >= c['h1_products'] - 1)
    fails = sum(1 for c in H1_CLUSTERS if len(h1_independent_count[c['id']]) < c['h1_products'] - 2)
    novel_total = sum(1 for proj in PROJECTS for _, h1_name, _ in project_assignments[proj] if h1_name == 'NO MATCH (project-specific)')

    print(f"\n=== SUMMARY ===")
    print(f"H1 clusters that replicate independently (±1): {replicates}/11")
    print(f"H1 clusters that fail replication (Δ < -2): {fails}/11")
    print(f"Novel project-specific clusters (no H1 match): {novel_total} total")
    print(f"Rank correlation: ρ={rho:.3f}")

    # Save results
    results_path = Path(__file__).parent.parent / 'results' / 'universality_replication.json'
    results_path.parent.mkdir(exist_ok=True)
    with open(results_path, 'w') as f:
        json.dump({
            'h1_independent_counts': {str(k): list(v) for k, v in h1_independent_count.items()},
            'rank_correlation': {'rho': round(rho, 3), 'p': round(p, 3)},
            'verdicts': verdicts,
            'novel_clusters': novel_total,
        }, f, indent=2)
    print(f"\nResults saved: {results_path}")


if __name__ == '__main__':
    main()
