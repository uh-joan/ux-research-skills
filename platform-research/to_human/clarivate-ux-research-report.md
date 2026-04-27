# Clarivate User Research: Cross-Domain Findings & AI Roadmap Implications

**Internal Research Report · UX Research Platform · April 2026**

---

## Executive Summary

An analysis of 104 user interviews across 9 Clarivate product domains reveals a finding with direct implications for the AI roadmap: **user emotional experiences are more similar across Clarivate products than they are different.**

Eleven emotional pain patterns are universal — spanning 5 or more of the 9 products studied. This was invisible when each product team analysed their own research in isolation.

When these universal patterns are used to re-score AI investment priorities, the conclusion is clear: **per-product AI roadmaps systematically undervalue platform-level investments**. Three capabilities keep surfacing independently across every product. Each team is building their own version. They should be building one shared version.

The three capabilities are: **data synthesis and reconciliation**, **trust and retrieval-first AI infrastructure**, and **natural language workflow automation**.

---

## The Research

### What We Analysed

| | |
|---|---|
| **Interviews** | 104 user sessions across 9 product domains |
| **Products** | DI&A, CPI, CDDI, Fusion, PT, MASS, MT360, KAI, OFFX |
| **User types** | Market analysts, portfolio managers, regulatory researchers, competitive intelligence professionals |
| **Method** | Nielsen Norman Group empathy mapping + semantic clustering (automated) |
| **Deliverables** | 400+ research artefacts generated from the same dataset |

### What We Were Looking For

Each product team runs their own user research. Findings stay within the product. This analysis asked a different question: **what do Clarivate users have in common, across all products?**

To answer it, we extracted the emotional content from every empathy map — the specific moments of frustration, anxiety, satisfaction, and ambivalence that users described — and clustered them using semantic embeddings. The algorithm groups entries by meaning, not keyword match.

---

## Finding 1: Eleven Universal Pain Clusters

The analysis identified 14 distinct emotional clusters. **Eleven are universal** — present in 5 or more of the 9 products.

> Universal means: different users, in different products, on different teams, independently described the same emotional experience.

| Cluster | Core experience | Products | n |
|---|---|---|---|
| AI Opportunity-Threat Ambivalence | Excited about AI capabilities, anxious about what it means for their role | 7 of 9 | 162 |
| Manual Correction Burden at Scale | Correcting data errors across 60–80 markets by hand | 8 of 9 | 69 |
| Expert Achievement Satisfaction | The feeling when rigorous work produces a defensible output | 8 of 9 | 72 |
| Methodological Confidence in Triangulation | Trust in their own process when they can cross-reference sources | 8 of 9 | 57 |
| Strategic Isolation & Disruption Anxiety | Anxiety about the CI function being sidelined or replaced | 7 of 9 | 37 |
| Data Fragmentation Fatigue | Manually assembling the same picture from 4–6 disconnected sources | 7 of 9 | 26 |
| Vendor Commercial Friction | Frustrated by pricing and contract constraints, hopeful for partnership | 7 of 9 | 23 |
| Vendor Partnership Dependency | Collaborative but aware that a deprecation decision could break their workflow | 5 of 9 | 22 |
| Constant Urgency Pressure | Organisational culture of "everything is needed yesterday" | 7 of 9 | 20 |
| Tool Navigation Friction | Frustration with lag, slow load times, non-intuitive navigation | 7 of 9 | 17 |
| Process Verification Anxiety | Unease about manual steps in the workflow that could introduce error | 6 of 9 | 15 |

Three clusters are product-specific (Regulatory Complexity, Research Isolation, Domain Expertise Anxiety) and do not appear universally.

### What This Means

The strongest universal clusters — Manual Correction Burden (8 of 9 products, n=69), Data Fragmentation Fatigue (7 of 9 products), and AI Ambivalence (7 of 9 products, n=162) — are not product problems. They are **platform problems that each product is encountering independently.**

Any AI capability that addresses these clusters creates value across the entire portfolio, not just for one product team.

---

## Finding 2: Per-Product AI Roadmaps Undervalue Platform Investments

We took 24 AI opportunities from across 8 products — already prioritised by individual product teams — and re-scored them using the universal cluster findings as weights. Opportunities that address clusters present in 8 of 9 products were weighted higher than opportunities that address clusters in 1–2 products.

**22 of 24 opportunities re-ranked.** The re-ranking revealed a systematic pattern: almost every P1 opportunity that touches a universal cluster (6+ products) deserves P0 consideration at the platform level. But when each team scores independently, without visibility into what the other 8 products are experiencing, they can only see their own P1.

Four opportunities were **demoted** — moved from P1 to P3 — because their underlying pain is product-specific:

- Multi-Parameter Candidate Screening
- Literature Summarisation
- Chemistry-Biology AI Integration
- Evidence Change Alerting

These are real user needs, but they are isolated to specific domains. They should be funded by those product teams, not from shared platform resources.

---

## Finding 3: Three Platform AI Capabilities

When universal clusters are the lens, three capability themes emerge consistently across products. Every team is independently building a version of each one.

---

### Capability 1: Data Synthesis & Reconciliation

**Addresses:** Manual Correction Burden (8 of 9 products) + Data Fragmentation Fatigue (7 of 9 products)

Users across every product described the same experience: manually assembling a coherent picture from data that lives in multiple systems, then correcting errors and inconsistencies by hand across 60–80 market rows, every cycle.

Every product team building an AI feature is independently solving cross-source entity resolution, fuzzy matching, and variance detection. The logic is nearly identical across products. The implementations are separate.

**Platform opportunity:** Shared data synthesis infrastructure with per-product adapters. One entity resolution engine that all AI features call into.

**Suggested MVP:** PT's Fuzzy-Match Entity Resolver, generalised and offered as a shared service.

---

### Capability 2: Trust & Retrieval-First AI Infrastructure

**Addresses:** AI Ambivalence (7 of 9 products, n=162) + Methodological Confidence + Tool Navigation Friction

The #1 AI adoption blocker across every product studied is trust and explainability. Users are not refusing AI — they are excited about it. They are anxious about whether they can defend outputs to stakeholders, whether citations are real, whether the methodology is sound.

Per-product RAG implementations are being built in parallel. Each team is solving source citation, hallucination prevention, and methodology provenance independently.

**Platform opportunity:** A shared retrieval-first AI framework — one that enforces source citation and methodology provenance by default — that all AI features run on top of. Per-product features configure what sources to retrieve from; the trust layer is shared.

**Suggested MVP:** PT's Retrieval-First AI Architecture, adopted as the platform-wide standard for any new AI feature.

---

### Capability 3: Natural Language Workflow Automation

**Addresses:** Constant Urgency Pressure (7 of 9 products) + Tool Navigation Friction + Data Fragmentation Fatigue

Users described workflows that take 60–90 minutes: find the data, assemble it from multiple sources, apply the right filters, format the output. The urgency pressure means this happens repeatedly, under time constraints, with the same friction every time.

Natural language query interfaces — where a user types what they want and receives a synthesised output — reduce these workflows to 5–10 minutes. MASS has prototyped this for one context. The underlying need is identical across 7 of 9 products.

**Platform opportunity:** Generalise MASS's NL Query Interface as a platform capability. Products configure the data sources and output format; the query-to-synthesis layer is shared.

---

## Recommendations

**1. Reorganise the AI roadmap by universal cluster, not by product.**
Products that share the same universal pain should co-invest in a shared capability rather than each building their own. The current per-product structure makes this invisible.

**2. Establish three platform-level AI investments as shared infrastructure:**
- Data Synthesis & Reconciliation (start with PT's Entity Resolver)
- Trust / Retrieval-First AI (start with PT's RAG Architecture)
- NL Workflow Automation (start with MASS's NL Query Interface)

**3. Fund the four demoted items from individual product budgets, not shared resources.** They are real user needs, but product-specific. Platform investment is not the right funding mechanism.

**4. Use AI Ambivalence (n=162, 7 of 9 products) as the design constraint for every AI feature.** Users are not resistant to AI — they want to be able to explain and defend AI-generated outputs. Source citation and methodology provenance are not nice-to-haves; they are the adoption threshold.

---

## Methodology Note

The emotional pain data was extracted from 104 empathy maps generated from interview transcripts using a structured Nielsen Norman Group methodology. Each empathy map captures verbatim quotes, inferred thoughts, observed actions, and emotional states with situational context.

Clustering used `sentence-transformers/all-MiniLM-L6-v2` embeddings, UMAP dimensionality reduction (15 components), and HDBSCAN clustering. This approach reduced noise from 49% (with standard PCA) to 12%, recovering manually-identified themes with high fidelity while surfacing additional patterns not visible in per-product analysis.

The confidence scoring algorithm (H4) uses pain-modulated weighting: high-intensity pain signals (≥8/10) are protected from frequency-based demotion, ensuring that low-frequency but severe user needs are not systematically underweighted.

---

## Appendix: Products Studied

| Product | Interviews | Key User Type |
|---|---|---|
| DI&A | 21 | Drug intelligence & analytics researchers |
| CPI | 16 | Competitive & portfolio intelligence analysts |
| CDDI | 12 | Clinical data & development intelligence |
| Fusion | 21 | Cross-domain intelligence platform users |
| PT | 9 | Patent & technology analysts |
| MASS | 3 | Market access & synthesis users |
| MT360 | 8 | Market tracking analysts |
| KAI | 7 | Knowledge & AI platform users |
| OFFX | 7 | Offshore & FX market researchers |

---

*Research conducted using the researcher\_ux platform — an automated qualitative research synthesis system built on Claude Code. All insights are traceable to source interview transcripts.*
