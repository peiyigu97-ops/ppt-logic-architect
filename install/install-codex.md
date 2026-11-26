# Install for OpenAI Codex

## What was verified, and what was not

Checked on this machine against Codex CLI `0.163.0` (Windows):

| Item | Status | Evidence |
|---|---|---|
| User skills live in `$CODEX_HOME/skills/<name>/SKILL.md`, default `~/.codex/skills` | **Verified** | `~/.codex/skills/` holds user skills (`check-a11y`, `easy-wireframe`, `perform-audit`) and a `.system/` folder. Codex's bundled `skill-creator` says to create skills in `$CODEX_HOME/skills`, and `skill-installer` installs into `$CODEX_HOME/skills/<name>` |
| Frontmatter fields Codex's own validator accepts | **Verified by reading** `skill-creator/scripts/quick_validate.py` | Allowed: `name`, `description`, `license`, `allowed-tools`, `metadata`. It rejects other keys, **including `compatibility`**, and rejects `<` or `>` in `description`. This skill uses only allowed keys |
| Explicit invocation as `$ppt-logic-architect` | **Verified by reading** `skill-creator/references/openai_yaml.md` | It describes `$skill-name` as the explicit-invocation form |
| `~/.agents/skills/` and project `.agents/skills/` | **Not verified.** I could not confirm that Codex 0.163 reads these | `~/.agents/skills/` exists here (shared with the `npx skills` CLI, whose lock file lists `codex` among its agents), but I found no Codex source or doc stating it scans that path. Prefer `~/.codex/skills` |
| Project-level skill folder for Codex | **Not verified** | `install.sh --scope project` writes `./.agents/skills/`; treat as experimental |
| Official validator run on this skill | **Not run.** It needs PyYAML, which is not installed here, and installing it was not done | The rules were checked by `scripts/validate.py` instead. Run the official one yourself, below |
| This skill loading and behaving correctly in Codex | **Not run** | See `evals/test-cases.md` |

## Option 1 - Script (macOS, Linux, Git Bash, WSL)

```bash
./install/install.sh --target codex --dry-run    # preview
./install/install.sh --target codex              # ${CODEX_HOME:-~/.codex}/skills/
./install/install.sh --target codex --force      # replace an existing install (backup kept)
```

## Option 2 - Manual copy

**macOS / Linux / Git Bash**

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/ppt-logic-architect "${CODEX_HOME:-$HOME/.codex}/skills/"
```

**Windows PowerShell**

```powershell
$dest = if ($env:CODEX_HOME) { "$env:CODEX_HOME\skills" } else { "$env:USERPROFILE\.codex\skills" }
New-Item -ItemType Directory -Force $dest | Out-Null
Copy-Item -Recurse -Force skills\ppt-logic-architect $dest\
```

The result must be exactly:

```
~/.codex/skills/ppt-logic-architect/SKILL.md
~/.codex/skills/ppt-logic-architect/references/...
~/.codex/skills/ppt-logic-architect/templates/...
~/.codex/skills/ppt-logic-architect/examples/...
```

## Validate with Codex's own validator (recommended)

Codex ships a validator with its bundled `skill-creator`. It needs PyYAML:

```bash
# one-off, without touching your global Python (requires uv):
uv run --with pyyaml python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/ppt-logic-architect

# or, with a normal environment:
pip install pyyaml
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/ppt-logic-architect
```

Expected output: `Skill is valid!`. If it complains about a key, `SKILL.md` frontmatter has drifted from the allowed set.

## Confirm it loaded

1. Start a **new** Codex session. The installer skill's own note says a newly installed skill is available "on their next turn", and a fresh session is the safe choice.
2. Try: `Use $ppt-logic-architect to audit the logic of <your outline file>. Do not rewrite it.`
3. The expected first reply names the mode (AUDIT), reconstructs what the deck argues, and ends with a phase gate.

If it is not picked up, confirm the path above, then confirm `SKILL.md` starts with `---` on line 1.

## Optional: Codex UI metadata

Codex can read an optional `agents/openai.yaml` for a display name and short description (see `skill-creator/references/openai_yaml.md`). It is not part of the shared source, so this repository does not include one. If you want it, add it only to your **installed copy**:

```yaml
interface:
  display_name: "PPT Logic Architect"
  short_description: "Design presentation logic, then audit it"
  default_prompt: "Use $ppt-logic-architect to structure a presentation from my notes."
```

Do not add Codex-only fields to `SKILL.md`; the validator rejects them.

## Optional companion: visual-explainer

Only needed for the visual hand-off (see `README.md`, "Pair it with visual-explainer"). The steps below follow visual-explainer's own README (v0.16.0), which lists `~/.codex/skills/visual-explainer` as its Codex path; **they were not run here**.

```bash
git clone https://github.com/nicobailon/visual-explainer.git
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R visual-explainer/plugins/visual-explainer "${CODEX_HOME:-$HOME/.codex}/skills/visual-explainer"
```

**Windows PowerShell**

```powershell
git clone https://github.com/nicobailon/visual-explainer.git
$dest = if ($env:CODEX_HOME) { "$env:CODEX_HOME\skills" } else { "$env:USERPROFILE\.codex\skills" }
Copy-Item -Recurse visual-explainer\plugins\visual-explainer "$dest\visual-explainer"
```

Invoke it as `$visual-explainer`. Its HTML output needs a browser, and its render step runs with Node. Start a new session afterwards. If it is missing, ppt-logic-architect says so and stops at `visual-brief.md`.

## Update and uninstall

- Update: `./install/install.sh --target codex --force`. The previous install is moved to `~/.codex/ppt-logic-architect-backups/<timestamp>/`, outside the skills directory, so it cannot load as a duplicate. Or re-copy.
- Uninstall: delete `~/.codex/skills/ppt-logic-architect/`.
- If you make your own backup, keep it outside `skills/`: a copy inside it holds a second `SKILL.md` with the same name.
