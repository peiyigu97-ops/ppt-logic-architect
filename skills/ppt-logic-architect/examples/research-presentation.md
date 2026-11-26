# Example 1 - Research Presentation (technical progress review)

> **All data, devices, and results in this example are fictional.** They exist only to demonstrate the method. Do not cite them.
> The example shows the *output* of each phase for a realistic case, including the places where the skill narrows a claim, refuses to fill a gap, and keeps inference apart from data.

**Case:** A graduate student is giving a progress review to two supervisors. The supervisors decide whether to approve a field study next term. The student has notes, two spreadsheets, a CSV, and a supervisor email, and no deck yet. **Mode: CREATE.** Language: English.

---

## Phase 1 - Intake & Diagnosis

### Source register

| ID | Source | Type | What it contains | Read? |
|---|---|---|---|---|
| S1 | `bench_energy_log.xlsx` | Data file | Average power by subsystem at fixed 100 Hz; 60-min scripted trace, fixed vs adaptive, one run each | Yes |
| S2 | `pilot_accuracy.csv` | Data file | Heart-rate error vs chest-strap reference; 8 participants; seated rest, walk 4 km/h, run 8 km/h; per-participant MAE | Yes |
| S3 | `firmware_notes.md` | Notes | How the rate selector works; lab-notebook entries on rate switching during runs | Yes |
| S4 | `supervisor_email.txt` | Email | Decision to be made; acceptance criteria | Yes |
| S5 | `related_work_notes.docx` | Notes | Summaries of two papers on fixed-rate sampling cost; **citations not supplied** | Yes |

### Extracted items (selected)

| ID | Item | Type | Source |
|---|---|---|---|
| E1 | At fixed 100 Hz, sampling takes 62% of average power (9.8 mW), MCU 24%, BLE 14% | Data (single run) | S1 |
| E2 | Scripted 60-min trace (70% rest, 20% walk, 10% run): fixed 9.8 mW, adaptive 6.5 mW, reduction 33.7% | Data (single run each; trace mix chosen by the student) | S1 |
| E3 | Seated rest, n=8: MAE fixed 1.2 bpm, adaptive 1.3 bpm | Data | S2 |
| E4 | Walk 4 km/h, n=8: MAE fixed 2.1, adaptive 2.3 | Data | S2 |
| E5 | Run 8 km/h, n=8: MAE fixed 3.4, adaptive 4.6 | Data | S2 |
| E6 | In 5 of 8 run trials the adaptive rate stayed at 50 Hz for 6-10 s after run onset | Data (notebook observation) | S3 |
| E7 | Acceptance criteria: MAE <= 3 bpm vs reference; average power reduction >= 25% | Fact (supervisor's stated criteria) | S4 |
| E8 | "Fixed-rate sampling dominates wearable HR energy cost" | Claim-by-source; **citations missing** | S5 |
| E9 | Rate selector picks 25, 50, or 100 Hz from accelerometer-magnitude thresholds | Fact (own design) | S3 |
| E10 | Pilot: 8 participants, ages 22-31, left wrist only, skin tone not recorded | Fact | S2 |
| - | "Adaptive sampling should work for everyone" (student's note) | **Assumption** | S3 |
| - | Photos of the PCB (3) | **Noise** for this argument; may go in the appendix | S3 |

### Brief

| Item | Content |
|---|---|
| Purpose | Get approval for a field study next term |
| Audience | Two supervisors; expert; will ask about baseline, sample, and limits |
| Central question | Is adaptive sampling ready to be tested in the field? |
| Type | Research progress review with a decision |
| Constraints | 15 minutes, up to about 12 main slides |

### Early gaps

The material cannot yet support: any claim about running accuracy being acceptable; any claim of energy saving beyond the scripted trace; any claim about populations other than young adults; the literature claim in E8 (no citations).

### Gate

```
### Phase 1 - Intake & Diagnosis: Result
Goal of this phase: Inventory the material and fix purpose, audience, and the central question.
Result: 5 sources, 10 evidence items, 1 assumption, 1 noise item; brief above.
Unresolved:
- [CAN PROCEED] S5 has no citations, so E8 cannot be used as evidence yet.
- [CAN PROCEED] The 70/20/10 activity mix has no stated basis.
Decisions for you:
1. Is "approval for a field study" the decision? (Assumed yes, from S4.)
2. Should the literature claim stay in the main line? (Recommended: move to the appendix until citations exist.)
Next: Phase 2 - Thesis & Argument Architecture. Reply "continue", or tell me what to change.
```

*(The user replies "continue; agreed on both".)*

PHASE-STATE: mode CREATE; audience supervisors (expert, decide on field study); central question "Is adaptive sampling ready to be tested in the field?"; approved phases: 1; open gaps: see below.

---

## Phase 2 - Thesis & Argument Architecture

### Thesis tests

The student's first wording was *"Adaptive sampling saves energy while maintaining accuracy."* It fails two tests:
- **Evidence match:** E5 shows accuracy is *not* maintained at running (4.6 vs the 3 bpm criterion).
- **Scope:** E10 covers eight young adults, one wrist.

### Central thesis (v2, narrowed)

> Adaptive sampling is ready for a field study limited to rest and walking: it cut bench power by 34% and stayed within the 3 bpm accuracy criterion in an eight-person pilot, but it misses the criterion at running intensity, which needs a fix before any claim there.

**We claim:** the two criteria in S4 are met on the tested conditions (energy on a scripted trace; accuracy at rest and walking).
**We do not claim:** accuracy at running; energy saving in real life; results for other wrist positions, skin tones, or age groups; the cause of the running error.

### Method decision

- Presentation type: research progress review with a decision; audience: expert supervisors.
- Using: **Evidence-Based Reasoning** (baseline); **Pyramid, answer first**, because the audience decides and wants the recommendation early; **Assertion-Evidence** for result slides.
- Not using: **SCQA as a frame**, because the audience already knows the context and wants results; **MECE**, because the structure is the two criteria in S4, not a partition of a whole.

### Logic tree

```
C0  Adaptive sampling is ready for a field study at rest and walking, not yet at running   [Medium]
|   Grouping: logical, by the supervisors' decision criteria (need, energy, accuracy, scope); not MECE
|
+-- C1  Sampling is the main energy cost, so it is the right target            [Medium]
|     +-- E1  62% of 9.8 mW at fixed 100 Hz (S1, single run)
|     +-- E8  literature claim                                                  (G7: no citations)
|
+-- C2  Adaptive sampling saves more than the 25% criterion on the bench      [Medium]
|     +-- E2  9.8 -> 6.5 mW (33.7%), scripted trace; E7 criterion
|     +-- G1 activity mix unsourced; G2 single run; G3 rest+walk-only saving not measured
|
+-- C3  Accuracy meets the 3 bpm criterion at rest and walking                 [Medium]
|     +-- E3 1.3 bpm; E4 2.3 bpm; E7 criterion
|     +-- G4 no variance reported; G5 n=8, young, one wrist
|
+-- C4  Accuracy misses the criterion at running                               [Medium]
|     +-- E5 4.6 bpm (fixed baseline also 3.4)
|     +-- C4a  Probable cause: slow rate switching                             [Low, inference]
|           +-- E6 5 of 8 trials stayed at 50 Hz for 6-10 s     (G6: untested)
|
+-- C5  So: field study at rest and walking, running fix in parallel           [derived]
      +-- from C2, C3, C4; (G8: sample size of 20 has no rationale)
```

### Likely objections

| Objection | Answered where | Status |
|---|---|---|
| "Is the 34% real or an artefact of your trace?" | Slides 5, 10 | Partly (G1, G2, G3 open) |
| "Eight people is not a result." | Slide 10 | Answered by stating the limit, and by the field study |
| "Why does the baseline also fail at running?" | Slide 7 | Answered (it does; stated) |
| "Is the lag really the cause?" | Slide 8 | Stated as untested |

### Gap register (created in this phase)

| ID | Gap | To close |
|---|---|---|
| G1 | 70/20/10 mix has no source | Source the mix, or call it "scripted trace" everywhere |
| G2 | One bench run per condition | Repeat at least three times |
| G3 | Saving for a rest+walk-only trace not measured (the 34% includes the running segment) | Run the trace with the running segment replaced by walking |
| G4 | No variance reported for MAE | Compute SD and per-participant spread from S2 (data already exists) |
| G5 | n=8, ages 22-31, one wrist, skin tone not recorded | Field study with a broader sample |
| G6 | Rate-switch lag as the cause of the running error is untested | Replay the run data with a faster switch |
| G7 | Literature citations missing | Student supplies citations |
| G8 | No rationale for n=20 | State a rationale (precision target or constraint) |

### Gate (summary)

```
### Phase 2 - Thesis & Argument Architecture: Result
Goal: Fix the thesis, its scope, and the evidence under each branch.
Result: Thesis v2 (narrowed from "maintaining accuracy" because of E5); tree with 5 branches; 8 gaps.
Unresolved: [CAN PROCEED] G1-G8; G3 and G4 can be closed with a short bench run and a calculation.
Decisions for you:
1. Accept the narrowed thesis? (Recommended: yes; the original is contradicted by E5.)
2. Run G3 and G4 before the review? (Recommended: yes; both are quick.)
Next: Phase 3 - Section Architecture.
```

---

## Phase 3 - Section Architecture

**Ordering principle:** answer first, then method, then results, then implications (Pyramid for a deciding audience; method-to-results order for a research report).

| # | Section | Role | Section claim | Slides |
|---|---|---|---|---|
| S1 | Decision and rationale | Give the recommendation; justify the target | Adaptive sampling is worth a field study, and sampling is the right target | 1-2 |
| S2 | What was built and how it was tested | Let the audience judge the evidence | The scheme and the two tests are matched to the two criteria | 3-4 |
| S3 | What the tests showed | The evidence | Energy and rest/walk accuracy pass; running fails; one candidate cause | 5-8 |
| S4 | What it means and what we ask | Implications, limits, the ask | The evidence supports a scoped field study | 9-11 |

| From | To | Relation | Why the second must follow |
|---|---|---|---|
| S1 | S2 | Which raises the question | The recommendation invites "what exactly was tested?" |
| S2 | S3 | Therefore | The criteria and tests are set, so results can be read against them |
| S3 | S4 | So what | Results are not a decision until set against the criteria and their limits |

**Where the ask lands:** slide 11 (stated in slide 1).

---

## Phase 4 - Slide-by-Slide Architecture

### Headline chain

> Adaptive sampling is ready for a field study at rest and walking, but not yet at running. Sampling takes 62% of the fixed-rate monitor's power, so it is the right place to save energy. The adaptive scheme picks 25, 50, or 100 Hz from motion. Two tests answer two questions: bench power for energy, an eight-person pilot for accuracy. Adaptive sampling cut average power by 34% on a scripted bench trace. At rest and walking it stayed within the 3 bpm criterion. At running it misses the criterion. The running error may come from slow rate switching, which is untested. Against both criteria, the results support rest and walking, not running. The evidence rests on eight young participants, one wrist position, and one bench run per condition. We ask approval for a 20-participant field study at rest and walking, with a running fix in parallel.

### Cards

### Slide 1 | Section: S1 Decision and rationale

**1. Slide Number:** 1
**2. Section:** S1
**3. Action-oriented Headline:** Adaptive sampling is ready for a field study at rest and walking, but not yet at running
**4. Core Message:** The recommendation and the decision requested, stated before the evidence.
**5. Supporting Evidence:** Summary of E2 (energy), E3-E4 (accuracy at rest and walking), E5 (running miss), against criteria E7.
**6. Reason for Inclusion:** Supervisors decide; stating the answer first lets them judge each later slide against it. Without it they must infer the ask from nine slides.
**7. Logical Relationship with Previous Slide:** Opening slide; states the thesis that slides 2-10 support.
**8. Transition to Next Slide:** A field study is worth approving only if the intervention targets something that matters, so slide 2 shows why sampling is the target.
**9. Suggested Visual Form:** Thesis statement with a three-row status strip (energy: met; accuracy at rest/walking: met; accuracy at running: not met).
**10. Evidence Source / Confidence:** E2-E5, E7 | Medium (inherits the weakest supporting claim; G1-G5)

### Slide 2 | Section: S1

**1. Slide Number:** 2
**2. Section:** S1
**3. Action-oriented Headline:** Sampling takes 62% of the fixed-rate monitor's average power, so it is the right place to save energy
**4. Core Message:** The intervention targets the dominant cost on this device.
**5. Supporting Evidence:** E1 (data): at fixed 100 Hz, sampling 62%, MCU 24%, BLE 14% of 9.8 mW. The literature claim (E8) is **not** used here: citations are missing (G7); it goes to Appendix A1.
**6. Reason for Inclusion:** Justifies the project's target. A supervisor would otherwise ask "why sampling?". If removed, the rest of the deck has no reason to exist.
**7. Logical Relationship with Previous Slide:** Because - the recommendation presupposes the target is worth reducing.
**8. Transition to Next Slide:** Having named the target, the audience needs to know what was done to it: slide 3 shows the scheme.
**9. Suggested Visual Form:** Stacked bar of power by subsystem with the total labelled.
**10. Evidence Source / Confidence:** S1, E1 | Medium (one device, one run)

### Slide 3 | Section: S2 What was built and how it was tested

**1. Slide Number:** 3
**2. Section:** S2
**3. Action-oriented Headline:** The adaptive scheme picks 25, 50, or 100 Hz from motion level, using accelerometer-magnitude thresholds
**4. Core Message:** What was built, in enough detail to interpret the results and the later running failure.
**5. Supporting Evidence:** E9 (own design). Threshold values: `[value needed from S3]`; not in the notes excerpt.
**6. Reason for Inclusion:** Slide 8 explains a failure by this mechanism; the audience must have seen it first.
**7. Logical Relationship with Previous Slide:** For example - slide 2 named the target; this shows how it is reduced.
**8. Transition to Next Slide:** A mechanism proves nothing until it is tested against criteria, so slide 4 sets out the tests.
**9. Suggested Visual Form:** Flow diagram: accelerometer, motion level, rate selector, PPG sampler.
**10. Evidence Source / Confidence:** S3, E9 | High (a description of the team's own design)

### Slide 4 | Section: S2

**1. Slide Number:** 4
**2. Section:** S2
**3. Action-oriented Headline:** Two tests answer two separate questions: bench power for energy, an eight-person pilot for accuracy
**4. Core Message:** The yardsticks come from the supervisors (S4) and were set before the results; each test has stated limits.
**5. Supporting Evidence:** E7 (criteria: MAE <= 3 bpm; power reduction >= 25%). Bench: 60-min scripted trace, one run per condition (S1). Pilot: 8 participants, chest-strap reference (E10).
**6. Reason for Inclusion:** Gives every later result a pass/fail line. Without it the audience cannot tell whether 2.3 bpm is good.
**7. Logical Relationship with Previous Slide:** Therefore - to know if the scheme works it must be measured against stated criteria.
**8. Transition to Next Slide:** With the yardsticks fixed, the first result is energy (slide 5).
**9. Suggested Visual Form:** Two-column table: question / test / criterion / known limits.
**10. Evidence Source / Confidence:** E7, E10, S1 | High (descriptions and quoted criteria)

### Slide 5 | Section: S3 What the tests showed

**1. Slide Number:** 5
**2. Section:** S3
**3. Action-oriented Headline:** Adaptive sampling cut average power by 34% (9.8 to 6.5 mW) on a scripted bench trace, above the 25% criterion
**4. Core Message:** The energy criterion is met on this trace. The trace and the single run limit how far it generalizes.
**5. Supporting Evidence:** *Data* (E2): fixed 9.8 mW, adaptive 6.5 mW, 33.7%. *Interpretation:* 8.7 points above the criterion (E7). Trace is 70% rest, 20% walk, 10% run (mix unsourced, G1); one run each (G2); the saving for rest+walk only is not measured (G3).
**6. Reason for Inclusion:** The energy leg of the recommendation. Without it, "ready" has no energy support.
**7. Logical Relationship with Previous Slide:** Therefore - slide 4's energy test, now with its result.
**8. Transition to Next Slide:** Energy saved is worthless if the heart rate is wrong, so slide 6 asks whether accuracy held.
**9. Suggested Visual Form:** Paired bars (fixed vs adaptive) with the 25% line; trace composition labelled under the chart.
**10. Evidence Source / Confidence:** S1, E2, E7 | Medium (single run; mix assumed; G1-G3)

### Slide 6 | Section: S3

**1. Slide Number:** 6
**2. Section:** S3
**3. Action-oriented Headline:** At rest and walking, adaptive sampling stayed within the 3 bpm criterion (MAE 1.3 and 2.3 bpm, n = 8)
**4. Core Message:** Accuracy holds in the two lower-intensity conditions; the fixed-rate baseline is shown alongside.
**5. Supporting Evidence:** *Data* (E3, E4): rest 1.3 vs 1.2 (fixed); walk 2.3 vs 2.1 (fixed). *Interpretation:* adaptive costs 0.1-0.2 bpm relative to fixed. SD and per-participant spread to be added from S2 (G4).
**6. Reason for Inclusion:** The accuracy leg for the scope we actually recommend.
**7. Logical Relationship with Previous Slide:** Which raises the question - slide 5's saving matters only if accuracy held; this answers it for two conditions.
**8. Transition to Next Slide:** Running is the third condition and behaves differently (slide 7).
**9. Suggested Visual Form:** Grouped bars by condition with the 3 bpm line, with per-participant dots to show spread.
**10. Evidence Source / Confidence:** S2, E3, E4, E7, E10 | Medium (n=8, young, one wrist; G4, G5)

### Slide 7 | Section: S3

**1. Slide Number:** 7
**2. Section:** S3
**3. Action-oriented Headline:** At running intensity, adaptive sampling misses the criterion (MAE 4.6 bpm vs 3.4 for fixed-rate)
**4. Core Message:** The failing condition is reported with the same weight as the passing ones. The fixed-rate baseline also exceeds 3 bpm here.
**5. Supporting Evidence:** *Data* (E5): adaptive 4.6, fixed 3.4, criterion 3.0. *Interpretation:* about 1.2 bpm of the error is added by the adaptive scheme; the remaining part is present in the baseline, so it is not due to adaptive sampling.
**6. Reason for Inclusion:** Marks the boundary of the thesis. If removed, readiness at running would be claimed by omission.
**7. Logical Relationship with Previous Slide:** However - slide 6's pass does not extend to the third condition.
**8. Transition to Next Slide:** A failure needs a candidate explanation before a fix can be proposed (slide 8).
**9. Suggested Visual Form:** The slide-6 chart extended with the running condition, with the gap to the criterion highlighted.
**10. Evidence Source / Confidence:** S2, E5, E7 | Medium (n=8; G4, G5)

### Slide 8 | Section: S3

**1. Slide Number:** 8
**2. Section:** S3
**3. Action-oriented Headline:** The running error may come from slow rate switching: in 5 of 8 run trials the rate stayed at 50 Hz for 6-10 s after run onset (hypothesis, untested)
**4. Core Message:** A candidate cause is supported by observation but has not been tested.
**5. Supporting Evidence:** *Data* (E6): 5 of 8 trials, 6-10 s lag. *Inference (label it as such):* the lag probably raises error in the first seconds of running. It cannot explain the baseline's own 3.4 bpm.
**6. Reason for Inclusion:** Gives the "fix in parallel" on slide 11 a basis. Without it, the fix is a hope.
**7. Logical Relationship with Previous Slide:** Because - a tentative explanation of slide 7.
**8. Transition to Next Slide:** Slides 5-8 hold three results and one open cause; slide 9 sets them against the criteria.
**9. Suggested Visual Form:** Timeline for one trial: motion level and selected rate over time, with the lag marked.
**10. Evidence Source / Confidence:** S3, E6 | Low (inference; untested; G6)

### Slide 9 | Section: S4 What it means and what we ask

**1. Slide Number:** 9
**2. Section:** S4
**3. Action-oriented Headline:** Against the two criteria, the results support rest and walking, not running
**4. Core Message:** The criteria-by-condition summary is the single place where all evidence meets the decision rule.
**5. Supporting Evidence:** Energy >= 25%: 34% on the scripted trace (met; Medium). Accuracy <= 3 bpm: rest met, walk met, run not met (Medium). Note that the 34% includes the running segment (G3).
**6. Reason for Inclusion:** Makes slide 1's claim traceable. Without it the supervisors must assemble the verdict themselves.
**7. Logical Relationship with Previous Slide:** Therefore - consolidates slides 5-8.
**8. Transition to Next Slide:** Before asking for approval we must say how far this evidence reaches (slide 10).
**9. Suggested Visual Form:** Criteria matrix (rows: criteria and conditions; columns: result, status, confidence).
**10. Evidence Source / Confidence:** E2-E7 | Medium

### Slide 10 | Section: S4

**1. Slide Number:** 10
**2. Section:** S4
**3. Action-oriented Headline:** The evidence comes from eight young participants, one wrist position, and one bench run per condition
**4. Core Message:** The limits are stated up front, and each one maps to something the field study can settle.
**5. Supporting Evidence:** E10 (sample), single bench runs (S1), G1-G6 with the field-study activity that addresses each.
**6. Reason for Inclusion:** Pre-empts the supervisors' first questions and ties the ask to specific gaps. Without it, slide 11 looks unmotivated.
**7. Logical Relationship with Previous Slide:** However - qualifies slide 9's verdict.
**8. Transition to Next Slide:** These limits are exactly what a field study can settle, so slide 11 proposes one.
**9. Suggested Visual Form:** Table: limit / what it affects / how the next step addresses it.
**10. Evidence Source / Confidence:** E10, S1, gap register | High (an honest description of the team's own limits)

### Slide 11 | Section: S4

**1. Slide Number:** 11
**2. Section:** S4
**3. Action-oriented Headline:** We ask approval for a 20-participant field study at rest and walking, with a running-mode fix developed in parallel
**4. Core Message:** The decision requested and what each part of the plan would settle.
**5. Supporting Evidence:** Follows from slides 9-10. *Proposal, not data:* n=20 has no stated rationale (G8): `[rationale needed]`.
**6. Reason for Inclusion:** The decision the deck exists for.
**7. Logical Relationship with Previous Slide:** Therefore - follows from the verdict (9) and its limits (10).
**8. Transition to Next Slide:** Closing slide; backup slides follow.
**9. Suggested Visual Form:** Plan timeline with the gaps (G1-G6) each activity closes.
**10. Evidence Source / Confidence:** Slides 9-10, gap register | Medium for the logic; **None** for the sample size until G8 is answered

### Appendix

**A1 - Related-work notes (backs slide 2).** *Reason:* shows the literature claim that sampling dominates cost. *Relationship:* supports slide 2. *Source/Confidence:* S5, E8 | **Low**: citations not supplied (G7). *Visual:* two-row table of papers. *Transition:* return to slide 2. *Headline:* "Two papers report that fixed-rate sampling dominates wearable HR energy cost (citations pending)".

**A2 - Bench setup and trace composition (backs slides 4-5).** *Reason:* answers "what exactly was the trace?" *Relationship:* detail for slide 5. *Source/Confidence:* S1 | High as a description. *Visual:* trace timeline with segments. *Headline:* "The scripted trace runs 42 min rest, 12 min walk, 6 min run".

**A3 - Pilot protocol and per-participant results (backs slides 6-7).** *Reason:* answers "what is the spread?" and closes G4 once SD is computed. *Relationship:* detail for slides 6-7. *Source/Confidence:* S2, E10 | High as a description. *Visual:* dot plot per participant per condition. *Headline:* "Per-participant error at running ranges widely" `[range to be computed from S2 before stating]`.

---

## Phase 5 - Logic Audit

The audit ran on the first Phase 4 draft. It found these issues, which were fixed at their source:

| ID | Severity | Location | Issue | Fix applied |
|---|---|---|---|---|
| A-01 | **Critical** | Draft thesis | "Maintaining accuracy" is contradicted by E5 (running) | Returned to Phase 2: thesis narrowed (v2) |
| A-02 | Major | Draft slide 5 headline | "Adaptive sampling reduces energy by 34%" drops the trace and single-run qualifiers | Headline now says "on a scripted bench trace"; G1-G3 listed |
| A-03 | Major | Draft slide 8 | Rate-switch lag stated as the cause | Reworded as a hypothesis; confidence Low; fix framed as parallel work |
| A-04 | Major | Draft slide 2 | Headline rested on a literature claim with no citations | Evidence changed to E1 (own data); literature moved to A1 |
| A-05 | Major | Slides 5, 9 | The 34% includes the running segment, where accuracy fails, while the thesis is scoped to rest and walking | **Open.** Stated on slides 5 and 9; closing it needs G3 (a quick bench run) |
| A-06 | Minor | Draft slides 7 and 9 | Running result stated twice with no new purpose | Slide 9 now consolidates; slide 7 keeps the detail |

**Audience questions:** baseline? (slides 6-7, answered); sample? (slide 10, answered); what is the spread? (A3, pending G4); is the lag the cause? (slide 8, stated as untested); why n=20? (**unanswered**, G8).

**What works:** the criteria come from the supervisors and are shown before results; the failing condition gets equal weight; limits are mapped to next steps.

---

## Phase 6 - Final Architecture Delivery

Written to `./ppt-architecture/`:

| File | Content |
|---|---|
| `master-outline.md` | Brief, thesis v2, method decision, four sections, progression, headline chain, cut list (PCB photos to appendix), gaps |
| `logic-tree.md` | The tree above, with warrants and objections |
| `slide-by-slide.md` | 11 main cards and 3 appendix cards |
| `evidence-matrix.md` | S1-S5, E1-E10, claim-to-evidence map, gaps G1-G8 |
| `logic-audit-report.md` | A-01 to A-06 with resolution status |

### Claim-to-evidence excerpt (from `evidence-matrix.md`)

| Claim | Slides | Evidence | Status | Confidence | Scope match? |
|---|---|---|---|---|---|
| C1 Sampling is the main cost | 2 | E1 | Sourced | Medium | One device, one run |
| C2 Saves more than 25% | 5, 9 | E2, E7 | Sourced | Medium | **Partial:** mix assumed (G1), single run (G2), includes running (G3) |
| C3 Accuracy OK at rest and walking | 6, 9 | E3, E4, E7 | Sourced | Medium | **Partial:** n=8, young, one wrist (G5) |
| C4 Running misses the criterion | 7, 9 | E5, E7 | Sourced | Medium | Same limits |
| C4a Cause is slow switching | 8 | E6 | Derived | **Low** | Untested (G6) |
| C5 Field study is justified | 9, 11 | C2-C4 | Derived | Medium | n=20 unsupported (G8) |

**Hand-off:** the approved `slide-by-slide.md` is the input to a slide-building tool. This skill does not start that step unless asked.
