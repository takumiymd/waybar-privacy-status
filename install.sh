#!/usr/bin/env bash

set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WAYBAR_SCRIPT_DIR="$HOME/.config/waybar/scripts"

mkdir -p "$WAYBAR_SCRIPT_DIR"

ln -sf "$PROJECT_DIR/scripts/privacy-status.py" "$WAYBAR_SCRIPT_DIR/privacy-status.py"
ln -sf "$PROJECT_DIR/scripts/toggle-mic.sh" "$WAYBAR_SCRIPT_DIR/toggle-mic.sh"
ln -sf "$PROJECT_DIR/scripts/toggle-camera-state.sh" "$WAYBAR_SCRIPT_DIR/toggle-camera-state.sh"

chmod +x "$PROJECT_DIR/scripts/privacy-status.py"
chmod +x "$PROJECT_DIR/scripts/toggle-mic.sh"
chmod +x "$PROJECT_DIR/scripts/toggle-camera-state.sh"

echo "Installed Waybar Privacy Status scripts."
echo
echo "Symlinks:"
echo "  $WAYBAR_SCRIPT_DIR/privacy-status.py"
echo "  $WAYBAR_SCRIPT_DIR/toggle-mic.sh"
echo "  $WAYBAR_SCRIPT_DIR/toggle-camera-state.sh"
echo
echo "Next:"
echo "  1. Add examples/waybar-config.jsonc to your Waybar config."
echo "  2. Add examples/waybar-style.css to your Waybar style.css."
echo "  3. Add examples/hyprland-bindings.conf to your Hyprland bindings."
echo "  4. Restart Waybar."
