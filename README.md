# IRAM OS 🌌

> **IRAM OS (formerly Omarchy) – The agentic desktop environment.**

A preconfigured Hyprland desktop environment featuring sharp geometric tiling, compact window gaps, edge-to-edge Waybar, automated multi-display management, and integrated developer tools.

<div align="center">

[![GitHub Release](https://img.shields.io/github/v/release/apravint/iram-os?color=7aa2f7&logo=github&label=Release)](https://github.com/apravint/iram-os/releases)
[![Compositor: Hyprland](https://img.shields.io/badge/Compositor-Hyprland%20Wayland-00c853.svg?logo=wayland&logoColor=white)](https://hyprland.org)
[![Base: Linux](https://img.shields.io/badge/Base-Linux-FCC624.svg?logo=linux&logoColor=black)](https://kernel.org)
[![Audio: PipeWire](https://img.shields.io/badge/Audio-PipeWire%20%2B%20WirePlumber-brightgreen.svg)](https://pipewire.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

<br/>

<img src="assets/preview.png" alt="IRAM OS Desktop" width="100%" style="border-radius: 4px;" />

</div>

---

## Overview

**IRAM OS** provides an out-of-the-box, fully configured Wayland desktop experience. It packages Hyprland dynamic tiling, a flush edge-to-edge status bar, PipeWire audio routing, automated multi-monitor setup, and 22 switchable color schemes into an easy-to-install setup.

### Key Components

- **Compositor**: [Hyprland](https://hyprland.org) with sharp 90° edges (`rounding = 0`), compact 2px inner window gaps, and fluid dwindle tiling.
- **Status Bar**: [Waybar](https://github.com/Alexays/Waybar) configured edge-to-edge with workspace tabs, CPU/RAM telemetry, active audio sink indicators, weather, and power controls.
- **Application Launcher**: [Wofi](https://hg.sr.ht/~scoopta/wofi) with matching rectangular borders and fuzzy application search.
- **Audio Routing**: [PipeWire](https://pipewire.org) + [WirePlumber](https://gitlab.freedesktop.org/pipewire/wireplumber) policies with 1-click output cycler (`iram-audio-toggle`) across HDMI monitors, TVs, analog jacks, and Bluetooth.
- **Display Manager GUI**: `iram-displays-gui` utility to detect displays, prevent coordinate overlap, set refresh rates, and persist geometry.
- **Theme Suite**: 22 synchronized color schemes (Tokyo Night, Catppuccin Mocha, Nord, Gruvbox, etc.) switchable on the fly without session restart.
- **Productivity & Utilities**: Integrated clipboard history (`cliphist`), screen snip/recorder, OCR text extractor (`tesseract`), terminal copilot (`??`), and system health checker.

### Agentic OS Architecture

Iram implements dedicated system layers for autonomous intelligence, separating tools, memory, retrieval, documents, and execution traces:

- **Tool Server (FastMCP)**: `iram-mcp-server` exposes native Hyprland window management, audio controls, display topology, theme switching, and system self-healing over stdio MCP.
- **Dense Vector Retrieval (Qdrant)**: `iram-qdrant` runs an embedded on-disk Qdrant database at `~/.local/state/iram/qdrant_db`, providing semantic search over repositories and session history without background daemon overhead.
- **Temporal Knowledge Graph (Graphiti)**: `iram-graphiti` maintains persistent project knowledge, tracking entities, dependencies, and architectural decisions over time.
- **Live Documentation Scraper (Crawl4AI)**: `iram-crawl` extracts web documentation and API references into clean, token-efficient Markdown.
- **Document Ingestion (Docling)**: `iram-docling` converts PDFs, Office documents, and presentation slides into structured Markdown tables and text.
- **Code-as-Action Engine (smolagents)**: `iram-code-agent` synthesizes and executes atomic Python snippets inside an AST sandbox to perform multi-step desktop tasks in fewer LLM round-trips.
- **Stateful Long Coding Loops (LangGraph)**: `iram-workflow` provides cyclic graphs (Plan → Execute → Verify → Self-Heal) with SQLite checkpointing to run long-running refactors and configuration changes safely.
- **Telemetry & Traces (Arize Phoenix)**: `iram-trace` logs spans, execution latencies, and error post-mortems, feeding real-time status to the Waybar telemetry HUD.

---

## Installation

### Method 1: Automated Installation (Recommended)

Run the automated installer on an existing Linux system:

```bash
# Clone the repository
git clone https://github.com/apravint/iram-os.git
cd iram-os

# Run installer
chmod +x install.sh
./install.sh
```

Or install directly via curl:

```bash
curl -fsSL https://raw.githubusercontent.com/apravint/iram-os/main/install.sh | bash
```

#### After Installation:
1. Log out of your current desktop session.
2. At the display manager login screen (SDDM or GDM), select **Iram** (or **Hyprland**).
3. Log in to start the session.

---

### Method 2: Bootable Live ISO

For bare-metal deployment, a bootable ISO image is available:

1. Download the latest `.iso` from [GitHub Releases](https://github.com/apravint/iram-os/releases).
2. Write to a USB drive with [Ventoy](https://www.ventoy.net/), [BalenaEtcher](https://etcher.balena.io/), or `dd`:
   ```bash
   sudo dd if=iram-os-24.04-amd64.iso of=/dev/sdX bs=4M status=progress oflag=sync
   ```
3. Boot the USB drive and select **Start IRAM OS Live**.
   - Default user: `iram`
   - Password: `iram` (passwordless sudo enabled)

---

## Keyboard Shortcuts

### General & Applications

| Shortcut | Action | Description |
| :--- | :--- | :--- |
| `Super + Return` | **Terminal** | Opens Alacritty terminal |
| `Super + Alt + Return` | **Tmux Terminal** | Opens terminal attached to tmux session |
| `Super + Space` | **App Launcher** | Opens Wofi searchable application launcher |
| `Super + V` | **Clipboard History** | Search and paste clipboard history (`cliphist`) |
| `Super + K` | **Keybindings Menu** | Displays on-screen interactive shortcut cheat sheet |
| `Super + Escape` | **Power Menu** | Lock, Suspend, Reboot, or Shutdown |
| `Super + Ctrl + T` | **Activity Monitor** | Opens `btop` process & resource monitor |

### Window & Workspace Tiling

| Shortcut | Action | Description |
| :--- | :--- | :--- |
| `Super + Q` / `Super + W` | **Close Window** | Closes active window |
| `Super + T` | **Toggle Floating** | Switches focused window between tiling and floating |
| `Super + F` | **Fullscreen** | Toggles true fullscreen mode |
| `Super + O` | **Pin / PiP** | Pins floating window across all workspaces (Picture-in-Picture) |
| `Super + G` | **Toggle Tab Group** | Groups windows into tabbed containers |
| `Super + S` or ``Super + ` `` | **Scratchpad** | Toggles drop-down scratchpad workspace |
| `Super + 1` .. `Super + 0` | **Switch Workspace** | Switch to Workspace 1 through 10 |
| `Super + Shift + 1..0` | **Move Window** | Move focused window to Workspace 1 through 10 |
| `Super + Mouse Drag` | **Move / Resize** | Left-click drag to move; Right-click drag to resize |

### Displays, Audio & Hardware

| Shortcut | Action | Description |
| :--- | :--- | :--- |
| `Super + Ctrl + D` | **Display Settings** | Opens `iram-displays-gui` monitor setup panel |
| `Super + Shift + A` | **Cycle Audio Output** | Cycles audio between HDMI, TV, Analog 3.5mm, and Bluetooth |
| `Super + Ctrl + A` | **Volume Mixer** | Opens `pavucontrol` mixer |
| `Super + Ctrl + B` | **Bluetooth Manager** | Opens `blueman-manager` device panel |
| `Super + Ctrl + W` | **Network Settings** | Opens network connection manager |

### Themes & Status Bar

| Shortcut | Action | Description |
| :--- | :--- | :--- |
| `Super + Ctrl + Shift + Space` | **Theme Switcher** | Opens interactive 22-palette theme selector |
| `Super + Ctrl + Space` | **Next Wallpaper** | Cycles wallpaper within active theme |
| `Super + Shift + Space` | **Toggle Top Bar** | Shows / hides Waybar |
| `Super + Ctrl + Shift + B` | **Restart Top Bar** | Restarts Waybar and reloads CSS styles |

### Screenshots, Recording & OCR

| Shortcut | Action | Description |
| :--- | :--- | :--- |
| `Print` or `Super + Shift + S` | **Region Screenshot** | Drag to snip region; saves to `~/Pictures` & clipboard |
| `Alt + Print` | **Screen Recorder** | Start / stop screen recording (`wf-recorder`) |
| `Super + Print` | **Color Picker** | Eyedropper tool to copy hex color (`hyprpicker`) |
| `Super + Ctrl + Print` | **OCR Text Snipper** | Extracts on-screen text directly to clipboard (`tesseract`) |

---

## Included CLI Utilities

All tools are located in `bin/` and automatically installed to `~/.local/bin/` and `/usr/local/bin/`:

| Command | Description |
| :--- | :--- |
| `iram-displays-gui` | GTK GUI for configuring monitor positions, resolutions, and refresh rates |
| `iram-audio-toggle` | Cycles active default audio sink and moves active playback streams |
| `iram-audio-init` | Startup sound service ensuring HDMI/TV outputs are unmuted and persistent |
| `iram-theme-switch` | CLI theme selector supporting 22 themes |
| `iram-theme-switcher-gui` | GTK GUI theme selector with visual color previews |
| `iram-theme-sync-all` | Re-applies active theme palette across Hyprland, Waybar, Wofi, and Mako |
| `iram-restart-bar` | Cleanly reloads Waybar with display readiness check |
| `iram-health-agent` | Diagnoses failed systemd services, recovers audio daemons, and frees RAM |
| `iram-screenshot` | Interactive region screenshot utility |
| `iram-screenrecord` | Screen recorder writing MP4 output to `~/Videos` |
| `iram-emoji-picker` | Wofi-based searchable emoji selector |
| `iram-power-menu` | Fast session power menu (lock, sleep, reboot, shutdown) |
| `iram-repo-traffic` | Real-time clone and traffic analytics for GitHub repositories |
| `iram-mcp-server` | FastMCP desktop server exposing Hyprland, audio, themes, and memory over stdio MCP |
| `iram-qdrant` | Embedded local Qdrant vector retrieval engine for codebase chunks and memory |
| `iram-graphiti` | Temporal knowledge graph tracking project decisions, facts, and entity relations |
| `iram-crawl` | Documentation scraper powered by Crawl4AI converting web pages to clean markdown |
| `iram-docling` | Document parser powered by Docling converting PDFs and Office files to markdown |
| `iram-code-agent` | Code-as-action autonomous agent running atomic Python scripts via smolagents |
| `iram-workflow` | Stateful coding graph with verification and self-healing loops via LangGraph |
| `iram-trace` | Observability and execution traces layer powered by Arize Phoenix |
| `repomix` | Single-file AI context bundler for repositories |
| `?? <query>` | Shell copilot translating plain English queries to bash commands |

---

## Configuration Paths

Configurations are standard dotfiles located in `~/.config/`:

```
~/.config/
├── hypr/
│   ├── hyprland.conf      # Compositor layout, gaps, keybindings, and window rules
│   └── cursor.conf        # Active cursor theme and size
├── waybar/
│   ├── config.jsonc       # Bar modules, ordering, and exec hooks
│   ├── style.css          # Waybar CSS layout and styling
│   └── colors.css         # Active theme color variables
├── wofi/
│   └── style.css          # Application launcher appearance
├── mako/
│   └── config             # Desktop notification styling
└── wireplumber/
    └── wireplumber.conf.d/
        └── 50-hdmi-priority.conf # Audio hardware prioritization rules
```

---

## Building the ISO from Source

To compile the bootable Live ISO from source:

```bash
# Clone the repository
git clone https://github.com/apravint/iram-os.git
cd iram-os

# Run ISO build engine (requires root)
sudo bash build/build-iso.sh
```

Outputs the final ISO and SHA-256 checksum in `out/`.

---

## Uninstallation

To restore original configurations and remove installed scripts:

```bash
cd iram-os
./uninstall.sh
```

## ⚖️ License & Trademarks

This project is licensed under the **[MIT License](LICENSE)**.

### Attributions & Upstream Projects
- **Upstream Omarchy**: Originally created by [David Heinemeier Hansson](https://github.com/omacom/omarchy) under the MIT License.
- **Compositor**: [Hyprland](https://hyprland.org) by Vaxry and contributors (BSD-3-Clause).
- **Status Bar**: [Waybar](https://github.com/Alexays/Waybar) by Alexays and contributors (MIT).
- **Audio Routing**: [PipeWire](https://pipewire.org) & [WirePlumber](https://gitlab.freedesktop.org/pipewire/wireplumber) (MIT / LGPL).

### Legal & Trademark Disclaimers
- **Omarchy / IRAM**: "Omarchy" was originally authored by David Heinemeier Hansson (omacom/omarchy). IRAM OS is an independent community adaptation and desktop environment, and is not an official release of the upstream Omarchy project.
- All other third-party trademarks, product names, logos, and brands mentioned or displayed in this repository are the property of their respective owners. Their inclusion does not imply affiliation or endorsement.
