# Logic Audit

The method for finding logic problems in a deck or an architecture, used in Phase 5 and as the core of AUDIT mode. It checks six things: argument validity, causal reasoning, transitions, redundancy, contradictions, and missing links. It also covers concept confusion and over-claiming.

## 1. The passes

Run these in order. Each pass looks at a different level, so a problem hidden in one is visible in another.

| Pass | Look at | Question |
|---|---|---|
| **1. Headline read** | Headlines only, in order | Do they tell the story as a paragraph, with no jumps? |
| **2. Slide check** | Each slide's claim and its evidence | Does the evidence prove this claim, no more and no less? |
| **3. Cross-slide** | Pairs and clusters | Redundancy? Contradiction? Terms used consistently? |
| **4. Whole argument** | Thesis, tree, sections | Does the thesis answer the central question? Do the sections together support it? |
| **5. Audience** | The stated audience | What would they ask that the deck does not answer? |

## 2. Argument validity

Does the conclusion follow from the premises?

- **Deductive**: if the premises are true, must the conclusion be true? Check each step.
- **Inductive**: are the cases enough, representative, and of the same kind?

Fallacies that appear often in decks:

| Fallacy | In a deck |
|---|---|
| Hasty generalization | A small pilot stated as a general finding |
| Post hoc | "We changed X, then Y improved, so X worked", with no control |
| False dichotomy | Only two options shown when others exist |
| Circularity | The headline restated as its own evidence |
| Cherry-picking | Only favourable cases or windows shown |
| Survivorship bias | Only successes analysed |
| Scope shift | The claim is about X, the evidence is about a related Y |
| Equivocation | A term changes meaning mid-argument |
| Appeal to authority or popularity | "Industry standard" or "everyone does this" in place of evidence |
| Base-rate neglect | A big percentage on a tiny base |

## 3. Causal reasoning

Check every "because", "therefore", "led to", "drives", "enables", "causes".

- **Direction**: could the effect be causing the "cause"?
- **Confounders**: what else changed at the same time?
- **Baseline**: compared to what? Without a baseline there is no effect size.
- **Mechanism**: is there a plausible reason, and was it examined?
- **Ordering**: did the cause come before the effect?
- **Sufficiency vs necessity**: does X guarantee Y, or only help?
- **Attribution**: if several factors changed, which one is credited, and why?

A correlation that the deck calls a cause is a Major finding, or Critical if the main thesis rests on it.

## 4. Transitions

For each adjacent pair of slides and sections, name the relation:

*because, therefore, however, for example, in addition, as a result, which raises the question, so we then need*

A transition is **missing** when you cannot name the relation, or when the second slide would make sense in any order. A transition is **wrong** when the stated relation does not hold (a "therefore" that does not follow).

Also check the **agenda versus content**: every promised section is delivered, and nothing important appears unannounced.

## 5. Redundancy

- The same claim in two places, in different words.
- The same evidence shown for two claims (fine if deliberate; flag it if it does no new work).
- A summary slide that restates without adding.
- A slide that removing would change nothing.

Test: for each slide, write what the audience would lack without it. If the answer is "nothing", it is redundant or purposeless.

## 6. Contradictions

- Numbers that differ between slides, or between slide and notes.
- A headline result that a data slide does not show.
- A term defined one way early and used another way later.
- A scope claim in the abstract that the body narrows.
- A requirement that a later design decision ignores.

## 7. Missing links

- A claim with no evidence, or evidence with no claim (an orphan).
- A conclusion that never appears in the body.
- A problem stated but not addressed; a solution with no problem it solves.
- A key term never defined.
- A step skipped between stages.
- A question the audience will ask that has no answer anywhere.

## 8. Concept confusion

- **Same word, two meanings** ("performance" as speed and as user rating).
- **Different words, one meaning** (introduced as if they were two things).
- **Level confusion**: a goal beside a method beside a metric.
- **Construct confusion**: measuring one thing and claiming another (task time as "usability").

## 9. Over-claiming

A conclusion goes beyond its evidence in:
- **Scope** (one device, one place, stated as all);
- **Strength** ("proves" for "is consistent with");
- **Generalization** (eight users, stated as the market);
- **Duration** (a single session, stated as long-term use);
- **Certainty** (no uncertainty or limits shown).

## 10. Severity

| Level | Definition |
|---|---|
| **Critical** | The central thesis, or a decision that depends on it, is unsupported or contradicted |
| **Major** | A supporting argument or the credibility or comprehension of the deck is significantly weakened; the thesis may survive |
| **Minor** | Local issues that do not affect the conclusion |

When in doubt between two levels, apply this test: **if the audience acts on this slide as written, could they reach a wrong or unjustified conclusion?** If yes, it is at least Major.

## 11. Finding format

```
ID: A-01
Severity: Critical | Major | Minor
Location: slide(s) - quote the wording where it matters
Issue type: <from the sections above>
Specific cause: <what exactly is wrong>
Potential impact: <what the audience concludes wrongly, or what the presenter cannot defend>
Suggested fix: <the kind of change, in one or two sentences>
```

## 12. Audience questions

For the stated audience, write the three to five questions most likely to be asked, and mark each **Answered (slide #)** or **Unanswered**. Typical for an expert committee: "What is the baseline?", "What is the sample size?", "What are the limits?", "What did you rule out?", "How does this differ from prior work?"

## 13. Calibration

- Cite the deck. A finding without a location is an opinion.
- Distinguish **unsupported** (no evidence given) from **contradicted** (the deck's own evidence disagrees).
- Distinguish "wrong" from "not shown".
- Do not inflate severity, and do not pad the report. A sound deck gets a short report.
- Include what works.
