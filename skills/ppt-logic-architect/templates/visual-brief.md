# Visual Brief

> Template for the optional hand-off to a drawing skill such as visual-explainer (see `references/visual-handoff.md`). Written only after Phase 6 approval and an explicit request for visuals. The brief is the **only content** the drawing step may use. Do not add facts here that are not in the approved files. Delete guidance lines (starting with `>`) in the final file.

**Project:** <name>   **Source architecture:** `slide-by-slide.md` v<n>, approved <date>
**Language:** <language>   **Audience:** <who>   **Thesis (C0):** <one sentence>

## Instruction to the drawing step

```
Build from this brief only. Add no numbers, sources, quotes, claims or labels that are not in it.
Copy each headline verbatim. Keep every slide, in order. Where a value is missing, show
"[value needed]" or a gap chip, never a plausible number. Show Low and None confidence and gaps
in the picture (outline, pattern or label), not only in colour. Do not describe anything as
verified. Keep each figure slide's claim as a plain sentence in the body text as well.
```

## Outputs requested

| Output | Wanted? | Notes |
|---|---|---|
| Logic-tree page (from `logic-tree.md`) | Yes / No | |
| Audit page (from `logic-audit-report.md`) | Yes / No | |
| Evidence table (from `evidence-matrix.md`) | Yes / No | As a slide or an appendix |
| Slide deck, HTML (from `slide-by-slide.md`) | Yes / No | |
| PPTX export | Yes / No | Best-effort and static: figures, captions and animation are dropped. Confirm the user was told |

## Deck-level

- Headline chain (verbatim, for agenda and dividers): <paragraph from `master-outline.md`>
- Sections in order: <S1 ... Sn> with the relation between each pair
- Confidence legend to draw once and reuse: High / Medium / Low / None, and "gap"
- Slide budget: <n> main + <m> appendix
- Tone or register hint (optional, the drawing step may override): <e.g. editorial, technical>

## Per-slide blocks

> One block per card, including appendix cards. Copy the headline verbatim.

### Slide <N>  |  Section <S#>  |  Card: `slide-by-slide.md` slide <N>

- **Headline (verbatim):** <...>
- **Claim in one sentence (also as body text):** <...>
- **Figure to draw:** <type from the card's Suggested Visual Form, with the elements: boxes, arrows with verbs, axes, rows>
- **Data to show (exact):**
  - <value> <unit> (E#, n=<..>, <condition>)
- **Must not show or infer:** <e.g. "no percentage for the rest-and-walk-only case: G3 open">
- **Caption (the claim the figure proves):** <...>
- **Confidence chip:** High | Medium | Low | None
- **Gap chips to show:** <G# and a short label, or "none">
- **Placeholder needed:** <e.g. "photo to be supplied by the user; callouts: ...", or "none">
- **Transition cue to next slide (optional, small):** <named relation, e.g. "therefore">

> Repeat for every slide.

## Logic-tree page block

- **Nodes:** each claim as a sentence with its confidence chip: C0 at the top, then the supporting arguments, then the evidence leaves (`E#`).
- **Gap nodes:** `G#` drawn dashed, with what would close each.
- **Edges:** labelled with the inference type (deductive or inductive) where the logic tree states it.
- **Caption:** the thesis, verbatim.

## Audit page block

- **Verdict:** <verbatim from the report>
- **Counts:** Critical <n>, Major <n>, Minor <n>
- **Evidence figures:** one per Critical and Major finding, showing the slide location and the claim versus its evidence.
- **Next steps:** <from the report>

## Verification record (fill after the drawing step)

| Check | Result | Note |
|---|---|---|
| Slide count and order match the cards | Pass / Fail | |
| Every headline matches its card | Pass / Fail | |
| Every number in the output appears in this brief | Pass / Fail | list any that do not |
| Low and None claims and gaps are visibly marked | Pass / Fail | |
| Viewed in a browser | Yes / No | If No, say "not viewed" in the report to the user |
