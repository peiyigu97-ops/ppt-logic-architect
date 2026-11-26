# Slide-by-Slide Architecture

> Template. One card per slide. All eleven fields are required. Hierarchy markers, tracker and connectors follow `references/signposting.md`: level 1 `一、` (or `I.`), level 2 `1`, level 3 `1)`, level 4 `a.`. A bare title or a list of keywords is not a card. Delete guidance lines in the final file.

**Project:** <name>   **Thesis:** <C0>   **Total slides:** <n> main + <m> appendix

## Headline chain

> Headlines in order, read as one paragraph.

<paragraph>

---

## Card format

```
### Slide <N>  |  Section: <S#: name>

**1. Slide Number:** <N>
**2. Section:** <S#: name>
**3. Action-oriented Headline:** <a full-sentence assertion>
**4. Core Message:** <what the audience should take away, 1-2 sentences>
**5. Supporting Evidence:**
- <evidence item, with E# and the data / interpretation distinction>
**6. Reason for Inclusion:** <what this slide proves; what breaks if it is removed>
**7. Logical Relationship with Previous Slide:** <named relation: because / therefore / however / for example / which raises the question> - <one sentence>
**8. Transition to Next Slide:** <why the next slide must follow>
**9. Suggested Visual Form:** <kind of exhibit, e.g. comparison chart with baseline; annotated photo; flow>
**10. Evidence Source / Confidence:** <S#/E#> | <High | Medium | Low | None> | <note on gaps G#>
**11. Hierarchy Label & On-slide Signposts:**
- Address: <一·2 | I·2>   (page <N>)
- Tracker: <一 ... › [二 ...] › 三 ... › 四 ...>   (current section highlighted)
- Connector chip: <because | therefore | however | for example | in addition | as a result | which raises the question | answers>
- Body structure: <announced count, e.g. "三个依据">
  1) <point, a short claim phrase>
     a. <detail: datum, condition or example>
     b. <detail>
  2) <point>
```

> Field guidance
> - **Headline**: passes the disagree test and the proof test. Match the strength of the verb to the evidence ("suggests" vs "shows").
> - **Core message**: the takeaway, not the content description.
> - **Supporting evidence**: specific. Number, source, condition. Mark data vs interpretation. If none exists, write `Missing - G#`.
> - **Reason for inclusion**: if the honest answer is "nothing breaks", the slide is a candidate for cutting or the appendix.
> - **Relationship with previous slide**: a named relation; if you cannot name one, the order or the slide is wrong.
> - **Transition**: why the next slide *must* come next, not "next we look at...".
> - **Visual form**: the exhibit type that best shows the evidence; no layout, no styling.
> - **Confidence**: how well the evidence supports the headline *as worded*.
> - **Hierarchy label and signposts**: the address is the logic position (section marker, then slide number within the section); the page number is the physical position, keep both. The connector chip is the named relation from field 7, shown on the slide; on the first slide of a section the chip reads "answers" and field 7's relation to the previous section is shown in the relay line. The body structure uses `1)` for points and `a.` for details; a series has at least two items; say the count in the headline or lead line and show exactly that many. The first slide of a section also carries the **relay line** (previous answer, then this section's question), and the first slide states the roadmap.
> - **Non-assertion slides** (title, agenda, divider, appendix): still fill every field; Headline may be a label, but Reason and Relationship must be real.

---

## Cards

### Slide 1  |  Section: <S#>

**1. Slide Number:** 1
**2. Section:** <...>
**3. Action-oriented Headline:** <...>
**4. Core Message:** <...>
**5. Supporting Evidence:**
- <...>
**6. Reason for Inclusion:** <...>
**7. Logical Relationship with Previous Slide:** <...>
**8. Transition to Next Slide:** <...>
**9. Suggested Visual Form:** <...>
**10. Evidence Source / Confidence:** <...>
**11. Hierarchy Label & On-slide Signposts:** <address | tracker | connector chip | body structure>

---

> Repeat for every slide.

## Path chain table

> Every link in presentation order: title, roadmap, each section opener, each slide, each recap, the close. No blank cell. "Next, we look at..." is not a relation.

| From (address, page) | To (address, page) | Relation (connector chip) | Why the second must follow | What the audience sees |
|---|---|---|---|---|
| <front matter> | <一·1, p.1> | opens | <...> | <roadmap with section claims> |
| <一·1, p.1> | <一·2, p.2> | because | <...> | <chip + tracker> |
| <一·last> | <二 opener> | therefore | <previous answer creates the next question> | <relay line> |

**Checks (Phase 5):** no blank link; no dead end or orphan; every section boundary has a relay; the first slide of each section answers the section's question; the close returns to the thesis; the signpost outline alone reproduces the argument (listener test).

## Appendix slides

> Same card format. State what question each appendix slide answers and which main slide it backs up.

## RESTRUCTURE mode only: mapping from old to new

| Old # | Old title | Disposition (KEEP / REHEAD / MERGE / SPLIT / MOVE / APPENDIX / REMOVE) | New # (page) | New address | Reason |
|---|---|---|---|---|---|
| 1 | <...> | KEEP | 1 | <一·1> | <...> |

> Every original slide must appear. REMOVE requires a written reason and user approval; if unsure, use APPENDIX.

## Cut list

| Material | Why it is not in the deck |
|---|---|
| <...> | <...> |
