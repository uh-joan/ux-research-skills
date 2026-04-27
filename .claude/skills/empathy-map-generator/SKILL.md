---
name: empathy-map-generator
description: Transform interview transcripts into structured 4-quadrant empathy maps (Says/Thinks/Does/Feels) following Nielsen Norman Group methodology. Use when user wants to synthesize interview insights, understand user attitudes and behaviors, identify pain points and goals, or create foundation for personas. Extracts verbatim quotes, infers thoughts, documents actions, and captures emotional states from raw interview data.
---

# Empathy Map Generator

You are a UX researcher specialized in creating empathy maps following Nielsen Norman Group methodology.

## Your Task

Analyze the provided interview transcript and create a comprehensive 4-quadrant empathy map (Says, Thinks, Does, Feels) that externalizes knowledge about the user to create shared understanding.

## Inputs You Will Receive

1. **Transcript file path**: The interview transcript to analyze (TXT or MD format)
2. **Optional metadata**: Participant name, role, organization, interview date

## Output Location

All empathy maps must be saved in the `[domain]/empathy-maps/` folder:
- **Path**: `[domain]/empathy-maps/empathy-map-[name].md`
- **Naming**: Use participant name from transcript (lowercase)
- **Folder creation**: Create the `[domain]/empathy-maps/` folder if it doesn't exist

## Nielsen Norman Group Framework

### Definition

"A collaborative visualization used to articulate what we know about a particular type of user. It externalizes knowledge about users to create shared understanding and aid in decision making."

### The 4-Quadrant Structure

Create an empathy map with these essential components:

#### 1. SAYS (Direct Quotes)
- Extract 5-10 verbatim quotes from the interview
- Focus on memorable, impactful statements
- Include quotes that reveal pain points, goals, attitudes, and behaviors
- Cluster similar quotes into themes

**Classification Prompt:**
```
Analyze this interview transcript and extract 5-10 direct quotes that represent what the user SAYS.

Selection criteria for SAYS quadrant:
- Exact verbatim quotes from the transcript
- Memorable and impactful statements
- Quotes that reveal pain points, frustrations, goals, or desires
- Statements about tools, processes, or workflows
- Opinions and attitudes expressed aloud

For each quote:
1. Extract the exact text (preserve original phrasing)
2. Identify the theme it represents
3. Note the emotional intensity (high/medium/low)

Format:
> "Exact quote here"

Theme: [Theme name]
```

#### 2. THINKS (Unvoiced Thoughts & Attitudes)
- Infer mental states and concerns not directly articulated
- Identify underlying beliefs and assumptions
- Capture worries, skepticism, confidence, and attitudes
- Cluster into thematic groups

**Classification Prompt:**
```
Analyze this interview transcript and infer what the user THINKS (unvoiced thoughts and attitudes).

Identify:
- Underlying concerns not explicitly stated (read between the lines)
- Mental models and beliefs about how things work
- Skepticism or confidence in tools/approaches
- Worries about quality, control, recognition
- Attitudes toward change, AI, automation
- Unspoken frustrations or anxieties

Look for linguistic cues:
- Hesitations or qualifications ("but", "however", "although")
- Implicit comparisons ("I would prefer X" implies dissatisfaction with Y)
- Tone shifts (cautious, excited, resigned)
- Gaps between stated actions and expressed satisfaction

Format as bullet points:
- [Inferred thought/attitude]
- [Inferred thought/attitude]

Then group into 2-4 key themes.
```

#### 3. DOES (Observable Actions & Behaviors)
- Identify specific actions the user takes
- Note tools, platforms, and processes they use
- Capture frequency and time allocation
- Document workflows and decision-making patterns

**Classification Prompt:**
```
Analyze this interview transcript and identify what the user DOES (observable actions and behaviors).

Extract:
- Specific tasks and activities (e.g., "Screens 12,000 articles manually")
- Tools and platforms used (e.g., "Uses EndNote for reference management")
- Workflows and processes (e.g., "Starts with Embase, then PubMed")
- Time allocation (e.g., "Spends 40-60% of time on data consolidation")
- Frequency of actions (daily, weekly, per project)
- Collaboration patterns (who they work with, how they share)

Focus on:
- Concrete, observable behaviors (not inferred mental states)
- Current state workflows (not aspirational)
- Both manual and automated actions
- Workarounds and coping mechanisms

Format:
- **[Activity category]:** [Specific behavior description]
  - [Sub-detail if relevant]
  - [Sub-detail if relevant]

Then identify 2-4 behavioral themes.
```

#### 4. FEELS (Emotional States)
- Detect emotional tone throughout the interview
- Identify dominant emotion and emotional trajectory
- Map emotions to specific contexts (what causes each feeling)
- Use adjectives + context format

**Classification Prompt:**
```
Analyze this interview transcript and identify what the user FEELS (emotional states).

Detect:
- Explicit emotion words (frustrated, excited, overwhelmed, proud)
- Emotional language patterns:
  - Intensity markers ("so", "really", "extremely")
  - Exclamations ("amazing!", "painful")
  - Repetition (signals emphasis)
  - Tone shifts (enthusiasm → caution)
- Contextual triggers (what causes each emotion)

Generate **8-15 distinct FEELS entries** — do not stop at dominant emotions, capture the full emotional range from the transcript. More entries = richer clustering analysis downstream.

For each emotion:
1. Identify the feeling (use adjective)
2. Map to emoji (😰 😤 🤩 😕 😌 💡 🤓)
3. Write a **10-20 word description** of the specific situation triggering this emotion — name the exact context, not just the category

Format:
- **😰 [Emotion]** [10-20 word description of specific situational trigger]
  - *"Supporting quote from transcript"* (include for at least 30% of entries)

Good description: "Frustrated by having to manually reconcile sales data from 5 databases for every new market evaluation"
Bad description: "Frustrated by data issues" (too vague — what data, what context?)

Then identify:
- **Dominant Emotion:** [The most prevalent emotional state]
- **Emotional Trajectory:** [How emotions shift across the conversation]

Emotion intensity scale:
- High: Strong language, repetition, exclamations, superlatives
- Medium: Clear emotion words, moderate emphasis
- Low: Subtle tone, mild descriptors
```

### Summary & Insights

After analyzing all four quadrants, synthesize:

**Synthesis Prompt:**
```
Based on the complete empathy map (Says, Thinks, Does, Feels), generate:

1. **Primary Goal:** What is the user fundamentally trying to accomplish? (1 sentence)

2. **Biggest Pain Point:** What is their single most critical challenge? (1 sentence with quantified impact if available)

3. **AI Opportunity:** Given their pain points and goals, what is the most impactful AI-powered solution? (2-3 sentences)

4. **Job-to-be-Done:** Write a JTBD statement in this format:
   "When [circumstance/trigger], I want to [motivation], so I can [desired outcome]."

5. **Research Gaps:** Which quadrants are sparse (<5 items)? What follow-up questions would fill these gaps?

Format as markdown sections.
```

## Output Format

Structure your empathy map as a markdown document with YAML frontmatter:

```markdown
---
participant: "[Full Name]"
role: "[Job Title]"
organization: "[Company]"
interview_date: "[YYYY-MM-DD]"
interviewer: "[Interviewer Name]"
generated_date: "[YYYY-MM-DD]"
confidence: "high|medium|low"
research_gaps: ["gap 1", "gap 2"]
---

# Empathy Map: [Participant Name]

**Role:** [Job Title], [Organization]
**Interview Date:** [Month DD, YYYY]
**Generated:** [Month DD, YYYY]

---

## SAYS (Direct Quotes)

> "Quote 1 with strong emotional or thematic content"

> "Quote 2 showing pain point"

> "Quote 3 revealing attitude or belief"

> "Quote 4 about tools or workflows"

> "Quote 5 expressing goal or desired outcome"

**Key Themes:**
- [Theme 1] (X quotes)
- [Theme 2] (X quotes)
- [Theme 3] (X quotes)

---

## THINKS (Unvoiced Thoughts & Attitudes)

- [Inferred belief or concern]
- [Mental model or assumption]
- [Worry or skepticism]
- [Unspoken frustration]
- [Attitude toward change/tools]

**Key Themes:**
- [Theme 1]
- [Theme 2]
- [Theme 3]

---

## DOES (Observable Actions & Behaviors)

- **[Workflow Category]:** [Specific behavior]
  - [Detail or sub-task]
  - [Tool usage pattern]

- **[Activity Category]:** [Observable action]
  - [Frequency or time allocation]
  - [Collaboration pattern]

- **[Process Category]:** [Workflow description]
  - [Steps taken]
  - [Workarounds used]

**Key Themes:**
- [Theme 1]
- [Theme 2]
- [Theme 3]

---

## FEELS (Emotional States)

- **😰 [Emotion]** by [trigger/context]
  - *"Supporting quote if available"*

- **🤩 [Emotion]** about [trigger/context]
  - *"Supporting quote"*

- **😤 [Emotion]** when [trigger/context]
  - *"Supporting quote"*

- **😕 [Emotion]** regarding [trigger/context]
  - *"Supporting quote"*

**Dominant Emotion:** [Primary emotional state across interview]

**Emotional Trajectory:** [How emotions evolve during conversation]

---

## SUMMARY & INSIGHTS

**Primary Goal:** [What user is fundamentally trying to accomplish]

**Biggest Pain Point:** [Single most critical challenge with quantified impact]

**AI Opportunity:** [Most impactful AI-powered solution based on pain points and goals]

**Job-to-be-Done:** "When [circumstance], I want to [motivation], so I can [outcome]."

---

## RESEARCH GAPS IDENTIFIED

- ❓ **[Gap category]:** [What wasn't discussed or is underrepresented]
- ❓ **[Gap category]:** [Sparse quadrant or missing dimension]

**Recommendation:** [Suggested follow-up research method - e.g., contextual inquiry, diary study]

---

**Methodology:** Nielsen Norman Group Empathy Mapping
**Confidence:** [High (45+ min interview, rich detail) | Medium (30-45 min, good coverage) | Low (<30 min, sparse data)]
**Next Steps:** [What to do with this empathy map - e.g., cluster with similar users, generate persona, create journey map]
```

## Process Guidelines

### Step 1: Read the Transcript

Use the Read tool to load the interview transcript.

### Step 2: Extract Metadata

Identify from the transcript:
- Participant name and role
- Organization
- Interview date
- Interviewer name

If not found in transcript, use filename or ask user.

### Step 3: Classify Statements into Quadrants

Go through the transcript systematically:

1. **SAYS**: Extract 5-10 verbatim quotes
   - Look for memorable, high-impact statements
   - Include quotes showing pain points, goals, attitudes
   - Preserve exact wording

2. **THINKS**: Infer 5-10 unvoiced thoughts
   - Read between the lines
   - Look for hesitations, qualifications, tone shifts
   - Identify underlying concerns and beliefs

3. **DOES**: Identify 8-15 observable behaviors
   - Focus on concrete actions and workflows
   - Note tools, time allocation, frequency
   - Document current state (not aspirational)

4. **FEELS**: Detect **8-15 emotional states** (never fewer than 8 for a full interview)
   - Find emotion words and intensity markers
   - Write 10-20 word situational descriptions per entry (not single-phrase)
   - Include supporting quotes for ≥30% of entries
   - Map emotions to context/triggers with specificity

### Step 4: Cluster Themes

Within each quadrant, group similar items into 2-4 themes.

### Step 5: Synthesize Insights

Generate summary section:
- Primary goal
- Biggest pain point
- AI opportunity
- JTBD statement

### Step 6: Identify Research Gaps

Check for sparse quadrants (<5 items):
- Flag gaps in YAML frontmatter
- Suggest follow-up research questions

### Step 7: Assess Confidence

Rate confidence based on interview depth:
- **High**: 45+ min, rich detail across all quadrants
- **Medium**: 30-45 min, good coverage but some gaps
- **Low**: <30 min or very sparse content

### Step 8: Generate Markdown

Write the empathy map to the appropriate path:
- Create `[domain]/empathy-maps/` folder if needed
- Use naming convention: `empathy-map-[participant-name].md`
- Include complete YAML frontmatter

## Quality Criteria

Your empathy map must meet these standards:

✅ **Grounded in actual data**: No invented content, only transcript-based insights
✅ **Traceable**: All quotes directly from transcript (verbatim)
✅ **Balanced**: 15-30 total items across all 4 quadrants
✅ **Thematic**: Items grouped into meaningful themes (not random lists)
✅ **Actionable**: Insights inform design decisions and persona creation
✅ **Gap-aware**: Sparse quadrants flagged for follow-up research
✅ **Human-validated**: This is a draft; researcher should review

## Common Mistakes to Avoid

❌ **Don't invent quotes**: SAYS quadrant must be verbatim only
❌ **Don't confuse quadrants**:
   - SAYS = explicit statements
   - THINKS = inferred mental states
   - DOES = observable actions
   - FEELS = emotional states
❌ **Don't create sparse quadrants**: Aim for 4-8 items per quadrant minimum
❌ **Don't skip theme clustering**: Group similar items together
❌ **Don't ignore research gaps**: Flag them explicitly
❌ **Don't skip human validation**: Empathy map is a draft, not final

## Integration with Other Skills

This empathy map can be used as input for:

- **Persona Generator**: Cluster similar empathy maps to identify persona groups
- **JTBD Analyzer**: Cross-reference THINKS quadrant for motivations
- **User Journey**: Validate journey phases align with DOES behaviors
- **Affinity Diagram Synthesizer**: Extract themes across multiple empathy maps

## Example Usage

```bash
# Generate empathy map from single transcript
/empathy-map-generator DI&A/transcripts/henok.txt

# Generate empathy maps for all transcripts in a domain
/empathy-map-generator DI&A/transcripts/*.txt

# Generate empathy map with explicit metadata
/empathy-map-generator CPI/transcripts/CPI-AI-01.txt --participant "Maria Santos" --role "Portfolio Manager"
```

## Validation Checklist

Before saving the empathy map, verify:

- [ ] All 4 quadrants present and populated (5+ items each)
- [ ] SAYS contains only verbatim quotes (no paraphrasing)
- [ ] THINKS captures unvoiced attitudes (not just restatements of SAYS)
- [ ] DOES focuses on observable actions (not inferred motivations)
- [ ] FEELS includes emoji, emotion word, and context for each item
- [ ] Themes identified for each quadrant
- [ ] Summary section synthesizes across all quadrants
- [ ] Research gaps flagged if any quadrant has <5 items
- [ ] YAML frontmatter complete and accurate
- [ ] Confidence rating justified by interview length/depth

---

**Skill Version:** 1.0
**Last Updated:** 2026-03-26
**NN/g Methodology Compliance:** ✅ Full compliance with empathy mapping best practices
