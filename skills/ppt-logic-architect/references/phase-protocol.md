# Phase Protocol

Read this after routing. It defines what each phase must produce, when it may end, and how the three modes use the phases.

## 1. Which phases each mode uses

| Phase | CREATE | RESTRUCTURE | AUDIT |
|---|---|---|---|
| 1 Intake & Diagnosis | Inventory raw material | Inventory the existing deck, slide by slide | Inventory the existing deck, slide by slide |
| 2 Thesis & Argument Architecture | Build thesis and tree | Reconstruct the as-is thesis and tree, then propose the target thesis and tree | Reconstruct the **as-is** thesis and tree only (what the deck actually argues) |
| 3 Section Architecture | Design sections | Propose new sections plus an old-to-new section map | Not used. Reconstruct the as-is section flow inside Phase 2 |
| 4 Slide-by-Slide Architecture | Write all cards | Write new cards plus the old-to-new slide mapping | Not used |
| 5 Logic Audit | Audit the design | Audit the proposed structure | **The core phase.** Audit the existing deck |
| 6 Final Architecture Delivery | Five files | Five files plus the mapping | `logic-audit-report.md` only |

AUDIT therefore runs: 1, 2 (as-is), 5, 6. After the report, offer RESTRUCTURE; do not start it unasked.

## 2. The gate

Every phase ends with the gate block defined in `SKILL.md`. Rules:

- One gate per phase; stop after it.
- At most three "Decisions for you", each with a recommended default.
- Mark every unresolved item `[BLOCKING]` (the next phase cannot be done well without it) or `[CAN PROCEED]`.
- If there is no real decision to make, say "No decisions needed - proceeding on the assumptions listed" and still wait for "continue".

### Approval handling

| User says | You do |
|---|---|
| "continue", "ok", "approved" | Record approval, emit `PHASE-STATE`, start the next phase |
| "ok, but change X" | Apply X, show only the changed part, then proceed. If X changes the thesis (Phase 2) or the section order (Phase 3), re-present that phase for confirmation first |
| Answers a question | Apply the answer, show what changed, proceed unless it altered the thesis or section order |
| Says nothing relevant, or asks a side question | Answer the side question; the gate stays open |
| "skip to Phase N" | Check what the skipped phases would have produced, list the assumptions you will use in their place, then proceed |
| "go back to Phase N" | Mark phases after N as **stale**, list what is affected, redo only the affected parts |
| "do phases 2 to 4 in one go" | Produce each phase's output in order, with one combined gate at the end of the last one |

### PHASE-STATE block

Emit this after every approved phase (keep it short):

```
PHASE-STATE
mode: CREATE | RESTRUCTURE | AUDIT
language: <user's language>
audience: <who, what they know, what they decide>
decision/purpose: <what the deck must achieve>
central-question: <one sentence>
thesis: <approved text> (v<n>)
method: <frameworks chosen>
sections: <S1..Sn, approved | pending>
approved-phases: <list>
stale-phases: <list or none>
open-gaps: <G ids>
```

## 3. Phase deliverables and exit criteria

A phase ends only when every item in its checklist is true or explicitly listed as unresolved.

### Phase 1 - Intake & Diagnosis
Produce:
1. **Source register**: every input gets an ID (`S1`, `S2`...), with type and what it contains.
2. **Extracted items**, each classified: Fact, Data, Claim-by-source (an assertion someone made), Assumption, Open question, or Noise (not relevant to any likely argument). Keep source IDs.
3. **Brief**: purpose, desired decision or outcome, audience (knowledge, stakes, likely objections), central question, constraints (time, slide budget, format, language).
4. **Project type** (research, design, technical, business, teaching, portfolio, defense...) and which method path it implies.
5. **Early gaps**: what the material cannot support.

Exit when: purpose, audience and the central question are written down (stated by the user or explicitly assumed), and every source is accounted for.

Ask questions here only if purpose, audience or the decision cannot be inferred. Otherwise write "Assumed: ..." and let the user correct it at the gate.

### Phase 2 - Thesis & Argument Architecture
Produce:
1. **Central thesis**: one sentence, arguable, scoped to the evidence. See thesis tests in `mode-create.md`.
2. **Scope statement**: "We claim..." and "We do not claim...".
3. **Method decision**: frameworks chosen and rejected, with one-line reasons (`references/method-selection.md`).
4. **Logic tree**: thesis, supporting arguments, evidence, each leaf linked to `E#` or to a `G#`.
5. **Likely objections** and where the tree answers them.

Exit when: every branch has evidence or a recorded gap, and the thesis is no stronger than the evidence under it.

### Phase 3 - Section Architecture
Produce:
1. **Sections in order**, each with a level-1 marker (一、二、三、 for a Chinese deck, I. II. III. otherwise), its role in the argument, and a **claim title**, not a topic label (`references/signposting.md`).
2. **Progression table**: for each adjacent pair of sections, the named relation, why the second must follow the first, and the **relay line** the audience will see (the previous answer, then the next question).
3. **Slide and time budget** per section (about 2 to 6 slides each; split a section beyond that).
4. **Narrative frame** if one was chosen (for example SCQA at deck level or section level).
5. **Where the ask or decision lands.**
6. **Draft signpost outline**: markers and claim titles for the sections, with the roadmap that will open the deck.

Exit when: no section lacks a role, a marker and a claim title, no transition is unnamed, and every section boundary has a relay.

### Phase 4 - Slide-by-Slide Architecture
Produce:
1. **All slide cards** with the eleven fields (`templates/slide-by-slide.md`), including the hierarchy address, tracker text, connector chip and the numbered structure of the slide body (`1)`, `a.`) with its announced count.
2. **Headline chain**: the headlines read in order, as a paragraph. It must tell the story on its own.
3. **Path chain table**: every link in presentation order (title, roadmap, section openers, slides, recaps, close) with its relation and why the second must follow. Complete the **signpost outline** from the Phase 3 draft.
4. **Cut list**: material left out, and why.
5. **Appendix list**: backup slides with their purpose and the main slide each one supports.

Exit when: every card is complete, no card lacks a reason for inclusion, every claim has evidence or a gap, every card has a label and a connector, and the path chain table has no blank link.

Present long decks one section at a time if a single message would be unreadable; the gate still comes once, after the last section, unless the user asks otherwise.

### Phase 5 - Logic Audit
Run the passes in `references/logic-audit.md`, including the signposting and path-integrity pass, on the Phase 4 output (or, in AUDIT mode, on the existing deck). Produce the findings with severity, location, cause, impact and fix. Then:
- **Critical** findings: return to the responsible phase and fix there. Do not patch silently in Phase 5.
- **Major** findings: fix, or ask the user to accept the risk explicitly.
- **Minor** findings: fix, or list.

Exit when: no Critical finding is open, or the user has explicitly accepted it as a stated risk.

### Phase 6 - Final Architecture Delivery
1. Confirm the output directory (default `./ppt-architecture/`). Do not overwrite existing files.
2. Fill the templates with the approved content. Keep IDs consistent across files.
3. Give a short summary: thesis, section list, open gaps and accepted risks.
4. Offer the hand-off: the approved `slide-by-slide.md` is the input for a slide-building tool or skill. Do not start that without being asked.

## 4. Skipping and user-supplied input

If the user already has a thesis, an outline or a finished phase, treat it as input to **check**, not to regenerate: restate it, test it against the exit criteria, and list what is missing. Keep the user's wording where it is sound.

## 5. When the material is thin

If the material cannot support a thesis, say so in Phase 1 or 2, show what it can support, and list what would be needed. Do not stretch weak material into a confident-looking deck.
