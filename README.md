# PPT Logic Architect

**An Agent Skill that designs the logic of a presentation before anyone opens slide software.**

Give it raw notes, data, papers, or an existing deck. It extracts what is actually known, builds a thesis and an argument tree, orders the sections with explicit progression, specifies every slide, and audits the whole thing for logical gaps. It stops for your approval after each phase. It does not make slides.

中文说明见 [README.zh-CN.md](README.zh-CN.md).

> **Status: v0.1.0.** The skill passes static validation (structure, frontmatter, references). The behavioral test cases in `evals/` are written but have not yet been run against a live agent. See [Testing](#testing) and [Limitations](#limitations).

## What problem it solves

Most weak presentations are not weak visually. They are weak in the argument: the thesis is a topic, the order follows the author's notes, the conclusion is stronger than the data, and no one can say why slide 14 exists. Fixing the layout does not fix any of that.

This skill works on the part that comes first:

- What is the deck actually claiming, and is that claim supported by the evidence you have?
- In what order must the audience hear it, and why does each step follow from the last?
- Which slides carry the argument, which repeat it, and which do nothing?

## How it differs from a PPT generator

| | PPT generators | PPT Logic Architect |
|---|---|---|
| Output | A `.pptx`, styled slides | Markdown architecture: thesis, logic tree, slide cards, evidence matrix, audit report |
| Starting point | A topic or a prompt | Your material, classified as fact, data, claim, assumption, open question |
| Headlines | Topic labels, often | Full-sentence assertions with matched evidence |
| Evidence | Filled in to look complete | Never invented. Missing evidence becomes a recorded gap |
| Existing decks | Re-skinned | Audited or restructured, with every original slide mapped |
| Control | One shot | Six phases, each ending in an approval gate |
| Frameworks | One template for everything | Chosen by purpose and audience, and the choice is justified |

It is meant to sit **upstream** of a slide-building tool: its approved `slide-by-slide.md` is a good input for one.

## Three modes

| Mode | Use it when | You get |
|---|---|---|
| **CREATE** | You have scattered material and no deck | A full architecture, built phase by phase |
| **RESTRUCTURE** | You have a deck or outline that flows badly | A new structure plus an old-to-new mapping of **every** original slide |
| **AUDIT** | You want a review and no rewriting | Findings rated Critical / Major / Minor, each with location, cause, impact, and fix direction |

## The six phases

| Phase | Name | Ends with |
|---|---|---|
| 1 | Intake & Diagnosis | Source register, classified evidence, brief, early gaps |
| 2 | Thesis & Argument Architecture | Scoped thesis, method decision, logic tree |
| 3 | Section Architecture | Ordered sections, named progression between them |
| 4 | Slide-by-Slide Architecture | One complete card per slide |
| 5 | Logic Audit | Findings, fixed at their source |
| 6 | Final Architecture Delivery | Five Markdown files |

Every phase ends with a gate: the goal, the result, what is unresolved (marked `BLOCKING` or `CAN PROCEED`), at most three decisions with recommended defaults, and the next step. The agent waits. You can skip a phase you have already done, go back to an earlier one, or ask for several phases at once with one gate at the end.

## What a slide card contains

Every slide gets all ten fields: Slide Number, Section, Action-oriented Headline, Core Message, Supporting Evidence, Reason for Inclusion, Logical Relationship with Previous Slide, Transition to Next Slide, Suggested Visual Form, and Evidence Source / Confidence. A title and a few keywords are not a card.

## Methodology

Loaded on demand, not all at once:

- **Pyramid Principle**: top-down argument, vertical and horizontal logic
- **SCQA**: situation, complication, question, answer; used only where a real complication exists
- **Assertion-Evidence**: claim headlines backed by evidence
- **MECE**: only for lists that really are partitions; otherwise honest "logical grouping"
- **Evidence-Based Reasoning**: claim, evidence, warrant; fact versus inference; source tracking; gaps
- **Logic Audit**: validity, causality, transitions, redundancy, contradictions, missing links
- **Design Research & Engineering Reasoning**: the chain from research question to validation, with eight checks (see below)

A method-selection guide decides which of these apply. The skill is built to refuse forcing MECE onto overlapping ideas or SCQA onto an audience that already knows the context.

### Design research and engineering module

For industrial design, interaction design, product-service systems, hardware prototyping, HCI, engineering research, portfolios, and defenses. It checks the chain Research Question, Method, Findings, Insights, Requirements, Concepts, Feasibility, Prototype, Testing, Iteration, Final Solution, Validation, and asks:

1. Do the findings support the insight?
2. Can each insight become a requirement?
3. Do the requirements explain the chosen design?
4. Is the technical route backed by feasibility evidence?
5. Did the prototype verify the key hypothesis?
6. Do the test results support the conclusion?
7. Is there a jump from research straight to form?
8. Is an untested hypothesis presented as a finding?

## Install

You need the skill folder `skills/ppt-logic-architect/`. It is plain Markdown: no scripts, no network, no packages.

```bash
git clone <your-fork-or-clone-url> ppt-logic-architect
cd ppt-logic-architect

./install/install.sh --target claude     # Claude Code: ~/.claude/skills/
./install/install.sh --target codex      # Codex: ${CODEX_HOME:-~/.codex}/skills/
./install/install.sh --target all --dry-run   # preview first
```

Or copy the folder yourself: put `skills/ppt-logic-architect/` into your agent's skills directory, so that `SKILL.md` sits at `<skills-dir>/ppt-logic-architect/SKILL.md`. The folder name must equal the skill name.

Start a **new** session afterwards so the agent re-scans its skills. Details and path verification notes: [install/install-claude-code.md](install/install-claude-code.md), [install/install-codex.md](install/install-codex.md).

On Windows without Git Bash or WSL, copy the folder manually with File Explorer or PowerShell; the guides show both.

## Use it in Claude Code

Ask in plain language, or name the skill:

```text
Use ppt-logic-architect to build a presentation structure from the notes in ./research/.
Use ppt-logic-architect to restructure deck-outline.md. Keep everything useful.
Use ppt-logic-architect in AUDIT mode on thesis-defense.pptx. Do not rewrite it.
```

Some Claude Code versions may also expose installed skills as a `/ppt-logic-architect` command; this has not been verified for this skill.

## Use it in Codex

```text
$ppt-logic-architect  Build a presentation structure from the notes in ./research/.
Use $ppt-logic-architect to audit the logic of slides.md. Do not rewrite.
```

Codex also selects skills from their descriptions, so a request like "check the logic of my defense deck" can trigger it without naming it.

## Trigger each mode

The skill reads your request and says which mode it chose. To force one, say so:

| Mode | Phrases that route to it |
|---|---|
| CREATE | "build a PPT outline from these notes", "turn my research into a storyline", "plan the slides" |
| RESTRUCTURE | "restructure this deck", "fix the flow", "reorganize the sections", "keep everything useful" |
| AUDIT | "audit", "review the logic", "is this argument sound", "find the problems", "don't rewrite" |

If it is unclear whether you want RESTRUCTURE or AUDIT, it defaults to AUDIT (which changes nothing) and offers RESTRUCTURE afterwards.

## What gets written

Phase 6 writes five files, by default into `./ppt-architecture/`, never overwriting existing files without asking:

| File | Content |
|---|---|
| `master-outline.md` | Brief, thesis, method decision, sections, progression, headline chain, decision log |
| `logic-tree.md` | The argument tree with evidence links, warrants, and objections |
| `slide-by-slide.md` | Every slide card, plus the old-to-new mapping in RESTRUCTURE |
| `evidence-matrix.md` | Sources, evidence items, claim-to-evidence map, assumptions, gaps |
| `logic-audit-report.md` | Findings by severity and their resolution |

Fully worked examples, using fictional data, are in [`skills/ppt-logic-architect/examples/`](skills/ppt-logic-architect/examples/): a research progress review and an industrial-design jury review.

## Extend the methodology

1. Add `skills/ppt-logic-architect/references/<your-method>.md`: what it is, when it fits, **when it does not**, how to apply it, pitfalls.
2. Register it in `references/method-selection.md`.
3. Add a row to the "Which references to load" table in `SKILL.md`.
4. Add a test case in `evals/test-cases.md` that fails without it.

Add a new project-type module (for example clinical research or legal argument) by following `references/design-research-reasoning.md`. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Compatibility

The skill is a single folder with a `SKILL.md` whose frontmatter uses only fields accepted by both the Agent Skills specification and Codex's skill validator (`name`, `description`, `license`, `metadata`). One source folder serves every tool; installers copy or link it.

Requirements: the agent must be able to read the files you point to. File-write access is only needed for the Phase 6 deliverables; without it the agent prints them in chat. Reading `.pptx` directly depends on the agent being able to run code (for example `python-pptx`); otherwise export an outline or PDF.

## Testing

Two layers, deliberately separate:

- **Static** (`python scripts/validate.py`): frontmatter fields and limits, name equals directory, every relative reference resolves, all ten card fields are present, examples are complete and labelled fictional. This proves the package is well-formed. It proves nothing about behavior.
- **Behavioral** ([`evals/test-cases.md`](evals/test-cases.md)): eight cases with seeded flaws (scattered notes with conflicting numbers, a messy deck with duplicates, a design project that jumps from research to form, a technical result within instrument error, an over-claimed conclusion, redundant slides, gate and skip handling, and pressure to fabricate). Each has observable must / must-not lines and an answer key in [`evals/expected-behavior.md`](evals/expected-behavior.md).

## Limitations

- Behavioral test cases have been written but not yet run on a live agent in this release. Treat the first runs as part of validation and report failures.
- Output quality depends on the underlying model following a long instruction set. Weaker models may skip gates or soften findings; the test cases are designed to expose that.
- The skill reasons about structure and evidence. It cannot verify that a source is real or that a number is correct, and it will say when it could not read something.
- It does not generate slides, speaker scripts, or visuals.

## Suggested GitHub repository metadata

**Description:** An Agent Skill that designs the logic of a presentation before any slides exist: thesis, argument tree, slide-by-slide architecture, and logic audit. For Claude Code, Codex, and other Agent Skills tools.

**Topics:** `agent-skills`, `claude-code`, `codex`, `presentation`, `pptx`, `storytelling`, `pyramid-principle`, `logic`, `design-research`, `ai-agents`

## License

MIT. See [LICENSE](LICENSE).
