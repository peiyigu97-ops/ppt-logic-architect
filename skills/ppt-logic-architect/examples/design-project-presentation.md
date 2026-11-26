# Example 2 - Design Project Presentation (industrial design, jury review)

> **All participants, measurements, and results in this example are fictional.** They exist only to demonstrate the method. Do not cite them.
> This example runs the **Design Research & Engineering Reasoning** chain: finding, insight, requirement, concept, feasibility, prototype, test, iteration, validation. It shows where the chain holds, where a link is only a design judgement, and where the skill narrows a claim.

**Case:** A student presents a final-year project to a jury of two faculty members and one industry partner. The jury's brief (S8) says the jury will judge whether the design is *derived from research* and *validated against its requirements*. The student has observation notes, a survey export, measurement sheets, three concept sketches, two test records, and the jury brief. **Mode: CREATE.** Language: English.

---

## Phase 1 - Intake & Diagnosis

### Source register

| ID | Source | Type | Contents |
|---|---|---|---|
| S1 | `observation_notes.md` | Field notes | 9 home sessions, ages 62-84, reduced grip strength; each opened 3 jars; notes and photos |
| S2 | `survey_export.csv` | Survey | 41 responses, convenience sample from two community centres; self-report |
| S3 | `lid_measurements.xlsx` | Measurements | 27 jars matched to those seen in S1: lid diameter and opening torque |
| S4 | `friction_bench.xlsx` | Bench data | Band-on-glass friction, 6 trials, dry |
| S5 | `concept_sketches.pdf` | Sketches and notes | 3 concepts with the student's own scoring |
| S6 | `proto_test_T1.xlsx` | Bench test | Works-like rig on 12 lid types at 4.6 N·m |
| S7 | `usability_T2.md` | Usability test | 8 participants; protocol with success criterion written before the sessions |
| S8 | `jury_brief.md` | Brief | What the jury will assess |

### Material classified by stage of the chain

| Stage | What exists | Evidence status |
|---|---|---|
| Research question | "Why do people with reduced grip fail to open jars, and what must an aid change?" | Present |
| Method | Home observation (n=9), survey (n=41) | Present; small and convenience samples |
| Findings | E1-E5 below | Present |
| Insights | Student's interpretation, partly written | Partly present |
| Requirements | A spec list with no trace to insights | **Weak link** |
| Concepts | 3 sketches, scored by the student alone | Present; self-scored |
| Feasibility | Capstan calculation, friction data | Present; dry glass only |
| Prototype | Works-like rig (T1); looks-and-feels model (T2) | Present |
| Testing | T1 (12 lid types), T2 (8 participants) | Present; limits below |
| Iteration | Two changes | Present |
| Validation | "Users loved it" in the draft notes | **Opinion, not validation** |

### Evidence items (selected)

| ID | Item | Type | Source |
|---|---|---|---|
| E1 | 6 of 9 participants abandoned at least one of 3 jars within 2 min | Data (observation) | S1 |
| E2 | 8 of 9 voiced fear of dropping or breaking a glass jar | Data (interview remarks, counted) | S1 |
| E3 | 7 of 9 pressed the lid against body or counter, or used the palm, instead of a fingertip pinch | Data (observation) | S1 |
| E4 | 5 of 9 owned an opening aid; 4 of the 5 kept it unused in a drawer (reasons: setup effort 3, lid fit 2) | Data | S1 |
| E5 | 29 of 41 (71%) ranked jar opening in their top three kitchen difficulties | Data (self-report, convenience sample) | S2 |
| E6 | 27 jars: lid diameter 43-89 mm; opening torque 1.1-4.6 N·m, median 2.4 | Data | S3 |
| E7 | Friction coefficient of band on dry glass 0.45-0.60 (6 trials) | Data | S4 |
| E8 | Capstan ratio e^(mu*pi) = 4.1 to 6.6 for those mu values | Derived (calculation) | E7 |
| E9 | Concept scoring against R1-R3: A fails R2; B fails R3; C meets all three | Opinion (student's own scoring) | S5 |
| E10 | T1: 11 of 12 lid types held at 4.6 N·m; 1 slipped (89 mm lid with residue); after a grippier band, 1 retest held | Data | S6 |
| E11 | T2: 7 of 8 opened a hard jar (lid torque >= 3.5 N·m) unaided within 60 s with the prototype, vs 2 of 8 with their usual method; the criterion written beforehand was >= 6 of 8 | Data | S7 |
| E12 | T2: 6 of 8 rated palm force "comfortable"; the 2 participants with the largest hands rated it low (handle too small) | Data (self-report) | S7 |
| E13 | T2: 5 of 8 participants had been in S1 sessions; single session; dry jars only; timed by the team | Fact (limits) | S7 |
| E14 | T2 video: 8 of 8 began turning after a single placement action (coded by the student alone) | Data (single coder) | S7 |
| E15 | Jury assesses research-to-design derivation and validation against requirements | Fact | S8 |
| A1 | Palm force of 25 N or less is comfortable | **Assumption** (no measurement) | student |

### Brief

| Item | Content |
|---|---|
| Purpose | Convince the jury the design is derived from research and validated, with limits stated |
| Audience | 2 faculty, 1 industry partner; will probe the research-to-design link and the test |
| Central question | Does the final design solve the jar-opening problem we found, and how well do we know it? |
| Type | Design project / jury review (industrial design) |
| Constraints | 20 minutes; about 12 main slides |

### Gate

```
### Phase 1 - Intake & Diagnosis: Result
Goal of this phase: Inventory the material, classify it by stage of the research-to-design chain, fix the brief.
Result: 8 sources; 15 evidence items; 1 assumption (A1); chain stages mapped.
Unresolved:
- [BLOCKING for Phase 2] Requirements are not traced to insights; I will derive the trace from E3-E6 and mark what cannot be traced.
- [CAN PROCEED] "Users loved it" has no data; it will not be used as evidence.
- [CAN PROCEED] Concepts were scored only by the author.
Decisions for you:
1. Should the deck open with the final claim (jury-friendly) or follow the process order? (Recommended: open with the claim, then follow the process.)
2. Do you have palm-force measurements for T2 that are not in S7? (If not, the force requirement stays an assumption.)
Next: Phase 2 - Thesis & Argument Architecture.
```

*(The user replies: "open with the claim; no force data".)*

---

## Phase 2 - Thesis & Argument Architecture

### Thesis tests

The student's draft: *"The Palm Lever solves jar opening for people with reduced grip strength."* It fails:
- **Evidence match:** the palm-force requirement is unmeasured (A1); wet or oily jars are untested; eight participants is a pilot.
- **Verb strength:** "solves" is stronger than a single-session test of eight allows.

### Central thesis (v2, narrowed)

> A handheld palm-lever opener with a self-tightening band lets people with reduced grip strength open hard jars one-handed with no setup step: in an eight-person test, 7 opened a hard jar unaided within 60 s against 2 using their usual method. Required palm force and wet-jar performance are not yet verified.

**We claim:** the design meets three research-derived requirements (one-handed palm operation, no setup step, lid range 40-90 mm) in the conditions tested.
**We do not claim:** that it solves the problem in general; that the palm-force target is met; performance on wet or oily jars; long-term use; the egg-shaped handle form as a research result.

### Method decision

- Type: design project / jury; audience probes the research-to-design link.
- Using: **Design Research chain** as the backbone (the jury's brief E15 asks exactly for it); **Assertion-Evidence** for slides; **Evidence-Based Reasoning** for labelling findings, inferences, and assumptions.
- Using lightly: **Pyramid** at deck level only (the claim is stated first, but the process order is kept, because the derivation is the argument).
- Not using: **SCQA** (the audience wants the derivation, not a story setup); **MECE** (the requirement list is a derived set, not a partition of a whole; the concept comparison is a scored comparison, not MECE).

### Logic tree

```
C0  A handheld palm-lever band opener meets R1-R3 in tests with eight people; R4 and wet jars unverified   [Medium]
|   Grouping: follows the design research chain; not MECE
|
+-- C1  Need: users with weak grip fail jars, and existing aids are abandoned          [Medium]
|     +-- E1, E2, E4 (n=9)   E5 (n=41, self-report)            (G8: convenience, self-report)
|
+-- C2  Insight: the difficulty is holding and turning at once with one weak hand;
|       aids fail on setup and fit, not on lack of torque                                 [Medium]
|     +-- E3 (7 of 9 used palm or body); E4 (reasons)         (G1: single coder; interpretation)
|
+-- C3  Requirements R1-R4 follow from the insights and measurements
|     +-- R1 one-handed palm operation   <- E3 (C2)
|     +-- R2 no setup step (one placement action before turning) <- E4 (C2)
|     +-- R3 lids 40-90 mm               <- E6 (43-89 mm)
|     +-- R4 palm force <= 25 N          <- A1 (assumption)                             [R4: None]
|
+-- C4  Design choice: the band opener is the only concept meeting R1-R3                [Low]
|     +-- E9 (self-scored)                                     (G5)
|     +-- Feasibility: E7, E8 (capstan 4.1-6.6x on dry glass)  (G3: dry only)           [Medium]
|     +-- Form: egg-shaped palm handle = design judgement, supported only by E3        (G6)
|
+-- C5  Tests: bench held 11 of 12 lid types; users 7 of 8 vs 2 of 8                    [Medium]
|     +-- E10 (G7: one retest); E11, E14 (G4: 5 of 8 returning, single session)
|
+-- C6  Validation: R1-R3 met on current evidence; R4 unverified                        [Medium]
      +-- E11, E12, E14, E6, E10                               (G2: R4 not measured)
```

### Gap register

| ID | Gap | To close |
|---|---|---|
| G1 | Insight coded by the author alone | Second coder on the observation notes |
| G2 | R4 (<= 25 N) is an assumption; only subjective comfort was recorded | Force-sensor test with new participants |
| G3 | Friction and feasibility data are for dry lids only | Test wet and oily lids |
| G4 | T2: 5 of 8 returning, single session, timed by the team | Independent group; longer-term use |
| G5 | Concepts scored by the author alone | Score with an external reviewer |
| G6 | Egg-shaped handle form is a design judgement | Label it as such; test form alternatives if claimed as research-driven |
| G7 | Grippier band retested on 1 lid only | Re-run T1 on all 12 lid types with the new band |
| G8 | Survey is a convenience sample and self-report | Limit E5 to "a common difficulty in this sample" |

### Gate (summary)

```
### Phase 2 - Thesis & Argument Architecture: Result
Goal: Fix the thesis, its scope, and the evidence under each link of the chain.
Result: Thesis v2 (narrowed from "solves"); tree with 6 branches; R4 recorded as an assumption; 8 gaps.
Unresolved: [CAN PROCEED] G1-G8. G7 is the cheapest to close (re-run T1 with the new band).
Decisions for you:
1. Accept the narrowed thesis? (Recommended: yes.)
2. Keep R4 as a stated assumption, or drop it? (Recommended: keep; the jury will see the honesty, and it points to next steps.)
Next: Phase 3 - Section Architecture.
```

---

## Phase 3 - Section Architecture

**Ordering principle:** the design process order, with the claim stated first. The jury's question is "how do we get from research to this form?", so the chain order is the argument.

| # | Section | Role | Section claim | Slides |
|---|---|---|---|---|
| S1 | Research to requirements | Establish the need and derive what the design must do | The requirements come from observation and measurement, one of them an assumption | 1-4 |
| S2 | Concept and feasibility | Show why this design, and that it can work | Only one concept met R1-R3, and the mechanism is physically plausible | 5-6 |
| S3 | Build and test | Test the mechanism and the use | The mechanism held in 11 of 12 lid types and users succeeded 7 of 8 | 7-9 |
| S4 | Validation and limits | Check the solution against the requirements and state what remains | R1-R3 met, R4 and wet jars not yet verified | 10-12 |

| From | To | Relation | Why the second must follow |
|---|---|---|---|
| S1 | S2 | Therefore | Requirements are the yardstick for choosing a concept |
| S2 | S3 | Which raises the question | Feasibility on paper invites "does it work in hands?" |
| S3 | S4 | So what | Test results mean nothing until compared with the original requirements |

**Level-1 markers and section claims** (Roman numerals, because the deck is in English; a Chinese deck uses 一、二、三、). The internal ids S1-S4 used in the cards map to the markers I-IV in order; the markers are what the audience sees:

| Marker | Section claim (the title shown on the slides) | Slides (pages) |
|---|---|---|
| I. | The requirements come from observation and measurement, and one of them is an assumption | 1-4 |
| II. | Only one concept meets R1-R3, and its mechanism is physically plausible | 5-6 |
| III. | The mechanism held in 11 of 12 lid types, and users succeeded 7 of 8 | 7-9 |
| IV. | R1-R3 are met on current evidence; R4 and wet jars are not yet verified | 10-12 |

**Relay lines** (shown on the first slide of each section: the previous answer, then this section's question):

- II, relation *therefore*: "I derived four requirements. II asks: which design meets them, and can it work?"
- III, relation *which raises the question*: "II chose a concept and showed it is plausible on paper. III asks: does it work in hands?"
- IV, relation *so what*: "III tested the mechanism and the use. IV asks: against the original requirements, what is verified?"

**Roadmap:** I Research to requirements > II Concept and feasibility > III Build and test > IV Validation and limits. Because the deck has 12 main slides, section openers are the first content slide of each section, not separate divider slides (`references/signposting.md`).

---

## Phase 4 - Slide-by-Slide Architecture

### Headline chain

> A handheld palm-lever opener lets people with weak grip open hard jars one-handed, and here is the evidence and where it stops. Six of nine older participants gave up on a jar within two minutes, and eight feared dropping it. The difficulty is holding the jar and turning the lid at once with one weak hand, and existing aids fail on setup and fit. Four requirements follow, three traced to evidence and one, palm force, an assumption. Of three concepts, only the handheld band opener meets R1 to R3. A capstan calculation and friction tests indicate the band can hold lids up to 89 mm on dry glass. The works-like rig held 11 of 12 lid types at the highest measured torque. Seven of eight participants opened a hard jar unaided within 60 seconds, against two of eight with their usual method. Two test results changed the design. The final design meets R1 to R3 on current evidence, while R4 and wet jars are unverified. The evidence comes from eight participants, five returning, on dry jars in one session. Next, verify palm force and wet-jar performance with new participants before any production claim.

### Signpost outline

> Markers, titles and connector chips only. Listener test: reading just this reproduces the argument.

```text
I. The requirements come from observation and measurement, and one of them is an assumption
   1 A handheld palm-lever opener lets people with weak grip open hard jars one-handed, and here is the evidence and where it stops   [opens]
   2 Six of nine older participants gave up on a jar within two minutes, and eight feared dropping it   [because]
   3 The core difficulty is holding the jar and turning the lid at once with one weak hand, and existing aids fail on setup and fit   [therefore]
   4 Four requirements follow from the research; three are traced to evidence and one, palm force, is an assumption   [therefore]
II. Only one concept meets R1-R3, and its mechanism is physically plausible
   1 Of three concepts, only the handheld band opener meets all of R1-R3   [answers]
   2 A capstan calculation and bench friction tests indicate the band can hold lids up to 89 mm on dry glass   [which raises the question]
III. The mechanism held in 11 of 12 lid types, and users succeeded 7 of 8
   1 The works-like rig held 11 of 12 lid types at the highest measured torque; one lid with residue slipped   [answers]
   2 Seven of eight participants opened a hard jar unaided within 60 seconds, against two of eight with their usual method   [therefore]
   3 Two test results changed the design: a grippier band after the slip, and a larger handle after two users with large hands rated it uncomfortable   [as a result]
IV. R1-R3 are met on current evidence; R4 and wet jars are not yet verified
   1 The final design meets R1-R3 on current evidence; R4 and wet-jar performance are unverified   [answers]
   2 The evidence comes from eight participants, five of them returning, on dry jars in a single session   [however]
   3 Next, verify palm force and wet-jar performance with new participants before making any production claim   [therefore]
```

### Path chain table

> Every link in presentation order. The relation is the connector chip; at a section boundary it is the relation recorded in the relay line. "Why the second must follow" is the previous card's field 8.

| From (address, page) | To (address, page) | Relation | Why the second must follow | What the audience sees |
|---|---|---|---|---|
| Roadmap (slide 1) | I·1 (p.1) | opens | The deck states its answer and its four sections first | Roadmap with the section claims |
| I·1 (p.1) | I·2 (p.2) | because | The claim only matters if the problem is real, so slide 2 shows what the research found. | Chip "because", tracker on I |
| I·2 (p.2) | I·3 (p.3) | therefore | Findings are not yet insights. Slide 3 asks what they mean. | Chip "therefore", tracker on I |
| I·3 (p.3) | I·4 (p.4) | therefore | An insight guides a design only after it becomes a testable requirement (slide 4). | Chip "therefore", tracker on I |
| I·4 (p.4) | II·1 (p.5) | therefore | With criteria fixed, concepts can be compared against them (slide 5). | Relay line, chip "answers", tracker moves to II |
| II·1 (p.5) | II·2 (p.6) | which raises the question | Meeting requirements on paper does not mean it can work physically; slide 6 checks feasibility. | Chip "which raises the question", tracker on II |
| II·2 (p.6) | III·1 (p.7) | which raises the question | A calculation does not show it works in a real rig; slide 7 tests it. | Relay line, chip "answers", tracker moves to III |
| III·1 (p.7) | III·2 (p.8) | therefore | Holding a lid is not the same as a person opening a jar; slide 8 tests use. | Chip "therefore", tracker on III |
| III·2 (p.8) | III·3 (p.9) | as a result | The tests also showed what to change (slide 9). | Chip "as a result", tracker on III |
| III·3 (p.9) | IV·1 (p.10) | so what | After the changes, the design must be compared with the original requirements (slide 10). | Relay line, chip "answers", tracker moves to IV |
| IV·1 (p.10) | IV·2 (p.11) | however | The verdict depends on how strong the tests were; slide 11 says. | Chip "however", tracker on IV |
| IV·2 (p.11) | IV·3 (p.12) | therefore | These limits define the next steps (slide 12). | Chip "therefore", tracker on IV |
| Appendix A·1 | I·2, I·3 (pp.2-3) | backs | Answers "how were the 9 chosen and what was recorded?" | Appendix label and a pointer back to the main slide |
| Appendix A·2 | II·2 (p.6) | backs | Lets the industry partner check the numbers | Appendix label and a pointer back to the main slide |
| Appendix A·3 | II·1 (p.5) | backs | Shows why A and B were not chosen and exposes the single-scorer limit | Appendix label and a pointer back to the main slide |

**Path check:** 11 links between main slides, plus 3 appendix links; no blank link, no dead end, no orphan; each section boundary has a relay; slide 10 (IV·1) is the validation recap against R1-R4 and slide 12 returns to the thesis with the next steps.


### Cards

### Slide 1 | Section: S1 Research to requirements

**1. Slide Number:** 1
**2. Section:** S1
**3. Action-oriented Headline:** A handheld palm-lever opener lets people with weak grip open hard jars one-handed, and here is the evidence and where it stops
**4. Core Message:** The claim and its stated limits, before the derivation.
**5. Supporting Evidence:** Summary of E11 (7 of 8 vs 2 of 8) and the unverified items (R4, wet jars; G2, G3).
**6. Reason for Inclusion:** The jury judges derivation and validation (E15); stating the claim and its limits first lets them test each later slide against it.
**7. Logical Relationship with Previous Slide:** Opening; states the thesis that slides 2-11 support.
**8. Transition to Next Slide:** The claim only matters if the problem is real, so slide 2 shows what the research found.
**9. Suggested Visual Form:** Photo of the prototype in use with the claim and the "not yet verified" list beside it.
**10. Evidence Source / Confidence:** E11, gaps G2-G3 | Medium
**11. Hierarchy Label & On-slide Signposts:** `I·1` (page 1) | tracker `[I] · II · III · IV` | chip: **opens**
```text
Roadmap: I Research to requirements > II Concept and feasibility > III Build and test > IV Validation and limits
(one claim, two limits)
1) Claim: 7 of 8 opened a hard jar unaided within 60 s, against 2 of 8 with their usual method (E11)
2) Not yet verified
   a. Palm force, R4 (G2)
   b. Wet and oily jars (G3)
```

### Slide 2 | Section: S1

**1. Slide Number:** 2
**2. Section:** S1
**3. Action-oriented Headline:** Six of nine older participants gave up on a jar within two minutes, and eight feared dropping it
**4. Core Message:** The need is observed, not assumed.
**5. Supporting Evidence:** *Data:* E1 (6 of 9 abandoned), E2 (8 of 9 feared dropping). *Context:* E5, 29 of 41 ranked jar opening in their top three difficulties; **self-report, convenience sample (G8)**, so it supports only "a common difficulty in this sample".
**6. Reason for Inclusion:** The first link in the chain: findings. Without it the later requirements have no basis.
**7. Logical Relationship with Previous Slide:** Because - the claim on slide 1 answers a problem; this shows the problem.
**8. Transition to Next Slide:** Findings are not yet insights. Slide 3 asks what they mean.
**9. Suggested Visual Form:** Photo strip from the sessions with count callouts; sample size on the slide.
**10. Evidence Source / Confidence:** S1, S2, E1, E2, E5 | Medium (n=9; small)
**11. Hierarchy Label & On-slide Signposts:** `I·2` (page 2) | tracker `[I] · II · III · IV` | chip: **because**
```text
(three findings)
1) 6 of 9 abandoned at least one jar within 2 minutes (E1)
2) 8 of 9 feared dropping or breaking a glass jar (E2)
3) 29 of 41 survey respondents ranked jar opening in their top three difficulties (E5)
   a. Self-report
   b. Convenience sample (G8)
```

### Slide 3 | Section: S1

**1. Slide Number:** 3
**2. Section:** S1
**3. Action-oriented Headline:** The core difficulty is holding the jar and turning the lid at once with one weak hand, and existing aids fail on setup and fit
**4. Core Message:** The insight, with the observations it rests on, labelled as interpretation.
**5. Supporting Evidence:** *Data:* E3 (7 of 9 pressed the lid against body or counter, or used the palm), E4 (4 of 5 owned aids sit unused; reasons: setup 3, fit 2). *Interpretation (label it):* people compensate for weak pinch by using the body to hold the jar, and aids add a setup step. Coded by one author (G1).
**6. Reason for Inclusion:** Links findings to what the design must change. If removed, requirements appear without a reason.
**7. Logical Relationship with Previous Slide:** Therefore - slide 2's findings, interpreted.
**8. Transition to Next Slide:** An insight guides a design only after it becomes a testable requirement (slide 4).
**9. Suggested Visual Form:** Two annotated photos (body-brace and an unused aid) with the supporting counts.
**10. Evidence Source / Confidence:** S1, E3, E4 | Medium (n=9; single coder; G1)
**11. Hierarchy Label & On-slide Signposts:** `I·3` (page 3) | tracker `[I] · II · III · IV` | chip: **therefore**
```text
(two observations and the insight they support)
1) Observation: 7 of 9 pressed the lid against body or counter, or used the palm (E3)
2) Observation: 4 of 5 owned aids sit unused (E4)
   a. Setup effort: 3 participants
   b. Lid fit: 2 participants
3) Insight (interpretation): the difficulty is holding and turning at once with one weak hand; aids fail on setup and fit
Coded by one author (G1)
```

### Slide 4 | Section: S1

**1. Slide Number:** 4
**2. Section:** S1
**3. Action-oriented Headline:** Four requirements follow from the research; three are traced to evidence and one, palm force, is an assumption
**4. Core Message:** Each requirement's origin is shown, including the one with none.
**5. Supporting Evidence:** R1 one-handed palm operation <- E3. R2 no setup step (one placement action before turning) <- E4. R3 lids 40-90 mm <- E6 (43-89 mm measured). R4 palm force <= 25 N <- **A1, assumption, not measured (G2)**.
**6. Reason for Inclusion:** The bridge between research and design, and the link most weak design decks skip. Without it, slide 5 is a jump from findings to a concept.
**7. Logical Relationship with Previous Slide:** Therefore - insights turned into criteria a design can be judged against.
**8. Transition to Next Slide:** With criteria fixed, concepts can be compared against them (slide 5).
**9. Suggested Visual Form:** Trace table: requirement / source evidence / how it will be verified.
**10. Evidence Source / Confidence:** E3, E4, E6, A1 | R1-R3: Medium; R4: **None** (assumption)
**11. Hierarchy Label & On-slide Signposts:** `I·4` (page 4) | tracker `[I] · II · III · IV` | chip: **therefore**
```text
(four requirements)
1) R1 one-handed palm operation <- E3
2) R2 no setup step <- E4
3) R3 lids of 40-90 mm <- E6 (43-89 mm measured)
4) R4 palm force of 25 N or less <- A1, an assumption, not measured (G2)
```

### Slide 5 | Section: S2 Concept and feasibility

**1. Slide Number:** 5
**2. Section:** S2
**3. Action-oriented Headline:** Of three concepts, only the handheld band opener meets all of R1-R3
**4. Core Message:** The concept choice is explained by the requirements, with its limit.
**5. Supporting Evidence:** E9: A (under-cabinet clamp) fails R2, because it needs installation; B (countertop base with lever) fails R3, because the fixed jaws cover only part of the range; C (handheld palm lever with self-tightening band) meets R1-R3. **Scored by the author alone (G5).**
**6. Reason for Inclusion:** Answers "why this design?" from the requirements, so the choice is not preference. If removed, the form seems arbitrary.
**7. Logical Relationship with Previous Slide:** Therefore - requirements applied to options.
**8. Transition to Next Slide:** Meeting requirements on paper does not mean it can work physically; slide 6 checks feasibility.
**9. Suggested Visual Form:** Concept comparison matrix with sketches and requirement ticks.
**10. Evidence Source / Confidence:** S5, E9 | Low (single scorer; G5). *Form note:* the egg-shaped handle is a design judgement, supported only by the palm use in E3 (G6); it is not presented as a research result.
**11. Hierarchy Label & On-slide Signposts:** `II·1` (page 5) | tracker `I · [II] · III · IV` | chip: **answers**
```text
Relay line: I derived four requirements. II asks: which design meets them, and can it work?
(three concepts)
1) A, under-cabinet clamp: fails R2 (needs installation)
2) B, countertop base with lever: fails R3 (fixed jaws cover only part of the range)
3) C, handheld palm lever with a self-tightening band: meets R1-R3
Scored by the author alone (G5)
```

### Slide 6 | Section: S2

**1. Slide Number:** 6
**2. Section:** S2
**3. Action-oriented Headline:** A capstan calculation and bench friction tests indicate the band can hold lids up to 89 mm on dry glass
**4. Core Message:** The mechanism is physically plausible within stated conditions.
**5. Supporting Evidence:** E7 (friction coefficient 0.45-0.60, 6 dry trials), E8 (capstan amplification 4.1x to 6.6x over a half wrap), E6 (lid range and torque). *Limit:* dry glass only (G3).
**6. Reason for Inclusion:** Feasibility evidence for the route. Without it, "the band will hold" is an assertion.
**7. Logical Relationship with Previous Slide:** Which raises the question - the chosen concept must be physically plausible.
**8. Transition to Next Slide:** A calculation does not show it works in a real rig; slide 7 tests it.
**9. Suggested Visual Form:** Free-body schematic of the band with the equation and the measured range.
**10. Evidence Source / Confidence:** S4, E6, E7, E8 | Medium (dry only; G3)
**11. Hierarchy Label & On-slide Signposts:** `II·2` (page 6) | tracker `I · [II] · III · IV` | chip: **which raises the question**
```text
(three pieces of feasibility evidence)
1) Friction coefficient 0.45-0.60 on dry glass (E7, 6 trials)
2) Capstan amplification of 4.1x to 6.6x over a half wrap (E8)
3) Lid range 43-89 mm, opening torque 1.1-4.6 N·m (E6)
Limit: dry glass only (G3)
```

### Slide 7 | Section: S3 Build and test

**1. Slide Number:** 7
**2. Section:** S3
**3. Action-oriented Headline:** The works-like rig held 11 of 12 lid types at the highest measured torque; one lid with residue slipped
**4. Core Message:** The key hypothesis was tested on a rig built for that question, and one failure is reported.
**5. Supporting Evidence:** *Hypothesis:* a self-tightening band holds lids from 43 to 89 mm at 4.6 N·m. *Data* (E10): 11 of 12 held; the 89 mm lid with residue slipped.
**6. Reason for Inclusion:** The prototype's purpose was this hypothesis, so this is where it is verified. Without it, the design is a model with no evidence.
**7. Logical Relationship with Previous Slide:** Therefore - the plausible mechanism, now tested.
**8. Transition to Next Slide:** Holding a lid is not the same as a person opening a jar; slide 8 tests use.
**9. Suggested Visual Form:** Results table by lid type with the slipped lid highlighted.
**10. Evidence Source / Confidence:** S6, E10 | Medium (bench only, dry lids except the one residue lid)
**11. Hierarchy Label & On-slide Signposts:** `III·1` (page 7) | tracker `I · II · [III] · IV` | chip: **answers**
```text
Relay line: II chose a concept and showed it is plausible on paper. III asks: does it work in hands?
(a hypothesis and its result)
1) Hypothesis: a self-tightening band holds lids from 43 to 89 mm at 4.6 N·m
2) Result: 11 of 12 lid types held; the 89 mm lid with residue slipped (E10)
```

### Slide 8 | Section: S3

**1. Slide Number:** 8
**2. Section:** S3
**3. Action-oriented Headline:** Seven of eight participants opened a hard jar unaided within 60 seconds, against two of eight with their usual method
**4. Core Message:** The usability test beat the success criterion set before the sessions.
**5. Supporting Evidence:** *Data* (E11): 7 of 8 vs 2 of 8; criterion written beforehand: at least 6 of 8. E14: 8 of 8 began turning after one placement action (single coder). *Limits on the slide* (E13): 5 of 8 returning, single session, dry jars, timed by the team (G4).
**6. Reason for Inclusion:** The main behavioural evidence. It tests R1 and R2 in hands.
**7. Logical Relationship with Previous Slide:** Therefore - from the mechanism to the person.
**8. Transition to Next Slide:** The tests also showed what to change (slide 9).
**9. Suggested Visual Form:** Paired dot chart per participant: usual method vs prototype, with the criterion line.
**10. Evidence Source / Confidence:** S7, E11, E13, E14 | Medium (n=8; 5 returning; single coder for E14)
**11. Hierarchy Label & On-slide Signposts:** `III·2` (page 8) | tracker `I · II · [III] · IV` | chip: **therefore**
```text
(two results)
1) Success: 7 of 8 opened a hard jar unaided within 60 s, against 2 of 8 with their usual method (E11); criterion set beforehand: at least 6 of 8
2) Use: 8 of 8 began turning after one placement action (E14, single coder)
Limits: 5 of 8 returning, single session, dry jars, timed by the team (E13, G4)
```

### Slide 9 | Section: S3

**1. Slide Number:** 9
**2. Section:** S3
**3. Action-oriented Headline:** Two test results changed the design: a grippier band after the slip, and a larger handle after two users with large hands rated it uncomfortable
**4. Core Message:** Each change is tied to the result that triggered it.
**5. Supporting Evidence:** Change 1: E10 (slip) -> textured silicone band; retested on that lid only, held (**1 lid, G7**). Change 2: E12 (2 of 8 with the largest hands rated palm force low) -> larger handle; not retested.
**6. Reason for Inclusion:** Shows iteration is evidence-driven, not decoration. Without it "version 3" has no reason.
**7. Logical Relationship with Previous Slide:** As a result - the tests produced changes.
**8. Transition to Next Slide:** After the changes, the design must be compared with the original requirements (slide 10).
**9. Suggested Visual Form:** Before/after detail photos, each with the test result that caused it.
**10. Evidence Source / Confidence:** S6, S7, E10, E12 | Low (neither change fully retested; G7)
**11. Hierarchy Label & On-slide Signposts:** `III·3` (page 9) | tracker `I · II · [III] · IV` | chip: **as a result**
```text
(two changes)
1) Grippier band, after the slip (E10)
   a. Retested on that lid only: held
   b. Not retested on the other lid types (G7)
2) Larger handle, after 2 of 8 users with the largest hands rated palm force low (E12); not retested
```

### Slide 10 | Section: S4 Validation and limits

**1. Slide Number:** 10
**2. Section:** S4
**3. Action-oriented Headline:** The final design meets R1-R3 on current evidence; R4 and wet-jar performance are unverified
**4. Core Message:** Validation is against the original requirements, not against opinion.
**5. Supporting Evidence:** R1: E11, E14 (met). R2: E14 (met; single coder). R3: E10 (11 of 12 + 1 retest; met on dry lids). R4: only subjective comfort, E12 (6 of 8); **not measured (G2)**.
**6. Reason for Inclusion:** The answer to the central question. Without it, the audience does not see what has been verified.
**7. Logical Relationship with Previous Slide:** Therefore - the changed design set against the requirements from slide 4.
**8. Transition to Next Slide:** The verdict depends on how strong the tests were; slide 11 says.
**9. Suggested Visual Form:** Requirements table: requirement / evidence / status / confidence.
**10. Evidence Source / Confidence:** E10-E14 | Medium for R1-R3; None for R4
**11. Hierarchy Label & On-slide Signposts:** `IV·1` (page 10) | tracker `I · II · III · [IV]` | chip: **answers**
```text
Relay line: III tested the mechanism and the use. IV asks: against the original requirements, what is verified?
(four requirements checked)
1) R1 one-handed palm operation: met (E11, E14)
2) R2 no setup step: met (E14; single coder)
3) R3 lids of 40-90 mm: met on dry lids (E10)
4) R4 palm force: unverified; only subjective comfort recorded (E12; G2)
```

### Slide 11 | Section: S4

**1. Slide Number:** 11
**2. Section:** S4
**3. Action-oriented Headline:** The evidence comes from eight participants, five of them returning, on dry jars in a single session
**4. Core Message:** The limits are specific, and each has a way to be closed.
**5. Supporting Evidence:** E13 plus the gap register G1-G8, each with its closing action.
**6. Reason for Inclusion:** Pre-empts the jury's sharpest questions and shows the team knows the limits. Without it, slide 10 looks over-confident.
**7. Logical Relationship with Previous Slide:** However - qualifies slide 10's verdict.
**8. Transition to Next Slide:** These limits define the next steps (slide 12).
**9. Suggested Visual Form:** Limits table: limit / effect on claim / how to close.
**10. Evidence Source / Confidence:** E13, gap register | High (a description of the team's own limits)
**11. Hierarchy Label & On-slide Signposts:** `IV·2` (page 11) | tracker `I · II · III · [IV]` | chip: **however**
```text
(three limits)
1) Sample: 8 participants, 5 of them returning (E13)
2) Conditions: dry jars, a single session
3) Coding and scoring: one coder (G1), one scorer (G5)
```

### Slide 12 | Section: S4

**1. Slide Number:** 12
**2. Section:** S4
**3. Action-oriented Headline:** Next, verify palm force and wet-jar performance with new participants before making any production claim
**4. Core Message:** The path from "meets R1-R3 in a pilot" to "ready" is concrete.
**5. Supporting Evidence:** Plan: force-sensor test (G2), wet and oily lids (G3), re-run T1 with the new band (G7), independent group (G4), second coder (G1).
**6. Reason for Inclusion:** Closes the argument by stating what separates the current claim from the full one.
**7. Logical Relationship with Previous Slide:** Therefore - the limits become the work plan.
**8. Transition to Next Slide:** End of the main line; the appendix follows for questions.
**9. Suggested Visual Form:** Short timeline of the verification steps, each tagged with the gap it closes.
**10. Evidence Source / Confidence:** Slides 10-11, gap register | Medium (a plan; no result yet)
**11. Hierarchy Label & On-slide Signposts:** `IV·3` (page 12) | tracker `I · II · III · [IV]` | chip: **therefore**
```text
(five verification steps)
1) Force-sensor test of palm force (G2)
2) Wet and oily lids (G3)
3) Re-run T1 with the new band on all 12 lid types (G7)
4) Independent participant group (G4)
5) Second coder for the observation notes (G1)
```

### Appendix

**A1 - Observation protocol and sample (backs slides 2-3).** *Reason:* answers "how were the 9 chosen and what did you record?" *Relationship:* detail for slides 2-3. *Source/Confidence:* S1 | High as a description. *Visual:* protocol outline with participant table. *Headline:* "Nine participants aged 62-84 each opened three jars in their own kitchens". *Hierarchy:* Appendix A·1; backs I·2 and I·3 (pages 2-3).

**A2 - Capstan calculation and friction data (backs slide 6).** *Reason:* lets the industry partner check the numbers. *Relationship:* detail for slide 6. *Source/Confidence:* S4, E7, E8 | Medium (dry only; G3). *Visual:* equation, six trials. *Headline:* "Six friction trials give mu of 0.45 to 0.60 and a capstan ratio of 4.1 to 6.6 over a half wrap". *Hierarchy:* Appendix A·2; backs II·2 (page 6).

**A3 - Rejected concepts and the scoring (backs slide 5).** *Reason:* shows why A and B were not chosen and exposes the single-scorer limit (G5). *Relationship:* detail for slide 5. *Source/Confidence:* S5, E9 | Low. *Visual:* sketches with scoring notes. *Headline:* "Concepts A and B each fail one requirement, by the author's scoring". *Hierarchy:* Appendix A·3; backs II·1 (page 5).

---

## Phase 5 - Logic Audit

The audit ran on the first Phase 4 draft. It found:

| ID | Severity | Location | Issue | Fix applied |
|---|---|---|---|---|
| A-01 | **Critical** | Draft thesis | "Solves jar opening" exceeds the evidence: R4 unmeasured, wet jars untested, n=8 | Returned to Phase 2: thesis narrowed (v2) |
| A-02 | **Critical** | Draft slides 3 to 5 | A jump from research findings straight to the egg-shaped concept, with no requirements | Slide 4 added; every requirement traced; form marked as design judgement (G6) |
| A-03 | Major | Draft slide 9 | "Users loved the prototype" offered as validation | Replaced with the measured result (E11) and the pre-set criterion; validation is against R1-R4 (slide 10) |
| A-04 | Major | Draft slide 4 | Palm-force target (25 N) presented as a research finding | Marked as an assumption (A1); confidence None; moved into next steps |
| A-05 | Major | Draft slide 6 | "The band will hold any jar" from a dry-glass calculation | Reworded: "indicate ... on dry glass"; G3 stated |
| A-06 | Major | Draft slide 8 | Test success criterion not shown; looked post hoc | Criterion shown with its pre-test date source (S7) |
| A-07 | Minor | Draft slides 2 and 5 | The survey figure (71%) was used as proof of need | Limited to "a common difficulty in this sample" (G8) |
| A-08 | Minor | Draft section titles and connectors | Sections were titled by topic ("Research", "Concept", "Test", "Validation"), and slide 10 followed slide 9 with no named relation to the original requirements | Titles rewritten as claims (I to IV); relay lines added at each opener; every slide has a connector chip; path chain table built |

**Design-chain checks (final structure):**

| Check | Result | Slides |
|---|---|---|
| 1 Findings support insight | Pass, with a single-coder limit (G1) | 2-3 |
| 2 Insights become requirements | Pass | 4 |
| 3 Requirements explain the design | Partial: concept choice self-scored (G5); form is a judgement (G6) | 5 |
| 4 Technical route has feasibility evidence | Pass for dry glass; wet untested (G3) | 6 |
| 5 Prototype verified the key hypothesis | Pass (T1 on a works-like rig) | 7 |
| 6 Test results support the conclusion | Partial: returning participants, single session (G4) | 8 |
| 7 No jump from research to form | Pass after A-02 | 3-5 |
| 8 No hypothesis presented as a finding | Pass after A-03 and A-04; R4 labelled | 4, 10 |

**Path integrity (signposting pass):** 11 links between main slides plus 3 appendix links, no blank link, no dead end, no orphan. Listener test passed: the signpost outline alone reproduces the argument. The III to IV boundary is carried by the relay line ("so what") and the first slide of IV answers its question.

**Audience questions:** why this form? (slides 4-5; form flagged as judgement); was the test independent? (slide 11, stated); was force measured? (**no**, slide 10); does it work on wet jars? (**untested**, slide 11); how were concepts scored? (A3, single scorer).

**What works:** a pre-set test criterion; failures and limits shown; every requirement traced, including the one with no evidence.

---

## Phase 6 - Final Architecture Delivery

Written to `./ppt-architecture/`: `master-outline.md`, `logic-tree.md`, `slide-by-slide.md` (12 main and 3 appendix cards), `evidence-matrix.md` (S1-S8, E1-E15, A1, gaps G1-G8), and `logic-audit-report.md` (A-01 to A-07).

### Requirement-to-evidence excerpt (from `evidence-matrix.md`)

| Requirement | Source of the requirement | Verification evidence | Status | Confidence |
|---|---|---|---|---|
| R1 one-handed palm operation | E3 | E11, E14 | Met in test | Medium |
| R2 no setup step | E4 | E14 (single coder) | Met in test | Medium |
| R3 lids 40-90 mm | E6 | E10 | Met on dry lids | Medium |
| R4 palm force <= 25 N | **A1 (assumption)** | E12 (subjective only) | **Unverified** | **None** |

**Hand-off:** the approved `slide-by-slide.md` is the input to a slide-building step. This skill does not start that unless asked.
