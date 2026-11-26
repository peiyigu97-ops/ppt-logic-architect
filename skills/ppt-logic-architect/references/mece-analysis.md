# MECE Analysis

**Mutually Exclusive, Collectively Exhaustive.** A check for lists that claim to partition a whole: no overlap between items, and no gap in the whole. Commonly attributed to Barbara Minto and popularized in consulting.

MECE is a tool for specific situations. It is not a universal standard for good structure.

## 1. The two conditions

| Condition | Meaning | Test |
|---|---|---|
| **Mutually exclusive** | Each item belongs in one category only | Can a single instance fit two buckets? If yes, the boundary is unclear |
| **Collectively exhaustive** | Together the categories cover the whole | What real instance fits none? If any, there is a gap |

## 2. Classification basis

A MECE split needs **one principle of division** applied consistently.

- Good: costs split by *phase* (design, tooling, production), one basis.
- Bad: users split into "students, elderly, tech-savvy". Three different bases (occupation, age, attitude).

Steps:
1. Name the **whole** being divided ("all causes of battery drain in the prototype").
2. Choose one **basis** ("by subsystem").
3. List categories and give each a **boundary rule** (what is in, what is out).
4. Run the overlap test and the gap test.
5. If an "Other" bucket is needed, state it. Keep it small; a large "Other" means the partition is incomplete.

## 3. Same-level discipline

Categories must be at the same level of abstraction. "Hardware, software, and the battery" mixes levels (the battery is part of hardware).

## 4. Where MECE fits

- Causes of a problem; subsystems of a product; stages of a process.
- Option sets: "the realistic ways to meet requirement R".
- Risk and failure-mode categories.
- Segments with a clear, countable basis.
- Cost breakdowns.

## 5. Where it does not, and what to do instead

- **Ideas, themes, user needs**: these overlap by nature. A need can be both functional and emotional.
- **Chronological narratives**: sequence is the structure.
- **Exploratory findings**: patterns emerge and cross-cut.
- **Wholes that cannot be defined**: "exhaustive" has no meaning without a bounded whole.

In these cases, use **logical grouping with an explicit criterion**, and write "Grouped by <criterion>; categories overlap by design; not MECE". That is an honest and acceptable result. Do not force the split.

## 6. Declaring scope

Exhaustiveness is relative to a defined whole. Say it: "Exhaustive within the six subsystems listed in S2." If the whole is open-ended, do not claim "collectively exhaustive"; say "main categories".

## 7. Pitfalls

- **Overlap hidden by vague labels** ("Quality" and "Reliability").
- **A fake third category** added to reach three.
- **"Other" as a dump** for anything awkward.
- **Exhaustive claim with no reference set**.
- **Using MECE to hide the lack of an argument**: a neat partition of topics is not a thesis.

## 8. Output

In the logic tree, add a line to each group: `Grouping: MECE within <whole> by <basis>` or `Grouping: logical grouping by <criterion>; overlap by design`.
