#!/usr/bin/env bash

CACHE_DIR="${XDG_CACHE_HOME:-$HOME/.cache}/waybar-privacy-status"
STATE_FILE="$CACHE_DIR/camera_state"

mkdir -p "$CACHE_DIR"

current="$(cat "$STATE_FILE" 2>/dev/null || echo on)"

case "$current" in
  off)
    echo "on" > "$STATE_FILE"
    ;;
  *)
    echo "off" > "$STATE_FILE"
    ;;
esac

pkill -RTMIN+9 waybar 2>/dev/null || true
