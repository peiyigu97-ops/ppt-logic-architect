# Visual Hand-off (optional, after Phase 6)

This skill designs the logic. It does not draw. A companion skill, **visual-explainer** (github.com/nicobailon/visual-explainer, MIT), draws figures and builds HTML pages and slide decks. This file says when and how to hand an approved architecture to it without losing the evidence discipline.

Interface verified against visual-explainer **v0.16.0** (its SKILL.md, slides reference, PPTX README and install section were read on 2026-11-26). Nothing here was run end to end. If its commands or figure tags have changed, trust its own documentation over this file and tell the user what differs.

## 1. When this may start

All of these must be true:

1. Phase 6 is delivered and the user has **approved the architecture**. A request to "just make it into slides" before that is a request to skip the gates. Decline in one or two sentences and offer the fastest path to approval.
2. The user **asked** for visuals, a deck, diagrams or a PPTX. Offer it once after Phase 6; never start it unasked.
3. The Phase 5 audit has no open Critical finding, or the user accepted it as a stated risk. A diagram makes a weak claim look stronger. Say so if a Critical finding is open.

## 2. Is visual-explainer available?

Check the skill list you can see for `visual-explainer`. If you cannot tell, ask the user once.

- **Not installed:** say so plainly. Do not describe output as rendered. Offer to write `visual-brief.md` now so nothing is lost, and point to the install steps in this project's `install/` guides. Never fabricate a render.
- **Installed:** continue.

## 3. What to hand off

| Our artifact | Hand to visual-explainer as | Page type |
|---|---|---|
| `logic-tree.md` | A web diagram of the argument tree | One figure-led page |
| `logic-audit-report.md` | A review page: verdict, evidence figures, risks, next steps | One page |
| `evidence-matrix.md` | A table with status chips (claim, evidence, status, confidence, gap) | Section of a page, or an appendix slide |
| `slide-by-slide.md` | A slide deck, one slide per card | HTML deck |
| `master-outline.md` (headline chain, progression) | The agenda and section-divider slides | Part of the deck |

Default offer: the logic-tree page and the slide deck. Ask once which of the five the user wants. Do not hand off all five by default.

Commands, from its documentation: `/generate-web-diagram`, `/generate-slides`, `/compare`. In Claude Code, plugin commands are namespaced as `/visual-explainer:<command>`. In Codex, invoke `$visual-explainer`. Slides: `/generate-slides`; add `--pptx` only if the user needs a PPTX (see section 7).

## 4. Writing the brief

Fill `templates/visual-brief.md` from the approved cards. The brief is the **only content** the drawing step may use.

- Headlines are copied verbatim from the cards. Do not let the drawing step rewrite a claim.
- Each figure slide states its claim in one sentence, so the claim survives a text-only export.
- Every number carries its `E#`, unit, `n` and condition, exactly as in `evidence-matrix.md`.
- Low and None confidence claims, assumptions and gaps are marked so they stay visible in the picture. State should show in form (outline, pattern, label), not only in colour.

## 5. From "Suggested Visual Form" to figures

visual-explainer decides the final figure; these are starting suggestions to put in the brief. Its own figure vocabulary includes `<ve-flow>`, `<ve-bars>`, `<ve-waffle>`, `<ve-stack>`, `.ve-table`, small multiples, steppers and hand-drawn SVG.

| Suggested Visual Form in the card | Suggest in the brief |
|---|---|
| Comparison chart with baseline | Sorted bars, baseline row marked, `n` on the chart |
| Trend over time | Line or sparkline over the stated window |
| Parts of a whole | Stack or waffle, with the whole defined |
| Flow, mechanism, pipeline, process | Box-and-arrow flow with a verb on each arrow; stepper if it moves |
| Criteria or requirements matrix, audit table | Table with status chips |
| Cases, failure modes, options | Small multiples, one mini diagram per case |
| Argument tree | Tree: claim nodes with a confidence chip, evidence leaves with `E#`, gaps as dashed nodes |
| Quotes | Quote cards with participant count and how the quotes were chosen |
| Annotated photo or render | **Placeholder frame plus callout text.** The drawing step does not supply photos; the user adds the image |
| Timeline or plan | Timeline with the gap each step closes |

## 6. Fidelity rules

1. **No new facts.** The drawing step adds no numbers, sources, quotes, claims or labels that are not in the brief. A figure that needs a value the brief lacks shows `[value needed]` or a gap chip, never a plausible number.
2. **Nothing dropped.** Every card appears as a slide, in order. Appendix cards stay in the appendix. A slide may be split for fit; it may not be removed.
3. **Strength of wording is preserved.** "suggests" does not become "shows". A hypothesis stays labelled as one.
4. **Confidence and gaps stay visible.** A Low or None claim must not be drawn with the same visual weight as a High one without a visible cue.
5. **The architecture wins.** If the drawing step wants to change the order or a claim, the change goes back to the user as an architecture edit, not into the deck.

## 7. Honest limits to tell the user

- **PPTX export is best-effort and static.** Per visual-explainer's own documentation, it keeps headings, subtitles, lists, paragraphs, tables and code, and **drops SVG, figures and captions**, plus animation, custom fonts and JavaScript. The diagrams you asked for are the part that does not carry over. The HTML deck is the real output; the PPTX is a text-and-table handoff. Say this before exporting, not after.
- **Neither skill edits an existing `.pptx` in place.** For RESTRUCTURE on a real deck, the old-to-new mapping table in `slide-by-slide.md` is the instruction set for whoever (or whatever tool) edits the file. Do not claim a file was changed unless a tool actually changed it.
- **Never state the result looks right unless it was opened in a browser.** If it was not viewed, say "not viewed".

## 8. Procedure

1. Confirm the three preconditions (section 1). Ask which outputs and whether a PPTX is needed. One question, with a default.
2. Check availability (section 2).
3. Write `visual-brief.md` (section 4), show the user the outline of it, and wait for a go-ahead if the deck is large. For a short deck, proceed.
4. Invoke visual-explainer with the brief as its source material: "Build from `visual-brief.md` only. Add no facts. Copy headlines verbatim."
5. **Verify the output against the brief**, and report the result:
   - slide count and order match the cards;
   - each headline matches its card;
   - extract every number from the generated source and check each appears in the brief (list any that do not);
   - every Low or None claim and every gap is visibly marked;
   - nothing is described as verified that was not.
6. Report what was checked and what was not (for example, "not opened in a browser"). If a check fails, fix by a small edit and re-check; do not regenerate the whole page.

## 9. Pitfalls

- Handing off before approval because the user is in a hurry.
- A beautiful figure that is stronger than its evidence.
- Letting the drawing step "fill in" a metric to make a chart look complete.
- Promising a PPTX with the diagrams in it.
- Treating a rendered page as a validated argument. Rendering changes how the logic looks, not whether it holds.
