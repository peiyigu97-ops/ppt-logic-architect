#!/usr/bin/env bash
# Install the ppt-logic-architect skill for Claude Code, Codex, or the shared
# ~/.agents/skills location. One source folder; this script only copies or links it.
#
#   ./install/install.sh --target claude            # ~/.claude/skills/
#   ./install/install.sh --target codex             # ${CODEX_HOME:-~/.codex}/skills/
#   ./install/install.sh --target agents            # ~/.agents/skills/
#   ./install/install.sh --target all --scope project
#
# Options:
#   --target claude|codex|agents|all   (default: claude)
#   --scope  user|project              (default: user; project = current directory)
#   --link                             symlink instead of copy (not recommended on Windows)
#   --force                            replace an existing install (a backup is kept)
#   --dry-run                          print what would happen, change nothing
#   -h, --help
set -euo pipefail

SKILL_NAME="ppt-logic-architect"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$(cd "$SCRIPT_DIR/.." && pwd)/skills/$SKILL_NAME"

TARGET="claude"; SCOPE="user"; MODE="copy"; FORCE=0; DRY=0

usage() { sed -n '2,20p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'; }

while [ $# -gt 0 ]; do
  case "$1" in
    --target) TARGET="${2:-}"; shift 2 ;;
    --scope)  SCOPE="${2:-}"; shift 2 ;;
    --link)   MODE="link"; shift ;;
    --force)  FORCE=1; shift ;;
    --dry-run) DRY=1; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown option: $1" >&2; usage >&2; exit 2 ;;
  esac
done

case "$TARGET" in claude|codex|agents|all) ;; *) echo "Invalid --target: $TARGET" >&2; exit 2 ;; esac
case "$SCOPE" in user|project) ;; *) echo "Invalid --scope: $SCOPE" >&2; exit 2 ;; esac

[ -f "$SRC/SKILL.md" ] || { echo "Cannot find $SRC/SKILL.md. Run this from a full clone of the repository." >&2; exit 1; }

dest_dir() {
  local t="$1"
  if [ "$SCOPE" = "project" ]; then
    case "$t" in
      claude) echo "$PWD/.claude/skills" ;;
      codex|agents) echo "$PWD/.agents/skills" ;;
    esac
  else
    case "$t" in
      claude) echo "${CLAUDE_CONFIG_DIR:-$HOME/.claude}/skills" ;;
      codex)  echo "${CODEX_HOME:-$HOME/.codex}/skills" ;;
      agents) echo "$HOME/.agents/skills" ;;
    esac
  fi
}

run() { if [ "$DRY" = 1 ]; then echo "  [dry-run] $*"; else "$@"; fi; }

install_one() {
  local t="$1" base dest
  base="$(dest_dir "$t")"; dest="$base/$SKILL_NAME"
  echo "-> $t ($SCOPE): $dest"
  if [ -e "$dest" ] || [ -L "$dest" ]; then
    if [ "$FORCE" != 1 ]; then
      echo "   already exists; skipped (use --force to replace; a backup will be kept)"
      return 0
    fi
    # Keep the backup OUTSIDE the skills directory: a backup inside it would hold a
    # second SKILL.md with the same name, and the agent could load both.
    local bakroot bak
    bakroot="$(dirname "$base")/$SKILL_NAME-backups"
    bak="$bakroot/$(date +%Y%m%d%H%M%S)"
    echo "   existing install moved to $bak"
    run mkdir -p "$bakroot"
    run mv "$dest" "$bak"
  fi
  run mkdir -p "$base"
  if [ "$MODE" = "link" ]; then
    run ln -s "$SRC" "$dest"
  else
    run cp -R "$SRC" "$dest"
  fi
  if [ "$DRY" != 1 ]; then
    [ -f "$dest/SKILL.md" ] || { echo "   ERROR: SKILL.md not found after install" >&2; return 1; }
    echo "   installed ($MODE)"
  fi
  # Paths verified on a real machine: ~/.claude/skills and ~/.codex/skills.
  # The others follow the shared Agent Skills convention but were not confirmed for Codex.
  if [ "$t" = "agents" ] || { [ "$t" = "codex" ] && [ "$SCOPE" = "project" ]; }; then
    echo "   note: this location is unverified for Codex; see install/install-codex.md"
  fi
}

if [ "$TARGET" = "all" ]; then
  # codex and agents share a project path; install each distinct location once
  install_one claude
  install_one codex
  if [ "$SCOPE" = "user" ]; then install_one agents; fi
else
  install_one "$TARGET"
fi

echo
echo "Done. Start a NEW session so the agent re-scans its skills, then try:"
echo "  \"Use ppt-logic-architect to audit the logic of this deck: <file>\""
