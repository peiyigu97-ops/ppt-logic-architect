# Changelog

All notable changes to this project are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.3.0] - 2026-11-26

### Added
- **Signposting standard**: a fixed four-level hierarchy on every deck (一、→ 1 → 1) → a. for a Chinese deck; I. → 1 → 1) → a. otherwise), with claim titles, an address for every slide (for example `三·2`), a tracker, a named connector chip, a relay line at every section boundary, a roadmap and a closing recap. New `references/signposting.md` and the Chinese worked example `examples/signposting-example-zh.md`.
- **Path integrity**: a path chain table (every link, in presentation order, with its relation) built in Phase 4 and checked in Phase 5, plus a listener test. Signposting findings get severity levels.
- Slide card field 11, "Hierarchy Label & On-slide Signposts"; a signpost outline in `master-outline.md`; a path chain table and a "new address" column in the RESTRUCTURE mapping.
- AUDIT question 11 ("Is the logic path visible?") and a signposting checklist in `logic-audit-report.md`.
- Test case TC10 and behavior B20; `scripts/validate.py` now checks that every example card has field 11, that each example has a signpost outline and a path chain table, and that no body structure has a lone `1)` or `a.`.

### Changed
- Slide cards now have eleven fields (was ten). Both worked examples were extended with hierarchy labels, relay lines, a signpost outline and a path chain table.
- The visual hand-off must keep labels, trackers and connector chips unchanged and may not restyle them into plain bullets.

### Note
- Numbering makes the structure visible; it does not make the logic sound. The audit still checks the logic. The behavior of the new rules has not yet been run on a live agent.

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
