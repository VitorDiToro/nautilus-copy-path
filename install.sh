#!/usr/bin/env bash
set -euo pipefail

EXT_DIR="${XDG_DATA_HOME:-$HOME/.local/share}/nautilus-python/extensions"
SCRIPT_DIR="$(dirname "$0")"

mkdir -p "$EXT_DIR"
cp "$SCRIPT_DIR/copy_path.py" "$SCRIPT_DIR/copy_path_i18n.py" "$EXT_DIR/"
nautilus -q 2>/dev/null || true
echo "Installed copy_path.py and copy_path_i18n.py to $EXT_DIR and reloaded Nautilus."
