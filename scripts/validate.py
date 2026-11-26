#!/usr/bin/env python3
"""Static structure checks for the ppt-logic-architect skill.

Checks structure only. It cannot tell whether an agent behaves correctly;
that is what evals/test-cases.md is for.

Usage:  python scripts/validate.py [path-to-skill-dir]
Exit code 0 = all checks passed, 1 = at least one failure.
Python 3.8+, standard library only.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT / "skills" / "ppt-logic-architect"

# Portable frontmatter fields: the intersection of the Agent Skills specification
# and what Codex's own skill validator (skill-creator/scripts/quick_validate.py)
# accepts. The spec also defines `compatibility`, but Codex's validator rejects it,
# so this project does not use it. Requirements are documented in README.md instead.
ALLOWED_FIELDS = {"name", "description", "license", "allowed-tools", "metadata"}
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
CARD_FIELDS = [
    "Slide Number", "Section", "Action-oriented Headline", "Core Message",
    "Supporting Evidence", "Reason for Inclusion",
    "Logical Relationship with Previous Slide", "Transition to Next Slide",
    "Suggested Visual Form", "Evidence Source / Confidence",
]
TEMPLATES = ["master-outline.md", "logic-tree.md", "slide-by-slide.md",
             "evidence-matrix.md", "logic-audit-report.md"]
EXAMPLES = ["research-presentation.md", "design-project-presentation.md"]
REFERENCES = [
    "phase-protocol.md", "mode-create.md", "mode-restructure.md", "mode-audit.md",
    "method-selection.md", "pyramid-principle.md", "scqa-framework.md",
    "assertion-evidence.md", "mece-analysis.md", "evidence-based-reasoning.md",
    "logic-audit.md", "design-research-reasoning.md",
]

failures = []
passes = 0


def check(ok, label, detail=""):
    global passes
    if ok:
        passes += 1
        print(f"  PASS  {label}")
    else:
        failures.append(label)
        print(f"  FAIL  {label}" + (f"  -> {detail}" if detail else ""))


def parse_frontmatter(text):
    """Minimal YAML subset: top-level scalars (plain, quoted, or folded across
    indented lines) and one nested mapping level. Enough to validate a SKILL.md."""
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    if not m:
        return None
    fields, cur, nested = {}, None, None
    for raw in m.group(1).splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw[0] not in " \t":
            key, _, val = raw.partition(":")
            key, val = key.strip(), val.strip()
            cur, nested = key, None
            fields[key] = val if val else ({} if key == "metadata" else "")
        else:
            line = raw.strip()
            if isinstance(fields.get(cur), dict):
                k, _, v = line.partition(":")
                fields[cur][k.strip()] = v.strip().strip('"').strip("'")
            else:
                fields[cur] = (fields[cur] + " " + line).strip()
    for k, v in list(fields.items()):
        if isinstance(v, str) and len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
            fields[k] = v[1:-1]
    return fields


def main():
    print(f"Skill directory: {SKILL_DIR}\n")
    skill_md = SKILL_DIR / "SKILL.md"

    print("[1] Layout")
    check(skill_md.is_file(), "SKILL.md exists")
    for sub in ("references", "templates", "examples"):
        check((SKILL_DIR / sub).is_dir(), f"{sub}/ exists")
    for f in REFERENCES:
        check((SKILL_DIR / "references" / f).is_file(), f"references/{f}")
    for f in TEMPLATES:
        check((SKILL_DIR / "templates" / f).is_file(), f"templates/{f}")
    for f in EXAMPLES:
        check((SKILL_DIR / "examples" / f).is_file(), f"examples/{f}")
    if not skill_md.is_file():
        return

    text = skill_md.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)

    print("\n[2] Frontmatter (Agent Skills specification)")
    check(fm is not None, "frontmatter block present and delimited by ---")
    if fm is None:
        return
    unknown = set(fm) - ALLOWED_FIELDS
    check(not unknown, "no fields outside the specification", f"unknown: {sorted(unknown)}")
    name = fm.get("name", "")
    check(bool(name), "name present")
    check(len(name) <= 64 and bool(NAME_RE.match(name)),
          "name: 1-64 chars, lowercase letters/digits/hyphens, no leading/trailing/double hyphen", name)
    check(name == SKILL_DIR.name, "name equals the directory name", f"{name!r} vs {SKILL_DIR.name!r}")
    desc = fm.get("description", "")
    check(1 <= len(desc) <= 1024, f"description is 1-1024 chars (is {len(desc)})")
    check("Use when" in desc or "use when" in desc, "description says when to use the skill")
    check("<" not in desc and ">" not in desc, "description has no angle brackets (Codex validator rule)")
    meta = fm.get("metadata", {})
    check(isinstance(meta, dict) and all(isinstance(v, str) for v in meta.values()),
          "metadata is a string-to-string map")
    check(len(text.splitlines()) <= 500, f"SKILL.md <= 500 lines (is {len(text.splitlines())})")

    print("\n[3] Relative references resolve")
    ref_re = re.compile(r"`((?:references|templates|examples)/[A-Za-z0-9_.\-]+\.md)`")
    files = [skill_md] + sorted((SKILL_DIR / "references").glob("*.md")) + \
            sorted((SKILL_DIR / "templates").glob("*.md")) + sorted((SKILL_DIR / "examples").glob("*.md"))
    broken, total = [], 0
    for f in files:
        for ref in ref_re.findall(f.read_text(encoding="utf-8")):
            total += 1
            if not (SKILL_DIR / ref).is_file():
                broken.append(f"{f.relative_to(SKILL_DIR)} -> {ref}")
    check(not broken, f"all {total} skill-relative references resolve", "; ".join(broken))

    print("\n[4] Progressive loading")
    referenced = set(re.findall(r"references/([A-Za-z0-9_.\-]+\.md)", text))
    missing = [r for r in REFERENCES if r not in referenced]
    check(not missing, "SKILL.md points to every reference file", f"not referenced: {missing}")
    for f in REFERENCES:
        p = SKILL_DIR / "references" / f
        if p.is_file():
            n = len(p.read_text(encoding="utf-8").splitlines())
            check(n <= 500, f"references/{f} <= 500 lines (is {n})")
    check(len(text) < 25000, f"SKILL.md body is lean (is {len(text)} chars)")

    print("\n[5] Slide card standard")
    slide_t = (SKILL_DIR / "templates" / "slide-by-slide.md")
    if slide_t.is_file():
        st = slide_t.read_text(encoding="utf-8")
        for i, field in enumerate(CARD_FIELDS, 1):
            check(f"{i}. {field}" in st, f"template card field {i}: {field}")
    for field in CARD_FIELDS:
        check(field in text, f"SKILL.md lists card field: {field}")

    print("\n[6] Content rules")
    for ex in EXAMPLES:
        p = SKILL_DIR / "examples" / ex
        if p.is_file():
            t = p.read_text(encoding="utf-8")
            check("fictional" in t.lower(), f"{ex} states its data is fictional")
            check(not re.search(r"\b(Low|Medium|High)-(Low|Medium|High)\b", t),
                  f"{ex} uses only High/Medium/Low/None confidence labels")
            cards = len(re.findall(r"\*\*10\. Evidence Source / Confidence:\*\*", t))
            check(cards >= 10, f"{ex} has complete cards (found {cards})")
    for f in files:
        t = f.read_text(encoding="utf-8")
        check(not re.search(r"\bTODO\b|\bFIXME\b|lorem ipsum", t, re.I),
              f"no TODO/FIXME/lorem in {f.relative_to(SKILL_DIR)}")

    print("\n[7] Project files")
    for rel in ("README.md", "LICENSE", "CHANGELOG.md", "CONTRIBUTING.md",
                "evals/test-cases.md", "evals/expected-behavior.md",
                "install/install-codex.md", "install/install-claude-code.md", "install/install.sh"):
        check((ROOT / rel).is_file(), rel)

    print(f"\n{passes} passed, {len(failures)} failed")
    if failures:
        print("Failures:")
        for f in failures:
            print(f"  - {f}")


if __name__ == "__main__":
    main()
    sys.exit(1 if failures else 0)
