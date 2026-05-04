---
name: scenario-mapper
description: Create scenario maps and Agile user stories from Jobs-to-be-Done analysis following Nielsen Norman Group methodology. Use when user wants to translate research into design scenarios, map user goals to product features, identify opportunity gaps, or generate user stories for development. Bridges JTBD insights to actionable design exploration and sprint planning with scenario narratives and acceptance criteria.
license: MIT
metadata:
  author: Joan Saez-Pons
  version: 1.0.0
  category: UX Research
  methodology: Nielsen Norman Group
---

# Scenario Mapper

**Version:** 1.0.0
**Category:** Product Strategy & UX Research
**Complexity:** Intermediate
**Prerequisites:** JTBD analysis files (from `jtbd-analyzer` skill)

---

## Purpose

Transforms Jobs-to-be-Done (JTBD) analysis into actionable design scenarios and Agile user stories for product managers and design teams. Uses Nielsen Norman Group's scenario mapping methodology to bridge the gap between user research insights and design exploration.

**When to Use:**
- After completing JTBD analysis to generate design scenarios
- Before design sprints or ideation workshops
- When translating user research into actionable feature concepts
- To create backlog-ready user stories grounded in real user needs
- When stakeholders ask "what should we build based on this research?"

**Framework Origin:**
- **Scenario Structure:** Nielsen Norman Group scenario mapping methodology (5-element framework)
- **User Stories:** Agile/Scrum user story format (Cohn, 2004)
- **JTBD Integration:** Christensen JTBD framework for context and motivation

---

## Framework Structure

### NN/g 5-Element Scenario Model

```
Scenario = Actor + Motivator + Intention + Action + Resolution

Where:
1. ACTOR = Specific persona (from JTBD analysis)
2. MOTIVATOR = Contextual trigger (from JTBD switching triggers)
3. INTENTION = User's goal (from JTBD job statement)
4. ACTION = High-level steps (derived from current solution + pain points)
5. RESOLUTION = Desired outcome (from JTBD outcome dimension)
```

### Agile User Story Format

```
As a [Actor/Persona],
I want to [Action/Capability],
So that [Outcome/Value].

Acceptance Criteria:
- [Testable condition 1]
- [Testable condition 2]
- [Testable condition 3]

JTBD Context: [Link to originating job from analysis]
Pain Points Addressed: [From JTBD pain points]
```

---

## Input Requirements

### Required Inputs

1. **JTBD Analysis Files** (from `.claude/skills/jtbd-analyzer/`)
   - Individual user JTBD analyses (`jtbd-analysis-[user].md`)
   - Merged persona-level analyses (`jtbd-analysis-[persona].md`)
   - Cross-persona analysis (`jtbd-cross-persona-analysis.md`)

### Optional Inputs

2. **AI Opportunity Assessment** (from `.claude/skills/ai-opportunity-analyzer/`)
   - Used for scenario prioritization (focus on Priority 1 opportunities)
3. **Product Context**
   - Current product capabilities (to avoid duplicating existing features)
   - Technical constraints (to keep scenarios realistic)
4. **Persona Documentation** (if available)
   - Richer actor characterization

---

## Output Specification

### Primary Output: Scenario Map Document

**File Format:** Markdown (`.md`)
**File Location:** `[project]/scenarios/scenario-map-[date].md`

**Report Sections:**

#### 1. Executive Summary
- Total scenarios generated
- Personas covered
- Top 5 high-priority scenarios (by frequency × pain severity)
- Key design themes across scenarios

#### 2. Scenario Inventory

For each scenario:

```markdown
## Scenario [#]: [Descriptive Name]

**Priority:** [High/Medium/Low] (based on JTBD frequency + pain severity)
**Persona Coverage:** [X/Y personas affected]
**Frequency:** [Daily/Weekly/Monthly/Quarterly] (from JTBD)

### Scenario Narrative (NN/g 5-Element Structure)

**Actor:** [Persona Name + Brief Context]
**Motivator:** [Contextual trigger - what prompts this scenario]
**Intention:** [User's goal - what they're trying to achieve]
**Action:** [High-level steps - how they currently approach it]
**Resolution:** [Desired outcome - success state]

---

### User Story (Agile Format)

**As a** [Persona Name],
**I want to** [Capability/Feature],
**So that** [Value/Outcome].

**Acceptance Criteria:**
- [ ] [Testable condition 1]
- [ ] [Testable condition 2]
- [ ] [Testable condition 3]

---

### JTBD Connection

**Originating Job:** [Job title from JTBD analysis]
**Job Statement:** "[When X, I want to Y, so I can Z]"
**Confidence Level:** [High/Medium/Low] (from JTBD analysis)
**User Quotes:**
> "[Verbatim quote showing pain point]" — [User Name]

**Pain Points Addressed:**
1. [Pain point 1 from JTBD]
2. [Pain point 2 from JTBD]
3. [Pain point 3 from JTBD]

**Switching Triggers:**
- [Trigger 1: condition that makes users seek new solution]
- [Trigger 2: ...]

---

### Design Exploration

**Open Questions:**
- [ ] [Question 1 - unresolved issue requiring research]
- [ ] [Question 2 - ...]

**Design Considerations:**
- [Edge case or constraint to consider]
- [Data/infrastructure requirement]
- [Integration dependency]

**Potential Features:**
- Feature Idea 1: [Brief description]
- Feature Idea 2: [Brief description]
- Feature Idea 3: [Brief description]

---

### Success Metrics

**How to measure if this scenario is solved:**
- [Metric 1: e.g., "Time to complete task reduced by 50%"]
- [Metric 2: e.g., "User trust rating ≥8/10"]
- [Metric 3: e.g., "Zero manual data entry required"]
```

#### 3. Cross-Scenario Analysis

```markdown
## Design Themes

### Theme 1: [Pattern name, e.g., "Data Synthesis Across Platforms"]
**Scenarios:** #1, #3, #7, #12
**Common Pain:** [Shared pain point]
**Design Opportunity:** [Unified solution concept]
**User Stories:**
- [Aggregated user story spanning multiple scenarios]

### Theme 2: [Pattern name]
...
```

#### 4. Prioritization Matrix

```markdown
## Scenario Prioritization (MoSCoW Method)

### Must Have (Critical User Needs)
1. Scenario #X - [Name] (10/10 users, daily frequency)
2. Scenario #Y - [Name] (8/10 users, weekly frequency)

### Should Have (High Value)
1. Scenario #A - [Name] (6/10 users, weekly frequency)
2. Scenario #B - [Name] (5/10 users, monthly frequency)

### Could Have (Nice to Have)
1. Scenario #C - [Name] (3/10 users, quarterly frequency)

### Won't Have (Out of Scope)
1. Scenario #D - [Name] (1/10 users, rarely)
   - Reason: Low frequency, niche use case
```

#### 5. Workshop Preparation Guide

```markdown
## Using These Scenarios in Design Workshops

### Pre-Workshop Setup
1. Print scenarios #[X, Y, Z] (top priority)
2. Assign 1 scenario per breakout group (4-6 people)
3. Materials needed:
   - Whiteboard/digital board space
   - Sticky notes (3 colors: Ideas, Questions, Considerations)
   - 15 minutes per scenario

### Workshop Flow
1. **Familiarization (2 min):** Group reads scenario narrative
2. **Ideation (10 min):** Silent brainstorming → sticky note generation
3. **Discussion (3 min):** Share ideas, cluster themes

### Expected Outputs
- 10-20 design ideas per scenario
- 5-10 open questions requiring research
- 3-5 edge cases/considerations

### Post-Workshop
- Synthesize ideas across scenarios
- Prioritize features using MoSCoW method
- Create design briefs for top 3-5 concepts
```

---

## Scenario Generation Logic

### Step 1: Extract JTBD Jobs from Analysis Files
Scan all JTBD files for jobs with:
- **High Confidence** (multiple users mentioned same job)
- **High Frequency** (daily/weekly occurrence)
- **High Pain Severity** (strong emotional language, switching triggers)
- **Clear Outcome** (actionable, measurable success state)

### Step 2: Map JTBD to 5-Element Scenario Structure

**JTBD → Scenario Mapping:**
```
JTBD Component           → Scenario Element
─────────────────────────────────────────────
Persona                  → Actor
Switching Trigger        → Motivator
Job Statement (When X)   → Motivator (context)
Job Statement (I want Y) → Intention (goal)
Current Solution         → Action (existing steps)
Job Statement (So I can Z) → Resolution (outcome)
Functional Dimension     → Action (tasks)
Emotional Dimension      → Motivator (feelings)
Social Dimension         → Resolution (perception)
Pain Points              → Design Considerations
```

### Step 3: Generate Agile User Story

**Template:**
```
As a [Actor from scenario],
I want to [solve the pain point/job],
So that [achieve the resolution/outcome].
```

**Acceptance Criteria Derivation:**
- Extract from JTBD "success criteria" (if present)
- Infer from pain points (inverse: "No longer experience X")
- Translate from switching triggers ("Must be faster than manual process")

### Step 4: Prioritize Scenarios

**Prioritization Formula:**
```
Scenario Priority Score = (Frequency × Pain Severity × User Coverage) / 3

Where:
- Frequency: 10=daily, 8=weekly, 6=monthly, 4=quarterly, 2=yearly
- Pain Severity: 1-10 (from JTBD switching trigger intensity)
- User Coverage: % of user base affected (from JTBD confidence level)
```

**MoSCoW Assignment:**
- **Must Have:** Score ≥8.0 + affects ≥60% of users
- **Should Have:** Score 6.0-7.9 OR affects 40-59% of users
- **Could Have:** Score 4.0-5.9 OR affects 20-39% of users
- **Won't Have:** Score <4.0 OR affects <20% of users

---

## Workflow

### Phase 1: Preparation (10-15 min)
1. Locate JTBD analysis files in project directory
2. (Optional) Load AI Opportunity Assessment for context
3. Identify target personas (default: all personas from JTBD analysis)
4. Confirm product constraints (existing features, technical limits)

### Phase 2: Scenario Generation (30-45 min)
For each high-confidence JTBD job:
1. Extract Actor (persona), Motivator (trigger), Intention (goal)
2. Synthesize Action (current solution + pain points)
3. Define Resolution (desired outcome)
4. Write 5-element scenario narrative
5. Convert to Agile user story
6. Derive acceptance criteria (3-5 testable conditions)
7. Link back to originating JTBD (job ID, user quotes)
8. Calculate priority score

**Quality Checks:**
- Does scenario match JTBD context? (verify with user quotes)
- Is intention clear and user-centered? (not system-focused)
- Are acceptance criteria testable? (no vague language)
- Does resolution align with JTBD outcome? (verify success state)

**Quality gate before saving:** Each scenario must contain at least one verbatim user quote in the "User Quotes" field — pull directly from JTBD files or transcripts. If the JTBD file lacks quotes, read the upstream transcript. A scenario with no user quotes is incomplete regardless of narrative quality. Quotes must appear as blockquotes (`> "..."`) or inline `"..."` in the JTBD Connection section.

### Phase 3: Cross-Scenario Analysis (20-30 min)
1. Group scenarios by design theme (common pain points)
2. Identify patterns across personas (universal vs. niche needs)
3. Synthesize aggregated user stories for multi-scenario solutions
4. Flag conflicting requirements (persona A needs X, persona B needs opposite)

### Phase 4: Prioritization (15-20 min)
1. Calculate priority scores for all scenarios
2. Apply MoSCoW method (Must/Should/Could/Won't)
3. Rank within each tier by priority score
4. Document prioritization rationale (frequency + pain + coverage)

### Phase 5: Workshop Preparation (10-15 min)
1. Select top 3-5 scenarios for design workshop
2. Generate workshop facilitation guide
3. Prepare scenario cards/handouts
4. Create synthesis template for post-workshop outputs

**Total Time Estimate:** 90-120 minutes for 8-12 scenarios

---

## Use Cases

### Use Case 1: Design Sprint Preparation
**Scenario:** Product team completing 3-day design sprint next week. Need user-centered scenarios to frame ideation.

**Inputs:**
- JTBD cross-persona analysis from recent research
- 4 personas (12 users total)
- Product roadmap priorities

**Process:**
1. Run Scenario Mapper skill on JTBD files
2. Select top 5 "Must Have" scenarios
3. Print scenario cards for workshop
4. Facilitate scenario-mapping sessions (day 1 of sprint)
5. Synthesize design ideas into concepts (day 2)
6. Prototype top concept (day 3)

**Output:** 5 prioritized scenarios → 15+ design ideas → 3 concepts → 1 prototype

### Use Case 2: Backlog Grooming for Agile Teams
**Scenario:** Scrum team needs backlog populated with user stories for next 3 sprints. Want stories grounded in research, not assumptions.

**Inputs:**
- JTBD analysis from 10 user interviews
- AI Opportunity Assessment (Priority 1 features)

**Process:**
1. Run Scenario Mapper skill
2. Extract user stories from generated scenarios
3. Add to backlog with JTBD links
4. Prioritize using MoSCoW + story points
5. Refine acceptance criteria during sprint planning

**Output:** 20-30 backlog-ready user stories with traceability to research

### Use Case 3: Feature Validation with Stakeholders
**Scenario:** Engineering proposes building "AI chat" feature. Product team needs to validate if this solves real user jobs.

**Inputs:**
- JTBD analysis (check: is there a "conversational search" job?)
- Proposed feature description

**Process:**
1. Search generated scenarios for "chat" or "conversational" patterns
2. If no scenario exists → validate with new JTBD research before building
3. If scenario exists → compare proposed feature against acceptance criteria
4. If mismatch → redesign feature to match user story

**Outcome:** Avoid "feature checklist AI" by grounding in actual scenarios

### Use Case 4: Cross-Persona Synthesis
**Scenario:** Multiple personas have overlapping jobs (e.g., "search patents"). Need unified design that serves all personas without over-customization.

**Inputs:**
- JTBD cross-persona analysis
- 3 personas with "patent search" job

**Process:**
1. Generate scenarios for each persona
2. Compare Actor/Motivator/Intention across scenarios
3. Identify common Resolution (shared outcome)
4. Design one solution with configurable paths (not 3 separate features)

**Output:** Aggregated user story: "As a patent professional, I want to search patents by [jurisdiction/molecule/status], so that I can [assess FTO/find prior art/monitor competitors]"

---

## Integration with Existing Skills

### JTBD Analyzer → Scenario Mapper
**Workflow:** Run JTBD Analyzer first, then Scenario Mapper to generate actionable scenarios

**Data Flow:**
```
Interview Transcripts
    ↓
[JTBD Analyzer Skill]
    ↓
jtbd-analysis-[user].md
jtbd-analysis-[persona].md
jtbd-cross-persona-analysis.md
    ↓
[Scenario Mapper Skill] ← YOU ARE HERE
    ↓
scenario-map-[date].md
(with user stories + workshop guide)
```

**Key JTBD Fields Used:**
- **Switching Triggers** → Motivator
- **Job Statement** → Intention + Resolution
- **Frequency** → Prioritization score
- **Pain Points** → Design Considerations
- **User Quotes** → Evidence in scenario narrative

### AI Opportunity Analyzer → Scenario Mapper
**Workflow:** Use AI Opportunity Assessment to focus scenario generation on viable features

**Data Flow:**
```
ai-opportunity-assessment.md
    ↓
Filter to Priority 1 + Priority 2 opportunities
    ↓
[Scenario Mapper Skill]
    ↓
Generate scenarios ONLY for validated opportunities
```

**Benefit:** Avoid wasting time on scenarios for features that scored low on business value/technical feasibility

### Scenario Mapper → User Journey Skill
**Workflow:** Embed scenarios into journey map stages

**Integration:**
```
User Journey Map: "Consideration Stage"
    ↓
Embedded Scenarios:
- Scenario #3: Compare Patent Status Across Jurisdictions
- Scenario #7: Assess Litigation Risk for Market Entry
```

**Benefit:** Journey maps provide macro view (touchpoints over time), scenarios provide micro view (specific task flows)

---

## Key Insights from Framework Research

### NN/g Scenario Best Practices

**1. Keep Scenarios High-Level**
> "Over-specificity can lead to solutions that are too tailored to the scenario while ignoring the range of possible real-life situations."

**Implication:** Avoid prescribing UI details in scenarios. Focus on intent and outcome, not interface mechanics.

**2. Ground in Real User Context**
> "Persona-based scenarios ensure user data is central to ideation and leads to user-centered solutions."

**Implication:** Every scenario must trace back to JTBD analysis with user quotes as evidence.

**3. Use Scenarios for Ideation, Not Requirements**
> "Scenarios focus on developing the correct sequence of actions... but lack character development, plot, and user goals."

**Implication:** NN/g scenarios → design exploration. For detailed requirements, use Cockburn use cases (not in this skill).

### Agile User Story Best Practices (Mike Cohn)

**INVEST Criteria for Good User Stories:**
- **I**ndependent (can be implemented separately)
- **N**egotiable (details emerge during conversation)
- **V**aluable (delivers value to user)
- **E**stimable (can be sized for sprint planning)
- **S**mall (fits in one sprint)
- **T**estable (acceptance criteria are clear)

**Implication:** Generate stories that pass INVEST test by:
- Keeping scope focused (one job = one story)
- Linking to JTBD outcome (ensures value)
- Deriving testable acceptance criteria

### JTBD vs. Scenarios Distinction

**JTBD (from research):**
- **Purpose:** Understand *why* users do things
- **Format:** "When [context], I want to [motivation], so I can [outcome]"
- **Bias Risk:** Low (outcome-focused, solution-agnostic)

**Scenarios (this skill):**
- **Purpose:** Explore *how* solutions could work
- **Format:** Actor → Motivator → Intention → Action → Resolution
- **Bias Risk:** Medium (includes "Action" which implies solution)

**Key Principle:** Use JTBD insights to **ground** scenarios in real needs, but keep scenarios **flexible** on specific solutions during ideation.

---

## Anti-Patterns (What NOT to Do)

### ❌ Anti-Pattern 1: Solution-Prescriptive Scenarios
**Description:** Writing scenarios that dictate specific UI elements or technical implementation

**Example (BAD):**
> "Patent Strategy Specialist clicks the 'Advanced Filter' dropdown, selects 'Saudi Arabia' from the jurisdiction list..."

**Why It Fails:** Locks design team into one solution; stifles creativity

**Correct Approach:** Keep scenarios high-level
> "Patent Strategy Specialist filters patents by Saudi Arabia to assess MENA market entry..."

### ❌ Anti-Pattern 2: Scenarios Without JTBD Evidence
**Description:** Generating scenarios based on assumptions or competitor features, not user research

**Example (BAD):**
> "User wants to chat with AI about drug data"

**Why It Fails:** No evidence users have a "conversational search" job

**Correct Approach:** Check JTBD analysis first. If no matching job → conduct research, don't invent scenarios.

### ❌ Anti-Pattern 3: Acceptance Criteria That Aren't Testable
**Description:** Vague, subjective criteria like "UI should be intuitive"

**Example (BAD):**
- [ ] Interface is user-friendly
- [ ] System is fast

**Why It Fails:** Can't verify success during QA

**Correct Approach:** Make criteria measurable
- [ ] User completes task in ≤3 clicks (vs. current 8 clicks)
- [ ] System returns results in <5 seconds (from JTBD latency requirement)

### ❌ Anti-Pattern 4: One Scenario Per User (No Synthesis)
**Description:** Treating every individual user JTBD as a separate scenario

**Example (BAD):**
- Scenario 1: User A searches patents
- Scenario 2: User B searches patents
- Scenario 3: User C searches patents

**Why It Fails:** Creates redundant scenarios; misses common patterns

**Correct Approach:** Synthesize cross-persona scenarios when jobs overlap
- Scenario 1: Patent professionals search patents (covers personas A, B, C with variations noted)

### ❌ Anti-Pattern 5: Ignoring Frequency and Prioritization
**Description:** Treating all scenarios equally, even rare edge cases

**Example (BAD):**
Generating 50 scenarios with no prioritization → design team overwhelmed

**Why It Fails:** Dilutes focus; wastes time on low-impact scenarios

**Correct Approach:** Apply MoSCoW method. Start workshops with "Must Have" scenarios only.

---

## FAQ

### Q: How many scenarios should I generate?
**A:** Aim for **8-15 scenarios** for a typical project (4 personas, 2-4 jobs per persona). Use MoSCoW to prioritize; most design sprints can only handle 3-5 scenarios in depth.

### Q: What if JTBD analysis is incomplete?
**A:** Scenario Mapper requires high-confidence JTBD data. If analysis has gaps:
1. Run scenarios for completed jobs only
2. Flag "Open Questions" in scenarios where research is insufficient
3. Prioritize additional JTBD research before building features for low-confidence scenarios

### Q: Should scenarios include AI-specific features?
**A:** Yes, if JTBD analysis shows users want AI. But avoid "AI for AI's sake":
- ✅ Good: "I want to predict litigation timelines" (AI solves real job)
- ❌ Bad: "I want to chat with AI" (solution-focused, no evidence of job)

Check AI Opportunity Assessment for validated AI opportunities before creating AI scenarios.

### Q: How do scenarios differ from user journeys?
**A:**
- **User Journeys:** Macro view of entire experience over time (awareness → consideration → purchase → use → advocacy)
- **Scenarios:** Micro view of specific task within a journey stage

**Integration:** Embed scenarios into journey stages. Example:
```
Journey Stage: "Consideration" (evaluating product fit)
    ↓
Scenarios:
- Scenario #3: Compare features against requirements
- Scenario #7: Assess pricing vs. budget
```

### Q: Can I use scenarios for usability testing?
**A:** Yes, but convert scenarios → test tasks:
- **Scenario (design exploration):** High-level, outcome-focused
- **Test Task (usability testing):** Specific, actionable, doesn't reveal UI

**Example:**
- Scenario: "Patent specialist needs to verify no barriers exist for Saudi market entry"
- Test Task: "You're launching a biosimilar in Saudi Arabia. Use this tool to check if any patents would block your launch."

### Q: What if personas have conflicting needs?
**A:** Document in "Design Considerations":
```markdown
**Persona Conflict:**
- Patent attorneys need detailed legal claims text (high complexity)
- Business development needs plain-language summaries (high simplicity)

**Design Opportunity:** Provide both views with toggle option
```

Create two user stories if needs are mutually exclusive, or one story with configurable modes.

---

## Changelog

**v1.0.0 (2026-03-26)**
- Initial release
- NN/g 5-element scenario framework
- Agile user story generation with acceptance criteria
- MoSCoW prioritization method
- Design workshop preparation guide
- Cross-scenario synthesis
- Integration with JTBD Analyzer and AI Opportunity Analyzer skills

---

## References

### Nielsen Norman Group Research
- **Scenario Mapping: Design Ideation Using Personas** (2024)
  - 5-element scenario structure (Actor, Motivator, Intention, Action, Resolution)
  - Scenario-mapping workshop methodology
  - Granularity best practices
- **UX Stories Communicate Designs** (2022)
  - Distinction between scenarios and UX stories
  - Character development and narrative principles
- **From Research Goals to Usability-Testing Scenarios: A 7-Step Method** (2022)
  - Converting research insights into actionable scenarios

### Agile/Scrum References
- **Cohn, M.** (2004). *User Stories Applied: For Agile Software Development.* Addison-Wesley.
  - INVEST criteria for user stories
  - Acceptance criteria best practices
- **MoSCoW Method:** Prioritization framework (Must/Should/Could/Won't)

### JTBD Framework
- **Christensen, C.** (2003). *The Innovator's Solution.* Harvard Business Review Press.
- **Moesta, B.** (2020). *Demand-Side Sales 101.* Lioncrest Publishing.
- **Existing JTBD Analyzer Skill:** `.claude/skills/jtbd-analyzer/`

### Comparison Research
- "Jobs to Be Done vs Use Cases" (Sivo Insights, 2024)
- "Use Cases, User Stories, and Jobs to Be Done" (Medium - Leon HML, 2020)

---

## Support & Feedback

**Skill Author:** Claude Code + UX Research Team
**Skill Location:** `.claude/skills/scenario-mapper/`
**Related Skills:**
- `.claude/skills/jtbd-analyzer/` (prerequisite)
- `.claude/skills/ai-opportunity-analyzer/` (optional input for prioritization)
- `.claude/skills/user-journey/` (complementary - macro view)

**Questions or Improvements:** Document learnings in `docs/proposed-skills.md`
