# Omarchy for Ubuntu 🌌

[![Build & Release Live ISO](https://github.com/apravint/omarchy-ubuntu/actions/workflows/build-iso.yml/badge.svg)](https://github.com/apravint/omarchy-ubuntu/actions/workflows/build-iso.yml)
[![GitHub Release](https://img.shields.io/github/v/release/apravint/omarchy-ubuntu?color=blue&logo=github)](https://github.com/apravint/omarchy-ubuntu/releases)
[![Type: Operating System](https://img.shields.io/badge/Type-Linux%20Operating%20System-blue.svg)](#-why-omarchy-for-ubuntu-is-a-true-operating-system-not-a-customization)
[![Base: Ubuntu LTS](https://img.shields.io/badge/Base-Ubuntu%20LTS-orange.svg)](https://ubuntu.com)
[![Compositor: Hyprland](https://img.shields.io/badge/Compositor-Hyprland%20Wayland-brightgreen.svg)](https://hyprland.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **A standalone, turnkey Linux Operating System distribution powered by the Hyprland Wayland compositor, native dual-display management, persistent systemd daemons, and PipeWire audio architecture.**  
> Built on top of the rock-solid **Ubuntu LTS** base, ready to boot live or install directly onto bare-metal hardware.

![Omarchy for Ubuntu Preview](assets/preview.png)

---

> [!IMPORTANT]
> ### 🛡️ A Full Operating System &mdash; Not a Theme, Skin, or Dotfiles Customization
> **Omarchy for Ubuntu is a complete, standalone Linux distribution.** It is **not** a cosmetic skin, desktop theme, or collection of shell scripts.
>
> * **Bootable on Bare Metal**: Ships as a hybrid **UEFI + BIOS Live ISO image** (`omarchy-ubuntu-*.iso`) that boots directly from a USB flash drive or virtual machine without requiring an existing operating system.
> * **Independent System Architecture**: Includes its own Linux kernel, systemd service architecture, hardware drivers, user-space skeleton (`/etc/skel/`), and dedicated OS identification (`/etc/os-release` ID: `omarchy-ubuntu`).
> * **Kernel-Level Hardware Handling**: Features automated multi-monitor collision protection, GPU-aware display geometry allocation, and non-blocking PipeWire/ALSA audio arbitration.
> * **Native Daemon Infrastructure**: Core services (status bar, wallpapers, audio init) run as managed systemd units (`waybar.service`, `swaybg.service`) with hardware-readiness loops &mdash; not ephemeral terminal subprocesses.
> * **Built-in System Installer**: Easily installable to your SSD, NVMe drive, or dual-boot disk configuration.

---

## 🏗️ Operating System Architecture

```
┌────────────────────────────────────────────────────────────────────────┐
│                        OMARCHY APPLICATIONS                           │
│   Wofi Launcher • Alacritty • Btop • Cliphist • Tesseract OCR • Pavu   │
├────────────────────────────────────────────────────────────────────────┤
│                     OMARCHY SYSTEM SERVICES                            │
│   waybar.service  •  swaybg.service  •  omarchy-displays  •  Mako      │
├────────────────────────────────────────────────────────────────────────┤
│                     WAYLAND COMPOSITOR LAYER                           │
│     Hyprland (Fluid Bezier Animations • Custom Window Geometry Rules)   │
├────────────────────────────────────────────────────────────────────────┤
│                      AUDIO & GRAPHICS STACK                            │
│      PipeWire + WirePlumber (Direct ALSA 2-Ch Routing) • DRM / KMS     │
├────────────────────────────────────────────────────────────────────────┤
│                       BASE OPERATING SYSTEM                            │
│         Ubuntu LTS (Noble / Resolute) • systemd init • Casper          │
├────────────────────────────────────────────────────────────────────────┤
│                       LINUX KERNEL & HARDWARE                          │
│          Linux Kernel (x86_64) • GPU / CPU / Display Drivers           │
└────────────────────────────────────────────────────────────────────────┘
```

---

## ⚡ Installing & Booting Omarchy for Ubuntu

### Method 1: Bootable Live ISO (Recommended for New Installations)
Install Omarchy for Ubuntu directly onto your computer or test it risk-free in live mode.

1. **Download the Official ISO**:  
   Visit the [**Releases**](https://github.com/apravint/omarchy-ubuntu/releases) page and download:
   - `omarchy-ubuntu-*.iso`
   - `sha256sum.txt`
2. **Flash to USB**:  
   Flash the `.iso` to an 8GB+ USB flash drive using [BalenaEtcher](https://etcher.balena.io/), [Ventoy](https://www.ventoy.net/), or [Rufus](https://rufus.ie/).
3. **Boot Your Hardware**:  
   Insert the USB drive into your PC, access your boot menu (`F12`, `F11`, `F10`, or `Esc`), and select the USB drive.
4. **Live Environment Credentials**:  
   - **Username**: `omarchy`
   - **Password**: `omarchy` *(Passwordless sudo enabled)*
5. **Install to Disk**:  
   Click the installer icon or run the graphical setup to deploy Omarchy for Ubuntu to your internal drive.

---

### Method 2: System Upgrade (For Existing Ubuntu Installations)
If you already have Ubuntu LTS installed and want to convert your current installation into Omarchy without reformatting your drive:

```bash
curl -fsSL https://raw.githubusercontent.com/apravint/omarchy-ubuntu/main/install.sh | bash
```

*Or clone and inspect the installer locally:*
```bash
git clone https://github.com/apravint/omarchy-ubuntu.git
cd omarchy-ubuntu
./install.sh
```

Once installed, log out and select **Omarchy** from your login screen.

---

## 🛠️ Building the OS ISO from Source

Omarchy for Ubuntu includes a self-contained ISO generation engine that bootstraps and compiles the entire operating system from scratch:

```bash
# 1. Clone the OS repository
git clone https://github.com/apravint/omarchy-ubuntu.git
cd omarchy-ubuntu

# 2. Compile the Live ISO (requires root privileges)
sudo bash build/build-iso.sh
```

### The Build Engine Pipeline:
1. **Debootstrap**: Pulls a clean minimal Ubuntu LTS base environment.
2. **Chroot Provisioning**: Configures kernel modules, network managers, audio drivers, and display servers.
3. **Desktop Injection**: Installs the Hyprland compositor, Waybar, 22 system themes, and Omarchy system utilities into `/etc/skel/`.
4. **SquashFS Compression**: Compresses the rootfs using high-ratio `zstd` compression.
5. **Hybrid Bootloader**: Generates dual UEFI and legacy BIOS partition tables via `xorriso` and `grub-mkrescue`.
6. **Artifact Output**: Creates `out/omarchy-ubuntu-*.iso` and calculates SHA256 checksums.

*Every GitHub release automatically triggers this build engine in the cloud via GitHub Actions CI/CD.*

---

## ✨ Built-in OS Features

- **Automated Dual-Display Management (`omarchy-displays-gui`)**:
  - Automatically identifies primary monitors and extended secondary displays.
  - Built-in collision prevention ensures displays never overlap at identical `0x0` coordinates.
- **Hardware-Aware Audio Routing**:
  - Instant output sink toggle (`Super + Shift + A` or middle-click the Waybar volume module) between monitors, external TVs, and audio jacks.
  - Dedicated ALSA stereo profiles prevent HDMI converter channel contention.
- **22 Curated Dynamic Themes**:
  - Includes *Tokyo Night, Catppuccin Mocha, Nord, Gruvbox, Everforest, Retro 82, Lumon, Matte Black, Hackerman*, and more.
  - Instant live palette synchronization re-tints Hyprland borders, Waybar pills, Wofi menus, Alacritty terminal, and Mako alerts simultaneously without compositor restarts.
- **Persistent Daemon Architecture**:
  - Waybar and Swaybg run under systemd user slices with automatic monitor readiness checks (`waybar.service`, `swaybg.service`).

---

## ⌨️ Essential Keyboard Shortcuts

### 🚀 System Control & Launchers
| Shortcut | Action |
| :--- | :--- |
| `Super + Space` | **Omarchy Command Center Menu** |
| `Super + Alt + Space` | **Wofi** Application Launcher |
| `Super + Return` | **Alacritty** GPU-Accelerated Terminal |
| `Super + Alt + Return` | **Tmux** Persistent Terminal Session |
| `Super + K` | **Keybindings Cheat Sheet Menu** |
| `Super + Shift + A` | **Audio Output Switcher** (Toggle TV, Monitor, Headphones) |
| `Super + Ctrl + T` | **Activity & Process Monitor** (`btop`) |
| `Super + Ctrl + Shift + Space` | **22-Theme Switcher** |
| `Super + Ctrl + Space` | **Next Background Wallpaper** |
| `Super + V` | **Clipboard History Manager** (`cliphist`) |
| `Super + Escape` | **Power & Session Dashboard** (Lock, Suspend, Reboot, Shutdown) |

### 📸 Capture, Screen Recording & OCR
| Shortcut | Action |
| :--- | :--- |
| `Print` or `Super + Shift + S` | **Region Screenshot** (Saves to `~/Pictures` & clipboard) |
| `Alt + Print` | **Screen Recording** (Toggle Start / Stop MP4 recording) |
| `Super + Print` | **Color Picker Eyedropper** (`hyprpicker` hex code to clipboard) |
| `Super + Ctrl + Print` | **OCR Text Extraction** (`tesseract` directly to clipboard) |
| `Super + Ctrl + C` | **Capture Dashboard Menu** |

### 🪟 Tiling Window Management
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

## 📂 OS Source Tree

```
omarchy-ubuntu/
├── .github/
│   ├── workflows/
│   │   └── build-iso.yml       # Automated cloud ISO compilation & release pipeline
│   └── ISSUE_TEMPLATE/
│       ├── bug_report.md       # Standardized bug reporting form
│       └── feature_request.md  # Feature suggestion form
├── assets/
│   └── preview.png             # OS desktop showcase preview
├── build/
│   └── build-iso.sh            # Complete UEFI/BIOS Live ISO build engine
├── config/
│   ├── hypr/                   # Hyprland window rules, monitors & keybindings
│   ├── waybar/                 # Top bar layout & CSS styling
│   ├── wofi/                   # Application launcher configuration
│   └── systemd/user/           # Waybar & Swaybg systemd daemon service units
├── bin/                        # Omarchy system CLI utilities, display & audio tools
├── system/                     # Wayland session descriptor & profile exports
├── install.sh                  # One-line web and local installer
├── uninstall.sh                # Clean uninstaller and configuration restorer
├── LICENSE                     # MIT Open Source License
└── README.md                   # Operating System documentation & specifications
```

---

## 📄 License & Open Source

- Released under the open-source **[MIT License](LICENSE)**.
- Base operating system components powered by [Ubuntu](https://ubuntu.com), [Hyprland](https://hyprland.org), [Waybar](https://github.com/Alexays/Waybar), and [PipeWire](https://pipewire.org).
