# Changelog

All notable changes to this project are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

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
