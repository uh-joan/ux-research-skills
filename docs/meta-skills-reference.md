# Meta-Skills Reference

These skills operate **above** the per-project workflow. They don't generate research artifacts for a single project — they orchestrate or synthesize across projects or across the entire pipeline.

---

## `/research-pipeline` — Pipeline Auditor & Orchestrator

**What it does:** Audits which workflow steps are missing for a project (or all projects) and runs the missing ones in sequence.

**When to use:**
- You inherited a partially-completed project and don't know what's been done
- You want to fill gaps across all 9 projects without manually checking each one
- You want to run all missing steps for a new project in one command

**It does NOT replace running individual skills.** It just detects gaps and chains them.

**Usage:**
```bash
/research-pipeline          # audit + fill gaps for ALL projects
/research-pipeline DI&A     # audit + fill gaps for one project
```

**What it checks per project:**

| Step | Expected output |
|------|----------------|
| Transcripts | files in `transcripts/` |
| Empathy maps | one `.md` per transcript in `empathy-maps/` |
| Journey maps | one `.md` per transcript in `journey/` |
| Personas | 3-5 `.md` files in `personas/` |
| JTBD | one `.md` per transcript + cross-persona in `jtbd/` |
| Scenarios | at least one `.md` in `scenarios/` |
| AI opportunities | at least one `.md` in `ai-opportunities/` |

**Known gaps as of 2026-04-27:** Scenario maps are missing for all 9 projects (13/~45 expected). Fusion has 0 JTBD files despite 21 interviews.

---

## `/cross-project-synthesizer` — Cross-Domain Synthesis

**What it does:** Reads completed research outputs across multiple projects and synthesizes patterns that are invisible at per-project scope — shared personas, universal pain themes, cross-domain AI opportunities.

**When to use:**
- You've completed (or mostly completed) multiple projects and want to find what they have in common
- You're building a platform-level roadmap, not a product-specific one
- You want to know if a pain found in project A also appears in projects B, C, D

**Usage:**
```bash
/cross-project-synthesizer              # synthesize across all discovered projects
/cross-project-synthesizer DI&A CPI     # synthesize across specific projects
```

**Output:** `cross-project-synthesis/` directory with:
- Universal persona archetypes (patterns across project-specific personas)
- Shared pain themes with frequency across projects
- Cross-domain AI opportunity ranking

**Relationship to `/empathy-clustering`:** The clustering skill finds shared emotional patterns within or across projects at the raw FEELS level. The synthesizer works at a higher level — it reads finished artifacts (personas, JTBD, AI opportunity assessments) and finds strategic patterns across them. They complement each other; clustering feeds the synthesizer.

---

*These skills don't belong in the per-project workflow diagram — they're tools for when you step back from individual projects.*
