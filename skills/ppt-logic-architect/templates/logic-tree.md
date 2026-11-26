# Logic Tree

> Template. The tree is the argument: a thesis, the arguments that must hold for it, and the evidence under each. Every leaf links to an evidence item (`E#`) or a gap (`G#`). Delete guidance lines in the final file.

**Thesis (C0):** <one sentence>
**Central question:** <...>
**Grouping principle at the top level:** <e.g. "Logical grouping by stage of the argument">

## Tree

```
C0  <thesis>                                         [Confidence: High|Medium|Low]
├── C1  <supporting argument 1: a conclusion, not a topic>   [Conf]
│   │   Answers: "<the question C0 raises>"
│   │   Grouping: MECE within <whole> by <basis> | logical grouping by <criterion>; overlap by design
│   ├── C1.1  <sub-claim>                            [Conf]
│   │   ├── E1  <evidence>  (S1, loc)
│   │   └── E2  <evidence>  (S2, loc)
│   └── C1.2  <sub-claim>                            [Conf]
│       └── G1  <missing evidence>                   (gap)
├── C2  <supporting argument 2>
│   └── ...
└── C3  <supporting argument 3>
    └── ...
```

> Rules:
> - Each node is a **claim** written as a sentence, never a topic label.
> - A parent must follow from its children (vertical logic); siblings must be the same kind of thing (horizontal logic).
> - Mark the type of inference between parent and children: **deductive** or **inductive**.
> - A branch with no evidence gets a `G#`, not a placeholder.

## Vertical logic check

| Parent | Question it raises | Do the children answer it? | Note |
|---|---|---|---|
| C0 | <e.g. "Why should we believe this?"> | Yes / Partly / No | <...> |
| C1 | <...> | <...> | <...> |

## Warrants

> For each key link: why does this evidence support this claim?

| Claim | Evidence | Warrant (why the evidence supports the claim) | Qualifier (scope) | Rebuttal (what would break it) |
|---|---|---|---|---|
| C1.1 | E1, E2 | <...> | <population, conditions> | <...> |

## Anticipated objections

| Objection | Where the tree answers it | Status |
|---|---|---|
| <what a sceptic would say> | C#/slide # | Answered / Partly / Unanswered |

## Mapping to sections

> A branch maps to a level-1 section (marker `一、`), its sub-claims to level-2 slides (address `一·2`), and its evidence to level-3 points (`1)`) and level-4 details (`a.`). Use the same labels as the slide cards (`references/signposting.md`).

| Branch | Section (marker) | Slide addresses (pages) | Points on the slides |
|---|---|---|---|
| C1 | 一、S1 | 一·1 to 一·4 (p.3-6) | 一·2: 1) E1, 2) E2 |
