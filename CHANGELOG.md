# Changelog

All notable changes to this project are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.2.0] - 2026-11-26

### Added
- Optional visual hand-off to the [visual-explainer](https://github.com/nicobailon/visual-explainer) skill: `references/visual-handoff.md` and `templates/visual-brief.md`. It starts only after Phase 6 approval and an explicit request, and carries the evidence discipline into the visuals (no new facts, headlines verbatim, confidence and gaps visible, output checked against the brief).
- Test case TC9 (hand-off gate, missing companion, fidelity, PPTX and in-place-edit honesty) and behavior B19.
- Companion install steps in both install guides.

### Changed
- `SKILL.md` description and "Do not" rule: the skill still never draws or builds slides itself; visuals go only through the hand-off.

### Known limits
- visual-explainer's `--pptx` export is best-effort and drops SVG, figures and captions. Neither skill edits an existing `.pptx` in place. The integration was checked against visual-explainer v0.16.0's documentation and has not been run end to end.

## [0.1.0] - 2026-11-26

### Added
- `ppt-logic-architect` skill (`skills/ppt-logic-architect/SKILL.md`) with three modes: CREATE, RESTRUCTURE, AUDIT.
- Six-phase workflow with a mandatory approval gate after each phase, skip and go-back handling, and a `PHASE-STATE` record.
- Reference files, loaded on demand: phase protocol, one file per mode, method selection, Pyramid Principle, SCQA, Assertion-Evidence, MECE, Evidence-Based Reasoning, Logic Audit, and Design Research & Engineering Reasoning.
- Templates: `master-outline.md`, `logic-tree.md`, `slide-by-slide.md`, `evidence-matrix.md`, `logic-audit-report.md`.
- Two worked examples (research progress review; industrial design jury review), both using fictional data.
- `evals/`: eight behavioral test cases with seeded flaws, an answer key, and scoring rules.
- Installation guides for Claude Code and Codex, and `install/install.sh`.
- English README and Chinese usage guide.
