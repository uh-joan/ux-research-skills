# H4 Analysis: Confidence Propagation Results

**Status:** COMPLETED — DISCONFIRMATORY (prediction wrong, but reveals deeper insight)
**Date:** 2026-04-27
**Dataset:** CPI (10 interviews, 17 AI opportunities)

---

## Results vs. Prediction

| Criterion | Predicted | Actual | Verdict |
|-----------|-----------|--------|---------|
| P1 reclassification rate | 25-35% | 43% | ⚠️ Exceeded (correct direction, wrong magnitude) |
| Reclassified opps defensible | Low-confidence | Mixed | ❌ Critical false demotion found |
| Skill update warranted | Yes (simple weight) | Conditional | ⚠️ Needs design rework first |

**Verdict:** DISCONFIRMATORY — blind confidence weighting causes a critical false demotion.

---

## Critical Finding: Confidence Weighting Breaks MENA/Brazil Priority

**The formula demoted MENA/Brazil Regional Coverage Expander from P0 to P4.**

This is WRONG. Here's why:
- **Original score:** 8.8 (highest in entire study)
- **Source coverage:** 3/10 users (30%)
- **Confidence factor:** 0.6
- **Adjusted score:** 5.28 (P4)

But the CPI empathy analysis explicitly established the "Pain Intensity ≠ Frequency" principle:
> "High pain intensity with low frequency can justify P0 investment when customer retention is at stake."

The 3 MENA users described pain at **9.0/10 intensity with explicit churn threats**. Blind frequency discounting eliminates exactly the kind of high-value, high-stakes signal the platform discovered through empathy analysis.

**This is a design flaw in the formula, not a scoring accident.**

---

## What the Formula Gets RIGHT

Confidence weighting correctly demotes:
1. **Jurisdiction-Specific Patent Status Tracker** (3/10 users, 7.7 → 4.62): Only 3 users mentioned this, none with high emotional intensity. Correctly de-prioritized.
2. **KOL/Expert Network Mapper** (2/10 users, 5.5 → 2.20): Very low coverage, no pain signal.
3. **Biosimilar Comparability Package Generator** (4/10 users, 7.5 → 6.00): Legitimate demotion to P2.

It also correctly confirms:
- Patent Litigation Timeline Predictor (8/10 users): Stays P1 ✓
- Multi-Source Data Verification (10/10 users): Stays P1 ✓
- Multi-Parameter Candidate Screening (5/10 users): Stays P1 ✓

---

## The Real Design: Pain-Modulated Confidence

The hypothesis was wrong not in direction but in mechanism. The correct design is:

```
confidence_factor = max(pain_floor, (n_interviews / total) / 0.5)

Where pain_floor:
  - pain_intensity ≥ 8.0:  pain_floor = 0.9  (almost no penalty even for 1/10 users)
  - pain_intensity 6.0-7.9: pain_floor = 0.6  (mild penalty)
  - pain_intensity < 6.0:   pain_floor = 0.3  (standard penalty)
```

Under this formula:
- **MENA/Brazil** (pain 9.0/10, 3/10 users): pain_floor = 0.9, adjusted = 8.8 × 0.9 = 7.92 → P1 ✓
- **Jurisdiction Tracker** (pain ~5/10, 3/10 users): pain_floor = 0.3, adjusted = 7.7 × 0.6 = 4.62 → P4 ✓
- **KOL Mapper** (pain ~3/10, 2/10 users): pain_floor = 0.3, adjusted = 5.5 × 0.4 = 2.20 → P4 ✓

This preserves critical high-stakes signals while discounting low-pain, low-coverage items.

---

## Implication for ai-opportunity-analyzer SKILL.md

**DO implement:** Pain-modulated confidence weighting when pain intensity data is available.
**DON'T implement:** Blind frequency-only confidence weighting (it destroys critical signals).

Revised skill update:
```
Confidence Weighting Rule:
  IF pain_intensity ≥ 8.0: apply no confidence penalty (protect critical pain signals)
  IF pain_intensity 6.0-7.9: confidence_factor = max(0.6, n_users/total/0.5)
  IF pain_intensity < 6.0: confidence_factor = max(0.3, n_users/total/0.5)
  
Document explicitly in SKILL.md:
  "High-intensity pain (≥8/10) from even 1-2 users can justify P1 priority
   when it represents a customer retention emergency or catastrophic workflow failure."
```

---

## Key Insight (EXPLORATORY)

**The interaction between pain intensity and source confidence is the real design problem.**
The current scoring formula already handles this partially via empathy-driven re-scoring.
The missing piece is: formalize when to apply the frequency discount and when to protect against it.

This is **not a bug in the current skill** — the CPI empathy re-scoring paper already applied the correct judgment intuitively. The contribution of H4 is to make that judgment **explicit and algorithmic**.

---

## What This Rules Out

- ~~"Blind confidence weighting is a safe improvement"~~ — Ruled out. Can demote critical signals.
- ~~"Source count alone determines reliability"~~ — Ruled out. Pain intensity modulates the penalty.

---

## What This Suggests

- **H4b (follow-up):** Implement pain-modulated confidence in ai-opportunity-analyzer SKILL.md and validate on DI&A's 21-interview dataset where we have better ground truth.
- **Update findings.md:** Add this interaction as a key platform-level insight.
- **New guidance in ai-opportunity-analyzer:** Add explicit section on "When to apply confidence discounting."
