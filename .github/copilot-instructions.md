# UX Research Repository — Copilot Instructions

This is a UX research codebase for Clarivate product research. It contains interview artefacts, analysis outputs, and reusable research skills. All research follows Nielsen Norman Group methodology.

---

## Repository Structure

Each product has its own folder with a standardised sub-structure:

```
[PROJECT]/
  transcripts/        # Raw interview transcripts (.vtt or .txt)
  empathy-maps/       # One empathy-map-[name].md per participant + clustering-analysis.md
  journey/            # One user-journey-[name].md per participant
  personas/           # personas-overview.md + optional individual persona files
  jtbd/               # jtbd-analysis-[name].md per participant + combined jtbd-analysis-[PROJECT].md
  scenarios/          # scenario-map-[date].md
  ai-opportunities/   # ai-opportunity-assessment.md
```

Active tracked projects: **CCI** (Cortellis Clinical Intelligence). Other project folders exist locally but are in .gitignore.

---

## CCI Project — Current State (as of 2026-05-06)

**Participants:** 21 users across 8 organisations (pharma, biotech, CRO, independent consultants)
**Artefacts completed:** empathy maps (21), journey maps (21), clustering analysis, personas (4), JTBD analyses (21 individual + 1 combined)

### Four CCI Personas

| Persona | Real name | Based on | Archetype |
|---|---|---|---|
| Cristina Morrow | Strategic Intelligence Director | cristina-goso, jack-jacobs, sol-reyna, russ-steward, andrea-martin, barbara-novo, marco-schindler, maurice-mezzino | BD/Strategy/M&A |
| Kevin Park | Drug Discovery Scientist | kevin-sokol, daniel-emerling, shrikant-wankhade, andre-bicudo | Drug discovery/medicinal chemistry |
| Freya Hartmann | Safety & Regulatory Expert | fredrik-gruenenfelder, lee-mcguinness, jana-mayerova, ivan-santos, rosanne-middleton | Pharmacovigilance/patents/regulatory |
| Sarah Chen | Information Professional | liz-stoehr, sarah-vogel, anna-migliazza, gaurav-vij | Information specialist/CI analyst |

### 14 Emotional Clusters (from empathy-clustering)

Universal patterns (>40% of cohort):
1. **Expert Confidence Under Deadline Pressure** — 12 users (57%) — dominant signal
2. **Platform Value Ambivalence** — 11 users (52%) — appreciation + erosion of trust
3. **Search Discovery Uncertainty** — 9 users (43%) — self-blame for platform failures
4. **Persistent UX Disorientation** — 9 users (43%) — frustration → resignation

Common patterns (5–8 users): Multi-Tool Resignation, Professional Self-Restraint, Cautious AI Ambivalence, Data Access Dead-Ends, Visualisation Cognitive Overload, Patent Access Dead-End, Alert Urgency/Setup Fatigue, Mission-Driven Source Rigour

Niche patterns (3–4 users): Workflow Workaround Burden, Stale Data Curation Overload

Full cluster details: `CCI/empathy-maps/clustering-analysis.md`

---

## Research Pipeline

```
Transcripts
    ↓
empathy-map-generator  →  [project]/empathy-maps/empathy-map-[name].md
    ↓
user-journey           →  [project]/journey/user-journey-[name].md
    ↓
empathy-clustering     →  [project]/empathy-maps/clustering-analysis.md  (runs Python)
    ↓
persona-generator      →  [project]/personas/personas-overview.md
    ↓
jtbd-analyzer          →  [project]/jtbd/jtbd-analysis-[name].md
    ↓
scenario-mapper        →  [project]/scenarios/scenario-map-[date].md
    ↓
ai-opportunity-analyzer →  [project]/ai-opportunities/ai-opportunity-assessment.md
```

Reusable prompts for all steps live in `.github/prompts/`. The same skills also exist as Claude Code skills in `.claude/skills/` (for automated agentic execution).

---

## Methodology Reference

- **Empathy maps:** NN/g 4-quadrant (Says / Thinks / Does / Feels) + Summary + AI Opportunity
- **Journey maps:** NN/g 5-component (Actor, Scenario, Phases, Emotions, Opportunities)
- **Personas:** NN/g qualitative personas — segmented by job function + goal + stakes
- **JTBD:** Christensen framework — When [context] / I want to [motivation] / So I can [outcome]; functional + emotional + social dimensions
- **Scenario mapping:** NN/g 5-element (Actor + Motivator + Intention + Action + Resolution) + Agile user stories
- **Clustering:** sentence-transformers all-MiniLM-L6-v2 → UMAP(15d) → HDBSCAN — reference implementation in `platform-research/experiments/H1-semantic-clustering/code/run_clustering.py`

---

## Naming Conventions

- Participant files: use `firstname-lastname` lowercase hyphenated (e.g., `andre-bicudo`)
- Empathy maps: `empathy-map-[name].md`
- Journey maps: `user-journey-[name].md`
- JTBD individual: `jtbd-analysis-[name].md`
- JTBD combined: `jtbd-analysis-[PROJECT].md`
- Personas overview: `personas-overview.md`
- Individual persona: `persona-[firstname-lastname].md`

---

## Key Files to Know

| File | Contents |
|---|---|
| `CCI/empathy-maps/clustering-analysis.md` | 14-cluster emotional analysis, 21 users, design implications |
| `CCI/personas/personas-overview.md` | 4 CCI personas with full NNg persona profiles |
| `CCI/jtbd/jtbd-analysis-CCI.md` | Combined JTBD analysis across all CCI personas |
| `docs/ai-powered-ux-workflow.md` | Full pipeline documentation |
| `platform-research/experiments/H1-semantic-clustering/` | Validated Python clustering implementation |

---

## Python Environment (for empathy-clustering)

Required packages:
```
sentence-transformers hdbscan umap-learn scikit-learn pandas numpy
```

Install once: `pip install sentence-transformers hdbscan umap-learn scikit-learn pandas numpy`
