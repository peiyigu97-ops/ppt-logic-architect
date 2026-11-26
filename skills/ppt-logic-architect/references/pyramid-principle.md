# Pyramid Principle

A top-down way to structure an argument: one governing thought at the top, supported by a small number of arguments, each supported by evidence. Associated with Barbara Minto's *The Minto Pyramid Principle*.

## 1. The structure

```
Governing thought (the thesis: the answer to the audience's question)
├── Supporting argument A  (answers: "Why / how do you know?")
│   ├── Evidence A1
│   └── Evidence A2
├── Supporting argument B
│   └── ...
└── Supporting argument C
```

In a deck: thesis = the main message; sections = supporting arguments; slides = evidence and sub-arguments. Each slide headline is a node.

## 2. Vertical logic

Every node answers a question raised by the node above it ("Why?", "How do we know?", "What does that mean?"). Read downward as a conversation: parent states, child answers the sceptic.

Tests:
- **Question test**: write the question each level raises. If the children do not answer it, the structure is wrong.
- **Conclusion test**: the parent must be a conclusion *drawn from* its children, not a label for them. "Market factors" is a label. "Demand is shifting to refills" is a conclusion.
- **Removal test**: remove one child. If the parent still follows, the child may be redundant. If the parent no longer follows with all children present, something is missing.

## 3. Horizontal logic

Siblings under one parent must be the same kind of thing and form a recognizable argument. There are two valid forms:

| Form | Pattern | Check |
|---|---|---|
| **Deductive** | Rule, case, conclusion; each step follows from the one before | Is each step true, and does the conclusion follow from them? |
| **Inductive** | Several parallel observations, each pointing to the same conclusion | Are the observations of the same type, and do they truly share the conclusion? |

Group by one stated criterion: time order, structure (parts of a whole), degree (importance), or process. If the siblings cannot be grouped under a single criterion, the parent is probably wrong.

## 4. Grouping

- Keep each group small: usually two to five items. This is a heuristic for readability, not a rule. If a group has more, look for a higher-level grouping; if it has one, the child is probably the parent restated.
- Order siblings on purpose (time, structure, importance) and say which.
- Each group gets a summary insight ("so what?") rather than a topic name.

## 5. Applying it

1. Write the central question the audience will ask.
2. Write the answer in one sentence: that is the governing thought.
3. List the arguments that must hold for the answer to be believed.
4. Under each, list the evidence you actually have. Evidence you do not have is a `G#`.
5. Check vertical and horizontal logic.
6. Map the tree to sections and slides.

Write the result in `templates/logic-tree.md` format.

## 6. Pitfalls

- **Labels instead of conclusions** at every level.
- **Mixed abstraction levels** among siblings (a goal beside a tactic beside a metric).
- **Forced symmetry**: three arguments when the material gives two, padded.
- **Bottom-up ending**: the audience gets the data first and a conclusion at slide 28, when the decision-maker has left.
- **Answer unsupported by its children**: the top is bold and the branches are weak. Narrow the top.

## 7. When it fits and when it does not

Fits: decision-oriented, time-pressed audiences; any deck that makes an argument.
Weak fit: exploratory talks, teaching sequences, narratives where the order of discovery matters. Use it at the section level only, and say so.
