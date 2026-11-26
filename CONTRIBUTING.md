# Contributing

Thanks for helping improve `ppt-logic-architect`. This project is a skill, so the product is **agent behavior**. Most changes are edits to Markdown that change how an agent reasons. Please test them that way.

## Ground rules

1. **One source of truth.** The skill lives only in `skills/ppt-logic-architect/`. Do not create per-tool copies. Installers copy or link this folder.
2. **Keep `SKILL.md` lean.** It routes and sets rules. Method detail belongs in `references/`, loaded on demand.
3. **Use only portable frontmatter fields** in `SKILL.md`: `name`, `description`, `license`, `metadata`, `allowed-tools`. These are defined by the Agent Skills specification and accepted by Codex's own validator. The spec also defines `compatibility`, but Codex's validator rejects it, so it is not used here. Tool-specific extensions do not belong in the shared file; Codex UI settings go in an optional `agents/openai.yaml`, never in `SKILL.md`.
4. **Relative links must resolve.** Every path in `SKILL.md` and `references/` is relative to the skill folder.
5. **Never put fabricated data in non-example files.** Examples must say they are fictional.
6. **Keep the principles.** Logic before layout, evidence before conclusion, human approval, no premature generation, one visible path. A change that weakens a principle needs a strong argument.
7. **Keep the signposting standard intact.** The hierarchy (一、→ 1 → 1) → a.), claim titles, connectors and relay lines are defined once, in `references/signposting.md`. If you change a level, a marker or the connector vocabulary, change it there and in `SKILL.md`, `templates/slide-by-slide.md`, both worked examples and TC10 together.

## Adding or changing a methodology

1. Add `skills/ppt-logic-architect/references/<name>.md`. Cover: what it is, when it fits, **when it does not**, how to apply it, pitfalls, and what it adds to the output.
2. Register it in `references/method-selection.md` (selection table, fit test).
3. Add a row to the "Which references to load" table in `SKILL.md`, so the agent loads it only when needed.
4. If it changes a deliverable, update the matching file in `templates/`.
5. Add or update at least one test case in `evals/test-cases.md` that fails without your change.

A methodology that is meant to apply to every deck is probably too broad. The skill is built on selecting methods by fit.

## Adding a project-type module

Follow `references/design-research-reasoning.md`: define the chain, the checks, the evidence types, the typical breaks, and per-type variants. Route to it from `SKILL.md`.

## Testing a change

1. Run the static check: `python scripts/validate.py`.
2. Run the cases in `evals/test-cases.md` that your change could affect, at least twice each, on at least one agent. Record results as described in `evals/expected-behavior.md`.
3. In the pull request, state which cases you ran and what changed in the behavior.

A static check passing does **not** mean the behavior is right.

## Style

- Plain, direct English. Short sentences. Tables for choices, lists for steps.
- State rules as observable behavior ("Do not delete a slide without a stated reason"), not attitudes ("be careful").
- Write for an agent reading it cold: define terms, give an example where a rule is subtle.
- Keep field labels in English even when output is in another language, so output stays checkable.

## Commits and pull requests

- Small, focused commits. Describe the behavior change, not just the file.
- Update `CHANGELOG.md` under `[Unreleased]`.
- Do not include real project data, personal information, or credentials.

## Reporting problems

Open an issue with: the agent and version, the input (redacted if needed), what the skill did, and what you expected. Transcripts of a failed test case are the most useful report.
