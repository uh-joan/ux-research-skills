# AI Opportunity Analyzer

**Version:** 1.0.0
**Status:** ✅ Production Ready
**Created:** 2026-03-26

## Quick Start

Evaluates and prioritizes AI product opportunities using a three-dimensional framework:

```
AI Opportunity Score = f(User Needs, Business Value, Technical Feasibility)
```

### When to Use

- After completing JTBD analysis to identify AI-solvable jobs
- When evaluating which AI features to build first
- To validate "should we add AI?" requests from stakeholders
- To avoid "AI for AI's sake" and ensure real user value

### Example Usage

```bash
# Via Claude Code skill
"Analyze AI opportunities from JTBD analysis in DI&A/jtbd/"

# Direct CLI (placeholder)
node index.js --jtbd-dir DI&A/jtbd/ --output DI&A/ai-opportunities/assessment-q1-2026.md
```

## Framework Overview

### Three Dimensions (each scored 0-10)

#### 1. User Needs
- Pain point severity (from JTBD switching triggers)
- Frequency of job occurrence
- Current solution inadequacy
- User trust threshold for AI in this context
- Explainability requirements

#### 2. Business Value
- Strategic alignment with product vision
- Competitive differentiation potential (vendor-backed AI moat)
- Revenue impact (direct, retention, upsell)
- User reach (% of user base affected)
- Vendor credibility enhancement

#### 3. Technical Feasibility
- LLM capability match (text generation, summarization, extraction)
- Data availability and quality
- Hallucination risk tolerance
- Latency constraints
- Integration complexity

### AI Feasibility Matrix (Output)

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

**Priority 1 (Quick Wins):** Build now
**Priority 2 (Strategic Bets):** R&D investment required
**Priority 3 (Backlog):** Build if capacity allows
**Priority 4 (Avoid):** Do not build

## Key Insights from Research

### 1. Vendor Credibility Gap
> "I would be more trusting... because it is coming from DRG or Clarivate"

**Implication:** AI opportunities requiring vendor-backed positioning score higher on trust threshold and competitive differentiation.

### 2. "Powered by AI" Is Not a Value Proposition
**NN/g Principle:** Must solve real user problems

**Implication:** User Needs score must be ≥7/10 for Priority 1/2 opportunities. Reject opportunities with low user needs even if technically easy.

### 3. Trust Boundaries Matter
**NN/g Pattern:** "LLMs should be real tools, not fake friends"

**Implication:** High-stakes domains (medical, legal, financial) require Explainability Need = 9-10/10. Users refuse AI without transparency in critical contexts.

## Example Assessment

**Opportunity:** AI-Powered Literature Screening Assistant

**Scores:**
- User Needs: 9.0/10 (high pain, explicit vendor-backed trust requirement)
- Business Value: 9.0/10 (strategic alignment, defensible moat)
- Technical Feasibility: 8.4/10 (proven LLM use case, good data availability)

**Combined Score:** 8.8/10
**Priority:** 1 (Quick Wins) ✅
**Recommendation:** Build Now - Q1 2026 roadmap

**Evidence:**
- JTBD: "Complete Rapid Systematic Literature Review Under Deadline Pressure"
- Switching Trigger: "AI can do in one hour what would take weeks... trustworthy and valid"
- User Reach: 2/2 users (Dr. Sarah Mitchell persona)

## File Structure

```
.claude/skills/ai-opportunity-analyzer/
├── README.md         ← You are here
├── SKILL.md          ← Complete skill documentation (15,000 words)
└── index.js          ← CLI placeholder for future automation
```

## Integration with Other Skills

### Prerequisites
- **JTBD Analyzer** (`.claude/skills/jtbd-analyzer/`) - Run this first to extract jobs from user research
- **Persona Generator** (`.claude/skills/persona-generator/`) - Provides trust threshold context

### Workflow
```
Interview Transcripts
    ↓
[JTBD Analyzer Skill]
    ↓
jtbd-analysis-*.md files
    ↓
[AI Opportunity Analyzer Skill] ← You are here
    ↓
ai-opportunity-assessment-[date].md
    ↓
Prioritized AI roadmap (Priority 1-4)
```

## Output Format

**Primary Output:** `DI&A/ai-opportunities/ai-opportunity-assessment-[date].md`

**Report Sections:**
1. Executive Summary (top 3-5 recommendations)
2. Opportunity Inventory (detailed assessments with scores)
3. Prioritization Matrix (Priority 1-4 grid)
4. Cross-Opportunity Insights (vendor credibility patterns, data gaps, trust boundaries)
5. Roadmap Recommendations (Phase 1-3 build sequence)

## Anti-Patterns (What NOT to Do)

❌ **"AI for AI's sake"** - Adding AI because competitors have it (User Needs <5/10)
❌ **Ignoring Trust Boundaries** - AI in high-stakes domains without explainability
❌ **Vendor Credibility Neglect** - Generic AI features that look like ChatGPT wrappers
❌ **Technical Feasibility Overconfidence** - Assuming LLMs can solve math/logic/real-time problems
❌ **Sales-Driven Feature Checklist** - Building AI features without JTBD evidence

## Time Estimate

**For 5-10 Opportunities:**
- Prepare inputs: 10-15 min
- Extract candidates: 20-30 min
- Score opportunities: 30-45 min each
- Synthesize insights: 30-45 min
- Generate matrix: 15-20 min

**Total:** 4-6 hours for comprehensive assessment

## Support

**Documentation:** See `SKILL.md` for complete framework details, scoring rubrics, use cases, and FAQ

**Questions:** Document learnings in `docs/proposed-skills.md` or create domain-specific variants (e.g., `ai-opportunity-analyzer-healthcare.md`)

## References

- Christensen, C. (2005). *The Innovator's Solution*
- Moesta, B. (2020). *Demand-Side Sales 101*
- Nielsen Norman Group GenAI Research Agenda (2024-2025)
- AI Feasibility Matrix (Industry standard framework)

---

**Next Steps:**
1. Ensure JTBD Analyzer has been run on all user transcripts
2. Run: `"Analyze AI opportunities from JTBD analysis in DI&A/jtbd/"`
3. Review output in `DI&A/ai-opportunities/` directory
4. Present top Priority 1 opportunities to leadership for roadmap planning
