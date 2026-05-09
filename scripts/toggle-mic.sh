#!/usr/bin/env bash

wpctl set-mute @DEFAULT_AUDIO_SOURCE@ toggle
pkill -RTMIN+9 waybar 2>/dev/null || true
