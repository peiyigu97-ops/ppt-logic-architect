# Method Selection

Choose frameworks by **purpose, audience and content type**. Do not apply all of them. Record the choice in Phase 2 as a short **Method decision**.

## 1. Selection table

| Presentation type | Primary | Secondary | Usually not |
|---|---|---|---|
| Decision or approval pitch (business case, funding, go/no-go) | Pyramid (answer first) + Assertion-Evidence | SCQA for the opening if the audience needs a reason to care; MECE for option sets | Chronological story of the work |
| Research or technical report (progress review, lab meeting) | Evidence-Based Reasoning; Question, Method, Results, Interpretation, Limits | Pyramid within the discussion; Assertion-Evidence for results slides | SCQA as the whole-deck frame |
| Thesis or project defense | Evidence-Based Reasoning; contribution-first Pyramid | Design Research chain (if design); anticipated-questions appendix | MECE on non-partitions |
| Design project or case study | Design Research chain (`design-research-reasoning.md`) | Assertion-Evidence; SCQA for the framing slides | Pyramid as a rigid top-down order that hides the process |
| Design portfolio | Curation logic: depth and range of judgement | Design Research chain, per selected project | Showing every project |
| Engineering or technical review | Claim, Evidence, Warrant; requirement-to-verification trace | MECE for failure modes and risk categories; Assertion-Evidence | SCQA unless there is a real complication |
| Status or progress update | Pyramid, summary first | Minimal | SCQA, long narratives |
| Teaching or explanation | Simple-to-complex progression | Assertion-Evidence lightly | MECE, SCQA |
| Keynote or inspirational talk | Narrative arc | Pyramid at section level only | Dense evidence slides |

If the deck is a hybrid (a research update that ends in a funding ask), use the first type for the body and the second for the closing section. Say so.

## 2. Fit tests for each framework

**Pyramid Principle** (`pyramid-principle.md`) fits when the audience wants the answer early and will judge the reasoning. Poor fit when the point is discovery, or when giving the answer first would destroy the purpose of the talk.

**SCQA** (`scqa-framework.md`) fits when the audience needs a shared starting point and a reason to care. Use it only if you can state a **real complication** that follows from the situation. Poor fit when the audience already knows the context and wants results; when there is no tension; when it would be a ritual opener that adds two slides and no logic.

**Assertion-Evidence** (`assertion-evidence.md`) fits almost every deck that makes claims. Relax it only for title, agenda, divider, and appendix slides, and for decks that are narrative rather than argumentative.

**MECE** (`mece-analysis.md`) fits a list that claims to be a complete partition: causes, options, segments, components, risk categories. Poor fit for ideas, needs, and themes that overlap by nature; for chronological sequences; for any list where "exhaustive" has no defined whole. Prefer "logically grouped, with a stated criterion", and say it is not MECE.

**Evidence-Based Reasoning** (`evidence-based-reasoning.md`) applies to every deck that asserts anything. It is the baseline, not an option.

**Design Research chain** (`design-research-reasoning.md`) fits any design, HCI, hardware, product-service, engineering-research, portfolio, or defense deck that moves from investigation to a solution.

## 3. Anti-patterns

- **Template worship**: SCQA slide, then three MECE pillars, then a summary, for every deck.
- **Forced triads**: three supporting points because three feels complete.
- **MECE theatre**: categories that look tidy but overlap or leave out a real case.
- **Pyramid as camouflage**: an answer-first headline over evidence that does not support it.
- **Framework as the story**: the deck explains the framework instead of making the argument.

## 4. Output of this step

Write this in Phase 2:

```
Method decision
- Presentation type: <type>; audience: <who>
- Using: <framework> because <reason>
- Not using: <framework> because <reason>
- Hybrid note: <if any>
```
