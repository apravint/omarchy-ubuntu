# 🚀 Public Launch Announcements for Iram for Ubuntu

Use these pre-crafted, high-engagement posts to launch Iram for Ubuntu to the open-source community.

---

## 1. Reddit: r/linux & r/unixporn

### 📌 Post Title:
> **I built Iram for Ubuntu: A turnkey bootable Hyprland OS on Ubuntu LTS with 22 dynamic themes and automated dual-display management**

### 📝 Post Body:
```markdown
Hey r/linux / r/unixporn!

I've been working on a project to bridge the gap between bleeding-edge Wayland tiling window managers and enterprise-grade system stability: **Iram for Ubuntu**.

Traditionally, if you want to run Hyprland with fluid animations and modern tiling, you're pushed toward rolling-release distros like Arch or NixOS, which require constant maintenance and can break with proprietary drivers or enterprise workloads. If you try to compile Hyprland on Ubuntu yourself, you often end up in dependency and portal hell.

**Iram for Ubuntu** solves this by providing a complete, bootable Linux operating system distribution:

### ✨ What’s Inside:
* **True Standalone OS**: Ships as a hybrid **UEFI/BIOS bootable Live ISO** (`iram-os-*.iso`) built using an automated in-house compiler.
* **Intelligent Multi-Display**: Automatically prevents monitor overlapping at `0x0` coordinates and includes a native GUI monitor manager (`iram-displays-gui`).
* **Studio-Grade PipeWire Audio**: Instant sink toggling (`Super + Shift + A`) with ALSA stereo fallback to prevent HDMI TV converter stalls.
* **Persistent Daemon Architecture**: Status bar (`Waybar`) and wallpaper engine (`Swaybg`) run as managed `systemd` user units with monitor readiness polling loops (no fragile terminal scripts).
* **22-Theme Live Sync Engine**: Switch between Tokyo Night, Catppuccin Mocha, Nord, Gruvbox, Everforest, and 17 others instantly with `Super + Ctrl + Shift + Space` — re-tints Hyprland borders, Waybar pills, Wofi launcher, and Alacritty terminal with 0 restarts.
* **Turnkey Live Environment**: Direct autologin into the live Hyprland session with passwordless sudo (`iram:iram`) and installer to disk.

### 📦 Download & Source Code:
* **GitHub Repository**: https://github.com/apravint/iram-os
* **Latest ISO Download**: https://github.com/apravint/iram-os/releases/tag/v26.04.0
* **One-line Upgrade for existing Ubuntu users**:
  `curl -fsSL https://raw.githubusercontent.com/apravint/iram-os/main/install.sh | bash`

I would love to get your feedback, bug reports, and hardware compatibility test results!
```

---

## 2. Hacker News: Show HN

### 📌 Title:
> **Show HN: Iram for Ubuntu — Turnkey Hyprland desktop OS on Ubuntu LTS**

### 📝 Body:
```text
Hi Hacker News,

I built Iram for Ubuntu, a standalone Linux distribution that brings the fluid dynamics of the Hyprland Wayland compositor to the rock-solid base of Ubuntu LTS.

GitHub: https://github.com/apravint/iram-os
Latest ISO & Release: https://github.com/apravint/iram-os/releases/tag/v26.04.0

Why I built it:
Many developers love the keyboard-driven ergonomics, workspace grouping, and fluid animations of Hyprland, but don't want the rolling-release friction of Arch or NixOS for their daily driver workstations (especially when using Docker, CUDA, proprietary VPNs, or enterprise toolchains). Meanwhile, stock Ubuntu GNOME can feel heavy and lacks dynamic tiling.

Iram for Ubuntu provides:
- A hybrid UEFI/BIOS bootable Live ISO image with direct hardware installer
- Automated dual-display coordinate allocation preventing geometry collisions
- Managed systemd user services for Waybar and Swaybg with hardware readiness checks
- Dynamic PipeWire audio routing with instant keyboard sink toggles
- A 22-theme palette synchronization subsystem that updates window borders, bar modules, terminal colors, and menus simultaneously without restarting the compositor

You can test it directly by booting the Live ISO from a USB drive or converting an existing Ubuntu system via the included install script.

Feedback and contributions are warmly welcome!
```
