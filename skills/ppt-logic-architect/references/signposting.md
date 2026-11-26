# Signposting & Path Integrity

The architecture must read as **one continuous path** that the audience can see. At any slide a listener should be able to answer three questions: where am I in the argument, how did I get here, where am I going next. This file defines the labels and signposts that make that visible, and the check that proves the path has no breaks.

Numbers expose structure; they do not create logic. A deck can be perfectly numbered and still be illogical. The audit still checks the logic (`references/logic-audit.md`); this file checks that the logic is **visible**.

## 1. The hierarchy chain (fixed)

| Level | Marker, Chinese deck | Marker, other languages | What it labels | Its title is | Restarts |
|---|---|---|---|---|---|
| 1 | 一、 二、 三、 | I. II. III. | A section (章节) | The section claim | never |
| 2 | 1 2 3 | 1 2 3 | A slide inside the section | The assertion headline | in each section |
| 3 | 1) 2) 3) | 1) 2) 3) | A point on the slide: a reason, step or piece of evidence | A short claim phrase | on each slide |
| 4 | a. b. c. | a. b. c. | A detail under a point: a datum, condition or example | A label or a value | under each point |

- **Address** of a slide: section marker, then slide number, for example `三·2` (Chinese) or `III·2`. A point: `三·2·1)`. A detail: `三·2·1)a.`. The **page number** (`Slide N` in the card) is the physical position in the deck; the address is the logic position. Keep both, and always quote both when locating something.
- Front matter (title, roadmap) and closing slides (Q&A) are unnumbered. Appendix slides use `附录A` or `Appendix A`, then level 2 and below inside it.
- **Use the language of the deck.** Chinese deck: 一、 for level 1. Any other language: I. The user can override the level-1 glyph; the chain and the other three levels do not change. Never mix styles at one level.
- Four levels is the maximum. If a fifth seems needed, the structure is wrong; split a section or promote a point to a slide.

## 2. Rules (all mandatory)

1. **Marker and title always together.** Never a bare marker, never a title without its marker. Level 1 and level 2 titles are claims (see `references/assertion-evidence.md`), never topic labels: not "三、结果" but "三、结果显示：休息与步行达标，跑步未达标".
2. **A series has at least two items.** No lone `1)`, no `a.` without `b.`. A single item is plain text.
3. **Contiguous and complete.** 一、二、三 with no gaps; 1 2 3 restarting in each section; no skipped level (no `a.` directly under a slide, no `1)` under a section).
4. **Announce the count.** When a parent has N children, say N where the parent is read: "三个依据", "three reasons", "两项检验". Then exactly N markers follow.
5. **Order is a reason, not an accident.** Siblings are ordered by one stated principle: time, process, structure, importance, or cause to effect. If there is no principle, they are not a numbered list; make them a group.
6. **Siblings are the same kind** of thing (horizontal logic). A cause, a method and a metric are not three parallel points.
7. **Size, as a heuristic:** sections 3-5 for most decks (2-6 possible); slides per section 2-6, split a section that goes beyond 6; points per slide 2-4, at most 5; details per point 2-4. State the reason for any exception.
8. **Same label everywhere**: roadmap, tracker, slide, speaker notes, evidence matrix, audit report, hand-off brief. Renumbering one place means renumbering all.
9. **One level-2 claim per slide.** The `1)` points prove it; the `a.` details support their point and nothing else.

## 3. Signposts: what the audience sees

Three jobs: **preview** (where we are going), **position** (where we are), **review** (what we have established).

| Signpost | Job | Where | Content |
|---|---|---|---|
| Roadmap | Preview | Thesis or agenda slide | The level-1 markers with their section **claims**, plus the thesis. Not topics |
| Tracker (breadcrumb) | Position | Every numbered slide, in a fixed place | `三  结果表明…  ›  2`: the current section highlighted among all sections |
| Section opener | Position, relay | First slide of each section; a separate divider slide only when the deck has more than about 12 slides | Marker, section claim, and **one relay line**: the previous section's answer, then this section's question |
| Connector chip | Progression | Every slide except the first | The named relation to the previous slide, from the vocabulary below |
| In-slide numbering | Structure | Slide body | `1) 2) 3)` points, `a. b. c.` details, with the announced count |
| Section recap | Review | Last slide of a section, or the next opener | One line: what is now established |
| Closing recap | Review | Last content slide | The thesis and the level-1 claims, one per marker, in one view |

### Connector vocabulary (one chip per slide)

| Relation | 中文 chip | Use when |
|---|---|---|
| because | 因为 | This slide supplies the reason for the previous claim |
| therefore | 因此 | This slide draws a consequence of the previous one |
| however | 但是 | This slide contrasts, limits or reverses it |
| for example | 例如 | This slide illustrates the previous claim |
| in addition | 此外 | This slide adds a parallel point to the same parent |
| as a result | 于是 | This slide shows what followed from an action or test |
| which raises the question | 那么 | The previous slide leaves a question this one answers |
| so what | 这意味着 | This slide draws the implication of results already established |
| answers (first slide of a section) | 回答 | This slide answers the section's question |
| opens (first slide of the deck) | 开场 | The first slide; it carries the roadmap |
| recap (closing slide) | 回顾 | The closing slide that returns to the thesis |

"接下来 / Next / Moving on" is **not** a relation. If no chip fits, the link is missing.

**First slide of a section.** Its chip reads "answers". The relation to the *previous section* (for example "therefore" or "so what") is not lost: it is shown in the **relay line** at the opener, and it is the relation recorded for that boundary in the path chain table. Within a section, the chip is the relation in the card's field 7.

## 4. Path integrity

The deck is a single path. Build the **path chain table** in Phase 4 and check it in Phase 5.

| From | To | Relation (chip) | Why the second must follow | What the audience sees |
|---|---|---|---|---|
| 一·2 | 二 opener | therefore | The answer to the need (一) creates the question about method (二) | Relay line on the opener |

Include every link in presentation order: title, roadmap, each section opener, each slide, each recap, the close. Then check:

1. **No blank link** and no topic-only link ("next, we look at X").
2. **No dead end and no orphan**: every slide is led to by the one before it and leads to the one after it (appendix slides lead back to the slide they support).
3. **Section boundaries**: the last slide of section N and the opener of section N+1 are joined by a relay: the answer N gives creates the question N+1 asks.
4. **First slide of a section answers the section's question** (chip: 回答). **The close returns to the thesis.**
5. **Listener test**: read only the signpost outline (markers, titles, chips). It must reproduce the argument without any slide body.
6. **Parallel points** under one parent are the same kind, and their order has a stated reason.
7. **Backward references** say so: "回到 一·2" / "back to I·2".

## 5. The signpost outline (a Phase 3 and Phase 6 output)

A nested outline of markers, titles and chips, readable on one page. Draft it in Phase 3 with sections only; complete it in Phase 4 with slides. Example (fictional data):

```
一、采样占整机功耗的 62%，所以它是节能的正确目标            [开场]
   1 采样占固定速率监测器平均功耗的 62%                       [因为]
   2 自适应方案按运动强度在 25/50/100 Hz 间切换                [例如]
二、两项检验分别回答能耗与精度两个问题                       [那么]
   1 台架测功耗，8 人试验测精度，判据由导师事先设定            [回答]
三、结果：休息与步行达标，跑步未达标                         [因此]
   1 台架轨迹上平均功耗下降 34%                               [回答]
   2 休息与步行精度在 3 bpm 判据以内                          [因此]
   3 跑步精度超出判据（4.6 bpm）                              [但是]
   4 慢切换可能是原因（假设，未检验）                         [因为]
四、证据支持范围受限的外场试验                               [因此]
   ...
```

The same outline, with page numbers added, is the table of contents the speaker can carry.

## 6. Applying it, by mode

- **CREATE.** Phase 3: assign level-1 markers with claim titles, the relay between sections, and the draft signpost outline. Phase 4: add level-2 labels, connectors, in-slide structure and the path chain table. Phase 5: run the path integrity checks. Phase 6: the outline goes into `master-outline.md`, the table into `slide-by-slide.md`.
- **RESTRUCTURE.** The old-to-new mapping gives the old page number and the **new address**. The original numbering, if any, is recorded as found; do not discard it silently.
- **AUDIT.** Report numbering and path problems as findings with both the page number and the deck's own label (or "unlabelled"). Do not renumber the deck; describe the fix. A deck with no hierarchy at all is a finding, not a reason to refuse the audit.

## 7. Severity for signposting findings

| Level | Examples |
|---|---|
| **Major** | No visible sections in a deck of more than about 10 slides; a section boundary with no relay; the numbering contradicts the real logic (a list numbered as a sequence that is not one); a dead end or orphan on the main path |
| **Minor** | A lone `1)`; mixed marker styles; a skipped number; a topic-label section title; a connector that is not a relation; a count announced as three with two items |

A broken path that makes the argument impossible to follow is Major even when every individual slide is sound.

## 8. Pitfalls

- **Numbering as decoration.** Markers on a pile of topics.
- **Topic titles under a marker**: "一、背景  二、方法  三、结果". The structure is visible; the claims are not.
- **Different numbering in the agenda and on the slides.**
- **Deep nesting** to look rigorous. Four levels is the ceiling, not the goal.
- **Lists that are not lists**: `1) 2) 3)` over items with no common parent claim.
- **Sequence implied, none exists**: numbers that suggest an order the content does not have.
- **Signposts only in the speaker's head.** If the audience cannot see the marker, tracker and chip, they do not exist.
