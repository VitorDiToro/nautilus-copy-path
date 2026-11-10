#!/usr/bin/env bash
set -euo pipefail

EXT_DIR="${XDG_DATA_HOME:-$HOME/.local/share}/nautilus-python/extensions"
mkdir -p "$EXT_DIR"
cp "$(dirname "$0")/copy_path.py" "$EXT_DIR/copy_path.py"
nautilus -q 2>/dev/null || true
echo "Installed copy_path.py to $EXT_DIR and reloaded Nautilus."
