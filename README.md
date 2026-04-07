# UX Research Skills

AI-powered Claude Code skills for transforming interview transcripts into actionable product insights.

## Overview

This repository contains automated skills for qualitative UX research following Nielsen Norman Group methodology and Jobs-to-be-Done framework. Transform 9-16 interview transcripts into strategic deliverables in hours instead of weeks.

## Setup

1. **Configure environment variables:**
   ```bash
   cp .env.example .env
   cp .mcp.json.example .mcp.json
   # Edit .env and add your FIGMA_ACCESS_TOKEN
   ```

2. **Install Claude Code skills** (already in `.claude/skills/`)

3. **Conduct user interviews** using [Interview Guide](docs/interview-guide.md)

## Quick Start

1. **Create project folder** (e.g., `AWESOME_PROJECT/`)
2. **Add interview transcripts** to `[PROJECT]/transcripts/`
3. **Run Claude Code skills** in sequence:

```bash
# Step 1 & 2 (parallel): Extract insights
empathy-map-generator    # → empathy-maps/
user-journey            # → journey/

# Step 3: Cluster users
persona-generator       # → personas/

# Step 4: Identify motivations
jtbd-analyzer          # → jtbd/

# Step 5 & 6 (parallel): Design solutions
scenario-mapper        # → scenarios/
ai-opportunity-analyzer # → ai-opportunities/

# Step 7 (optional): Visualize
journey-figma-creator  # → Figma visuals
```

## Workflow

```
Interview Transcripts
        ↓
Step 1: Empathy Maps ────┐
Step 2: User Journeys ───┤
        ↓                │
Step 3: Personas ←───────┘
        ↓
Step 4: JTBD Analysis
        ↓
        ├─→ Step 5: Design Scenarios
        └─→ Step 6: AI Opportunities
                ↓
        Step 7: Figma Visuals (optional)
```

## Skills Included

- **empathy-map-generator** - 4-quadrant synthesis (Says/Thinks/Does/Feels)
- **user-journey** - Workflow visualization with emotional trajectory
- **persona-generator** - Behavioral clustering into 3-5 personas
- **jtbd-analyzer** - Jobs-to-be-Done extraction
- **scenario-mapper** - Design scenarios and feature concepts
- **ai-opportunity-analyzer** - AI/ML opportunity prioritization
- **journey-figma-creator** - Visual journey maps for stakeholders (WIP)

## Output

- Evidence-based product roadmap
- Prioritized feature backlog (P1/P2/P3/P4)
- Visual artifacts for stakeholder alignment
- Research-grounded design decisions

## Time Savings

Traditional manual research: **4-6 weeks**
AI-powered automation: **Hours to 1-2 days**
Time saved: **85-95%**

## Methodology

Based on:
- Nielsen Norman Group qualitative research standards
- Clayton Christensen Jobs-to-be-Done framework
- Pain intensity-driven prioritization

---

## Resources

- [AI-Powered UX Workflow](docs/ai-powered-ux-workflow.md) - Detailed step-by-step workflow
- [Interview Guide](docs/interview-guide.md) - Semi-structured interview script for user research
