---
name: ai-opportunity-analyzer
description: Analyze user workflows and JTBD to identify AI/ML product opportunities with feasibility and risk assessment. Use when user wants to find AI automation opportunities, evaluate AI augmentation potential, assess LLM use cases, or prioritize AI features by user needs, business value, and technical feasibility. Accounts for hallucination risk, trust boundaries, explainability needs, and vendor credibility requirements specific to AI products.
---

# AI Opportunity Analyzer

**Version:** 1.0.0
**Category:** Product Strategy & AI/ML
**Complexity:** Advanced
**Prerequisites:** JTBD analysis, user research transcripts or persona documentation

---

## Purpose

Evaluates and prioritizes AI product opportunities using a three-dimensional assessment framework that combines user needs, business value, and technical feasibility. Unlike generic opportunity prioritizers, this skill accounts for AI-specific considerations: LLM capabilities, hallucination risk, trust boundaries, vendor credibility requirements, and explainability needs.

**When to Use:**
- After completing JTBD analysis to identify AI-solvable jobs
- When evaluating which AI features to build first
- To validate AI opportunity hypotheses against user needs + business value + technical feasibility
- When stakeholders ask "should we add AI to this?"
- To avoid "AI for AI's sake" and ensure real user value

**Framework Origin:**
- **User Needs Dimension:** Clayton Christensen JTBD framework + Nielsen Norman Group UX research methods
- **Business Value Dimension:** Lean Startup validated learning + Impact/Effort prioritization
- **Technical Feasibility Dimension:** AI Feasibility Matrix (Industry standard: Technical Feasibility × Business Impact)
- **Trust Considerations:** NN/g GenAI research agenda (2024-2025)

---

## Framework Structure

### Three-Dimensional Assessment Model

```
AI Opportunity Score = f(User Needs, Business Value, Technical Feasibility)

Where each dimension includes AI-specific sub-criteria:

1. USER NEEDS (0-10 points)
   - Pain point severity (from JTBD switching triggers)
   - Frequency of job occurrence
   - Current solution inadequacy
   - User trust threshold for AI in this context
   - Explainability requirements

2. BUSINESS VALUE (0-10 points)
   - Strategic alignment with product vision
   - Competitive differentiation potential
   - Revenue impact (direct or retention)
   - User reach (% of user base affected)
   - Vendor credibility enhancement

3. TECHNICAL FEASIBILITY (0-10 points)
   - LLM capability match (text generation, summarization, extraction, reasoning)
   - Data availability and quality
   - Hallucination risk tolerance
   - Latency constraints
   - Integration complexity
```

### AI Feasibility Matrix (2×2 Grid)

```
High Business Impact ↑
                    │
    PRIORITY 1      │    PRIORITY 2
    Quick Wins      │    Strategic Bets
    ────────────────┼────────────────
    PRIORITY 3      │    PRIORITY 4
    Backlog         │    Avoid
                    │
                    └──────────────→ High Technical Feasibility
```

**Priority 1 (Quick Wins):** High business impact + High technical feasibility → **Build first**
**Priority 2 (Strategic Bets):** High business impact + Lower technical feasibility → **R&D investment required**
**Priority 3 (Backlog):** Lower business impact + High technical feasibility → **Build if capacity allows**
**Priority 4 (Avoid):** Lower business impact + Lower technical feasibility → **Do not build**

---

## Input Requirements

### Required Inputs

1. **JTBD Analysis Files** (from `.claude/skills/jtbd-analyzer/`)
   - Individual user JTBD analyses (`jtbd-analysis-[user].md`)
   - Merged persona-level analyses (`jtbd-analysis-[persona].md`)
   - Cross-persona analysis (`jtbd-cross-persona-analysis.md`)

2. **Product Context**
   - Current product capabilities (what AI can enhance vs. replace)
   - Competitive landscape (what AI solutions exist)
   - Business objectives (revenue targets, strategic goals)

3. **Technical Context**
   - Available LLM capabilities (GPT-4, Claude, domain-specific models)
   - Data infrastructure (structured databases, document repositories)
   - Integration requirements (APIs, user workflows)

### Optional Inputs

- User research transcripts (for deeper pain point analysis)
- Persona documentation (for trust threshold insights)
- Existing feature prioritization matrices
- Stakeholder input on strategic priorities

---

## Output Specification

### Primary Output: AI Opportunity Assessment Report

**File Format:** Markdown (`.md`)
**File Location:** `DI&A/ai-opportunities/ai-opportunity-assessment-[date].md`

**Report Sections:**

#### 1. Executive Summary
- Total opportunities evaluated
- Top 3 Priority 1 (Quick Wins)
- Top 2 Priority 2 (Strategic Bets)
- Key insights and recommendations

#### 2. Opportunity Inventory
For each identified opportunity:

```markdown
## Opportunity [#]: [Descriptive Name]

**JTBD Connection:** [Which job(s) from JTBD analysis this addresses]
**User Quote:** "[Verbatim quote from transcript showing pain point]"

### Three-Dimensional Assessment

#### User Needs Score: [X/10]
- **Pain Severity:** [1-10] - [Explanation with evidence]
- **Frequency:** [1-10] - [Daily/Weekly/Monthly/Quarterly]
- **Current Solution Inadequacy:** [1-10] - [What users "fire" and why]
- **Trust Threshold:** [1-10] - [Can users tolerate AI here? Vendor-backed requirement?]
- **Explainability Need:** [1-10] - [Must AI show reasoning? Regulatory requirement?]

**User Needs Total:** [X/50] → **Normalized: [X/10]**

#### Business Value Score: [X/10]
- **Strategic Alignment:** [1-10] - [How well does this fit product vision?]
- **Competitive Differentiation:** [1-10] - [Defensible moat vs. ChatGPT/Claude?]
- **Revenue Impact:** [1-10] - [Direct revenue, retention, upsell potential]
- **User Reach:** [1-10] - [% of user base affected]
- **Vendor Credibility:** [1-10] - [Does this reinforce "vendor-backed AI" positioning?]

**Business Value Total:** [X/50] → **Normalized: [X/10]**

#### Technical Feasibility Score: [X/10]
- **LLM Capability Match:** [1-10] - [Does LLM excel at this task type?]
- **Data Availability:** [1-10] - [Quality of training/retrieval data]
- **Hallucination Risk:** [1-10] - [10 = low risk, 1 = high risk - inverse score]
- **Latency Tolerance:** [1-10] - [Can users wait seconds/minutes for results?]
- **Integration Complexity:** [1-10] - [10 = simple API, 1 = requires new infrastructure]

**Technical Feasibility Total:** [X/50] → **Normalized: [X/10]**

### Overall Priority

**Combined Score:** [Average of 3 dimensions: X.X/10]
**Feasibility Matrix Position:** [Priority 1/2/3/4]
**Recommendation:** [Build Now / R&D Phase / Backlog / Avoid]

### Implementation Notes
- **Switching Triggers to Leverage:** [From JTBD analysis]
- **Trust Considerations:** [Vendor-backed requirement? Explainability features needed?]
- **Success Metrics:** [How to measure if this solves the job?]
- **Risks:** [What could go wrong? Hallucination scenarios? User trust violations?]
```

#### 3. Prioritization Matrix Visualization

```markdown
## AI Feasibility Matrix

### Priority 1: Quick Wins (Build Now)
1. [Opportunity #X] - Combined Score: X.X/10
2. [Opportunity #Y] - Combined Score: X.X/10
3. [Opportunity #Z] - Combined Score: X.X/10

### Priority 2: Strategic Bets (R&D Investment)
1. [Opportunity #A] - Combined Score: X.X/10
2. [Opportunity #B] - Combined Score: X.X/10

### Priority 3: Backlog (Build If Capacity)
[List]

### Priority 4: Avoid (Do Not Build)
[List with brief rationale for why each fails criteria]
```

#### 4. Cross-Opportunity Insights

- **Vendor Credibility Requirements:** [Which opportunities REQUIRE vendor-backed positioning vs. generic AI?]
- **Data Infrastructure Gaps:** [What data is missing to enable top opportunities?]
- **Trust Boundary Recommendations:** [Where AI should vs. shouldn't be used based on user trust thresholds]
- **Hallucination Risk Mitigation Strategies:** [Common patterns across opportunities]

#### 5. Roadmap Recommendations

- **Phase 1 (0-6 months):** [Priority 1 opportunities with highest scores]
- **Phase 2 (6-12 months):** [Priority 1 remainder + Priority 2 R&D starts]
- **Phase 3 (12-18 months):** [Priority 2 builds + Priority 3 evaluations]

---

## Assessment Criteria Details

### User Needs Dimension (Detailed Rubric)

#### Pain Severity (1-10)
- **9-10:** Users describe pain as "unbearable," "show-stopper," "can't do my job"
- **7-8:** Users describe significant frustration, workarounds required
- **5-6:** Users describe moderate inconvenience, manageable but annoying
- **3-4:** Users describe minor irritation, nice-to-have improvement
- **1-2:** Users barely mention or don't notice the problem

**Evidence Sources:** JTBD switching triggers, emotional job dimensions, verbatim quotes

#### Frequency (1-10)
- **10:** Multiple times per day
- **8-9:** Daily
- **6-7:** Weekly
- **4-5:** Monthly
- **2-3:** Quarterly or less
- **1:** Rarely/annually

**Evidence Sources:** JTBD "Frequency" field

#### Current Solution Inadequacy (1-10)
- **9-10:** No current solution or complete failure of existing tools
- **7-8:** Current solution requires significant manual work or produces poor results
- **5-6:** Current solution partially works but has major gaps
- **3-4:** Current solution mostly works but could be improved
- **1-2:** Current solution is adequate

**Evidence Sources:** Competitive landscape mapping in JTBD analysis, "what are users hiring now?"

#### Trust Threshold (1-10)
- **9-10:** High-trust context - users explicitly want AI here, prefer vendor-backed AI
- **7-8:** Moderate-trust context - users open to AI with explainability
- **5-6:** Neutral context - users need proof of accuracy before trusting
- **3-4:** Low-trust context - users skeptical, need human verification
- **1-2:** No-trust context - users refuse AI in this domain (regulatory, ethical, safety)

**Evidence Sources:** User quotes about vendor credibility, ChatGPT vs. DRG/Clarivate preferences, regulatory context

#### Explainability Need (1-10)
- **9-10:** High explainability - users MUST see reasoning, citations, confidence scores (regulatory/compliance)
- **7-8:** Strong explainability - users want to understand how AI reached conclusions
- **5-6:** Moderate explainability - users want basic transparency ("AI suggested this because...")
- **3-4:** Low explainability - users care more about results than process
- **1-2:** No explainability needed - black box acceptable if results are good

**Evidence Sources:** User quotes about trust, validation needs, regulatory requirements

---

### Business Value Dimension (Detailed Rubric)

#### Strategic Alignment (1-10)
- **9-10:** Core product vision, differentiates entire product category
- **7-8:** Major strategic initiative, aligns with 3-year roadmap
- **5-6:** Supports strategic goals but not central
- **3-4:** Tangential to strategy, nice-to-have
- **1-2:** Misaligned with product vision

**Evidence Sources:** Product strategy documents, leadership priorities

#### Competitive Differentiation (1-10)
- **9-10:** Defensible moat - vendor data/relationships required, can't be replicated by ChatGPT
- **7-8:** Strong differentiation - domain-specific AI that general tools can't match
- **5-6:** Moderate differentiation - better UX or integration than generic AI
- **3-4:** Weak differentiation - similar to what ChatGPT/Claude can do
- **1-2:** No differentiation - commodity AI feature

**Evidence Sources:** Vendor credibility gap insights from JTBD, competitive analysis

#### Revenue Impact (1-10)
- **9-10:** Direct revenue driver (new upsell tier, premium feature) or prevents major churn
- **7-8:** Strong retention impact or conversion rate improvement
- **5-6:** Moderate efficiency gains that reduce costs or improve margins
- **3-4:** Minor cost savings or small retention lift
- **1-2:** No measurable revenue/cost impact

**Evidence Sources:** Business case, customer lifetime value analysis, churn data

#### User Reach (1-10)
- **9-10:** Affects 80-100% of user base
- **7-8:** Affects 50-79% of user base
- **5-6:** Affects 25-49% of user base
- **3-4:** Affects 10-24% of user base
- **1-2:** Affects <10% of user base

**Evidence Sources:** Persona coverage, JTBD confidence scores (how many users mentioned this job?)

#### Vendor Credibility Enhancement (1-10)
- **9-10:** Uniquely positions vendor as AI leader in category, PR/marketing value
- **7-8:** Reinforces "vendor-backed AI" positioning vs. generic tools
- **5-6:** Neutral branding impact
- **3-4:** Slight commoditization risk
- **1-2:** Damages vendor credibility (looks like ChatGPT wrapper)

**Evidence Sources:** User trust threshold data, vendor preference quotes from JTBD

---

### Technical Feasibility Dimension (Detailed Rubric)

#### LLM Capability Match (1-10)
- **9-10:** LLMs excel at this task - text summarization, extraction, generation (proven use cases)
- **7-8:** LLMs are good at this - question answering, document Q&A with retrieval
- **5-6:** LLMs are okay at this - basic reasoning, simple classification
- **3-4:** LLMs struggle with this - complex reasoning, math, multi-step logic
- **1-2:** LLMs fail at this - precise numerical analysis, guaranteed correctness, real-time data

**Evidence Sources:** LLM benchmarks, existing AI product case studies

#### Data Availability (1-10)
- **9-10:** High-quality structured data available, already digitized and curated
- **7-8:** Good data available but needs cleaning/structuring
- **5-6:** Moderate data available but fragmented across systems
- **3-4:** Limited data, requires significant manual curation
- **1-2:** No data available or data is proprietary/inaccessible

**Evidence Sources:** Data infrastructure audit, content libraries, vendor databases

#### Hallucination Risk (Inverse Score: 1-10)
- **9-10:** Low hallucination risk - constrained generation, retrieval-based, verifiable outputs
- **7-8:** Moderate-low risk - structured outputs with citations
- **5-6:** Moderate risk - open-ended generation but non-critical domain
- **3-4:** Moderate-high risk - open-ended generation in critical domain
- **1-2:** High hallucination risk - medical/legal advice, financial projections, safety-critical

**Evidence Sources:** Domain criticality, regulatory requirements, user trust threshold

#### Latency Tolerance (1-10)
- **9-10:** High latency tolerance - users can wait minutes/hours (batch processing, reports)
- **7-8:** Moderate-high tolerance - users can wait 30-60 seconds
- **5-6:** Moderate tolerance - users can wait 10-30 seconds
- **3-4:** Low tolerance - users expect <10 second response
- **1-2:** No tolerance - users expect instant (<1 second) response

**Evidence Sources:** User workflow analysis, current system performance expectations

#### Integration Complexity (1-10)
- **9-10:** Simple API integration, no new infrastructure required
- **7-8:** Moderate integration, use existing auth/data pipelines
- **5-6:** Some new infrastructure needed (vector DB, embedding service)
- **3-4:** Significant new infrastructure (ML ops, model fine-tuning pipelines)
- **1-2:** Requires complete platform overhaul

**Evidence Sources:** Technical architecture review, DevOps capacity

---

## Workflow

### Step 1: Prepare Inputs (10-15 min)
1. Ensure JTBD analysis is complete for target personas
2. Gather product context (current features, competitive landscape)
3. Document technical constraints (available LLMs, data infrastructure)
4. Identify stakeholders for business value input

### Step 2: Extract AI Opportunity Candidates (20-30 min)
Scan JTBD analysis files for AI-solvable jobs:

**AI Opportunity Signals in JTBD:**
- Jobs involving "search," "summarize," "synthesize," "analyze," "extract," "generate"
- Pain points about manual work, time consumption, or repetitive tasks
- Switching triggers mentioning "if AI could..." or "I tried ChatGPT but..."
- Competitive landscape with "manual process" or "no current solution"
- Functional jobs that require text/document processing

**Example from Research:**
```markdown
Job: Complete Rapid Systematic Literature Review Under Deadline Pressure
→ AI Opportunity: "AI-Powered Literature Screening Assistant"

Switching Trigger: "AI can do in one hour... trustworthy and valid"
→ User Needs Score: High pain (9/10), high frequency (8/10), vendor-backed trust required (9/10)
```

Create initial opportunity list with JTBD connections.

### Step 3: Score Each Opportunity (30-45 min per opportunity)

For each opportunity candidate:

1. **User Needs Assessment:**
   - Reference JTBD analysis for pain severity, frequency, current solution
   - Review user quotes for trust threshold and explainability needs
   - Score all 5 sub-criteria (1-10 each)
   - Calculate normalized score (sum/5)

2. **Business Value Assessment:**
   - Consult product strategy for strategic alignment
   - Analyze competitive differentiation (vendor credibility gap insights)
   - Estimate revenue impact (direct, retention, efficiency)
   - Calculate user reach from persona coverage
   - Score vendor credibility enhancement
   - Calculate normalized score (sum/5)

3. **Technical Feasibility Assessment:**
   - Evaluate LLM capability match (is this a proven LLM use case?)
   - Audit data availability and quality
   - Assess hallucination risk (inverse score)
   - Check latency tolerance from user workflows
   - Estimate integration complexity
   - Calculate normalized score (sum/5)

4. **Overall Priority Calculation:**
   - Combined Score = (User Needs + Business Value + Technical Feasibility) / 3
   - Map to Feasibility Matrix:
     - Technical Feasibility ≥7 AND Business Value ≥7 → **Priority 1 (Quick Wins)**
     - Technical Feasibility <7 AND Business Value ≥7 → **Priority 2 (Strategic Bets)**
     - Technical Feasibility ≥7 AND Business Value <7 → **Priority 3 (Backlog)**
     - Technical Feasibility <7 AND Business Value <7 → **Priority 4 (Avoid)**

### Step 4: Document Assessment (20-30 min)
- Write individual opportunity assessments following output specification
- **Include ≥1 verbatim user quote per opportunity** — pull directly from JTBD files or transcripts, not from scenario descriptions. If the scenario file lacks quotes, read the upstream JTBD file for evidence.
- Document switching triggers from JTBD as implementation leverage points
- Note trust considerations and explainability requirements

**Quality gate before saving:** Each opportunity must contain at least one line starting with `>` (blockquote) or a direct verbatim quote in `"..."`. An assessment with no user quotes is incomplete regardless of scoring quality.

### Step 5: Synthesize Cross-Opportunity Insights (30-45 min)
- Group opportunities by priority tier
- Identify common vendor credibility requirements
- Document data infrastructure gaps affecting multiple opportunities
- Create trust boundary recommendations
- Propose phased roadmap

### Step 6: Generate Prioritization Matrix (15-20 min)
- Sort opportunities within each priority tier by combined score
- Visualize in 2×2 AI Feasibility Matrix
- Write executive summary with top 3-5 recommendations

**Total Time Estimate:** 4-6 hours for 5-10 opportunities

---

## Use Cases

### Use Case 1: Feature Prioritization After JTBD Analysis
**Scenario:** Product team completed JTBD analysis for 4 personas (8 users) and identified 15 potential jobs. Need to decide which AI features to build in Q1-Q2.

**Inputs:**
- `jtbd-cross-persona-analysis.md`
- Individual persona JTBD files
- Product roadmap with strategic goals
- Technical audit of LLM capabilities and data availability

**Process:**
1. Extract 8 AI opportunity candidates from top-ranked jobs
2. Score each using three-dimensional framework
3. Generate prioritization matrix
4. Present top 3 Priority 1 opportunities to leadership

**Output:** `ai-opportunity-assessment-q1-2026.md` with roadmap recommendations

### Use Case 2: Validating "AI Feature Request" from Sales
**Scenario:** Sales team requests "AI chat for drug data" after losing deal to competitor. Need to validate if this is real user need or feature checklist.

**Inputs:**
- Sales feedback and competitor demo
- Relevant JTBD analysis (do users have "chat" job or different job?)
- Technical feasibility assessment

**Process:**
1. Create opportunity candidate: "AI Conversational Interface for Drug Data"
2. Score User Needs dimension (is there JTBD evidence? Pain severity? Trust threshold?)
3. Score Business Value (competitive differentiation, revenue impact)
4. Score Technical Feasibility (LLM capability, hallucination risk for drug data)
5. Calculate combined score and priority tier

**Outcome:** If User Needs score is low (<5/10) → Reject as "feature checklist AI"
If combined score ≥7/10 → Validate as real opportunity

**Output:** Single opportunity assessment memo for leadership decision

### Use Case 3: AI R&D Investment Decision
**Scenario:** Engineering proposes investing in fine-tuned domain-specific LLM vs. using GPT-4 API. Need business justification.

**Inputs:**
- Priority 1 and Priority 2 opportunities from previous assessment
- Technical feasibility scores (hallucination risk, LLM capability match)
- Cost comparison (fine-tuning vs. API costs)

**Process:**
1. Identify which Priority 1/2 opportunities would benefit from fine-tuning
2. Recalculate Technical Feasibility scores with fine-tuned model assumptions
3. Estimate how many opportunities move from Priority 2→Priority 1 with better feasibility
4. Calculate ROI: Cost of fine-tuning vs. Business Value unlocked

**Output:** R&D investment justification memo with sensitivity analysis

### Use Case 4: "Should We Add AI?" Decision Framework
**Scenario:** Stakeholder proposes adding AI to existing feature. Need systematic evaluation.

**Inputs:**
- Existing feature usage data
- JTBD analysis for users of that feature
- Proposed AI enhancement description

**Process:**
1. Create opportunity candidate for AI enhancement
2. Score User Needs (is there pain point? Do users want AI here? Trust threshold?)
3. Score Business Value (strategic alignment, differentiation)
4. Score Technical Feasibility (can LLM improve existing feature?)
5. Check if combined score ≥6/10 AND Priority 1 or 2

**Decision Rule:**
- Combined score <6/10 → **Reject** ("AI for AI's sake")
- Combined score ≥6/10 AND Priority 3/4 → **Backlog** (low priority)
- Combined score ≥7/10 AND Priority 1/2 → **Approve** (real value)

**Output:** Go/No-Go decision memo with scoring rationale

---

## Integration with Existing Skills

### JTBD Analyzer → AI Opportunity Analyzer
**Workflow:** Run JTBD Analyzer first, then AI Opportunity Analyzer to prioritize AI-solvable jobs

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
[AI Opportunity Analyzer Skill]
    ↓
ai-opportunity-assessment-[date].md
```

**Key JTBD Fields Used by AI Opportunity Analyzer:**
- **Switching Triggers** → User Needs (pain severity evidence)
- **Frequency** → User Needs (frequency score)
- **Competitive Landscape** → User Needs (current solution inadequacy)
- **User Quotes** → Trust threshold and explainability needs
- **Confidence Level** → User reach (how many users mentioned this job?)

### Persona Generator → AI Opportunity Analyzer
**Workflow:** Persona documentation provides user trust threshold and regulatory context

**Data Flow:**
```
Persona Files
    ↓
Trust threshold insights (vendor-backed AI preference)
Regulatory constraints (explainability requirements)
User sophistication level (AI adoption readiness)
    ↓
[AI Opportunity Analyzer Skill]
    ↓
Trust considerations in opportunity assessments
```

### UX Opportunity Prioritizer → AI Opportunity Analyzer
**Difference:** UX Opportunity Prioritizer uses 2D Impact/Effort matrix. AI Opportunity Analyzer uses 3D User Needs × Business Value × Technical Feasibility with AI-specific criteria.

**When to Use Which:**
- **UX Opportunity Prioritizer:** General product features (non-AI)
- **AI Opportunity Analyzer:** AI-specific features (LLM, ML, generative AI)

---

## Key Insights from Research Foundation

### Vendor Credibility Gap (Critical Success Factor)
**Finding from JTBD Analysis:**
> "I would be more trusting... because it is coming from DRG or Clarivate" (Dr. Sarah Mitchell persona, 2/2 users)

**Implication for AI Opportunity Analyzer:**
- Opportunities requiring vendor-backed positioning score higher on Trust Threshold (8-10/10)
- Generic AI features (similar to ChatGPT) score lower on Competitive Differentiation (3-5/10)
- Vendor data integration is Technical Feasibility prerequisite for high-trust domains

### Trust Boundary Principle
**NN/g Research Insight:**
> "LLMs should be designed as real tools, not fake friends"

**Implication:**
- Trust Threshold scoring must account for domain criticality
- High-stakes domains (medical, legal, financial) require Explainability Need = 9-10/10
- "AI chat" features should be evaluated skeptically unless JTBD evidence supports conversational job

### "Powered by AI" Is Not a Value Proposition
**NN/g Research Insight:**
> Must solve real user problems, not just add AI label

**Implication:**
- User Needs score must be ≥7/10 for any Priority 1/2 opportunity
- Reject opportunities with high Technical Feasibility but low User Needs (Priority 4)
- Sales-driven "AI feature requests" must show JTBD evidence

### AI Feasibility Matrix Sweet Spot
**Industry Framework:**
High Technical Feasibility + High Business Impact = Priority 1 (Quick Wins)

**Implication:**
- LLM capability match and data availability are gates for quick wins
- R&D investment (Priority 2) justified only if Business Value ≥7/10
- Avoid investing in low-impact opportunities even if technically easy

---

## Example Assessment (From Research Data)

### Opportunity #1: AI-Powered Literature Screening Assistant

**JTBD Connection:**
- **Job:** Complete Rapid Systematic Literature Review Under Deadline Pressure
- **Persona:** Dr. Sarah Mitchell (Practical Medical Strategist)
- **Evidence:** 2/2 users (Henok, Simon), Confidence: High
- **User Quote:** "AI can do in one hour what would take weeks... trustworthy and valid" (Henok)

#### User Needs Score: 9.2/10
- **Pain Severity:** 10/10 - "Weeks → hours" time savings, deadline pressure
- **Frequency:** 8/10 - 4-6 times per year (Henok), 6-10 times per year (Simon)
- **Current Solution Inadequacy:** 9/10 - Manual screening of 12,000 articles → 82 selections
- **Trust Threshold:** 9/10 - Explicit preference for vendor-backed AI (DRG/Clarivate)
- **Explainability Need:** 9/10 - Regulatory submissions require audit trail

**User Needs Total:** 45/50 → **9.0/10**

#### Business Value Score: 9.0/10
- **Strategic Alignment:** 10/10 - Core medical evidence use case, aligns with DRG mission
- **Competitive Differentiation:** 9/10 - Vendor data + domain expertise = defensible moat vs. ChatGPT
- **Revenue Impact:** 8/10 - Premium feature tier, prevents churn to AI-native competitors
- **User Reach:** 8/10 - Affects 50% of Dr. Sarah Mitchell persona (2/4 personas total = ~25% of overall base, but 100% of evidence users)
- **Vendor Credibility:** 10/10 - Reinforces "vendor-backed AI" positioning

**Business Value Total:** 45/50 → **9.0/10**

#### Technical Feasibility Score: 8.4/10
- **LLM Capability Match:** 9/10 - Text classification/summarization is proven LLM use case
- **Data Availability:** 9/10 - PubMed/MEDLINE structured data available via APIs
- **Hallucination Risk:** 7/10 - Medium risk (medical domain) but mitigated by retrieval-based approach
- **Latency Tolerance:** 10/10 - Users can wait hours for batch screening (Henok: "one hour")
- **Integration Complexity:** 7/10 - Requires PubMed API integration + vector search infrastructure

**Technical Feasibility Total:** 42/50 → **8.4/10**

#### Overall Priority

**Combined Score:** (9.0 + 9.0 + 8.4) / 3 = **8.8/10**
**Feasibility Matrix Position:** **Priority 1 (Quick Wins)** ✅
**Recommendation:** **Build Now - Q1 2026 roadmap**

**Switching Triggers to Leverage:**
1. "Vendor-backed AI synthesis" - Position as DRG/Clarivate-powered (not generic ChatGPT)
2. "Speed improvement" - Market as 10-100x faster than manual screening
3. "Explainability" - Show transparent reasoning with citation links

**Trust Considerations:**
- MUST include explainability features (citations, confidence scores)
- MUST position as vendor-backed (DRG/Clarivate branding)
- SHOULD provide audit trail for regulatory submissions

**Success Metrics:**
- Screening time: Weeks → Hours (10-100x improvement)
- User trust rating: ≥8/10 for AI-generated selections
- Adoption rate: ≥60% of Dr. Sarah Mitchell persona within 6 months

**Risks:**
- Hallucination risk in medical domain - mitigate with retrieval-based approach + human review
- Regulatory compliance - ensure audit trail meets submission standards
- Vendor data licensing - confirm PubMed/MEDLINE terms allow AI training/inference

---

## Anti-Patterns (What NOT to Do)

### ❌ Anti-Pattern 1: "AI for AI's Sake"
**Description:** Adding AI features because competitors have them, without JTBD evidence

**Example:** "Let's add an AI chatbot because everyone has one"

**Why It Fails:**
- User Needs score <5/10 (no pain point evidence)
- Business Value score <5/10 (no differentiation)
- Results in Priority 4 (Avoid)

**Correct Approach:** Only build AI features with User Needs score ≥7/10 from JTBD analysis

### ❌ Anti-Pattern 2: Ignoring Trust Boundaries
**Description:** Building AI features in high-stakes domains without explainability

**Example:** "AI drug interaction checker" with black box reasoning

**Why It Fails:**
- Trust Threshold score 1-2/10 (users refuse AI without transparency)
- Hallucination Risk score 1-2/10 (safety-critical domain)
- Results in Priority 4 (Avoid) or regulatory failure

**Correct Approach:** Require Explainability Need ≥8/10 for medical/legal/financial domains

### ❌ Anti-Pattern 3: Vendor Credibility Neglect
**Description:** Building generic AI features that look like ChatGPT wrappers

**Example:** "AI summarizer" with no vendor data integration

**Why It Fails:**
- Competitive Differentiation score <5/10 (users will just use ChatGPT)
- Vendor Credibility Enhancement score <3/10 (damages brand)
- Results in Priority 3/4 (Backlog/Avoid)

**Correct Approach:** Integrate vendor data/expertise for Competitive Differentiation ≥7/10

### ❌ Anti-Pattern 4: Technical Feasibility Overconfidence
**Description:** Assuming LLMs can solve problems they're not good at (math, logic, real-time)

**Example:** "AI financial forecasting" with guaranteed accuracy claims

**Why It Fails:**
- LLM Capability Match score <5/10 (LLMs are bad at precise numerical reasoning)
- Hallucination Risk score 1-2/10 (high risk in financial domain)
- Results in Priority 4 (Avoid)

**Correct Approach:** Validate LLM capability match against proven use cases before scoring ≥7/10

### ❌ Anti-Pattern 5: Sales-Driven Feature Checklist
**Description:** Prioritizing AI features because sales team requests them, without user evidence

**Example:** "Customer asked for AI chat in demo, we need to build it"

**Why It Fails:**
- User Needs score unknown (no JTBD analysis)
- May be feature checklist item, not real pain point
- Risk of Priority 4 (Avoid) after assessment

**Correct Approach:** Run AI Opportunity Analyzer assessment on sales requests to validate User Needs score

---

## FAQ

### Q: Should I score opportunities individually or as a team?
**A:** Hybrid approach recommended:
1. **Individual scoring first:** Product manager scores all dimensions with evidence
2. **Team calibration session:** Review top 5-10 opportunities with stakeholders (PM, Eng, Design)
3. **Consensus scoring:** Adjust scores based on team input, document disagreements

**Benefit:** Reduces bias, builds shared understanding of prioritization rationale

### Q: How do I handle opportunities with conflicting dimension scores?
**A:** Use Feasibility Matrix positioning as tiebreaker:

**Example:**
- Opportunity A: User Needs 9/10, Business Value 6/10, Technical Feasibility 8/10 → Combined 7.7/10, Priority 3 (Backlog)
- Opportunity B: User Needs 7/10, Business Value 9/10, Technical Feasibility 7/10 → Combined 7.7/10, Priority 1 (Quick Wins)

**Decision:** Build Opportunity B first (Priority 1 > Priority 3) even though combined scores are equal.

**Rationale:** Business Value + Technical Feasibility determine build order; User Needs ensures we're not building "AI for AI's sake"

### Q: How often should I re-run AI Opportunity Analyzer?
**A:** Quarterly or when major context changes:

**Re-assessment Triggers:**
- New JTBD analysis completed (new user research)
- LLM capabilities change (GPT-5 released, new models available)
- Competitive landscape shifts (competitor launches AI feature)
- Business strategy pivots (new revenue goals, market focus)
- Data infrastructure changes (new vendor partnerships, data access)

**Between Re-assessments:** Update individual opportunity scores if new evidence emerges (user feedback, technical spike results)

### Q: What if I don't have complete JTBD analysis yet?
**A:** Use lightweight scoring with caveats:

**Minimum Inputs:**
- User interviews or support tickets (for pain point evidence)
- Product usage data (for frequency estimates)
- Competitive analysis (for current solution inadequacy)

**Process:**
1. Score opportunities with available data
2. Flag low-confidence scores (e.g., "User Needs: ~7/10 - estimate, needs JTBD validation")
3. Prioritize JTBD analysis for top 3-5 opportunities before building

**Risk:** May mis-prioritize without solid JTBD evidence. Recommend running JTBD Analyzer skill first.

### Q: How do I handle "innovator's dilemma" opportunities?
**A:** Separate assessment track for Strategic Bets (Priority 2)

**Scenario:** Low current User Needs (users don't know they want it) but high future Business Value

**Approach:**
1. Score User Needs based on latent pain (proxy indicators, analogous user problems)
2. Boost Business Value score for strategic/disruptive potential
3. Accept Priority 2 positioning (R&D investment required)
4. Set validation milestones (prototype → user testing → re-score User Needs)

**Example:** "AI-Powered Hypothesis Generation" - users may not ask for it, but could transform research workflows

**Decision Framework:** Limit Priority 2 investments to 20-30% of AI roadmap; focus 70-80% on validated Priority 1 (Quick Wins)

### Q: Can I use this framework for non-AI product features?
**A:** Partially, but prefer UX Opportunity Prioritizer for non-AI

**Adaptations Needed:**
- Remove AI-specific criteria (LLM capability, hallucination risk, vendor credibility for AI)
- Simplify Technical Feasibility to standard "Effort" scoring (engineering time, complexity)
- Keep User Needs and Business Value dimensions (universal)

**Recommendation:** Use AI Opportunity Analyzer ONLY for AI/ML features. Use UX Opportunity Prioritizer (Impact/Effort) for traditional features.

---

## Changelog

**v1.0.0 (2026-03-26)**
- Initial release
- Three-dimensional assessment framework (User Needs × Business Value × Technical Feasibility)
- AI Feasibility Matrix (2×2 priority grid)
- Integration with JTBD Analyzer skill
- Detailed scoring rubrics for all 15 sub-criteria
- Example assessment from real research data (Literature Screening Assistant)
- Anti-patterns and FAQ sections

---

## References

### Academic & Industry Frameworks
- **Christensen, C.** (2005). *The Innovator's Solution: Creating and Sustaining Successful Growth.* Harvard Business Review Press.
- **Moesta, B.** (2020). *Demand-Side Sales 101: Stop Selling and Help Your Customers Make Progress.* Lioncrest Publishing.
- **AI Feasibility Matrix:** Industry standard framework for AI opportunity assessment (Technical Feasibility × Business Impact)

### Nielsen Norman Group (NN/g) Research
- **NN/g GenAI Research Agenda (2024-2025):**
  - Building usable interfaces for generative AI systems
  - Enhancing existing UX methods with AI
  - Trust and design considerations
- **NN/g Core Principle:** "Powered by AI" is not a value proposition - must solve real user problems
- **NN/g Design Pattern:** LLMs as "real tools, not fake friends"

### Project-Specific Research
- **JTBD Cross-Persona Analysis:** `/DI&A/jtbd/jtbd-cross-persona-analysis.md`
- **Vendor Credibility Gap Finding:** Dr. Sarah Mitchell persona JTBD analysis (2/2 users prefer vendor-backed AI)
- **Literature Screening Use Case:** Henok + Simon transcripts (systematic review pain points)

---

## Support & Feedback

**Skill Author:** Claude Code + User Research Team
**Skill Location:** `.claude/skills/ai-opportunity-analyzer/`
**Related Skills:**
- `.claude/skills/jtbd-analyzer/` (prerequisite)
- `.claude/skills/persona-generator/` (provides trust context)

**Questions or Improvements:** Document learnings in `docs/proposed-skills.md` or create skill variants for specific domains (e.g., `ai-opportunity-analyzer-healthcare.md` for medical-specific criteria)
