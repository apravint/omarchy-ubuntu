# Omarchy for Ubuntu 🌌

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Platform: Ubuntu](https://img.shields.io/badge/Platform-Ubuntu%20Linux-orange.svg)](https://ubuntu.com)
[![Compositor: Hyprland](https://img.shields.io/badge/Compositor-Hyprland-blue.svg)](https://hyprland.org)

> **Experience the authentic [Omarchy](https://github.com/omacom/omarchy) tiling desktop on Ubuntu.**  
> Powered by **Hyprland**, **Waybar**, **Wofi**, and Omarchy's complete 22-theme palette suite.

![Omarchy on Ubuntu Preview](assets/preview.png)

---

## ✨ Features

- **22 Curated Omarchy Themes**: Includes *Tokyo Night, Catppuccin, Nord, Gruvbox, Everforest, Retro 82, Lumon, Matte Black, Hackerman*, and more.
- **Universal Desktop Theme Engine (`omarchy-theme-sync-all`)**:
  - **Hyprland Window Borders**: Window borders dynamically re-tint live to match the active theme's gradient and glow without restarting the compositor.
  - **Dynamic Waybar Sync**: Waybar dynamically re-tints workspace pills, borders, clock, and system stats.
  - **Wofi Palette Sync**: Wofi launcher inherits exact background, selection, and accent colors.
  - **Mako Notifications**: Notification popups match the active theme styling.
- **Background Cycling (`Super + Ctrl + Space`)**: Instantly cycle through every curated wallpaper included with your active theme via `omarchy theme bg next`.
- **Searchable Keybindings Cheat Sheet (`Super + K`)**: Visual menu listing all shortcuts and actions.
- **Window Tab Grouping**: Group multiple windows into tabs with `Super + G` and cycle between them with `Super + Alt + Tab`.
- **Omarchy Window Rules**:
  - **Auto Picture-in-Picture (PiP)**: Video windows float, pin across workspaces, remove borders, and dock at `600x338`.
  - **Centered Utility Dialogs**: Volume controls (`pavucontrol`), file open/save dialogs, and portals float centered.
  - **Acrylic Opacity Profile**: Subtle `0.985` active / `0.96` inactive opacity with focus dimming (video/streaming apps retain 100% opacity).
- **Clipboard History**: Built-in `cliphist` integration accessible via `Super + V`.
- **Slide-in Scratchpad**: Hidden workspace accessible via ``Super + ` `` or `Super + S`.
- **Wofi Power Menu**: Clean logout/sleep/reboot/shutdown dashboard on `Super + Escape`.
- **Universal App Support**: Works seamlessly on any Ubuntu flavor (GNOME, KDE Plasma, XFCE) with smart browser and file manager fallbacks.
- **Dual-Session Safe**: Installs as an independent Wayland session (`omarchy.desktop`) alongside your existing desktop without modifying or overwriting your current environment.

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

### 🚀 Applications & Tools
| Shortcut | Action |
| :--- | :--- |
| `Super + Space` | **Omarchy Command Center Menu** |
| `Super + Alt + Space` | **Wofi** Application Launcher |
| `Super + Return` | **Alacritty** Terminal |
| `Super + Alt + Return` | **Tmux** Persistent Terminal Session |
| `Super + Shift + N` | **Neovim** Code Editor |
| `Super + K` | **Keybindings Cheat Sheet Menu** |
| `Super + Alt + K` | **Tmux Keybindings Reference** |
| `Super + Ctrl + T` | **Activity / Process Monitor** (`btop`) |
| `Super + Shift + D` | **Git TUI** (`lazygit`) |
| `Super + Ctrl + Q` | **Calculator** (`omacalc`) |
| `Super + Ctrl + S` | **LocalSend Share Menu** (Clipboard, File, Folder) |
| `Super + Ctrl + N` | **Toggle Nightlight** (4200K warm blue-light filter) |
| `Super + Ctrl + I` | **Toggle Idle / Stay Awake** (Inhibits screensaver & sleep) |
| `Super + /` / `Super + Alt + /` | Step Monitor & UI Scaling Up / Down |
| `Super + Shift + B` or `Super + B` | Preferred Web Browser |
| `Super + Shift + Alt + B` | Private / Incognito Browser |
| `Super + Shift + F` or `Super + E` | Preferred File Manager |
| `Super + Shift + Alt + F` | File Manager in Terminal Working Directory |

### 🌐 Web Apps Suite
| Shortcut | Action |
| :--- | :--- |
| `Super + Shift + A` | **ChatGPT** AI Chatbot |
| `Super + Shift + Alt + A` | **Grok** AI Chatbot |
| `Super + Shift + C` | **HEY Calendar** |
| `Super + Shift + E` | **HEY Email** |
| `Super + Shift + Alt + E` | Compose New Email |
| `Super + Shift + Y` | **YouTube** |
| `Super + Shift + Alt + G` | **WhatsApp Web** |
| `Super + Shift + Ctrl + G` | **Google Messages Web** |
| `Super + Shift + P` | **Google Photos** |
| `Super + Shift + S` | **Google Maps** |
| `Super + Shift + X` | **X / Twitter** |
| `Super + Shift + Alt + X` | Compose New Post on X |

### 📸 Capture, OCR & Text Tools
| Shortcut | Action |
| :--- | :--- |
| `Print` or `Super + Shift + S` | **Region Screenshot** (Saves to `~/Pictures/Screenshots` & copies to clipboard) |
| `Alt + Print` | **Screen Recording** (Toggle Start / Stop MP4 recording to `~/Videos`) |
| `Super + Print` | **Color Picker Eyedropper** (`hyprpicker` hex code to clipboard) |
| `Super + Ctrl + Print` | **OCR Text Extraction** (`tesseract` grabs text from screen directly to clipboard) |
| `Super + Ctrl + C` | **Capture Dashboard Menu** (Region, Fullscreen, Window, Record, Eyedropper) |
| `Super + Ctrl + D` | **Instant Dictionary Lookup** (Definition, phonetic pronunciation, examples) |
| `Super + Ctrl + X` | **Toggle Dictation** (Voxtype speech-to-text) |
| `F9` (Hold/Release) | **Push-to-Talk Dictation** (Voxtype) |

### ⏱️ Reminders & System Notices
| Shortcut | Action |
| :--- | :--- |
| `Super + Ctrl + R` | **Set Reminder** (Interactive Wofi dialog with presets: 5m, 15m, 25m, or custom note) |
| `Super + Ctrl + Alt + R` | **Show Active Reminders** (Notification summary of all running timers) |
| `Super + Ctrl + Shift + R`| **Clear All Reminders** |
| `Super + Ctrl + Alt + T` | **Date & Time Notice** (Desktop notification with full date, time, and week) |
| `Super + Ctrl + Alt + W` | **Weather Notice** (Current local temperature, conditions, and wind speed) |
| `Super + Ctrl + Alt + B` | **Battery Status Notice** (Charge percentage and health) |
| `Super + ,` | Dismiss Last Notification |
| `Super + Shift + ,` | Dismiss All Notifications |
| `Super + Ctrl + ,` | Toggle Do-Not-Disturb (Silencing Notifications) |

### 🎨 Theming, Backgrounds & Cursors
| Shortcut | Action |
| :--- | :--- |
| `Super + Ctrl + Shift + Space` | **Omarchy Theme Switcher** (22 themes) |
| `Super + Ctrl + Space` | **Cycle Background** (Next wallpaper in active theme) |
| `omarchy-cursor-switch` | **Cursor Theme Selector** (Applies dynamically across Hyprland & GTK) |
| `Super + Backspace` | Toggle Window Acrylic Transparency |
| `Super + Shift + Backspace` | Toggle Window Gaps |
| `Super + V` | **Clipboard History Manager** (`cliphist`) |
| `Super + Escape` | **Power Menu** (Lock, Suspend, Logout, Reboot, Shutdown) |
| `Super + Ctrl + L` | **Lock Screen** (`swaylock`) |

### 🪟 Window Management & Grouping
| Shortcut | Action |
| :--- | :--- |
| `Super + Q` or `Super + W` | Close active window |
| `Super + T` | Toggle Floating mode |
| `Super + O` | Pin & Float Window (Sticky PiP) |
| `Super + G` | Toggle Tabbed Window Group |
| `Super + Alt + G` | Eject window from Group |
| `Super + Alt + Tab` | Cycle forward through tabs in Group |
| `Super + Alt + Shift + Tab` | Cycle backward through tabs in Group |
| `Super + Ctrl + Left/Right` | Cycle through windows inside group |
| `Super + F` | Toggle Fullscreen |
| `Super + Alt + F` | Maximize window (keeping top bar) |
| `Super + J` | Toggle Split direction |
| `Super + P` | Toggle Pseudo-tiling |
| `Super + -` / `Super + =` | Resize active window horizontally |
| `Super + Shift + -` / `Super + Shift + =` | Resize active window vertically |
| `Super + ` ` ` or `Super + S` | Toggle **Scratchpad** workspace |
| `Super + Shift + ` ` ` or `Super + Alt + S` | Send window to **Scratchpad** |
| `Super + 1..0` | Switch to Workspace 1–10 |
| `Super + Tab` / `Super + Shift + Tab` | Cycle to next/previous Workspace |
| `Super + Shift + 1..0` | Move active window to Workspace 1–10 |
| `Super + Left/Right/Up/Down` | Move focus between windows |

### 🔊 Audio & Media
| Shortcut | Action |
| :--- | :--- |
| `XF86AudioRaiseVolume` / `LowerVolume` | Adjust Volume ±5% |
| `XF86AudioMute` | Toggle Audio Mute |
| `XF86AudioMicMute` | Toggle Microphone Mute |
| `XF86AudioPlay` / `Next` / `Prev` | Media Play / Pause / Skip |

---


## 📂 Repository Layout

```
omarchy-ubuntu/
├── assets/
│   └── preview.png             # Showcase screenshot
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
│   ├── omarchy-theme-sync-all  # Universal theme engine (Waybar, Wofi, Hyprland, Mako)
│   ├── omarchy-theme-bg-set    # Background setter with swaybg reload
│   ├── omarchy-menu-select     # Universal menu selector with Wofi fallback
│   ├── omarchy-power-menu      # System power & lock dashboard
│   ├── omarchy-clipboard-menu  # Cliphist clipboard search
│   ├── omarchy-update-waybar-theme # Palette extractor for Waybar CSS
│   ├── omarchy-launch-browser  # Universal browser launcher
│   ├── omarchy-launch-filemanager # Universal file manager launcher
│   └── omarchy-launch-polkit   # Universal polkit authentication agent launcher
├── system/
│   ├── omarchy.desktop         # Wayland session descriptor
│   ├── omarchy.conf            # /etc/omarchy.conf definition
│   └── omarchy.sh              # /etc/profile.d/ export
├── install.sh                  # All-in-one automated installer
├── uninstall.sh                # Clean uninstaller and backup restorer
├── LICENSE                     # MIT Open Source License
└── README.md
```

---

## 🗑️ Uninstallation

If you ever wish to remove Omarchy, run:

```bash
cd omarchy-ubuntu
./uninstall.sh
```
This restores all backed-up configurations (`.bak`) and cleanly removes the session entry without touching your primary desktop.

---

## ⚠️ Disclaimer

This is an independent community port created to bring the authentic Omarchy desktop experience to Ubuntu Linux. It is not affiliated with, sponsored, or endorsed by 37signals or OMACOM.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) &mdash; feel free to use, modify, distribute, and build upon it freely.

---

## 🤝 Credits & Acknowledgements

- Built upon the design vision of [Omarchy by OMACOM](https://github.com/omacom/omarchy).
- Powered by [Hyprland](https://hyprland.org/) and [Waybar](https://github.com/Alexays/Waybar).
