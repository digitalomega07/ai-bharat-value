#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python3 "$ROOT/scripts/sync-codex-skills.py"
DEST="${CODEX_HOME:-$HOME/.codex}/skills"
mkdir -p "$DEST"
for skill in "$ROOT"/codex-skills/*; do
  name="$(basename "$skill")"
  rm -rf "$DEST/$name"
  cp -R "$skill" "$DEST/$name"
  echo "installed $name"
done

