# Literature Survey — researcher_ux Platform Improvement

## Internal Sources (Primary)

### 1. Codebase: 11 Skills Documentation
- **Location:** `.claude/skills/*/SKILL.md`
- **Key Finding:** Core pipeline (empathy→persona→JTBD→AI-opps) is production-grade; scenario-mapper, pain-matrix, task-analysis, mental-model are beta/concept
- **Relevance:** Defines baseline capabilities and gap surface area

### 2. DI&A Project (Most Mature)
- **Location:** `DI&A/`
- **Key Finding:** 9 interviews, 4 personas, complete empathy+journey+JTBD+AI-opps pipeline. clustering-analysis.md is the gold standard for cross-interview synthesis.
- **Relevance:** Best example of what full pipeline output looks like; template for new skills

### 3. CPI Project (Richest Data)
- **Location:** `CPI/`
- **Key Finding:** 10 interviews, 3 personas, 17 AI opportunities, 14 scenario files. Demonstrated pain-intensity ≠ frequency principle (MENA gap: 9.0/10 pain, 30% reach → P0 priority)
- **Relevance:** Test case for confidence propagation (H4) and cross-project synthesis (H5)

### 4. docs/WORKFLOW-GAP-ANALYSIS.md
- **Location:** `docs/WORKFLOW-GAP-ANALYSIS.md`
- **Key Finding:** DI&A validation confirmed workflow works but identified gaps in clustering automation, scenario mapping, Figma visual creation
- **Relevance:** Confirms H1, H6, H7 hypotheses independently

### 5. docs/ai-powered-ux-workflow.md
- **Location:** `docs/ai-powered-ux-workflow.md`
- **Key Finding:** 379-line workflow doc covering all 7 pipeline stages with file naming conventions, parallel execution guidance, quality criteria
- **Relevance:** Baseline for pipeline automation design (H2)

## External Sources (Orchestra Research)

### 6. Orchestra autoresearch SKILL.md
- **URL:** https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/0-autoresearch-skill
- **Key Finding:** Two-loop architecture (inner: rapid experiments, outer: synthesis). Maps directly to UX platform inner/outer loop gap.
- **Relevance:** Framework for this research; architectural inspiration for cross-interview synthesis

### 7. Orchestra brainstorming-research-ideas SKILL.md
- **URL:** https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/21-research-ideation/brainstorming-research-ideas
- **Key Finding:** 10 ideation frameworks including tension hunting, abstraction ladder, cross-pollination, failure analysis
- **Relevance:** Used to generate H1-H7 hypotheses

### 8. Orchestra creative-thinking-for-research SKILL.md
- **URL:** https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/21-research-ideation/creative-thinking-for-research
- **Key Finding:** 8 cognitive frameworks including bisociation, problem reformulation, constraint manipulation, adjacent possible, Janusian thinking
- **Relevance:** Adjacent possible mapping (LLM capabilities enabling H1-H5); Janusian thinking for single/cross-interview tension

## Techniques to Investigate

### sentence-transformers
- **Purpose:** H1 semantic clustering of interview quotes
- **Key capability:** Sub-second embedding of text passages; cosine similarity clustering; works well on short quotes
- **Library:** `pip install sentence-transformers`
- **Model suggestion:** `all-MiniLM-L6-v2` (fast, good quality for clustering) or `all-mpnet-base-v2` (higher quality)

### DSPy
- **Purpose:** H3 prompt optimization using existing outputs as training signal
- **Key capability:** Compile natural-language programs into optimized prompts using few-shot examples and gradient-free optimization
- **Library:** `pip install dspy-ai`
- **Consideration:** Requires defining input/output signatures for each skill; optimization loop needs evaluation metric

### CrewAI / LangGraph
- **Purpose:** H2 multi-agent pipeline automation
- **Key capability:** Define agents with roles (UX researcher, analyst, synthesizer) and orchestrate sequential/parallel execution
- **Library:** `pip install crewai` or `pip install langgraph`
- **Consideration:** Claude Code already has agent-spawning capability; may not need external framework

### Long-context synthesis
- **Purpose:** H5 cross-project meta-analysis
- **Key capability:** Claude Opus 4.7 / Sonnet 4.6 with 200K token context can ingest all 9 project outputs in a single call
- **Design:** No embeddings needed — direct LLM synthesis of structured markdown files
