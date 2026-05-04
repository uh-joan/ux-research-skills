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
- **Claude Code** — with this repository cloned; skills are pre-installed in `.claude/skills/`

That's it. No coding required.

---

## Setup

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

Run each skill by typing `/skill-name` in Claude Code and pointing it to your transcripts or prior outputs.

| Step | Skill | Input | Output |
|------|-------|-------|--------|
| 1 | `empathy-map-generator` | Transcript (per participant) | `empathy-maps/` |
| 1b *(optional)* | `empathy-clustering` | 3+ empathy maps | Cross-user pain patterns |
| 2 | `user-journey` | Transcript (per participant) | `journey/` |
| 3 | `persona-generator` | Empathy maps + journey maps | `personas/` |
| 4 | `jtbd-analyzer` | Transcripts + personas | `jtbd/` |
| 5 | `scenario-mapper` | JTBD analyses | `scenarios/` |
| 6 | `ai-opportunity-analyzer` | JTBD analyses + personas | `ai-opportunities/` |
| 7 *(optional)* | `journey-figma-creator` | Journey map files | Figma visuals |

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

## Resources

- [Detailed workflow guide](docs/ai-powered-ux-workflow.md) — step-by-step instructions, quality checks, and examples
- [Interview guide](docs/interview-guide.md) — semi-structured script for discovery interviews
