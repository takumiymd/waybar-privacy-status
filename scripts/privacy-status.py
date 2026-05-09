#!/usr/bin/env python3

import glob
import json
import os
import subprocess
from pathlib import Path

CACHE_DIR = (
    Path(os.environ.get("XDG_CACHE_HOME", Path.home() / ".cache"))
    / "waybar-privacy-status"
)
CAMERA_STATE_FILE = CACHE_DIR / "camera_state"


def run(cmd):
    try:
        return subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
            timeout=1.5,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return None


def get_mic_state():
    result = run(["wpctl", "get-volume", "@DEFAULT_AUDIO_SOURCE@"])

    if result is None or result.returncode != 0:
        return "unknown", "Mic: unknown"

    output = result.stdout.strip()
    muted = "MUTED" in output.upper()

    if muted:
        return "off", f"Mic: muted ({output})"

    return "on", f"Mic: on ({output})"


def get_video_devices():
    return sorted(glob.glob("/dev/video*"))


def camera_is_in_use(devices):
    if not devices:
        return False

    result = run(["lsof", "-t", *devices])

    if result is None:
        return False

    return result.returncode == 0 and bool(result.stdout.strip())


def get_camera_names():
    result = run(["v4l2-ctl", "--list-devices"])

    if result is None or result.returncode != 0:
        return ""

    return result.stdout.strip()


def read_manual_camera_state():
    try:
        value = CAMERA_STATE_FILE.read_text().strip().lower()
        if value in {"on", "off"}:
            return value
    except FileNotFoundError:
        pass

    return "auto"


def get_camera_state():
    devices = get_video_devices()
    manual_state = read_manual_camera_state()

    if not devices:
        return "off", "Camera: no /dev/video device found"

    if manual_state == "off":
        return "off", "Camera: marked off by F10 state"

    if camera_is_in_use(devices):
        return "active", "Camera: active/in use"

    names = get_camera_names()
    tooltip = "Camera: available"

    if names:
        tooltip += f"\n\n{names}"

    return "on", tooltip


def main():
    mic_state, mic_tooltip = get_mic_state()
    cam_state, cam_tooltip = get_camera_state()

    mic_label = {
        "on": "ON",
        "off": "OFF",
        "unknown": "??",
    }.get(mic_state, "??")

    cam_label = {
        "on": "ON",
        "off": "OFF",
        "active": "ACTIVE",
        "unknown": "??",
    }.get(cam_state, "??")

    classes = ["privacy-status"]

    if mic_state == "off":
        classes.append("mic-off")

    if cam_state == "off":
        classes.append("cam-off")

    if cam_state == "active":
        classes.append("cam-active")

    if mic_state == "off" or cam_state == "off":
        classes.append("privacy-alert")
    else:
        classes.append("privacy-clear")

    text = f"MIC {mic_label}  CAM {cam_label}"
    tooltip = f"{mic_tooltip}\n{cam_tooltip}"

    print(
        json.dumps(
            {
                "text": text,
                "tooltip": tooltip,
                "class": classes,
            }
        )
    )


if __name__ == "__main__":
    main()
