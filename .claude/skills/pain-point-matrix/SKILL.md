---
name: pain-point-matrix
description: Create pain point prioritization matrix plotting user frustrations by Severity × Frequency to prioritize which problems to solve first. Use when user wants to prioritize fixes, understand critical pain points, calculate ROI for improvements, or create phased roadmaps. AUTO-DISCOVERS pain points from existing empathy maps, journey maps, and JTBD files in the project folder — no manual input needed. Just provide the project domain name.
---

# Pain Point Prioritization Matrix

## Your Task

Transform interview data into a **Pain Point Prioritization Matrix** that plots user frustrations by **Severity** (how bad) and **Frequency** (how often). This creates a clear visual framework for prioritizing which problems to solve first.

**You operate in AUTO-DISCOVERY mode by default.** When given a project domain name, you autonomously scan all existing research files and extract, merge, score, and prioritize pain points without requiring any manual input from the user.

## Auto-Discovery Mode (Default)

**Trigger**: `/pain-point-matrix [domain]` — just the domain name is enough.

### Step 0: Scan Available Files

Before anything else, discover what files exist:

```
List files in: [domain]/empathy-maps/empathy-map-*.md   → FEELS extraction
List files in: [domain]/journey/*.md                     → Pain Points per phase
List files in: [domain]/jtbd/*-jtbd-*.md                 → Switching triggers / obstacles
List files in: [domain]/task-analysis/*.md               → Task-level pain (if available)
List files in: [domain]/mental-models/*.md               → Support gaps (if available)
```

Read ALL discovered files. Do not ask the user for a list — find them yourself.

### Step 1: Extract From Empathy Maps (FEELS Quadrant)

In each `empathy-map-*.md`, find the `## FEELS` section. Extract entries that signal pain:

**Pain signal patterns:**
- Emotions: frustrated, concerned, overwhelmed, anxious, skeptical, constrained, helpless, worried
- Intensity markers: "High intensity", "🔴", intensity score ≥ 7/10
- Language: "scares", "struggle", "difficult", "hate", "broken", "painful", "exhausting"

**Extract as:**
```
Pain: [emotion/description in 5-10 words]
Quote: [verbatim quote from the bullet]
User: [filename without path: abhishek, brian, etc.]
Severity signal: [High/Medium/Low from intensity marker]
Source: empathy-map-[user].md
```

**Skip:** Positive emotions (confident, hopeful, excited) unless paired with a constraint.

### Step 2: Extract From Journey Maps (Pain Points Sections)

In each journey map, find sections matching `**Pain Points:**` or `### Pain Points` within each phase. Extract every bullet:

**Pattern to match:**
```
**Pain Points:**
- **[Bold name]** - [description or "quote"]
```

**Extract as:**
```
Pain: [bold name / first 8 words of description]
Quote: [any quoted text found]
Phase: [phase heading this appeared under]
User: [filename]
Frequency signal: [daily/weekly/monthly if mentioned in phase context]
Source: journey/[filename].md (Phase: [phase name])
```

### Step 3: Extract From JTBD Files (Pain Points + Switching Triggers)

In each JTBD file, find sections matching:
- `**Pain Points**` blocks under each job
- `Switching Triggers` sections (switching = very high pain)
- `⏰ Time:`, `🎯 Quality:`, `💰 Cost:`, `🔒 Risk:` labeled items

**Extract as:**
```
Pain: [description]
Category: [Time/Quality/Cost/Risk]
Switching: [true if from Switching Triggers — score severity +1]
Quote: [any supporting quote]
Frequency: [from job frequency label: daily/weekly/monthly/quarterly]
User/Persona: [file stem]
Source: jtbd/[filename].md
```

### Step 2.5: Deduplication and Merging

After extracting from all sources, merge entries that refer to the same underlying problem:

**Merge rule:** Two entries describe the same pain if they share the same core concept (e.g., "manual data consolidation", "multi-source search"). When merging:
- Combine all quotes into the merged entry
- Set `users_affected` = count of distinct users mentioning it
- Set confidence = `high` (3+ sources), `medium` (2 sources), `low` (1 source)
- Keep the most specific description

## Inputs You Will Receive

You will work with (all auto-discovered):
- **Empathy maps** in `[PROJECT]/empathy-maps/empathy-map-*.md` — FEELS quadrant pain signals
- **Journey maps** in `[PROJECT]/journey/*.md` — Pain Points listed per phase
- **JTBD files** in `[PROJECT]/jtbd/*.md` — Job obstacles + switching triggers
- **Task analysis** in `[PROJECT]/task-analysis/*.md` (optional)
- **Mental model diagrams** in `[PROJECT]/mental-models/*.md` (optional)
- **Project name** (e.g., CPI, DI&A, CDDI)

## Output Location

Create pain point matrices at:
```
/[PROJECT]/pain-point-matrix/pain-point-matrix-[persona-name].md
```

Example: `/CDDI/pain-point-matrix/pain-point-matrix-emma-hartmann.md`

For cross-persona overview:
```
/[PROJECT]/pain-point-matrix/pain-point-matrix-overview.md
```

## Nielsen Norman Group Framework

### What is a Pain Point Prioritization Matrix?

A 2×2 matrix that plots problems on two axes:
- **X-axis: Frequency** (How often does this happen?)
- **Y-axis: Severity** (How bad is it when it happens?)

This creates four priority quadrants:

```
High Severity
     ↑
     │  HIGH PRIORITY        CRITICAL
     │  (Frequent + Severe)  (Severe but rare)
     │
     │
     │  LOW PRIORITY         MEDIUM PRIORITY
     │  (Rare + mild)        (Frequent but mild)
     │
     └──────────────────────────────────────→ High Frequency
```

### Quadrant Definitions

1. **CRITICAL** (Top-right): High severity + High frequency
   - **Action**: Fix immediately - biggest user pain
   - **Example**: Daily workflow blocker that takes 2 hours to work around

2. **HIGH PRIORITY** (Top-left): High severity + Low frequency
   - **Action**: Fix soon - when it happens, it's really bad
   - **Example**: Monthly report that fails and requires restart

3. **MEDIUM PRIORITY** (Bottom-right): Low severity + High frequency
   - **Action**: Automate or streamline - death by a thousand cuts
   - **Example**: Clicking through 5 screens for every search

4. **LOW PRIORITY** (Bottom-left): Low severity + Low frequency
   - **Action**: Backlog - nice to have but not urgent
   - **Example**: Rare edge case that has a simple workaround

### Scoring Methodology

**Severity (1-5)** — auto-inferred from source signals:

| Signal in source file | Severity |
|---|---|
| FEELS "High intensity" OR switching trigger OR "can't complete task" | 5 |
| FEELS "Medium-high intensity" OR "significant time loss" OR "hours" of workaround | 4 |
| FEELS "Medium intensity" OR "manual workaround exists" OR friction language | 3 |
| FEELS "Low-medium intensity" OR "minor annoyance" | 2 |
| FEELS "Low intensity" OR cosmetic complaint | 1 |

Boost severity by +1 if:
- Pain appears in `Switching Triggers` (user would leave product for this)
- Quote contains: "can't", "impossible", "no way", "broken", "hate", "painful", "scares"
- Pain is tagged with `💰 Cost:` or `🔒 Risk:` in JTBD (business stakes)

**Frequency (1-5)** — auto-inferred from source signals:

| Signal in source file | Frequency |
|---|---|
| JTBD job frequency = "daily" OR journey phase = core daily workflow | 5 |
| JTBD = "weekly" OR "every session" OR "each time I do X" | 4 |
| JTBD = "monthly" OR "few times a week" | 3 |
| JTBD = "quarterly" OR "occasionally" | 2 |
| JTBD = "yearly" OR "rarely" OR edge case | 1 |

If no frequency signal found: default to 3 (weekly) and note as estimated.

**Priority Score** = Severity × Frequency (range: 1-25)
- **20-25**: Critical (must fix)
- **15-19**: High priority
- **8-14**: Medium priority
- **1-7**: Low priority

**Confidence** (based on number of sources confirming the pain):
- **High**: 3+ distinct users / 3+ source files
- **Medium**: 2 users / 2 source files
- **Low**: 1 user / 1 source file — flag as "needs validation"

## Classification Prompts

Use these to extract pain points from source materials:

### 1. Pain Point Identification
- "What frustrates the user?"
- "What takes longer than expected?"
- "What causes errors or mistakes?"
- "Where do they use workarounds?"
- "What makes them switch tools?"

### 2. Severity Scoring
- "Can they complete the task without a workaround?" (Yes = lower severity)
- "How much time does this pain point cost?" (>1 hour = higher severity)
- "What's the emotional impact?" (Strong negative language = higher severity)
- "Does this affect business outcomes?" (Revenue/compliance = higher severity)

### 3. Frequency Scoring
- "How often does this happen?" (Look for "every time", "daily", "weekly")
- "Is this part of a regular workflow?" (Yes = higher frequency)
- "Is this triggered by an event?" (Event-based = lower frequency)

### 4. Evidence Gathering
- Find verbatim quotes expressing pain
- Note workarounds as proof of severity
- Count users experiencing the same pain (prevalence)

### 5. Impact Analysis
- "What's the business cost?" (Time × hourly rate × users affected)
- "What's at risk?" (Compliance, revenue, customer churn)
- "What's the opportunity?" (Time saved, quality improved, errors eliminated)

## Output Format

### File Structure

```markdown
---
title: Pain Point Prioritization Matrix - [Persona Name]
persona: [Persona Name]
project: [PROJECT]
source_files:
  - empathy-map-[user1].md
  - user-journey-[user1].md
  - task-analysis-[user1].md
created: [YYYY-MM-DD]
framework: Pain Point Prioritization Matrix (Nielsen Norman Group)
---

# Pain Point Prioritization Matrix: [Persona Name]

## Overview

**Persona**: [Persona Name]
**Role**: [Role/Title]
**Based on**: [N] users ([User1], [User2], ...)
**Total Pain Points**: [N]
**Analysis Date**: [Date]

## Executive Summary

**Critical Pain Points** (score 20-25): [N] items
**High Priority** (score 15-19): [N] items
**Medium Priority** (score 8-14): [N] items
**Low Priority** (score 1-7): [N] items

**Top 3 Pains to Fix**:
1. **[Pain Point Name]** (Score: [X]) - [One-line impact]
2. **[Pain Point Name]** (Score: [X]) - [One-line impact]
3. **[Pain Point Name]** (Score: [X]) - [One-line impact]

---

## Pain Point Inventory

### Critical (Score 20-25) 🔥

#### PP-001: [Pain Point Name]
- **Description**: [What the pain point is]
- **Severity**: 5/5 - [Why it's severe]
- **Frequency**: 5/5 - [How often it happens]
- **Priority Score**: 25
- **Affected Users**: [N]/[Total] ([User1], [User2])
- **Current Workaround**: [What users do now]
- **Business Impact**: [Time cost, revenue impact, compliance risk]
- **Quote**: "[Verbatim from interview expressing frustration]"
- **Source**: empathy-map-[user].md, user-journey-[user].md (Phase X)
- **Opportunity**: [Specific solution or improvement]

#### PP-002: [Pain Point Name]
- **Description**: [...]
- **Severity**: 5/5
- **Frequency**: 4/5
- **Priority Score**: 20
- [...]

---

### High Priority (Score 15-19) ⚠️

#### PP-003: [Pain Point Name]
- **Description**: [...]
- **Severity**: 5/5
- **Frequency**: 3/5
- **Priority Score**: 15
- [...]

---

### Medium Priority (Score 8-14) ℹ️

#### PP-007: [Pain Point Name]
- **Description**: [...]
- **Severity**: 3/5
- **Frequency**: 4/5
- **Priority Score**: 12
- [...]

---

### Low Priority (Score 1-7)

#### PP-012: [Pain Point Name]
- **Description**: [...]
- **Severity**: 2/5
- **Frequency**: 2/5
- **Priority Score**: 4
- [...]

---

## Prioritization Matrix (Visual)

```
        Severity
           ↑
         5 │ PP-001 [25]           PP-003 [15]
           │ PP-002 [20]           PP-004 [15]
           │
         4 │ PP-005 [16]           PP-006 [12]
           │ PP-007 [12]
           │
         3 │ PP-008 [9]            PP-009 [12]
           │                       PP-010 [9]
           │
         2 │ PP-011 [6]            PP-012 [8]
           │                       PP-013 [6]
           │
         1 │ PP-014 [2]            PP-015 [4]
           │
           └─────┴─────┴─────┴─────┴─────→ Frequency
             1     2     3     4     5

Quadrants:
  🔥 CRITICAL (Top-Right): PP-001, PP-002, PP-005     [Fix immediately]
  ⚠️ HIGH (Top-Left): PP-003, PP-004                  [Fix soon]
  ℹ️ MEDIUM (Bottom-Right): PP-006, PP-007, PP-009, PP-010, PP-012, PP-013  [Streamline]
     LOW (Bottom-Left): PP-008, PP-011, PP-014, PP-015  [Backlog]
```

---

## Pain Point Clustering

### By Category

**Tool/System Issues** (PP-001, PP-005, PP-009):
- [Brief description of pattern]
- **Prevalence**: [N]/[Total] users affected

**Workflow/Process Issues** (PP-002, PP-006, PP-010):
- [Brief description of pattern]

**Data Quality Issues** (PP-003, PP-007):
- [Brief description of pattern]

**Learning Curve Issues** (PP-004, PP-008):
- [Brief description of pattern]

### By Journey Phase

**Phase 1 - [Phase Name]**:
- PP-001: [Pain point]
- PP-003: [Pain point]

**Phase 2 - [Phase Name]**:
- PP-002: [Pain point]
- PP-005: [Pain point]

### By Persona (for cross-persona matrix only)

**Emma Hartmann (Discovery Scientist)**:
- Critical: PP-001, PP-002
- High: PP-003

**Linda Berglund (Information Specialist)**:
- Critical: PP-005
- Medium: PP-006, PP-007

---

## ROI Analysis

### Estimated Impact of Fixing Top 5 Pain Points

| Pain Point | Users Affected | Time Lost/Week | Hourly Rate | Annual Cost | Fix Effort | ROI |
|------------|----------------|----------------|-------------|-------------|------------|-----|
| PP-001     | 5/5 (100%)     | 10 hrs         | $150        | $390,000    | Medium     | ⭐⭐⭐⭐⭐ |
| PP-002     | 4/5 (80%)      | 5 hrs          | $150        | $156,000    | High       | ⭐⭐⭐ |
| PP-003     | 3/5 (60%)      | 2 hrs          | $150        | $46,800     | Low        | ⭐⭐⭐⭐⭐ |
| PP-005     | 5/5 (100%)     | 3 hrs          | $150        | $117,000    | Medium     | ⭐⭐⭐⭐ |
| PP-006     | 2/5 (40%)      | 4 hrs          | $150        | $62,400     | High       | ⭐⭐ |

**Total Annual Cost** (Top 5): $772,200
**Quick Wins** (High ROI + Low Effort): PP-003

---

## Recommendations

### Phase 1: Must-Fix (Months 1-3)

1. **PP-001: [Pain Point Name]** (Score: 25)
   - **Solution**: [Specific feature or improvement]
   - **Effort**: [T-shirt size: S/M/L/XL]
   - **Impact**: Saves [X] hours/week for [N] users
   - **Dependencies**: [Any blockers or prerequisites]

2. **PP-002: [Pain Point Name]** (Score: 20)
   - [...]

### Phase 2: High Priority (Months 4-6)

3. **PP-003: [Pain Point Name]** (Score: 15)
   - [...]

4. **PP-004: [Pain Point Name]** (Score: 15)
   - [...]

### Phase 3: Incremental Improvements (Months 7-12)

5. **PP-006, PP-007: [Grouped pain points]**
   - [Bundled solution addressing multiple medium-priority pains]

### Backlog (Future)

- PP-011, PP-014, PP-015: [Low-priority items for future consideration]

---

## Integration with Other Outputs

### Empathy Map Connection
- Pain points sourced from "Pains" quadrant
- Emotional intensity informs severity scoring

### Journey Map Connection
- Pain points mapped to specific journey phases
- Frequency correlates with phase occurrence

### Task Analysis Connection
- Task-level pain points rolled up into matrix
- Task complexity influences severity

### Mental Model Connection
- Support gaps (❌ Not supported) = high severity
- Partial support (⚠️) = moderate severity
- Feature misalignment = source of pain

### JTBD Connection
- Job obstacles = pain points
- Job frequency = pain frequency

---

## Validation & Confidence

### Data Quality

**Evidence Strength**:
- **High confidence** (5+ user quotes): PP-001, PP-002, PP-005
- **Medium confidence** (2-4 user quotes): PP-003, PP-006
- **Low confidence** (1 user quote): PP-012, PP-015

### Assumptions

- Hourly rate: $150 (industry average for [role])
- Work weeks/year: 52
- Users affected: Based on [N] interview sample

### Limitations

- Sample size: [N] users (may not represent all [Persona] behavior)
- Self-reported frequency (actual may vary)
- Severity based on emotional language (subjective)

---

**Methodology Note**: Pain points extracted from empathy maps, journey maps, and task analyses across [N] users. Severity and frequency scored based on verbatim quotes, workaround complexity, and time impact. Priority scores calculated as Severity × Frequency following Nielsen Norman Group methodology.

**Sources**:
- Empathy maps: `empathy-map-[user1].md`, `empathy-map-[user2].md`
- Journey maps: `user-journey-[user1].md`, `user-journey-[user2].md`
- Task analyses: `task-analysis-[user1].md`, `task-analysis-[user2].md`
- Mental models: `mental-model-[persona].md`
```

## Process Guidelines

### Step 1: Read All Source Materials

For a **persona-level** matrix:
```bash
# Read all empathy maps for persona users
Glob: /[PROJECT]/empathy-maps/empathy-map-*.md
Read: [Selected files for persona users]

# Read journey maps
Read: /[PROJECT]/journey/user-journey-*.md (for persona users)

# Read task analyses (if available)
Read: /[PROJECT]/task-analysis/task-analysis-*.md (for persona users)

# Read mental model diagram (if available)
Read: /[PROJECT]/mental-models/mental-model-[persona].md
```

### Step 2: Extract Pain Points

From each source:
- **Empathy maps**: "Pains" quadrant (direct extraction)
- **Journey maps**: Pain points listed in each phase
- **Task analyses**: Pain points per task
- **Mental models**: Support gaps (❌ ⚠️)

Create a comprehensive list with:
- Pain point ID (PP-001, PP-002, ...)
- Description
- Source file(s)
- Verbatim quote(s)

### Step 3: Score Severity (1-5)

For each pain point, evaluate:
- **Blocker impact** (5): "Can't complete my work without workaround"
- **Time impact**: >1 hour = 4-5, 15-60 min = 3, <15 min = 1-2
- **Emotional language**: "Hate", "frustrating", "broken" = higher severity
- **Business risk**: Compliance, revenue, customer impact = +1 severity
- **Workaround complexity**: 3+ tools = higher severity

### Step 4: Score Frequency (1-5)

Look for temporal keywords in quotes:
- **"Every time", "constantly", "all day"** → 5
- **"Daily", "every session"** → 4
- **"Weekly", "few times a week"** → 3
- **"Monthly", "occasionally"** → 2
- **"Rarely", "sometimes", "edge case"** → 1

Cross-check with:
- Task frequency (from task analysis)
- Journey phase frequency (from journey map)

### Step 5: Calculate Priority Scores

```
Priority Score = Severity × Frequency
```

Categorize:
- **20-25**: Critical 🔥
- **15-19**: High Priority ⚠️
- **8-14**: Medium Priority ℹ️
- **1-7**: Low Priority

### Step 6: Count User Prevalence

For each pain point:
- Count how many users mentioned it
- Calculate percentage: [N users affected] / [Total users]
- **High prevalence** (>66%): Systemic issue
- **Medium prevalence** (33-66%): Segment-specific
- **Low prevalence** (<33%): Individual edge case

### Step 7: Create Visual Matrix

Plot pain points on 2×2 grid:
- X-axis: Frequency (1-5)
- Y-axis: Severity (1-5)
- Label each point with PP-ID and score

### Step 8: Cluster Pain Points

Group by:
- **Category**: Tool/system, workflow, data, learning curve
- **Journey phase**: Where in workflow does pain occur?
- **Persona** (for cross-persona matrix): Which user type feels this pain?

### Step 9: ROI Analysis

For top 5-10 pain points:
```
Annual Cost = (Time Lost/Week) × (Users Affected) × (Hourly Rate) × 52 weeks
```

Estimate fix effort (S/M/L/XL):
- **S (Small)**: <1 week dev time
- **M (Medium)**: 1-4 weeks
- **L (Large)**: 1-3 months
- **XL (Extra Large)**: >3 months

Calculate ROI:
- **High ROI**: High cost + Low effort
- **Low ROI**: Low cost + High effort

### Step 10: Phased Recommendations

**Phase 1 (Months 1-3)**: Critical + High priority items
**Phase 2 (Months 4-6)**: High priority + Quick wins (high ROI)
**Phase 3 (Months 7-12)**: Medium priority (bundled solutions)
**Backlog**: Low priority (defer)

## Quality Criteria

✅ **All pain points scored**: Every item has Severity, Frequency, Priority Score
✅ **Evidence-based**: Each pain point has verbatim quotes
✅ **User prevalence counted**: N/Total users affected is tracked
✅ **Visual matrix included**: ASCII diagram plots all pain points
✅ **Clustered by theme**: Pain points grouped by category/phase/persona
✅ **ROI calculated**: Top items have cost/benefit analysis
✅ **Phased recommendations**: Clear roadmap for fixes
✅ **Cross-referenced**: Links to empathy maps, journey maps, task analysis

## Common Mistakes to Avoid

❌ **Severity bias**: Not all pain points are 5/5 - be honest about impact
❌ **Missing frequency data**: Must estimate from quotes or context
❌ **No user count**: Prevalence matters (1 user vs. all users)
❌ **Vague pain points**: "Slow system" → "Database query takes 2 minutes, times out"
❌ **No quotes**: Every pain point needs verbatim evidence
❌ **Equal weighting**: Critical (25) is 6× more urgent than low (4)
❌ **Ignoring ROI**: High-score pain might have low business impact
❌ **No phasing**: Can't fix everything at once - prioritize phases

## Validation

Before finalizing, check:

1. Are severity scores justified by quotes or time impact?
2. Are frequency scores backed by temporal keywords?
3. Is user prevalence (N/Total) calculated for each pain?
4. Are all pain points plotted on the visual matrix?
5. Do critical items (20-25) have ROI analysis?
6. Are recommendations phased across 3-12 months?
7. Do pain point IDs match across all sections (PP-001, PP-002...)?

## Example Pain Point Snippet

```markdown
#### PP-001: Multi-database searching requires manual synthesis

- **Description**: Users must query 3+ databases (CDDI, Cortellis, PubMed) separately and manually combine results in Excel. No unified search or automatic deduplication.
- **Severity**: 5/5 - Blocker (workflow stops until synthesis is complete)
- **Frequency**: 5/5 - Daily (every competitive intelligence task)
- **Priority Score**: 25 (Critical 🔥)
- **Affected Users**: 5/5 (100%) - All Emma Hartmann persona users
- **Current Workaround**:
  1. Search CDDI → Export to Excel
  2. Search Cortellis → Export to Excel
  3. Search PubMed → Export to Excel
  4. Manually deduplicate and merge (1-2 hours)
- **Business Impact**:
  - Time cost: 10 hours/week × 5 users × $150/hr = $390,000/year
  - Quality risk: Manual merging introduces errors
- **Quote**: "I spend half my day just copying and pasting from different databases into one spreadsheet. It's soul-crushing work and I know I'm missing things."
  — Interview with Hartmut Schirok (lines 234-236)
- **Quote**: "Every. Single. Search. I have to do this dance across three systems. Why can't CDDI just pull everything together?"
  — Interview with Jon Winter-Holt (lines 145-147)
- **Source**:
  - empathy-map-hartmut-schirok.md (Pains quadrant)
  - user-journey-hartmut-schirok.md (Phase 2: Information Gathering)
  - task-analysis-hartmut-schirok.md (Task 1.2.1 - Multi-source search)
- **Opportunity**: Build unified search across all data sources with automatic deduplication and results merging. Estimated effort: Large (3 months). ROI: ⭐⭐⭐⭐⭐
```

---

## Integration Notes

This skill complements:
- **Empathy Map Generator** - Primary source for pain points
- **User Journey** - Pain points mapped to journey phases
- **Task Analysis** - Task-level pain points feed into matrix
- **Mental Model Diagram** - Support gaps = pain points
- **JTBD** - Job obstacles inform pain severity
