---
name: jtbd-analyzer
description: Extract structured Jobs-to-be-Done (JTBD) statements from interview transcripts following Clayton Christensen methodology. Use when user wants to understand user motivation and progress goals, identify why users "hire" products, cluster jobs across personas, or create functional/emotional/social job statements. Transforms interview data into JTBD format (When [situation], I want to [motivation], So I can [outcome]) with job clusters and cross-user patterns.
---

# Jobs-to-be-Done Analyzer

Extract structured Jobs-to-be-Done (JTBD) statements from interview transcripts to understand what "progress" users seek and why they "hire" products.

## Framework Background

**Method Origin:** Clayton Christensen (Harvard, 2005) → Bob Moesta refinement

**Core Concept:** People don't buy products—they "hire" them to make progress in specific circumstances. Understanding the job reveals the motivation, not just the action.

**JTBD Structure:**
```
When [context/circumstance] → Triggering situation
I want to [action/motivation] → Functional job
So I can [outcome/benefit] → Desired progress
```

**Three Job Dimensions:**
1. **Functional:** Tangible task/outcome (complete systematic review in 3 weeks)
2. **Emotional:** How it makes them feel (confident in data quality, reduce anxiety)
3. **Social:** How others perceive them (trusted expert, efficient professional)

## What This Skill Does

Automatically identifies and extracts Jobs-to-be-Done from interview transcripts using:
- LLM pattern recognition for "When/I want/So I can" linguistic structures
- Context extraction (trigger moments, circumstances, constraints)
- Job clustering across multiple interviews
- Frequency tracking (how many users mention this job?)
- Competitive mapping (what solutions are "hired" for each job today?)

## When to Use

Run this skill when you have:
- ✅ Interview transcripts (markdown or TXT format)
- ✅ Journey maps with identified pain points
- ✅ Personas that need motivational depth ("Why do they hire our product?")

**Ideal Timing:** After creating journey maps but before finalizing personas—JTBD adds the "why" layer.

## Input

1. **Interview transcripts** (one or more files)
   - Path: `DI&A/transcripts/*.txt` or `*.md`
   - Can process single interview or batch multiple

2. **Optional: Journey map** (for cross-reference)
   - Path: `DI&A/journey/user-journey-*.md`
   - Used to validate trigger moments align with journey phases

## Output

Structured JTBD analysis in markdown format:

```markdown
# Jobs-to-be-Done Analysis: [Persona Name]

**Based on:** [Interview sources]
**Date:** [Generation date]

---

## Primary Jobs Identified

### Job 1: [Job Title]
**Frequency:** [X times per year/month/week]
**Mentioned by:** [List of users who mentioned this job]
**Confidence:** [High/Medium/Low - based on # of mentions]

**When (Circumstance):**
- [Triggering situation 1]
- [Triggering situation 2]
- [Triggering situation 3]

**I want to (Motivation):**
- [Functional goal 1]
- [Functional goal 2]
- [Functional goal 3]

**So I can (Outcome):**
- [Desired end state 1]
- [Desired end state 2]
- [Desired end state 3]

**Job Dimensions:**
- 🎯 **Functional:** [Tangible task/outcome]
- ❤️ **Emotional:** [How it makes them feel]
- 👥 **Social:** [How others perceive them]

**Current Solution ("Hired Product"):**
- [Tool/method 1]: [Why they use it]
- [Tool/method 2]: [Why they use it]
- [Tool/method 3]: [Why they use it]

**Pain Points:**
- ⏰ [Time-related pain]
- 🎯 [Quality-related pain]
- 💰 [Cost-related pain]
- 🔒 [Risk-related pain]

**Switching Triggers (What would make them hire a different solution?):**
- [Trigger 1: Must achieve X improvement]
- [Trigger 2: Must solve Y pain point]
- [Trigger 3: Must provide Z benefit]

**Supporting Quotes:**
> "[Direct quote from transcript showing this job]"
>
> "[Another quote demonstrating this motivation]"

---

### Job 2: [Next Job Title]
[... same structure ...]

---

## Cross-Cutting Patterns

### Emotional Jobs (Underlying Motivations Across All Jobs)
1. **[Emotion 1]** - [Why this matters]
2. **[Emotion 2]** - [Why this matters]
3. **[Emotion 3]** - [Why this matters]

### Functional Jobs (Common Tangible Outcomes)
1. **[Function 1]** - [Metric]
2. **[Function 2]** - [Metric]
3. **[Function 3]** - [Metric]

### Social Jobs (How They Want to Be Perceived)
1. **[Perception 1]** - [Context]
2. **[Perception 2]** - [Context]
3. **[Perception 3]** - [Context]

---

## Product Implications: "Hire Our Solution For..."

### For Job 1:
**Build:** [Product/feature recommendation]
- **Functional benefit:** [Measurable improvement]
- **Emotional benefit:** [Anxiety reduction, confidence gain]
- **Social benefit:** [Reputation enhancement]

**Positioning:** "[When you need X, we help you Y]"

### For Job 2:
[... same structure ...]

---

## Competitive Landscape: What Are They "Hiring" Today?

| Solution | Job Hired For | Strengths | Weaknesses | Opportunity Gap |
|----------|--------------|-----------|------------|-----------------|
| **[Tool 1]** | [Job] | [Why it's hired] | [Why they'd fire it] | [Unmet need] |
| **[Tool 2]** | [Job] | [Why it's hired] | [Why they'd fire it] | [Unmet need] |
| **[Tool 3]** | [Job] | [Why it's hired] | [Why they'd fire it] | [Unmet need] |

**Opportunity:** [No current solution hired for X job]

---

## Validation Questions (For Future Interviews)

### Test JTBD Hypotheses:
- "Tell me about the last time you needed to [job]. What triggered that need?"
- "Walk me through how you decided which tool/solution to use for that job."
- "What would need to be true about a new solution for you to switch from [current solution]?"
- "How often does [job] come up in your workflow?" (validate frequency)
- "On a scale of 1-10, how painful is [job] currently?" (validate pain level)

### Identify New Jobs:
- "What tasks do you procrastinate on because they're tedious but necessary?"
- "If you had an extra 10 hours per week, what would you spend it on?"
- "What do you wish you could delegate but can't because it requires your judgment?"

---

## Methodology Notes

**JTBD Analysis Process:**
1. **Extract trigger moments** from transcripts (when, circumstance language)
2. **Identify desired outcomes** (so I can, in order to, because I need to)
3. **Map emotional/social jobs** beyond functional (anxiety, credibility, status)
4. **Cluster similar jobs** across users
5. **Validate with users** (show them JTBD statements, ask "does this resonate?")

**Tools Used:**
- LLM pattern matching for JTBD structure detection
- Sentiment analysis for emotional job identification
- Frequency tracking across transcripts

**Quality Criteria:**
- ✅ Grounded in actual interview data (direct quotes linked)
- ✅ Functional + Emotional + Social dimensions captured
- ✅ Frequency labeled with sample size (transparency)
- ✅ Competitive landscape mapped (what's hired today?)
- ✅ Validation questions generated (testable hypotheses)

---

**References:**
- Clayton Christensen, "The Innovator's Solution" (2005)
- Bob Moesta, "Demand-Side Sales 101" (2020)
- Tony Ulwick, "Outcome-Driven Innovation" (2016)
- NN/g: [Personas vs. Jobs-to-Be-Done](https://www.nngroup.com/articles/personas-jobs-be-done/)
```

## How to Use This Skill

### Basic Usage

**Single transcript:**
```
Analyze jobs-to-be-done from DI&A/transcripts/enid.txt
```

**Multiple transcripts (persona-level analysis):**
```
Analyze jobs-to-be-done for Dr. Sarah Mitchell persona using:
- DI&A/transcripts/henok.txt
- DI&A/transcripts/simon.txt
```

**With journey map cross-reference:**
```
Analyze jobs-to-be-done from DI&A/transcripts/enid.txt
Cross-reference with DI&A/journey/user-journey-enid.md
```

### Advanced Usage

**Competitive analysis focus:**
```
Extract jobs from [transcripts] and map to competitive landscape:
- What solutions are hired today?
- What are the switching triggers?
- What gaps exist?
```

**Validation question generation:**
```
Generate JTBD validation questions for future interviews based on [transcripts]
```

**Frequency validation:**
```
Compare job frequency across all 4 personas:
- Sample Participant (User A, User B, User C)
- Dr. Sarah Mitchell (User G, User H)
- Dr. Elena Martinez (User F)
- Jay Kumar (User E)
```

## Key Features

### 1. Pattern Recognition
- Detects "When/I want/So I can" linguistic structures
- Identifies implicit jobs (inferred from pain points, workarounds)
- Extracts context clues (deadlines, pressure, constraints)

### 2. Job Clustering
- Groups similar jobs across multiple users
- Labels frequency ("Mentioned by 3/4 users")
- Identifies cross-persona patterns (jobs shared by multiple archetypes)

### 3. Competitive Mapping
- What solutions are "hired" for each job today?
- Why would users "fire" current solutions?
- What are the switching triggers?

### 4. Three-Dimensional Analysis
- **Functional:** Tangible tasks and outcomes
- **Emotional:** Feelings, anxieties, confidence needs
- **Social:** How users want to be perceived by others

### 5. Validation Support
- Generates interview questions to test JTBD hypotheses
- Provides "does this resonate?" statements for user validation
- Labels confidence levels (High: 3+ mentions, Medium: 2 mentions, Low: 1 mention)

## Success Metrics

- **JTBD coverage:** 80%+ of user motivations captured in 3-5 primary jobs
- **Extraction accuracy:** 85%+ agreement between LLM extraction and human validation
- **Product alignment:** JTBD analysis informs 3+ roadmap decisions
- **User validation:** 85%+ of users say "yes, that's exactly why I hire this"

## Why This Matters

### Personas vs. JTBD
- **Personas answer:** "Who is the user?" (Dr. Sarah Mitchell = Medical Advisor, 38-45)
- **JTBD answers:** "What progress do they seek?" (Rapid evidence synthesis for deadlines)
- **Together:** Complete picture of user + motivation

### Product Strategy
- **Feature prioritization:** Build for highest-frequency, highest-pain jobs first
- **Positioning:** "When [circumstance], we help you [outcome]" (not "AI tool for researchers")
- **Competitive gaps:** Jobs that no current solution is hired for = opportunity

### Marketing Messaging
- Speak to motivations, not just features
- "Stop wasting 40% of your time on X" (addresses job pain)
- "When you need Y in days, not weeks" (addresses circumstance trigger)

## Technical Implementation

**Process:**
1. **Read transcript** → Parse into paragraphs
2. **LLM pattern extraction** → Identify "When/I want/So I can" structures
3. **Context enrichment** → Add emotional/social dimensions via sentiment analysis
4. **Job clustering** → Group similar jobs using semantic similarity
5. **Frequency tracking** → Count mentions across users
6. **Competitive mapping** → Extract mentioned tools/solutions
7. **Validation questions** → Generate testable hypotheses
8. **Human review** → Researcher validates extracted jobs (approve/edit/reject)

**Tools:**
- Claude Sonnet for pattern recognition and job extraction
- Semantic similarity for job clustering
- Quote linking for traceability
- Markdown output for easy review and editing

## Best Practices

### Do:
- ✅ Label job frequency with sample size ("Mentioned by 2/3 users")
- ✅ Link every job to direct quotes (traceability)
- ✅ Include functional + emotional + social dimensions
- ✅ Map competitive landscape (what's hired today?)
- ✅ Generate validation questions for future interviews
- ✅ Mark single-source jobs as "Needs validation"

### Don't:
- ❌ Fully automate (human validation required)
- ❌ Invent jobs not grounded in transcripts
- ❌ Ignore low-frequency jobs (might be high-impact)
- ❌ Skip competitive mapping (miss switching triggers)
- ❌ Use vague language ("users want better tools" → specify the job)

## Integration with Existing Workflow

**Current:**
1. Conduct interview → Transcript
2. Create journey map → Workflow phases
3. Synthesize persona → User archetype

**Enhanced with JTBD:**
1. Conduct interview → Transcript
2. **Run JTBD Analyzer** → Extract jobs
3. Create journey map → Phases + trigger moments linked to jobs
4. Synthesize persona → Archetype + 5 primary jobs

**Persona File Enhancement:**
Add "Primary Jobs" section after overview:
```markdown
## Dr. Sarah Mitchell - Practical Medical Strategist

### Primary Jobs (What She Hires Products For)

#### Job 1: Rapid Evidence Synthesis for Strategic Decisions
**Frequency:** 8-12x/year | **Mentioned by:** 2/2 users
[... full job details ...]
```

## Limitations & Mitigation

**1. Small Sample Size Risk:**
- **Issue:** 1-2 interviews may not validate job frequency
- **Mitigation:** Label confidence levels, mark "Needs validation" for single-source jobs

**2. LLM Hallucination Risk:**
- **Issue:** May infer jobs not explicitly stated
- **Mitigation:** Human validation required, link all jobs to direct quotes

**3. Job Evolution Over Time:**
- **Issue:** Jobs change as tools/workflows evolve
- **Mitigation:** Refresh JTBD analysis quarterly, track switching events

**4. Overlap with Journey Maps:**
- **Issue:** May feel redundant if journey maps already document triggers
- **Mitigation:** JTBD provides motivational depth (why) vs. journey map workflow (what)

## Example Output Preview

**Input:** `DI&A/transcripts/enid.txt` (Brand Manager interview)

**Output:** `DI&A/jtbd/jtbd-analysis-enid.md`

**Sample Extracted Job:**
```markdown
### Job 3: Respond to Leadership Without Derailing Execution

**Frequency:** 2-3 times per week
**Mentioned by:** Participant 3 (Brand Manager, Company A)
**Confidence:** Low (single source - needs validation)

**When (Circumstance):**
- Ad hoc leadership update requested mid-campaign
- Executive wants status on brand strategy
- Board presentation requires synthesis of current state

**I want to (Motivation):**
- Provide status quickly without spending hours on synthesis
- Demonstrate strategic progress to leadership
- Show campaign performance metrics

**So I can (Outcome):**
- Maintain focus on actual execution (not just reporting)
- Preserve time for strategic work vs. admin updates
- Keep leadership informed without derailing team momentum

**Job Dimensions:**
- 🎯 **Functional:** Generate status update in <30 minutes
- ❤️ **Emotional:** Reduce anxiety about "leadership tax" on time
- 👥 **Social:** Be seen as responsive to leadership while protective of team execution time

**Current Solution:**
- Manual PowerPoint decks (time-consuming)
- Email summaries (lack visual impact)
- Cross-functional meeting recaps (require synthesis)

**Pain Points:**
- ⏰ **Time:** "Updates are a lot more frequent, aren't driving business"
- 🎯 **Focus:** Distracted from strategic thinking and execution
- 💼 **Balance:** "You kind of have to balance because they're not typically driving business"

**Switching Triggers:**
- Auto-generated leadership dashboards with real-time metrics
- One-click status reports (no manual synthesis required)
- Exception-based reporting (only flag items requiring decisions)

**Supporting Quotes:**
> "The key things that are difficult are the ad hoc requests from leadership... the updates are a lot more frequent"
>
> "A lot of times updates aren't execution... just synthesis of strategies... they're not typically driving business"
```

---

## Next Steps After Running This Skill

1. **Review extracted jobs** → Researcher validates accuracy
2. **Add to personas** → Include "Primary Jobs" section
3. **Use for roadmap** → Prioritize by frequency × pain matrix
4. **Generate validation questions** → Test in future interviews
5. **Update quarterly** → Jobs evolve with tools/workflows
