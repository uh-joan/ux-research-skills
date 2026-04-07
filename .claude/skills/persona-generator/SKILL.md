---
name: persona-generator
description: Create qualitative user personas from interview transcripts and journey maps following Nielsen Norman Group methodology. Use when user wants to segment users by behaviors and attitudes, create composite persona profiles, identify shared goals and pain points across users, or synthesize multiple interviews into representative archetypes. Generates research-based personas with demographics, goals, behaviors, pain points, and verbatim quotes.
---

# Persona Generator

Create research-based user personas following Nielsen Norman Group best practices from interview transcripts and journey maps.

## Overview

This skill creates **qualitative personas** (NN/g's recommended type) by analyzing one or more user interviews and their corresponding journey maps. It identifies shared attitudes, goals, pain points, and behaviors across users to create composite personas that represent meaningful user segments.

## Input Options

### Option 1: Single User → Single Persona
Create a persona from one interview transcript and its journey map.

**Usage:** `Create a persona from simon.txt` or `Create a persona from user-journey-simon.md`

### Option 2: Multiple Users → Clustered Personas
Analyze multiple interviews/journeys to identify patterns and create 2-4 composite personas representing distinct user segments.

**Usage:** `Create personas from all interviews` or `Create personas from abhishek, vamsi, and shirley`

### Option 3: Manual Clustering
User specifies which interviews should be grouped into which persona.

**Usage:** `Create personas: Medical Advisors (simon, henok) and Analysts (abhishek, vamsi, shirley)`

## Nielsen Norman Group Framework

### Persona Type: Qualitative
- **Sample size:** 5-30 user interviews (we have 8)
- **Segmentation basis:** Shared attitudes, goals, pain points, behaviors
- **Best for:** Most organizations; balance of effort vs. value
- **Output:** Rich, actionable insights grounded in real user research

### Essential Components

Each persona must include:

1. **Header Section**
   - Name (realistic, memorable)
   - Photo placeholder description
   - Tagline (one sentence capturing their essence)
   - Demographic basics (age range, location, years of experience)

2. **Context & Background**
   - Job title and organization type
   - Team structure and reporting relationships
   - Key responsibilities
   - Experience level with relevant tools/platforms

3. **Goals & Motivations**
   - What they're trying to accomplish (from journey maps)
   - Success criteria
   - Career aspirations (if relevant)

4. **Attitudes & Mindsets**
   - How they approach problems
   - Preferences and working styles
   - Representative quotes from interviews

5. **Pain Points & Frustrations**
   - Biggest obstacles (synthesized from journey maps)
   - Workarounds they use
   - Unmet needs

6. **Behaviors & Workflows**
   - Typical tasks and processes
   - Tools and data sources used
   - Frequency and context of use
   - Decision-making patterns

7. **Relationship to Product/Service**
   - Usage context (required vs. choice)
   - Frequency of use
   - Device/platform preferences
   - Feature adoption patterns

## Clustering Logic

When creating personas from multiple users, cluster by:

1. **Primary segmentation factors** (in order):
   - **Job function/role** (Medical Advisor vs. Analyst vs. Strategic Leadership)
   - **Primary goal** (Evidence generation vs. Forecasting vs. Decision-making)
   - **Workflow type** (Research-driven vs. Data-driven vs. Synthesis-driven)

2. **Secondary factors**:
   - Tool usage patterns
   - Pain point themes
   - Data source preferences
   - Organization type (pharma vs. generic/biosimilar)

3. **What NOT to cluster by**:
   - Demographics alone (age, gender, location)
   - Company size
   - Superficial similarities

### Clustering Decision Tree

```
IF users share:
  - Same job function AND
  - Same primary goals AND
  - Similar pain point themes
THEN: Merge into single persona

ELSE IF users have:
  - Different job functions OR
  - Fundamentally different goals
THEN: Create separate personas

ELSE: Analyze workflow patterns to determine
```

## Output Format

### For Single Persona:
Create markdown file: `DI&A/personas/persona-[name].md`

### For Multiple Personas:
Create markdown file: `DI&A/personas/personas-overview.md` containing all personas

## Markdown Template

```markdown
# Persona: [Name]

![Photo placeholder: [Description]]

> "[Memorable tagline that captures their essence]"

## Overview

**Name:** [First Last]
**Age:** [Range, e.g., 35-45]
**Role:** [Job Title]
**Organization:** [Type of organization]
**Experience:** [Years in role/industry]
**Location:** [Geographic region]

**Based on:** [List of interview participants this persona represents]

---

## Background & Context

[2-3 paragraphs describing who they are, their team structure, organizational context, and how they got to this role]

**Key Responsibilities:**
- [Responsibility 1]
- [Responsibility 2]
- [Responsibility 3]

**Team Structure:** [Description of reporting relationships and collaboration]

---

## Goals & Motivations

**Primary Goals:**
1. [Goal 1 - from journey maps]
2. [Goal 2]
3. [Goal 3]

**Success Metrics:**
- [What defines success for them]
- [How they're evaluated]

**Motivations:**
> "[Quote showing what drives them]"

- [Intrinsic motivation 1]
- [Extrinsic motivation 2]

---

## Attitudes & Mindsets

> "[Representative quote #1]"

> "[Representative quote #2]"

**How they approach problems:**
- [Approach 1]
- [Approach 2]

**Working style:**
- [Style preference 1]
- [Style preference 2]

**Attitudes toward technology/tools:**
- [Attitude 1]
- [Attitude 2]

---

## Pain Points & Frustrations

**Biggest Obstacles:**

1. **[Pain point theme 1]**
   - [Specific manifestation]
   - [Impact on work]
   - Quote: "[User quote]"

2. **[Pain point theme 2]**
   - [Specific manifestation]
   - [Impact on work]
   - Quote: "[User quote]"

3. **[Pain point theme 3]**
   - [Specific manifestation]
   - [Impact on work]
   - Quote: "[User quote]"

**Workarounds:**
- [How they cope with pain point 1]
- [How they cope with pain point 2]

**Unmet Needs:**
- [Need 1]
- [Need 2]

---

## Behaviors & Workflows

**Typical Tasks:**
- [Task 1 with frequency]
- [Task 2 with frequency]
- [Task 3 with frequency]

**Tools & Data Sources:**
- [Tool 1 - primary use]
- [Tool 2 - secondary use]
- [Tool 3 - occasional use]

**Workflow Pattern:**
[Describe their typical workflow from journey map, e.g., "Starts with X, then moves to Y, iterates on Z"]

**Decision-Making:**
- [How they make decisions]
- [What influences their choices]
- [Constraints they work within]

---

## Relationship to Product/Service

**Usage Context:**
- [ ] Required for job / [ ] Optional choice
- Frequency: [Daily / Weekly / Monthly / Quarterly]
- Device: [Desktop / Mobile / Both]

**Feature Usage:**
- **Heavy use:** [Features they use constantly]
- **Moderate use:** [Features they use sometimes]
- **Rare use:** [Features they rarely need]

**Adoption Patterns:**
- [How they discover and adopt new features]
- [Barriers to adoption]

---

## Opportunities for Impact

Based on this persona's pain points and goals, the highest-impact improvements would be:

1. **[Opportunity 1]**
   - Why: [Addresses pain point X and goal Y]
   - Impact: [Expected outcome]

2. **[Opportunity 2]**
   - Why: [Addresses pain point X and goal Y]
   - Impact: [Expected outcome]

3. **[Opportunity 3]**
   - Why: [Addresses pain point X and goal Y]
   - Impact: [Expected outcome]

---

## Related Artifacts

- Journey Map: [Link to journey map file]
- Interview Transcripts: [Links to source interviews]
- Research Date: [When interviews conducted]

---

*This persona is based on qualitative user research following Nielsen Norman Group methodology. It represents a composite of [N] interview participants with shared attitudes, goals, and pain points.*
```

## Process Instructions

### Step 1: Analyze Input

**If single user provided:**
1. Read transcript file from `DI&A/transcripts/[name].txt`
2. Read journey map from `DI&A/journey/user-journey-[name].md`
3. Proceed to Step 3

**If multiple users or "all" specified:**
1. List all available transcripts and journeys
2. Read each journey map (faster than full transcripts)
3. Extract: role, goals, pain point themes, tools, workflow type
4. Proceed to Step 2

### Step 2: Cluster Users (for multiple users only)

1. **Create clustering matrix:**
   - Rows: Each user
   - Columns: Job function | Primary goal | Workflow type | Pain themes | Tools

2. **Apply clustering logic:**
   - Group users with matching function + goals + workflow
   - Separate users with fundamentally different roles or goals
   - Target: 2-4 personas (NN/g recommendation)

3. **Validate clusters:**
   - Each persona should represent ≥2 users (unless unique outlier)
   - Personas should be meaningfully distinct (not just minor variations)
   - Clusters should align with design/product decision-making needs

4. **Name clusters:**
   - Use job-function-based names: "Medical Evidence Generator", "Market Analyst", "Strategic Portfolio Manager"
   - Avoid demographic names: "The Millennial User", "The Expert"

### Step 3: Extract Persona Components

For each persona (or cluster):

1. **Read full transcripts** for users in this persona/cluster
2. **Read journey maps** for context and pain points
3. **Extract and synthesize:**
   - Demographics from actor profiles
   - Goals from scenario sections
   - Pain points from journey phases and opportunities
   - Quotes from mindsets sections and supporting quotes
   - Tools from actions and tools sections
   - Workflows from journey phases

4. **Create composite details:**
   - Synthesize shared patterns across users
   - Use direct quotes from interviews
   - Preserve specificity (tools, metrics, processes)
   - Note unique aspects even in composites

### Step 4: Write Persona Document

1. **Create realistic name:**
   - Use culturally appropriate names
   - Match approximate age/experience level
   - Make memorable but professional

2. **Write tagline:**
   - One sentence capturing essence
   - Should help stakeholders remember them
   - Based on primary goal or defining characteristic

3. **Populate all sections:**
   - Follow template exactly
   - Use actual quotes (with quotation marks)
   - Link to source materials
   - Note which users informed this persona

4. **Validate completeness:**
   - Every section filled with real data
   - At least 3-5 quotes throughout
   - Clear connection to research sources
   - Actionable opportunities identified

### Step 5: Create Output File(s)

**Folder:** `DI&A/personas/`

**Naming:**
- Single persona: `persona-[name].md` (e.g., `persona-alex-martinez.md`)
- Multiple personas: `personas-overview.md` containing all personas
- Optional individual files: `persona-[name].md` for each (if >3 personas)

**Always create the personas folder if it doesn't exist.**

## Quality Criteria

Each persona must:

✅ Be grounded in actual interview data (no invention)
✅ Include 5+ direct quotes from transcripts
✅ Clearly state which interviews it represents
✅ Have distinct pain points and goals from other personas
✅ Be actionable (inform design/product decisions)
✅ Be memorable (stakeholders can recall who they are)
✅ Avoid irrelevant demographic details
✅ Include specific tools, workflows, and behaviors
✅ Connect pain points to opportunities

## Common Pitfalls to Avoid

❌ **Creating personas from demographics alone**
   - Bad: "The 45-year-old male pharmacist"
   - Good: "The Medical Evidence Generator navigating limited research budgets"

❌ **Too many personas** (>5 creates confusion)
   - If >5 user types emerge, group by higher-level patterns

❌ **Personas that differ only slightly**
   - Merge similar personas; keep only meaningfully distinct ones

❌ **Irrelevant details**
   - Don't include: favorite coffee, hobbies (unless directly relevant)
   - Do include: tools used, frequency of tasks, decision constraints

❌ **Aspirational personas** (who we wish users were)
   - Ground in actual observed behaviors and attitudes

❌ **Static personas never updated**
   - Note research date; plan to update when significant new insights emerge

## Example Clustering Scenarios

### Scenario 1: 8 Users → 3 Personas

**Cluster 1: "Medical Evidence Generators"** (Simon, Henok)
- Job: Medical Advisor, Lead Epidemiologist
- Goal: Generate credible evidence for regulatory/strategic decisions
- Pain: Manual literature review, limited AI trust, data access barriers

**Cluster 2: "Market Intelligence Analysts"** (User A, User C, User D)
- Job: Insights Analytics, Forecasting Analyst
- Goal: Build accurate forecasts and market insights
- Pain: Fragmented data sources, manual triangulation, lack of refresh transparency

**Cluster 3: "Strategic Portfolio Leaders"** (User E, User F, User B)
- Job: Strategic Head, VP levels
- Goal: Make go/no-go decisions, manage product portfolio
- Pain: Resource negotiation, market definition uncertainty, 2nd-order thinking gaps

### Scenario 2: 8 Users → 4 Personas

Split Market Analysts by specialty:

**Cluster 2a: "Rapid Insights Analysts"** (User A)
- Focus: Quick turnaround ad-hoc analysis
- Pain: Data collection tedium, triangulation expertise requirement

**Cluster 2b: "Forecast Modelers"** (User C, User D)
- Focus: Long-term forecasting and planning
- Pain: Data refresh timing, Excel model complexity

## Usage Examples

```
# Create single persona
Create a persona from simon.txt

# Create personas from all available interviews
Create personas from all interviews in DI&A/

# Create personas from specific users
Create personas from abhishek, vamsi, and shirley

# Create manually clustered personas
Create personas:
- Medical Advisors: simon, henok
- Analysts: abhishek, vamsi, shirley
- Leaders: jehan, ferhat, paolo

# Create persona and also suggest clustering
Analyze all interviews and suggest persona clusters
```

## Output Summary

After creating personas, provide:

1. **Persona count:** How many personas created
2. **Clustering rationale:** Why users were grouped this way
3. **Key distinctions:** What makes each persona unique
4. **File locations:** Where personas were saved
5. **Next steps:** Suggestions for validation or refinement

---

*This skill implements Nielsen Norman Group's qualitative persona methodology (2024-2025), optimized for creating actionable, research-grounded personas that inform product and design decisions.*
