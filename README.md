# Omarchy for Ubuntu 🌌

> **Experience the authentic [Omarchy](https://github.com/omacom/omarchy) tiling desktop on Ubuntu.**  
> Powered by **Hyprland**, **Waybar**, **Wofi**, and Omarchy's complete 22-theme palette suite.

---

## ✨ Features

- **22 Curated Omarchy Themes**: Includes *Tokyo Night, Catppuccin, Nord, Gruvbox, Everforest, Retro 82, Lumon, Matte Black*, and more.
- **Dynamic Waybar Sync**: When you switch themes, Waybar dynamically re-tints its workspace pills, borders, clock, and accents to match your active wallpaper and palette.
- **Omarchy Window Rules**:
  - **Auto Picture-in-Picture (PiP)**: Video windows float, pin across workspaces, remove borders, and dock at `600x338`.
  - **Centered Utility Dialogs**: Volume controls (`pavucontrol`), file open/save dialogs, and portals float centered.
  - **Acrylic Opacity Profile**: Subtle `0.985` active / `0.96` inactive opacity with focus dimming (video/streaming apps retain 100% opacity).
- **Clipboard History**: Built-in `cliphist` integration accessible via `Super + V`.
- **Slide-in Scratchpad**: Hidden workspace accessible via ``Super + ` `` or `Super + S`.
- **Wofi Power Menu**: Clean logout/sleep/reboot/shutdown dashboard on `Super + Escape`.
- **Dual-Session Safe**: Installs as an independent Wayland session (`omarchy.desktop`) alongside your existing desktop (e.g. GNOME, KDE Plasma, or Windows 11 themes) without modifying your existing environment.

---

## 🚀 Quick Install

### One-line Installation:

```bash
git clone https://github.com/apravint/omarchy-ubuntu.git
cd omarchy-ubuntu
./install.sh
```

After installation completes, log out and select **Omarchy** from your login screen (display manager) session menu.

---

## ⌨️ Keybindings Cheatsheet

### 🚀 Applications
| Shortcut | Action |
| :--- | :--- |
| `Super + Space` | **Wofi** Application Launcher |
| `Super + Return` | **Alacritty** Terminal |
| `Super + Shift + B` or `Super + B` | Google Chrome / Default Browser |
| `Super + Shift + F` or `Super + E` | Dolphin / File Manager |
| `Super + Shift + Y` | YouTube Web App |
| `Super + Shift + A` | ChatGPT / AI Web App |

### 🎨 Theming & Tools
| Shortcut | Action |
| :--- | :--- |
| `Super + Ctrl + Shift + Space` | **Omarchy Theme Switcher** (22 themes) |
| `Super + V` | **Clipboard History Manager** (`cliphist`) |
| `Super + Escape` | **Power Menu** (Lock, Suspend, Logout, Reboot, Shutdown) |
| `Super + Shift + S` or `Print` | **Snipping Tool** (Area screenshot to clipboard) |

### 🪟 Window Management
| Shortcut | Action |
| :--- | :--- |
| `Super + Q` or `Super + W` | Close active window |
| `Super + T` | Toggle Floating mode |
| `Super + F` | Toggle Fullscreen |
| `Super + J` | Toggle Split direction |
| `Super + P` | Toggle Pseudo-tiling |
| `Super + ` ` ` or `Super + S` | Toggle **Scratchpad** workspace |
| `Super + Shift + ` ` ` or `Super + Alt + S` | Send window to **Scratchpad** |
| `Super + 1..0` | Switch to Workspace 1–10 |
| `Super + Shift + 1..0` | Move active window to Workspace 1–10 |
| `Super + Left/Right/Up/Down` | Move focus between windows |

### 🔊 Audio & Media
| Shortcut | Action |
| :--- | :--- |
| `XF86AudioRaiseVolume` / `LowerVolume` | Adjust Volume ±5% |
| `XF86AudioMute` | Toggle Audio Mute |
| `XF86AudioPlay` / `Next` / `Prev` | Media Play / Pause / Skip |

---

## 📂 Repository Layout

```
omarchy-ubuntu/
├── config/
│   ├── hypr/
│   │   └── hyprland.conf       # Complete Omarchy Hyprland configuration
│   ├── waybar/
│   │   ├── config.jsonc        # Top bar layout & widgets
│   │   └── style.css           # Glass acrylic styling with dynamic colors
│   └── wofi/
│       ├── config              # Launcher configuration
│       └── style.css           # Matching Omarchy launcher theme
├── bin/
│   ├── omarchy-theme-switch    # Interactive 22-theme switcher with live sync
│   ├── omarchy-power-menu      # System power & lock dashboard
│   ├── omarchy-clipboard-menu  # Cliphist clipboard search
│   └── omarchy-update-waybar-theme # Extracts palette from theme to Waybar CSS
├── system/
│   ├── omarchy.desktop         # Wayland session descriptor
│   ├── omarchy.conf            # /etc/omarchy.conf definition
│   └── omarchy.sh              # /etc/profile.d/ export
├── install.sh                  # All-in-one automated installer
└── README.md
```

---

## 🤝 Credits & Acknowledgements

- Built upon the design vision of [Omarchy by OMACOM](https://github.com/omacom/omarchy).
- Powered by [Hyprland](https://hyprland.org/) and [Waybar](https://github.com/Alexays/Waybar).
