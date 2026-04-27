# Experiment H5: Cross-Project Meta-Analysis Skill Design

**Hypothesis:** A cross-project-synthesizer skill reading outputs across all 9 product domains would reveal universal pain archetypes, shared persona patterns, and cross-domain AI opportunities.

**Prediction:** Analysis of all 53 interviews would identify 3-5 pain points universal to Clarivate research workflows, plus 2-3 persona archetypes appearing across multiple products.

**Status:** PROTOCOL LOCKED — 2026-04-27

---

## Skill Design

### New Skill: `cross-project-synthesizer`

This skill addresses the "outer loop" gap in the platform. Unlike all other skills that work per-project, this skill reads across ALL project outputs to find patterns invisible at the single-project level.

**Input:** A list of project directories (or "all" to scan automatically)

**Output:** 
- `cross-project-synthesis/universal-pain-analysis.md` — pain points appearing in 5+ projects
- `cross-project-synthesis/shared-persona-archetypes.md` — persona patterns recurring across domains
- `cross-project-synthesis/cross-domain-ai-opportunities.md` — AI opportunities applicable platform-wide
- `cross-project-synthesis/meta-findings.md` — strategic insights for Clarivate product platform team

### Algorithm Design

The key insight: Claude Opus 4.7 / Sonnet 4.6 has a 200K token context window. The ENTIRE cross-project dataset (400+ files at ~500 words each ≈ 200K tokens) may fit in a single context. No RAG needed — direct synthesis.

**Approach:**
1. Collect all personas, JTBD cross-persona analyses, and AI opportunity files
2. Feed into a single long-context synthesis call with structured prompts
3. Ask: What pain points appear across 5+ projects? What persona archetypes recur? What AI opportunities show up everywhere?

**Fallback if context limit exceeded:**
- Hierarchical synthesis: synthesize per-product → then synthesize the syntheses
- RAG approach: embed all content, query with specific cross-domain questions

### SKILL.md Draft

Key sections for the new skill:
- **Input format:** `[project-list] or "all"` + optional focus area
- **Synthesis dimensions:** Pain universality, Persona archetypes, AI opportunity overlap, Research methodology patterns
- **Output structure:** Universal findings + project-specific deviations + strategic recommendations
- **Quality check:** Every universal claim traced to 3+ specific project/user sources

## Validation Method

Test against known patterns:
1. **Known universal**: "vendor-backed AI" trust pattern (confirmed in DI&A + CPI + CDDI) — should be discovered
2. **Known domain-specific**: MENA patent data gap (CPI-specific) — should NOT appear as universal
3. **Hypothesis to test**: Is "data fragmentation/triangulation" a universal pain? (appears in DI&A, likely in others)

## Success Criteria

| Criterion | Success | Failure |
|-----------|---------|---------|
| Universal patterns | 3-5 pain points found in 5+ projects | 0-1 universal patterns |
| Persona archetypes | 2-3 recurring archetypes identified | All personas appear product-specific |
| Vendor trust signal | "Vendor-backed AI" trust identified as cross-domain | Signal missed or diluted |
| MENA specificity | MENA gap correctly scoped to CPI only | Wrongly elevated to universal |
| Actionability | Strategic recs for Clarivate platform team | Vague summaries only |

## Expected Impact

If confirmed: New `cross-project-synthesizer` skill deployed as the final stage of the pipeline, giving the platform-level view that no single-project analysis can provide. Direct input to Clarivate product strategy for cross-portfolio AI investments.

## Next Steps After Protocol Confirmation

1. Write SKILL.md for `cross-project-synthesizer`
2. Test on DI&A + CPI (2-project version first)
3. Scale to all 9 projects
4. Validate strategic findings with Tracy Darbeloff (Clarivate Lead PM)
