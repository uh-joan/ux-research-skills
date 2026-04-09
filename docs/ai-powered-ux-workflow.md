# AI-Powered UX Research Workflow

**Step-by-Step Process for Automating Qualitative Research**

Use this workflow when starting a new project to systematically transform raw interview transcripts into actionable product insights.

---

## Prerequisites

- **Input:** 10-20 interview transcripts (TXT or VTT format) in `[PROJECT]/transcripts/`
- **Skills:** Claude Code skills installed in `.claude/skills/`
- **Methodology:** Nielsen Norman Group qualitative research + Jobs-to-be-Done

---

## Step-by-Step Workflow

### Step 1: Generate Empathy Maps (Foundation)
**Skill:** `empathy-map-generator`
**Input:** Individual interview transcripts
**Output:** `[PROJECT]/empathy-maps/[participant-name]-empathy-map-YYYY-MM-DD.md`

**Purpose:** Extract structured insights from each interview using 4-quadrant NN/g format:
- **SAYS:** Verbatim quotes (exact words from transcript)
- **THINKS:** Inferred beliefs, attitudes, mental models
- **DOES:** Observed actions, behaviors, workflows
- **FEELS:** Emotional states, pain points (with intensity scores)

**Process:**
```bash
# For each transcript in transcripts/:
# Run: empathy-map-generator skill
# Output: One empathy map per participant
```

**Quality Check:**
- Each quadrant has 5-8 entries minimum
- SAYS uses exact verbatim quotes
- FEELS includes pain intensity scores (1-10)
- All insights grounded in actual transcript data

---

### Step 2: Map User Journeys (Workflows)
**Skill:** `user-journey`
**Input:** Interview transcripts (same as Step 1)
**Output:** `[PROJECT]/journey/[name]-journey-YYYY-MM-DD.md`

**Purpose:** Visualize workflows over time with emotional trajectory

**Process:**
```bash
# Individual journeys (per participant):
# Input: Interview transcripts
# Output: [participant-name]-journey-YYYY-MM-DD.md
```

**Journey Map Structure:**
- **Phases:** Sequential workflow stages
- **Actions:** What users do in each phase
- **Mindset:** What users think (thoughts and questions)
- **Emotions:** Positive/neutral/negative sentiment with trajectory
- **Pain Points:** Friction moments with intensity scores
- **Opportunities:** Improvement areas

**Quality Check:**
- Journey grounded in actual workflow from transcripts
- Emotional trajectory shows highs and lows
- Pain points include severity scores

---

### Step 3: Create Personas (Clustering)
**Skill:** `persona-generator`
**Input:** Interview transcripts + empathy maps (Step 1) + journey maps (Step 2)
**Output:** `[PROJECT]/personas/[persona-name]-persona-YYYY-MM-DD.md`

**Purpose:** Cluster users by behavioral patterns and create 3-5 composite personas

**Why Both Inputs Matter:**
- **Empathy maps** provide attitudinal data (SAYS/THINKS/FEELS)
- **Journey maps** provide behavioral data (DOES/workflows)
- **Combined** = complete multi-dimensional persona clustering

**Process:**
```bash
# Input: Transcripts + empathy maps + journey maps
# Run: persona-generator skill
# Output: 3-5 personas (e.g., 6/16, 4/16, 3/16, 2/16, 1/16 distribution)
```

**Each Persona Includes:**
- Demographics & role
- Goals & motivations (from journey scenarios)
- Pain points (from journey pain points)
- Technical savviness
- Behavioral patterns (from journey actions)
- Representative quotes (from transcripts)

**Quality Check:**
- Every participant mapped to exactly one persona
- No "orphan" participants
- Clear differentiation between personas

---

### Step 4: Extract Jobs-to-be-Done (Motivations)
**Skill:** `jtbd-analyzer`
**Input:** Interview transcripts (primary) OR journey maps OR empathy maps
**Output:** `[PROJECT]/jtbd/[name]-jtbd-YYYY-MM-DD.md`

**Purpose:** Identify why users "hire" your product using Christensen's JTBD framework

**Flexible Input Sources:**
- **Transcripts** (recommended): Direct extraction from interview data
- **Journey maps** (alternative): Extract from workflow context
- **Empathy maps** (alternative): Extract from THINKS/FEELS quadrants
- **Personas** (optional): Provide trust context for AI opportunity analysis

**Process:**
```bash
# Individual JTBD (per participant):
# Input: Transcripts OR journey maps
# Output: [participant-name]-jtbd-YYYY-MM-DD.md

# Cross-persona JTBD (synthesized):
# Input: All individual JTBD + personas from Step 3
# Output: cross-persona-jtbd-YYYY-MM-DD.md
```

**JTBD Format:**
```
When [situation],
I want to [motivation],
So I can [outcome]
```

**Quality Check:**
- Jobs focus on progress/outcomes, not features
- Includes functional, emotional, and social dimensions
- Jobs map to specific persona patterns

---

### Step 5: Create Design Scenarios (Solutions)
**Skill:** `scenario-mapper`
**Input:** JTBD analyses + journey maps
**Output:** `[PROJECT]/scenarios/scenario-map-YYYY-MM-DD.md`

**Purpose:** Translate user needs into design scenarios and feature concepts

**Process:**
```bash
# Input: JTBD + journey maps
# Run: scenario-mapper skill
# Output: scenario-map-YYYY-MM-DD.md
```

**Scenario Map Includes:**
- **Design Scenarios:** User stories for each JTBD
- **Frequency Analysis:** How often each scenario occurs
- **Cross-Persona Coverage:** Which personas share scenarios
- **Feature Concepts:** Product ideas addressing scenarios
- **Acceptance Criteria:** Definition of done

**Quality Check:**
- Every JTBD maps to at least one scenario
- Scenarios include frequency scores
- Clear link from research → design decisions

---

### Step 6: Prioritize AI Opportunities (ROI)
**Skill:** `ai-opportunity-analyzer`
**Input:** JTBD analyses from Step 4
**Output:** `[PROJECT]/ai-opportunities/ai-opportunity-assessment-YYYY-MM-DD.md`

**Purpose:** Score and rank AI/ML product opportunities using 3-dimensional assessment

**Process:**
```bash
# Input: JTBD analyses (individual + cross-persona)
# Optional: Personas from Step 3 (for trust context)
# Run: ai-opportunity-analyzer skill
# Output: ai-opportunity-assessment-YYYY-MM-DD.md
```

**Scoring Criteria (3 Dimensions):**
- **User Needs (1-10):** Pain severity, frequency, current solution inadequacy, trust threshold, explainability needs
- **Business Value (1-10):** Strategic alignment, competitive differentiation, revenue impact, user reach, vendor credibility
- **Technical Feasibility (1-10):** LLM capability match, data availability, hallucination risk, latency tolerance, integration complexity

**Priority Matrix:**
- **Priority 1 (Quick Wins):** High business value + high technical feasibility
- **Priority 2 (Strategic Bets):** High business value + lower technical feasibility
- **Priority 3 (Backlog):** Lower business value + high technical feasibility
- **Priority 4 (Avoid):** Low on both dimensions

**Quality Check:**
- Opportunities grounded in JTBD switching triggers
- All scores evidence-based (user quotes, frequency data)
- Trust and explainability requirements documented for AI features

---

### Step 7 (Optional): Visualize Journeys in Figma
**Skill:** `journey-figma-creator`
**Input:** Journey map markdown files
**Output:** Interactive Figma journey visualizations

**Purpose:** Create stakeholder-ready visual artifacts

**Process:**
```bash
# Input: journey/*.md files
# Run: journey-figma-creator skill
# Output: Figma file with visual journey maps
```

**Requirements:**
- Figma Desktop Bridge plugin installed
- Helix Design System tokens configured

---

## Complete Workflow Summary

```
┌─────────────────────────────────────────────────────────────────┐
│  INPUT: Interview Transcripts (9-16 per project)               │
└─────────────────────────────────────────────────────────────────┘
                           │
           ┌───────────────┴───────────────┐
           │                               │
           ▼                               ▼
┌─────────────────────────┐    ┌─────────────────────────┐
│  STEP 1: EMPATHY MAPS   │    │  STEP 2: USER JOURNEYS  │
│  (empathy-map-generator)│    │  (user-journey)         │
│  • SAYS/THINKS/DOES/    │    │  • Workflow phases      │
│    FEELS quadrants      │    │  • Emotional trajectory │
│  • Verbatim quotes      │    │  • Pain points          │
│  • Pain intensity       │    │  • Opportunities        │
└─────────────────────────┘    └─────────────────────────┘
           │                               │
           └───────────────┬───────────────┘
                           ▼
           ┌───────────────────────────────┐
           │  STEP 3: PERSONAS             │
           │  (persona-generator)          │
           │  • Cluster behaviors across   │
           │    empathy + journeys         │
           │  • 3-5 composite personas     │
           │  • Attitudinal + behavioral   │
           └───────────────────────────────┘
                           │
           ┌───────────────┴───────────────┐
           ▼                               ▼
┌─────────────────────────┐    ┌─────────────────────────┐
│  STEP 4: JTBD ANALYSIS  │    │  (Personas provide      │
│  (jtbd-analyzer)        │◄───┤   trust context for     │
│  • From transcripts OR  │    │   AI opportunities)     │
│    journeys OR empathy  │    │                         │
│  • Individual + cross-  │    │                         │
│    persona extraction   │    │                         │
└─────────────────────────┘    └─────────────────────────┘
           │
           └───────────────┬───────────────┐
                           │               │
                           ▼               ▼
           ┌───────────────────┐  ┌───────────────────────┐
           │  STEP 5: SCENARIOS│  │  STEP 6: AI           │
           │  (scenario-mapper)│  │  OPPORTUNITIES        │
           │  • From JTBD +    │  │  (ai-opportunity-     │
           │    personas       │  │   analyzer)           │
           │  • User stories   │  │  • From JTBD +        │
           │  • Feature        │  │    personas           │
           │    concepts       │  │  • 3D scoring matrix  │
           │  • Acceptance     │  │  • Priority tiers     │
           │    criteria       │  │    (P1/P2/P3/P4)      │
           └───────────────────┘  └───────────────────────┘
                           │               │
                           └───────┬───────┘
                                   ▼
           ┌───────────────────────────────────────────────┐
           │  STEP 7 (Optional): FIGMA VISUALS             │
           │  (journey-figma-creator)                      │
           │  • Visual journey maps for stakeholders       │
           │  • Requires Figma Desktop Bridge plugin       │
           └───────────────────────────────────────────────┘
                                   ▼
┌─────────────────────────────────────────────────────────────────┐
│  OUTPUT: Strategic Deliverables                                 │
│  ✓ Evidence-based product roadmap                              │
│  ✓ Prioritized feature backlog (Priority 1/2/3/4)              │
│  ✓ Visual artifacts for stakeholder alignment                  │
│  ✓ Research-grounded design decisions                          │
└─────────────────────────────────────────────────────────────────┘
```

**Key Workflow Characteristics:**
- **Parallel Processing:** Steps 1 & 2 run simultaneously (saves 2-3 days)
- **Flexible JTBD:** Can use transcripts, journeys, or empathy maps as input
- **Dual Outputs:** Steps 5 & 6 run in parallel from JTBD
- **Complete Personas:** Require both empathy (attitudinal) + journeys (behavioral)

---

## Time Savings vs. Traditional Research

| Traditional Process | AI-Powered Process | Time Saved |
|---------------------|-------------------|------------|
| Manual empathy mapping (2-3 days/interview) | Automated 4-quadrant synthesis (minutes) | **90%** |
| Persona creation from notes (1-2 weeks) | Empathy-driven clustering (hours) | **85%** |
| JTBD extraction (1 week) | Automated job identification (hours) | **90%** |
| Journey mapping (3-5 days) | AI-generated workflows + emotions (minutes) | **95%** |
| Opportunity scoring (1-2 weeks) | Pain intensity from empathy FEELS (hours) | **85%** |
| Stakeholder presentation prep (3-5 days) | Auto-generated Figma visuals (minutes) | **95%** |

**Total:** Weeks of manual synthesis → Hours of AI-assisted insights

---

## Example: Starting MT360 Project

```bash
# 1. Organize transcripts
mkdir -p MT360/transcripts MT360/empathy-maps MT360/journey MT360/personas MT360/jtbd MT360/scenarios MT360/ai-opportunities
# Add interview TXT files to MT360/transcripts/

# 2. Generate empathy maps (Step 1) - CAN RUN IN PARALLEL WITH STEP 3
cd MT360
# Run empathy-map-generator for each transcript
# Output: empathy-maps/[participant-name]-empathy-map-YYYY-MM-DD.md

# 3. Map user journeys (Step 2) - CAN RUN IN PARALLEL WITH STEP 2
# Run user-journey for each transcript
# Output: journey/[participant-name]-journey-YYYY-MM-DD.md

# 4. Create personas (Step 3)
# Run persona-generator on transcripts + empathy maps + journey maps
# Output: personas/[persona-name]-persona-YYYY-MM-DD.md

# 5. Extract JTBD (Step 4)
# Run jtbd-analyzer for individual + cross-persona
# Output: jtbd/[participant-name]-jtbd-YYYY-MM-DD.md
#         jtbd/cross-persona-jtbd-YYYY-MM-DD.md

# 6. Create scenarios (Step 5)
# Run scenario-mapper on JTBD analyses
# Output: scenarios/scenario-map-YYYY-MM-DD.md
# Note: Can run in parallel with Step 6

# 7. Prioritize AI opportunities (Step 6)
# Run ai-opportunity-analyzer on JTBD analyses
# Output: ai-opportunities/ai-opportunity-assessment-YYYY-MM-DD.md
# Note: Can run in parallel with Step 5

# 8. Visualize (Step 7 - optional)
# Run journey-figma-creator for stakeholder presentations
# Output: Figma file with visual journey maps
```

---

## Quality Principles

1. **Empathy-First:** All insights grounded in actual transcript data
2. **Pain ≠ Frequency:** Prioritize by emotional intensity, not just user count
3. **Methodology Rigor:** Strict adherence to Nielsen Norman Group standards
4. **Transparency:** Every claim traceable to source interview
5. **Gap Analysis:** Explicitly document what's NOT in transcripts
6. **Reproducibility:** Automated workflow ensures consistent quality

---

*Methodology: Nielsen Norman Group qualitative research + Christensen Jobs-to-be-Done*
*Pain intensity-driven prioritization from empathy FEELS quadrant*
