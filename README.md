# UX Research Skills

Transform interview transcripts into strategic product insights — in hours, not weeks.

Built for UX researchers following Nielsen Norman Group methodology and Jobs-to-be-Done framework.

---

## What you get

From a set of interview transcripts, this pipeline produces:

- **Empathy maps** — what users say, think, do, and feel (per participant)
- **User journey maps** — workflows, emotional trajectory, pain points
- **Personas** — 3-5 behavioral clusters grounded in both attitudes and actions
- **JTBD analysis** — why users hire your product, per persona and cross-product
- **Design scenarios** — user stories and feature concepts mapped to real needs
- **AI opportunity assessment** — prioritized AI/ML opportunities scored on user need, business value, and technical feasibility
- *(Optional)* **Figma journey visuals** — stakeholder-ready diagrams

---

## What you need

- **Interview transcripts** — TXT or VTT files, ideally 9–16 per project
- **GitHub Copilot** (VS Code) — prompt files are pre-installed in `.github/prompts/`
- **Claude Code** — skills are pre-installed in `.claude/skills/`; or

That's it. No coding required.

---

## Setup

### GitHub Copilot (VS Code)
1. Clone this repository
2. Open in VS Code with the GitHub Copilot extension
3. `copilot-instructions.md` loads automatically; prompt files are available via `/` in Copilot Chat
4. Install Python deps for the clustering step: `pip install sentence-transformers hdbscan umap-learn scikit-learn pandas numpy`

### Claude Code
1. Clone this repository
2. Open Claude Code in this folder
3. *(Optional — for Figma visuals only)* Add your `FIGMA_ACCESS_TOKEN` to `.mcp.json`

---

## Starting a project

Create a folder for your project (e.g. `AWESOME_PROJECT/`) and add your transcript files:

```
AWESOME_PROJECT/
└── transcripts/
    ├── participant-alice.txt
    ├── participant-bob.txt
    └── ...
```

Claude Code will create the output folders as you run each step.

---

## The research pipeline

In **Claude Code** type `/skill-name`; in **Copilot Chat** type `/Skill Name` (the prompt's `name:` field).

| Step | Skill | Claude Code | Copilot Chat | Input | Output |
|------|-------|-------------|--------------|-------|--------|
| 1 | Empathy map | `/empathy-map-generator` | `/Empathy Map Generator` | Transcript | `empathy-maps/` |
| 1b *(optional)* | Clustering | `/empathy-clustering` | `/Empathy Clustering` | 3+ empathy maps | `empathy-maps/clustering-analysis.md` |
| 2 | Journey map | `/user-journey` | `/User Journey Map` | Transcript | `journey/` |
| 3 | Personas | `/persona-generator` | `/Persona Generator` | Empathy + journey maps | `personas/` |
| 4 | JTBD | `/jtbd-analyzer` | `/JTBD Analyzer` | Empathy + journey maps | `jtbd/` |
| 5 | Scenarios | `/scenario-mapper` | `/Scenario Mapper` | JTBD analyses | `scenarios/` |
| 6 | AI opportunities | `/ai-opportunity-analyzer` | `/AI Opportunity Analyzer` | JTBD + personas | `ai-opportunities/` |
| 7 *(optional)* | Figma visuals | `/journey-figma-creator` | — *(requires Figma MCP, Claude Code only)* | Journey map files | Figma |

**Steps 1 and 2 can run in parallel** — start both at once to save time.
**Steps 5 and 6 can run in parallel** from the same JTBD outputs.
**Step 1b** is worth running when you have 3+ empathy maps and want to see cross-user pain clusters before building personas.

---

## Time savings

| Research activity | Traditional | With these skills |
|-------------------|-------------|-------------------|
| Empathy mapping | 2–3 days per interview | Minutes |
| Journey mapping | 3–5 days | Minutes |
| Persona creation | 1–2 weeks | Hours |
| JTBD extraction | 1 week | Hours |
| AI opportunity scoring | 1–2 weeks | Hours |
| Figma stakeholder visuals | 3–5 days | Minutes |

**Total: weeks of manual synthesis → hours of AI-assisted insights**

---

## Methodology

- [Nielsen Norman Group](https://www.nngroup.com/) qualitative research standards
- [Clayton Christensen](https://hbr.org/2016/09/know-your-customers-jobs-to-be-done) Jobs-to-be-Done framework
- Pain intensity-driven prioritization (emotional severity, not just frequency)

---

## Repository layout

```
.claude/skills/        # Claude Code skills (agentic — auto file read/write)
.github/
  copilot-instructions.md   # Auto-loaded project context for Copilot
  prompts/                  # Copilot prompt files (agent mode — /Name in VS Code)
docs/                  # Workflow guide and interview guide
```

---

## Resources

- [Detailed workflow guide](docs/ai-powered-ux-workflow.md) — step-by-step instructions, quality checks, and examples
- [Interview guide](docs/interview-guide.md) — semi-structured script for discovery interviews
