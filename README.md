# OmLinux 🌌

[![Build & Release Live ISO](https://github.com/apravint/omarchy-ubuntu/actions/workflows/build-iso.yml/badge.svg)](https://github.com/apravint/omarchy-ubuntu/actions/workflows/build-iso.yml)
[![GitHub Release](https://img.shields.io/github/v/release/apravint/omarchy-ubuntu?color=blue&logo=github)](https://github.com/apravint/omarchy-ubuntu/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Platform: Ubuntu 24.04 LTS](https://img.shields.io/badge/Base-Ubuntu%2024.04%20LTS-orange.svg)](https://ubuntu.com)
[![Compositor: Hyprland](https://img.shields.io/badge/Compositor-Hyprland-blue.svg)](https://hyprland.org)

> **The turnkey Linux operating system and desktop environment powered by Hyprland, Waybar, PipeWire, and OmLinux's complete 22-theme palette suite.**  
> Built on top of rock-solid **Ubuntu 24.04 LTS (Noble)** with out-of-the-box dual-monitor management, persistent systemd daemons, and zero-conflict keybindings.

![OmLinux Preview](assets/preview.png)

---

## ⚡ Get OmLinux

Choose the method that suits your workflow:

### Option 1: Bootable Live ISO (Recommended for New Installations)
Download the standalone, hybrid UEFI/BIOS bootable `.iso` image and flash it to any USB drive.

1. **Download the Latest ISO**:  
   Head to [**Releases**](https://github.com/apravint/omarchy-ubuntu/releases) and download `OmLinux-24.04-amd64.iso` and `sha256sum.txt`.
2. **Flash to USB**:  
   Use [BalenaEtcher](https://etcher.balena.io/), [Ventoy](https://www.ventoy.net/), or [Rufus](https://rufus.ie/) to write the image to a flash drive (8GB+ recommended).
3. **Boot & Test**:  
   Select your USB drive from your PC's boot menu (`F12`, `F11`, or `Esc`).
   - **Default Live User**: `omlinux`
   - **Default Password**: `omlinux` *(Passwordless sudo enabled)*
4. **Install**:  
   Run the desktop installer to install OmLinux directly to your SSD or hard drive.

---

### Option 2: One-Line Installer (For Existing Ubuntu Systems)
Already have Ubuntu 24.04 LTS installed? Transform your existing installation into OmLinux in minutes without losing your files or dual-boot setups:

```bash
curl -fsSL https://raw.githubusercontent.com/apravint/omarchy-ubuntu/main/install.sh | bash
```

*Or clone and run manually:*
```bash
git clone https://github.com/apravint/omarchy-ubuntu.git
cd omarchy-ubuntu
./install.sh
```

After installation completes, log out and select **OmLinux** from your display manager session menu.

---

## 🛠️ Build Your Own ISO Locally

You can generate the complete bootable Live ISO on any Ubuntu or Debian machine:

```bash
# 1. Clone the repository
git clone https://github.com/apravint/omarchy-ubuntu.git
cd omarchy-ubuntu

# 2. Run the automated ISO builder (requires sudo)
sudo bash build/build-iso.sh
```

The script will automatically bootstrap Ubuntu 24.04 LTS via `debootstrap`, inject all Hyprland configurations, compile the squashfs root, and produce a bootable image inside the `out/` folder:
- `out/OmLinux-24.04-amd64.iso`
- `out/sha256sum.txt`

Alternatively, you can trigger cloud builds directly on GitHub under the **Actions** tab with one click!

---

## ✨ System Highlights

- **Pre-Configured Hyprland Wayland Compositor**:
  - Fluid bezier window animations and acrylic opacity profiles.
  - Zero keybinding collisions; dedicated bindings for audio, screenshots, and tools.
- **Native Dual Display Manager (`omarchy-displays-gui`)**:
  - Built-in GUI tool to position, scale, enable, or disable multiple monitors.
  - Automatic collision protection ensures displays never overlap at identical coordinates.
- **PipeWire Audio Architecture**:
  - Instant output sink toggle (`Super + Shift + A` or middle-click on Waybar volume icon) between TV, monitors, and headphones.
  - Automatic ALSA card profile detection and unmuting.
- **22 Curated Themes with Live Sync (`omarchy-theme-sync-all`)**:
  - Includes *Tokyo Night, Catppuccin, Nord, Gruvbox, Everforest, Retro 82, Lumon, Matte Black, Hackerman*, and more.
  - Dynamically re-tints Hyprland borders, Waybar modules, Wofi menus, Alacritty terminal, and Mako notifications without restarting.
- **Robust Systemd Daemon Management**:
  - Waybar status bar and swaybg wallpaper runs as user systemd services (`waybar.service`, `swaybg.service`) with built-in monitor readiness checks.

---

## ⌨️ Essential Keybindings Reference

### 🚀 Launchers & Core Tools
| Shortcut | Action |
| :--- | :--- |
| `Super + Space` | **Omarchy Command Center Menu** |
| `Super + Alt + Space` | **Wofi** Application Launcher |
| `Super + Return` | **Alacritty** Terminal |
| `Super + Alt + Return` | **Tmux** Persistent Terminal Session |
| `Super + K` | **Keybindings Cheat Sheet Menu** |
| `Super + Shift + A` | **Audio Output Switcher** (Toggle between TV, Monitor & Headphones) |
| `Super + Ctrl + T` | **Activity / Process Monitor** (`btop`) |
| `Super + Ctrl + Shift + Space` | **22-Theme Switcher** |
| `Super + Ctrl + Space` | **Next Background Wallpaper** |
| `Super + V` | **Clipboard History Manager** (`cliphist`) |
| `Super + Escape` | **Power Menu** (Lock, Suspend, Logout, Reboot, Shutdown) |

### 📸 Capture & Text Extraction
| Shortcut | Action |
| :--- | :--- |
| `Print` or `Super + Shift + S` | **Region Screenshot** (Saves to `~/Pictures/Screenshots` & clipboard) |
| `Alt + Print` | **Screen Recording** (Toggle Start / Stop MP4 recording) |
| `Super + Print` | **Color Picker Eyedropper** (`hyprpicker` hex code to clipboard) |
| `Super + Ctrl + Print` | **OCR Text Extraction** (`tesseract` directly to clipboard) |
| `Super + Ctrl + C` | **Capture Dashboard Menu** |

### 🌐 Web Apps Suite
| Shortcut | Action |
| :--- | :--- |
| `Super + Ctrl + Shift + C` | **ChatGPT** AI Chatbot |
| `Super + Shift + Alt + A` | **Grok** AI Chatbot |
| `Super + Shift + C` | **HEY Calendar** |
| `Super + Shift + E` | **HEY Email** |
| `Super + Shift + Y` | **YouTube** |
| `Super + Shift + Alt + G` | **WhatsApp Web** |
| `Super + Shift + Ctrl + M` | **Google Maps** |
| `Super + Shift + X` | **X / Twitter** |

### 🪟 Window Management
| Shortcut | Action |
| :--- | :--- |
| `Super + Q` / `Super + W` | Close active window |
| `Super + T` | Toggle Floating mode |
| `Super + O` | Pin & Float Window (Sticky PiP) |
| `Super + G` | Toggle Tabbed Window Group |
| `Super + Alt + Tab` | Cycle forward through tabs in Group |
| `Super + F` | Toggle Fullscreen |
| `Super + S` or ``Super + ` `` | Toggle **Scratchpad** workspace |
| `Super + 1..0` | Switch to Workspace 1–10 |
| `Super + Shift + 1..0` | Move active window to Workspace 1–10 |

---

## 📂 Repository Layout

```
omarchy-ubuntu/
├── .github/
│   ├── workflows/
│   │   └── build-iso.yml       # Automated GitHub Actions ISO build & release CI
│   └── ISSUE_TEMPLATE/
│       ├── bug_report.md       # Standardized bug reporting form
│       └── feature_request.md  # Feature suggestion form
├── assets/
│   └── preview.png             # Showcase screenshot
├── build/
│   └── build-iso.sh            # Automated hybrid Live ISO build engine
├── config/
│   ├── hypr/                   # Hyprland window rules, monitors & keybindings
│   ├── waybar/                 # Top bar layout & CSS styling
│   ├── wofi/                   # Application launcher configuration
│   └── systemd/user/           # Waybar & Swaybg systemd service units
├── bin/                        # Omarchy CLI utilities, audio & display tools
├── system/                     # Wayland session descriptor & profile exports
├── install.sh                  # One-line web and local installer
├── uninstall.sh                # Clean uninstaller and config restorer
├── LICENSE                     # MIT Open Source License
└── README.md                   # Documentation & showcase
```

---

## 📄 License & Credits

- Licensed under the **[MIT License](LICENSE)**.
- Inspired by the aesthetic vision of [Omarchy by OMACOM](https://github.com/omacom/omarchy).
- Built on [Ubuntu](https://ubuntu.com), [Hyprland](https://hyprland.org), and [Waybar](https://github.com/Alexays/Waybar).
