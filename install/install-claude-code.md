# Install for Claude Code

## What was verified, and what was not

| Item | Status | Evidence |
|---|---|---|
| User skills live in `~/.claude/skills/<name>/SKILL.md` | **Verified on this machine** | `~/.claude/skills/` contains installed skills such as `slides` and `find-skills`, each with a `SKILL.md` and `name` / `description` frontmatter |
| Symlinked skill folders work | Observed, not independently tested | `find-skills`, `apple-design` and others in `~/.claude/skills/` are symlinks into `~/.agents/skills/` |
| Project skills in `<project>/.claude/skills/<name>/` | **Not verified here.** Documented Claude Code behavior | No project-level skill existed to inspect |
| `/ppt-logic-architect` slash invocation | **Not verified here** | Depends on Claude Code version |
| This skill loading and behaving correctly in Claude Code | **Not run** | See the test cases in `evals/test-cases.md` |

## Option 1 - Script (macOS, Linux, Git Bash, WSL)

```bash
./install/install.sh --target claude --dry-run   # preview
./install/install.sh --target claude             # install to ~/.claude/skills/
./install/install.sh --target claude --scope project   # install to ./.claude/skills/
./install/install.sh --target claude --force    # replace an existing install (backup kept)
```

If `CLAUDE_CONFIG_DIR` is set, the script uses `$CLAUDE_CONFIG_DIR/skills`; otherwise `~/.claude/skills`.

## Option 2 - Manual copy

**macOS / Linux / Git Bash**

```bash
mkdir -p ~/.claude/skills
cp -R skills/ppt-logic-architect ~/.claude/skills/
```

**Windows PowerShell**

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\skills" | Out-Null
Copy-Item -Recurse -Force skills\ppt-logic-architect "$env:USERPROFILE\.claude\skills\"
```

The result must be exactly:

```
~/.claude/skills/ppt-logic-architect/SKILL.md
~/.claude/skills/ppt-logic-architect/references/...
~/.claude/skills/ppt-logic-architect/templates/...
~/.claude/skills/ppt-logic-architect/examples/...
```

The folder name must equal the `name` in `SKILL.md` (`ppt-logic-architect`).

## Option 3 - Symlink (keeps one live copy while developing)

```bash
ln -s "$(pwd)/skills/ppt-logic-architect" ~/.claude/skills/ppt-logic-architect
```

On Windows, creating symlinks needs Developer Mode or an elevated shell. If in doubt, copy.

## Confirm it loaded

1. Start a **new** Claude Code session. Skills are scanned at session start.
2. Ask "which skills do you have?". `ppt-logic-architect` should be listed with its description. (Some versions also have a `/skills` command; not verified here.)
3. Try: `Use ppt-logic-architect to audit the logic of <your outline file>. Do not rewrite it.`

The expected first reply names the mode (AUDIT), reconstructs what the deck argues, and ends with a phase gate. If the skill is not listed, check the path above and that `SKILL.md` starts with `---` on line 1.

## Update and uninstall

- Update: `./install/install.sh --target claude --force`. The previous install is moved to `~/.claude/ppt-logic-architect-backups/<timestamp>/`, outside the skills directory, so it cannot load as a duplicate. Or re-copy.
- Uninstall: delete `~/.claude/skills/ppt-logic-architect/`.

## Notes

- `allowed-tools` is not set in `SKILL.md`. The skill needs to read files you point to, and to write files only in Phase 6. Claude Code will ask permission for those as usual.
- If you make your own backup, keep it outside `skills/`: a copy inside it holds a second `SKILL.md` with the same name.
