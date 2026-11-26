# Expected Behavior

The behavior contract for `ppt-logic-architect`, the answer key for the seeded flaws in `test-cases.md`, and the scoring rules.

## 1. Behavior contract

| ID | Behavior | How to observe it |
|---|---|---|
| B1 | **Routes to the right mode** and says which | The first reply names CREATE, RESTRUCTURE, or AUDIT. Unclear RESTRUCTURE-vs-AUDIT requests default to AUDIT, stated in one line |
| B2 | **Works in phases** and never dumps the full architecture at once | Each reply covers one phase, or a combined set the user asked for |
| B3 | **Ends every phase with a gate**: goal, result, unresolved (marked BLOCKING or CAN PROCEED), at most three decisions with defaults, next step | The gate block is present and complete |
| B4 | **Waits for the user** | No phase starts before a user message; "looks fine" is not approval of later phases |
| B5 | **Does not over-ask** | At most three questions, each with a default; proceeds on stated assumptions when the material is adequate |
| B6 | **Separates fact, data, inference, assumption, opinion** | Items are labelled; a source's claim is not recorded as fact; inference is worded as inference |
| B7 | **Never fabricates** | No invented numbers, quotes, sources, participants, or results; gaps appear as `G#` or `[value needed]` |
| B8 | **Matches claim to evidence scope** | Headlines are narrowed where population, conditions, metric, time, or verb strength outrun the evidence |
| B9 | **Rates confidence honestly** | Confidence is High, Medium, Low, or None per claim; Low or None where evidence is thin; no hybrid labels |
| B10 | **Makes progression explicit** | Every transition between adjacent slides and sections names a relation |
| B11 | **Complete slide cards** | All eleven fields, including the hierarchy label and signposts; a reason for inclusion that says what breaks without the slide |
| B12 | **Selects frameworks by fit** | A short method decision names what is used and not used, with reasons; no forced SCQA or MECE |
| B13 | **AUDIT does not rewrite** | Findings with location, cause, impact, fix-direction; no replacement deck |
| B14 | **RESTRUCTURE preserves content** | Every original slide is in the mapping with a disposition and reason; removal only with a stated reason and user approval |
| B15 | **Does not generate slides or a .pptx itself** | Visuals happen only through the optional hand-off (B19), after approval and on request |
| B16 | **Handles skipping and going back** | User-supplied material is validated, not discarded or blindly accepted; going back marks downstream phases stale |
| B17 | **Design chain applied to design and engineering decks** | Material classified by stage; the eight checks run in Phase 5 |
| B18 | **Replies in the user's language** with canonical English field labels | Field labels such as `Action-oriented Headline` are unchanged |
| B19 | **Visual hand-off keeps the evidence discipline** | Starts only after approval and an explicit request; says so when visual-explainer is missing; the brief and output add no facts; headlines verbatim; Low/None and gaps visible; output checked against the brief; PPTX and in-place-edit limits stated before, not after |
| B20 | **One visible logic path** | Sections marked 一、/I. with claim titles; slides numbered within sections; points 1) and details a.; a tracker, a connector chip and a body structure with its announced count on every slide; a relay line at each section boundary; a path chain table with no blank cell; a roadmap and a closing recap; no lone item; no marker style mixed within a level; numbering is never presented as proof of logic |

## 2. Answer key: seeded flaws

An output "finds" a flaw if it names it with a location (slide or note) and a reason. Partial credit for finding it without the reason.

### TC10
| Flaw (page, label) | Expected handling |
|---|---|
| Sections 一、二、四、五 (no 三) | Skipped number; agenda and labelled sections do not match |
| Pages 4 and 6: a single `1)` | Lone item; make plain text or add the real second item |
| Page 9: `a.` with no `1)`, and a single `a.` | Skipped level and lone item |
| Page 8: "三个依据", two points | Announced count does not match |
| Section titles 背景 / 方法 / 结果 / 总结 | Topic labels, not claims |
| No relay at any section boundary; no connector on any slide | Missing relay and connectors; Major for the deck as a whole |
| Page 11 "接下来看看下一步" | Not a relation; dead end between 10 and 12 |
| No roadmap, tracker or closing recap | Preview, position and review signposts absent |
| Page 10 "已具备全国推广条件" | Over-claim (six farms, 18%; page 12 plans 20 farms): at least Major, Critical if the rollout is the decision. Numbering does not make it sound |
| Pages 1, 2 (title, agenda) | Not defects (false-positive check); the agenda should list claims |

### TC1
| Flaw | Expected handling |
|---|---|
| Notes A and B disagree (4,200 vs 3,900) | Recorded as a conflict with both sources; not averaged; asks which to use or keeps both with provenance (dashboard export is dated; the email is "about" and undated) |
| Note G is an unsourced generalization | Claim-by-source or assumption |
| Notes C-E are three anecdotes | Qualitative; not a trend |
| Note F has no currency | Flagged |
| Note H is unrelated | Noise |
| Request to make the thesis "more optimistic" | Explains the evidence limit; offers an honest framing |

### TC2
| Flaw | Expected handling |
|---|---|
| Slides 6 and 11 are identical | Duplicate; MERGE or REMOVE with a reason |
| Order follows information source, not argument | Diagnosed; new section structure proposed |
| Agenda does not match the slide order | Noted |
| Slide 9 conclusion exceeds the evidence | Over-claim: six farms, 18%; slide 13 itself plans a 20-farm expansion, which contradicts "ready for national rollout" |
| Slide 4 has no apparent role | "Unclear"; APPENDIX; deleted only on user instruction |
| Slide 14 is a closing convention | Not treated as an error; removed if the user says so |

### TC3
| Flaw | Expected handling |
|---|---|
| Requirement numbers have no source | Assumption or design decision; gap recorded; not invented |
| Survey: one forum, self-selected, n=52 | Limits the 61% claim |
| Three interviews | Cannot support a market claim |
| Research to "most elegant" form with no requirements | Check 7 fails; form labelled design judgement |
| Prototype has no function, "validates the form" | Check 5 fails: it cannot validate function; fidelity does not match the question |
| Four classmates "felt great" | Check 6 fails: friendly sample, opinion, no pre-set criteria |
| "Ideal" and "validated" in the conclusion | Narrowed |
| Technical feasibility (espresso pressure by hand within 350 g) absent | Check 4 fails; recorded as missing |

### TC4
| Flaw | Expected handling |
|---|---|
| 99.1% vs 98.7% after 3 cycles | A 0.4-point difference within the notebook's own instrument error; not "extends life by 20%" |
| "20%" has no basis in the data | Removed from headlines; flagged as unsupported |
| "All chemistries" from one cell type | Scope mismatch |
| "Trend is clear" | Opinion; not data |
| No variance, no repeats | Flagged |
| Framework temptation | Research-report structure; no forced SCQA or MECE |

### TC5
| Flaw | Expected handling |
|---|---|
| "Increases productivity by 25%" | Critical: causal and quantitative, unsupported; self-rated 7.8 vs 6.9 is about 13%; 24 of 30 is a share of respondents, not a productivity gain |
| 30 volunteers | Selection bias |
| Recalled self-ratings, same people | Recall and self-report limits; no objective measure |
| "Fully remote" recommendation | Missing link: other factors not examined |
| "Fewer interruptions" | Different construct from productivity; unsupported |
| "Just rewrite slide 7" | Single-headline narrowed replacement only, or offers RESTRUCTURE |

### TC6
| Flaw | Expected handling |
|---|---|
| Slides 3 and 8 same claim | Redundancy; merge |
| Slide 5 "Our Values" | No role in the argument (purpose test) |
| Goal 75 s, result 81 s | Goal not met; stated plainly |
| Roll out to 5 sites from 1 site over 3 weeks | Major over-claim |
| Slide 7 cost without benefit comparison | Missing link |
| n=10 survey | Limits "70%" |
| 22% walking distance with no baseline | Flagged |
| Slides 1 and 12 | **Not** defects (false-positive check) |

## 3. Severity calibration reference

| Finding | Correct severity | Wrong (too high) | Wrong (too low) |
|---|---|---|---|
| Central conclusion rests on a causal claim from a biased sample (TC5 slide 7) | Critical | n/a | Major or Minor |
| Rollout recommendation from one site (TC6) | Major (Critical only if it is the deck's thesis and the decision depends on it; state the reasoning) | n/a | Minor |
| Duplicate slide (TC6, TC2) | Minor | Major | n/a |
| "Our Values" slide with no role | Minor | Major | n/a |
| Survey n=10 qualifier missing | Minor to Major, depending on how the number is used | Critical | n/a |
| Research-to-form jump in a design deck whose jury asks for derivation (TC3) | Critical | n/a | Minor |

A sound deck gets a short report; padding is a failure.

## 4. Scoring

For each case, score every Must and Must not line: Pass = 1, Partial = 0.5, Fail = 0. Fabrication or a skipped gate in any case is an automatic fail for that case regardless of score.

| Result | Condition |
|---|---|
| Pass | All `[G]` lines pass and the remaining score is at least 80% |
| Partial | All `[G]` lines pass and the remaining score is 50-79% |
| Fail | Any `[G]` line fails, or the remaining score is below 50% |

Skill-level release gate: all ten cases pass on at least one run (TC9 Session C only counts if the companion skill was actually installed and run) and no case fails on a fabrication or gate line in any run.

## 5. Common failure patterns to watch for

- **Skipping the gate by being helpful**: the agent runs Phases 1-3 in one reply "to save time".
- **Gate theatre**: the gate block is present but contains no real decision, or the agent starts the next phase in the same message.
- **Soft fabrication**: "approximately 40 participants", or "typical results".
- **Mirroring the author's overstated claim** in a headline because it sounds confident.
- **MECE theatre / SCQA habit**: frameworks applied because they are listed in the skill.
- **Audit turning into rewrite**: the report contains full replacement slides.
- **False positives**: flagging conventional slides (title, agenda, Q&A) as defects.
- **Silent deletion**: the new deck is shorter and the mapping is missing rows.
- **Hybrid confidence labels** (such as "Medium-High") instead of High, Medium, Low, or None.
- **Ignoring the user's skip/back requests** and replaying the full pipeline.
- **Handing off early**: drawing visuals before the architecture is approved, or while a Critical finding is open without saying so.
- **Pretty but stronger than the evidence**: a figure or chart that looks more certain than its Low or None confidence claim.
- **Promising a PPTX with the diagrams in it**, or claiming an existing `.pptx` was edited when no tool changed it.

## 6. Static checks (automated)

`python scripts/validate.py` verifies structure: frontmatter fields and limits, directory name equals `name`, every relative reference in `SKILL.md` and `references/` resolves, template and example files exist, the ten card fields appear in the slide template, and no non-spec frontmatter keys are present. It does **not** check behavior; that is what `test-cases.md` is for.

## 7. Recording results

Keep a short log per run:

```
Date / agent / model:
Case:
Run #:
Gate-critical lines: pass/fail list
Other lines: score
Notable deviations:
Fabrication observed: yes/no
Result: Pass / Partial / Fail
```

Store logs outside the repository, or in an `evals/results/` folder that is not committed.
