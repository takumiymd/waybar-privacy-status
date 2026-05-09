# Waybar Privacy Status

A small Waybar custom module for showing microphone and camera privacy status on Arch Linux / Hyprland.

The module is designed for a minimal HUD-style Waybar setup. It stays hidden when everything is normal, then appears in a wine-red warning style when the microphone is muted, the camera is manually marked off, or the camera is actively in use.

## Features

- Shows microphone mute state from PipeWire/WirePlumber
- Shows camera availability from `/dev/video*`
- Detects whether the camera is currently in use
- Supports manual camera privacy state toggle
- Designed for Waybar custom JSON modules
- Includes Hyprland keybind examples

## Preview behavior

Mic on:

```text
MIC ON
```

Mic muted:

```text
MIC OFF
```

Camera on:

```text
CAM ON
```

Camera off:

```text
CAM OFF
```

## Requirements

Install dependencies:

```bash
sudo pacman -S --needed wireplumber v4l-utils lsof
```

Required commands:

- `wpctl`
- `v4l2-ctl`
- `lsof`
- `waybar`

## Installation

Clone this repo:

```bash
```bash
git clone https://github.com/takumiymd/waybar-privacy-status.git
cd waybar-privacy-status
```
Run the install script:

```bash
./install.sh
```

This creates symlinks under:

```bash
~/.config/waybar/scripts/
```

## Waybar config

Add this to your Waybar config:

```jsonc
"custom/privacy-status": {
  "exec": "~/.config/waybar/scripts/privacy-status.py",
  "return-type": "json",
  "format": "{}",
  "interval": 2,
  "signal": 9,
  "tooltip": true
}
```

Then add the module to your preferred section.

Example:

```jsonc
"modules-center": [
  "custom/focus-mode",
  "custom/privacy-status",
  "clock"
]
```

## Waybar CSS

Add this to your Waybar `style.css`:

```css
@define-color nejen_red #b35461;

/* Privacy module base */
#custom-privacy-status {
  background: transparent;
  border: 1px solid transparent;
  box-shadow: none;

  padding: 0 8px;
  margin: 0 4px;

  border-radius: 8px;

  font-weight: 700;
  letter-spacing: 2px;
}

/* Mic off / camera off */
#custom-privacy-status.privacy-alert,
#custom-privacy-status.mic-off,
#custom-privacy-status.cam-off {
  color: @nejen_red;
  border-color: rgba(179, 84, 97, 0.65);
  background: rgba(179, 84, 97, 0.08);

  text-shadow:
    0 0 5px rgba(179, 84, 97, 0.55),
    0 0 14px rgba(179, 84, 97, 0.25);

  box-shadow:
    0 0 6px rgba(179, 84, 97, 0.18),
    inset 0 0 8px rgba(179, 84, 97, 0.08);
}

/* Camera actively in use */
#custom-privacy-status.cam-active {
  color: @nejen_red;
  border-color: rgba(179, 84, 97, 0.75);
  background: rgba(179, 84, 97, 0.10);

  text-shadow:
    0 0 5px rgba(179, 84, 97, 0.55),
    0 0 14px rgba(179, 84, 97, 0.25);

  box-shadow:
    0 0 6px rgba(179, 84, 97, 0.22),
    inset 0 0 8px rgba(179, 84, 97, 0.10);
}

/* Normal state: hidden and takes no space */
#custom-privacy-status.privacy-clear {
  color: transparent;
  background: transparent;
  border: none;
  box-shadow: none;

  padding: 0;
  margin: 0;
  min-width: 0;
}
```

## Hyprland bindings

Add this to your Hyprland bindings:

```ini
# Mic mute toggle
bind = , XF86AudioMicMute, exec, ~/.config/waybar/scripts/toggle-mic.sh

# Camera status toggle
bind = SUPER, C, exec, ~/.config/waybar/scripts/toggle-camera-state.sh
```

## ASUS ProArt P13 camera key note

ASUS ProArt P13 expose the physical F10 webcam key incorrectly.
In my case, I use Super + c as Camera On and Off.


## Project structure

```text
waybar-privacy-status/
├── README.md
├── install.sh
├── .gitignore
├── scripts/
│   ├── privacy-status.py
│   ├── toggle-mic.sh
│   └── toggle-camera-state.sh
└── examples/
    ├── hyprland-bindings.conf
    ├── waybar-config.jsonc
    └── waybar-style.css
```

