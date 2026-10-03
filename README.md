# Omarchy for Ubuntu 🌌
### The Turnkey Hyprland Desktop Operating System on Ubuntu LTS

<div align="center">

[![Build & Release Live ISO](https://github.com/apravint/omarchy-ubuntu/actions/workflows/build-iso.yml/badge.svg)](https://github.com/apravint/omarchy-ubuntu/actions/workflows/build-iso.yml)
[![GitHub Release](https://img.shields.io/github/v/release/apravint/omarchy-ubuntu?color=7aa2f7&logo=github&label=Latest%20ISO)](https://github.com/apravint/omarchy-ubuntu/releases)
[![Type: Operating System](https://img.shields.io/badge/Type-Linux%20Operating%20System-blue.svg?logo=linux)](#-about-omarchy-for-ubuntu)
[![Base: Ubuntu LTS](https://img.shields.io/badge/Base-Ubuntu%20LTS-E95420.svg?logo=ubuntu&logoColor=white)](https://ubuntu.com)
[![Compositor: Hyprland](https://img.shields.io/badge/Compositor-Hyprland%20Wayland-00c853.svg?logo=wayland&logoColor=white)](https://hyprland.org)
[![Audio: PipeWire](https://img.shields.io/badge/Audio-PipeWire%20%2B%20WirePlumber-brightgreen.svg)](https://pipewire.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

<br/>

**A complete, turnkey, bootable Linux operating system combining the rock-solid stability and massive software ecosystem of Ubuntu LTS with the bleeding-edge fluid dynamics of the Hyprland Wayland compositor.**

[Download Live ISO](https://github.com/apravint/omarchy-ubuntu/releases) • [About the OS](#-about-omarchy-for-ubuntu) • [Key Features](#-core-features--innovations) • [Installation Guide](#-installation--deployment) • [Keybindings](#-comprehensive-keyboard-shortcuts) • [Architecture](#-operating-system-architecture)

<br/>

<img src="assets/preview.png" alt="Omarchy for Ubuntu Desktop Showcase" width="100%" style="border-radius: 12px; box-shadow: 0 8px 24px rgba(0,0,0,0.4);" />

</div>

---

## 🌟 About Omarchy for Ubuntu

### What is Omarchy for Ubuntu?
**Omarchy for Ubuntu** is a modern, standalone 64-bit Linux distribution engineered from the ground up for developers, power users, creators, and tiling window enthusiasts. 

Traditionally, the Linux community has faced an unfortunate dilemma:
1. **Choose Arch Linux / NixOS** to get access to cutting-edge Wayland compositors like Hyprland, but accept rolling-release fragility, frequent manual maintenance, driver breaks, and friction with proprietary enterprise software (CUDA, Docker, Steam, proprietary VPNs).
2. **Choose Ubuntu LTS** for rock-solid stability, 5–10 years of security updates, hardware vendor support, and ubiquitous `.deb` packages, but remain locked into heavy, conventional desktop environments like GNOME or KDE that lack modern dynamic tiling workflows.
3. **Attempt to manually compile Hyprland on Ubuntu**, which almost universally leads to dependency breakage, broken portal integrations (`xdg-desktop-portal`), display manager race conditions, multi-monitor collisions, and fragile shell scripts that collapse after system updates.

**Omarchy for Ubuntu solves this entirely.** It bridges the reliability of Ubuntu LTS with the lightning-fast, hardware-accelerated animations of Hyprland, pre-configured with studio-grade audio routing, multi-display intelligence, persistent systemd daemons, and 22 curated aesthetic themes.

---

### 🛡️ A Full Operating System — Not a Customization, Theme, or Dotfiles Pack

> [!IMPORTANT]
> **Omarchy for Ubuntu is an independent, complete Linux Operating System distribution.**  
> It is **not** a theme, dotfiles collection, or cosmetic skin applied on top of GNOME.

* **Independent Bootable ISO Image (`omarchy-ubuntu-*.iso`)**: Boot directly on bare-metal hardware via UEFI or legacy BIOS without needing any pre-installed OS.
* **Complete Linux Kernel & Initramfs**: Ships with its own `linux-generic` kernel, hardware modules, network stack, and Casper live-boot engine.
* **Official System Identity**: Features dedicated OS identification in `/etc/os-release` (`ID=omarchy-ubuntu`, `PRETTY_NAME="Omarchy for Ubuntu LTS"`).
* **Managed System Daemons**: System services (status bar, wallpapers, display daemon, audio arbitration) run as first-class, managed **systemd units** with hardware-readiness polling loops — eliminating rogue background scripts and race conditions.
* **Turnkey Live Environment**: Boots straight into a graphical live desktop session with zero login friction (`User: omarchy`, passwordless sudo), ready for hardware testing, diagnostics, or direct installation to NVMe/SSD storage.
* **Unified Hardware Abstraction**: Automated multi-monitor coordinate calculation, dual-display separation, and non-blocking PipeWire audio switching built directly into the OS shell.

---

## 🏗️ Operating System Architecture

The following diagram illustrates how Omarchy for Ubuntu integrates from bare metal to user space:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        USER APPLICATIONS & APPS                        │
│   Alacritty • Wofi • Btop • Cliphist • Tesseract OCR • Pavucontrol    │
├────────────────────────────────────────────────────────────────────────┤
│                       OMARCHY SUITE & DAEMONS                          │
│   waybar.service  •  swaybg.service  •  omarchy-displays  •  Mako      │
├────────────────────────────────────────────────────────────────────────┤
│                       WAYLAND COMPOSITOR LAYER                         │
│   Hyprland (Bezier Motion Curves • Dynamic Tiling • Grouping • PiP)   │
├────────────────────────────────────────────────────────────────────────┤
│                        AUDIO & HARDWARE SUBSYSTEM                      │
│   PipeWire + WirePlumber (ALSA Stereo Profiles • Auto-Device Switch)   │
├────────────────────────────────────────────────────────────────────────┤
│                        SYSTEM RUNTIME & SERVICES                       │
│   systemd (PID 1) • SDDM Display Manager • NetworkManager • D-Bus      │
├────────────────────────────────────────────────────────────────────────┤
│                          BASE OPERATING SYSTEM                         │
│   Ubuntu LTS (Noble Numbat / Resolute) • dpkg / APT • Casper Live Boot │
├────────────────────────────────────────────────────────────────────────┤
│                         KERNEL & HARDWARE DRIVERS                      │
│   Linux Kernel (x86_64) • DRM/KMS • Mesa Graphics • Proprietary Drivers│
└────────────────────────────────────────────────────────────────────────┘
```

---

## ✨ Core Features & Innovations

### 🪟 1. Production-Grade Hyprland Wayland Compositor
- **Bespoke Fluid Animation Engine**: Tuned Bezier curve acceleration (`ease-out-cubic`) provides buttery-smooth window opening, workspace sliding, and floating transitions.
- **Dynamic Smart Tiling & Grouping**: Seamlessly split screens, create tabbed window groups (`Super + G`), toggle floating picture-in-picture (`Super + O`), or hide windows in a designated scratchpad workspace (`Super + S`).
- **Zero X11 Overhead**: Fully native Wayland architecture for tear-free display rendering, ultra-low input latency, and high refresh-rate gaming/productivity.

### 🖥️ 2. Intelligent Multi-Display Engine (`omarchy-displays-gui`)
- **Automated Coordinate Allocation**: Solves the classic Linux multi-monitor bug where secondary displays overlap at coordinate `0x0`. The OS automatically reads connected monitors (EDID), places extended displays side-by-side, and persists geometry across reboots.
- **Dedicated GUI Control Panel**: Launch `omarchy-displays-gui` anytime to configure resolutions, refresh rates, positions, and primary display tags graphically.
- **TV & Ultrawide Optimization**: Auto-detects 4K screens, external TVs, and ultrawide monitors without manual configuration file editing.

### 🔊 3. Studio-Grade PipeWire Audio Architecture
- **Hardware-Aware Audio Routing**: Seamlessly arbitrates audio between HDMI TV outputs, monitor speakers, USB DACs, and analog 3.5mm headphone jacks.
- **Instant Output Switching**: Press `Super + Shift + A` or middle-click the Waybar volume pill to cycle output sinks on the fly without interrupting playback.
- **Stereo Fallback Profiles**: Prevents multichannel surround-sound HDMI converter stalls by automatically enforcing ALSA 2-channel compatibility.

### 🎨 4. Dynamic 22-Theme Suite with Live Zero-Restart Sync
Switch your entire operating system aesthetic instantly with `Super + Ctrl + Shift + Space`. The built-in synchronization engine re-tints every OS component in milliseconds without restarting Hyprland or losing your open windows:
- **Curated Palettes**: *Tokyo Night, Catppuccin Mocha, Nord, Gruvbox Dark, Everforest, Retro 82, Lumon, Cyberpunk, Rose Pine, Solarized Dark, Matte Black, Hackerman*, and more.
- **Synchronized Ecosystem**: Re-colors Hyprland active window borders, Waybar pills and tooltips, Wofi search dialogs, Alacritty terminal palettes, and Mako desktop notifications simultaneously.

### ⏱️ 5. Resilient Systemd Daemon Management
- Unlike standard dotfile setups that launch components via brittle `exec-once` terminal commands, Omarchy for Ubuntu manages Waybar, Swaybg, and display daemons through **systemd user units** (`waybar.service`, `swaybg.service`).
- Includes hardware readiness polling loops: if an external monitor takes 3 seconds to wake up, the daemon waits cleanly rather than crashing the status bar.

### 🌐 7. Native Model Context Protocol (MCP) Server Integration
- **Standardized Agent Tool Protocol**: Integrates Anthropic's **Model Context Protocol (MCP)** specification directly into the desktop agent pipeline.
- **Built-in `omarchy-mcp-server`**: Provides native JSON-RPC tools for Hyprland window manipulation (`get_hyprland_windows`, `dispatch_hyprland`), system health diagnostics, theme switching (`set_omarchy_theme`), and live stock market news (`get_stock_news`).
- **Extensible Ecosystem**: Pre-configured in `~/.config/mcp/omarchy_mcp_config.json` with support for `@modelcontextprotocol/server-filesystem`, `mcp-server-git`, and `mcp-server-fetch`.

---

## 🚀 Installation & Deployment

### Option 1: Bootable Live ISO (Recommended for New Installations)
*Deploy Omarchy for Ubuntu directly onto bare-metal hardware or run it risk-free in live mode.*

#### Step 1: Download the Live ISO
Download the latest ISO image and checksum from the [Official Releases](https://github.com/apravint/omarchy-ubuntu/releases):
- `omarchy-ubuntu-<version>-amd64.iso`
- `sha256sum.txt`

Verify the download integrity:
```bash
sha256sum -c sha256sum.txt
```

#### Step 2: Flash to a USB Drive
Write the ISO to an 8GB+ USB flash drive using your preferred utility:
- **[Ventoy](https://www.ventoy.net/) (Recommended)**: Simply copy `omarchy-ubuntu-*.iso` directly onto your Ventoy USB drive.
- **[BalenaEtcher](https://etcher.balena.io/)**: Select the ISO, choose your USB drive, and click **Flash**.
- **[Rufus](https://rufus.ie/)**: Select the ISO and write in **DD Image Mode**.
- **CLI (`dd`)**:
  ```bash
  sudo dd if=omarchy-ubuntu-24.04-amd64.iso of=/dev/sdX bs=4M status=progress oflag=sync
  ```
  *(Replace `/dev/sdX` with your USB drive identifier)*

#### Step 3: Boot Your Hardware
1. Insert the USB drive into your PC.
2. Power on and open your BIOS/UEFI Boot Menu (typically `F12`, `F11`, `F10`, or `Esc`).
3. Select your USB drive to boot.
4. Choose **🚀 Start Omarchy for Ubuntu Live (Default)**.

#### Live Session Credentials:
- **Username**: `omarchy`
- **Password**: `omarchy` *(Passwordless sudo is pre-enabled)*

#### Step 4: Install to Disk
From the live session, launch the graphical installer from the desktop or run:
```bash
sudo omarchy-install
```

---

### Option 2: System Upgrade (Convert Existing Ubuntu Installation)
*If you already have Ubuntu LTS installed and wish to convert your current installation into Omarchy without reformatting your drive:*

```bash
curl -fsSL https://raw.githubusercontent.com/apravint/omarchy-ubuntu/main/install.sh | bash
```

*Or inspect and run locally:*
```bash
git clone https://github.com/apravint/omarchy-ubuntu.git
cd omarchy-ubuntu
chmod +x install.sh
./install.sh
```

Once installation finishes:
1. Log out of your desktop session.
2. In your display manager (SDDM/GDM), select **Omarchy** from the session menu.
3. Log in to start your authentic Omarchy desktop experience.

---

### Option 3: Virtual Machine Deployment (Testing)
Omarchy for Ubuntu runs smoothly in virtualized environments:
- **QEMU / KVM (Recommended)**:
  ```bash
  qemu-system-x86_64 -enable-kvm -m 4G -smp 4 \
    -vga virtio -display gtk,gl=on \
    -cdrom omarchy-ubuntu-24.04-amd64.iso -boot d
  ```
- **VirtualBox / VMware**:
  - Allocate at least 4 GB RAM, 25 GB Disk, and 4 vCPU cores.
  - Enable **3D Graphics Acceleration** and set Video Memory to 128 MB.

---

## 🛠️ Building the OS ISO from Source

Omarchy for Ubuntu includes an automated build pipeline capable of compiling the entire bootable ISO from source:

```bash
# 1. Clone the repository
git clone https://github.com/apravint/omarchy-ubuntu.git
cd omarchy-ubuntu

# 2. Run the automated ISO compiler (requires sudo)
sudo bash build/build-iso.sh
```

### The 9-Stage ISO Build Pipeline:
1. **Host Tooling Verification**: Installs `debootstrap`, `xorriso`, `squashfs-tools`, `mtools`, and GRUB EFI/BIOS utilities on the build host.
2. **Directory Workspace Sanitation**: Cleans mounts and establishes clean staging trees.
3. **Ubuntu Base Debootstrap**: Downloads a minimal Ubuntu base directly from canonical mirrors.
4. **Chroot Environment Provisioning**:
   - Injects DNS and official repository sources (main, restricted, universe, multiverse).
   - Injects the authenticated `ppa:cppiber/hyprland` repository.
   - Installs the Linux kernel (`linux-generic`), `initramfs-tools`, and Casper live-boot framework.
   - Installs PipeWire, WirePlumber, SDDM, Hyprland, Waybar, Wofi, Alacritty, and system fonts.
   - Clones and links the official Omarchy core theme suite into `/usr/share/omarchy`.
   - Creates the default live user `omarchy` with passwordless sudo and SDDM autologin.
5. **Desktop & Script Injection**: Copies system binaries (`/usr/local/bin/`), user skeleton configurations (`/etc/skel/`), application icons, and custom `/etc/os-release` branding.
6. **Kernel & Initrd Extraction**: Dereferences and extracts `vmlinuz` and `initrd.img` into `/casper/`.
7. **High-Ratio SquashFS Compression**: Compresses the root filesystem into `filesystem.squashfs` using `zstd -15`.
8. **Hybrid UEFI / BIOS ISO Generation**: Synthesizes dual-mode bootloader tables using `grub-mkrescue` and `xorriso`.
9. **Checksum Calculation**: Outputs final `.iso` image and `sha256sum.txt` in `out/`.

---

## ⌨️ Comprehensive Keyboard Shortcuts

### 🤖 Agentic OS & System Control Launchers
| Shortcut | Action | Description |
| :--- | :--- | :--- |
| `Super + A` | **🤖 Omarchy Agentic OS** | Launches AI Agent prompt for automated OS & window management |
| `Super + Shift + A` | **💬 Agent Interactive Sidecar** | Opens floating interactive AI chat sidecar terminal window |
| `Super + Ctrl + H` | **🛡️ Instant OS Self-Healing** | Diagnoses failed systemd units, restores PipeWire audio, cleans RAM |
| `Super + Ctrl + V` | **🎙️ AI Voice Assistant** | Hands-free audio recording, transcription, and agent execution |
| `Super + Shift + Print` | **👁️ Screen Vision Analyst** | Captures screen region and analyzes code errors/tables with Vision AI |
| `Super + Ctrl + G` | **🛡️ AI Security Guard** | Audits listening ports, SSH/sudo login attempts, and firewall status |
| `Super + Alt + N` | **📈 Live Stock Market News** | Interactive Wofi menu for real-time financial headlines & ticker news |
| `Super + Space` | **Command Menu** | Unified system launcher and quick action center |
| `Super + Alt + Space` | **Wofi Application Menu** | Fast searchable desktop app launcher |
| `Super + Return` | **Terminal** | Opens GPU-accelerated Alacritty terminal |
| `Super + Alt + Return` | **Tmux Session** | Opens terminal attached to persistent tmux session |
| `Super + K` | **Keybindings Cheat Sheet** | On-screen interactive shortcut cheat sheet |
| `Super + Ctrl + A` | **Audio Control Panel** | Opens PipeWire audio mixer & output selector (`pavucontrol`) |
| `Super + Ctrl + B` | **Bluetooth Manager** | Scans and pairs Bluetooth devices (`blueman-manager`) |
| `Super + Ctrl + W` | **Network Settings** | Wi-Fi and network connection manager (`nm-connection-editor`) |
| `Super + Ctrl + D` | **Displays Management** | Multi-monitor resolution and refresh rate GUI (`omarchy-displays-gui`) |
| `Super + Ctrl + P` | **Power & Session** | Fast system power and session control (`omarchy-power-menu`) |
| `Super + Ctrl + E` | **Emoji Picker** | 1,800+ searchable emojis with automatic clipboard copy (`omarchy-emoji-picker`) |
| `Super + Ctrl + T` | **Activity Monitor** | Launches real-time resource monitor (`btop`) |
| `Super + Ctrl + Shift + Space` | **22-Theme Switcher** | Open interactive theme selector palette |
| `Super + Ctrl + Space` | **Cycle Wallpaper** | Cycles to next wallpaper in current theme |
| `Super + Shift + Space` | **Toggle Top Bar** | Shows or hides the Waybar status bar dynamically |
| `Super + Ctrl + Shift + B` | **Restart Top Bar** | Instantly reloads Waybar process and styles |
| `Super + Backspace` | **Toggle Opacity** | Toggles window transparency on the focused application |
| `Super + Shift + Backspace` | **Toggle Gaps** | Toggles Hyprland window tiling gaps on/off |
| `Super + V` | **Clipboard Manager** | Search and paste clipboard history with previews (`cliphist`) |
| `Super + Escape` | **Power & Session Menu** | Lock, Suspend, Reboot, or Power Off the system |

### 📸 Capture, Screen Recording & OCR
| Shortcut | Action | Description |
| :--- | :--- | :--- |
| `Print` or `Super + Shift + S` | **Region Screenshot** | Interactive drag-to-snip; saves to `~/Pictures` & copies to clipboard |
| `Alt + Print` | **Screen Recorder** | Start / Stop MP4 screen recording with notification |
| `Super + Print` | **Color Picker** | Eyedropper tool; copies exact hex color code to clipboard (`hyprpicker`) |
| `Super + Ctrl + Print` | **OCR Text Snipper** | Drag over any screen text to extract directly to clipboard (`tesseract`) |
| `Super + Ctrl + C` | **Capture Dashboard** | Opens graphical capture tools control center |

### 🪟 Window & Workspace Management
| Shortcut | Action | Description |
| :--- | :--- | :--- |
| `Super + Q` / `Super + W` | **Close Window** | Closes currently focused window |
| `Super + T` | **Toggle Floating** | Switches focused window between tiling and floating mode |
| `Super + O` | **Pin / PiP Mode** | Floats and pins window across all workspaces (Sticky PiP) |
| `Super + G` | **Toggle Tab Group** | Groups multiple windows into a single tabbed container |
| `Super + Alt + Tab` | **Cycle Tabs** | Cycles forward through tabs in the active group |
| `Super + F` | **Toggle Fullscreen** | Expands active window to true fullscreen |
| `Super + S` or ``Super + ` `` | **Toggle Scratchpad** | Shows / hides quick drop-down scratchpad workspace |
| `Super + 1` .. `Super + 0` | **Switch Workspace** | Switches view to Workspace 1 through 10 |
| `Super + Shift + 1..0` | **Move Window** | Moves focused window to Workspace 1 through 10 |
| `Super + Mouse Drag` | **Move / Resize** | Left-click drag to move window; Right-click drag to resize |

---

## 🎨 Built-in Theme Collection

Omarchy for Ubuntu includes **22 curated, handcrafted themes** pre-installed:

| Theme Name | Style Description | Recommended Wallpaper Tone |
| :--- | :--- | :--- |
| **Tokyo Night** *(Default)* | Classic neon cyberpunk indigo & violet | Deep navy blue / neon cityscape |
| **Catppuccin Mocha** | Soothing pastel palette on deep dark background | Minimalist abstract / geometric |
| **Nord** | Arctic, north-bluish clean aesthetic | Snowy alpine landscapes / frost |
| **Gruvbox Dark** | Warm, retro earthy brown and amber tones | Vintage nature / retro typography |
| **Everforest** | Organic green nature-inspired palette | Misty pine forests / botanical |
| **Retro 82** | 1980s synthwave CRT nostalgic colorway | Retrowave sunset / wireframe grid |
| **Lumon** | Clean corporate monochrome with subtle cyan | Minimalist architecture / industrial |
| **Cyberpunk** | High-contrast electric yellow & magenta | Futuristic night / circuit patterns |
| **Rose Pine** | Warm floral muted tones with soft contrast | Dusk gradients / celestial art |
| **Solarized Dark** | Scientifically calibrated low-strain palette | Classic cyan & slate geometry |
| **Matte Black** | Stealth pitch black with sharp white accents | Pure dark OLED / carbon fiber |
| **Hackerman** | Classic terminal phosphor green on black | Matrix digital rain / terminal code |

*Press `Super + Ctrl + Shift + Space` at any time to switch themes instantly.*

---

## 💻 Hardware Requirements

### Minimum Requirements:
- **Processor**: 64-bit x86_64 Dual-Core CPU (2.0 GHz+)
- **Memory**: 2 GB RAM (4 GB recommended for multitasking)
- **Storage**: 15 GB available drive space (SSD recommended)
- **Graphics**: GPU with OpenGL 3.1 / Vulkan support (Intel HD Graphics 4000+, AMD GCN+, NVIDIA GTX 600+)
- **Display**: 1280x720 minimum resolution

### Recommended Specifications:
- **Processor**: Quad-Core Intel Core i5/i7 or AMD Ryzen
- **Memory**: 8 GB+ RAM
- **Storage**: 30 GB+ NVMe SSD
- **Graphics**: Intel Iris Xe, AMD Radeon RX, or NVIDIA GeForce (GTX 1060+)
- **Display**: 1920x1080 (FHD) or 2560x1440 (QHD) / 4K with multi-monitor support

---

## 📂 Repository File Structure

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
│   ├── alacritty/              # GPU-accelerated terminal styling & font settings
│   ├── hypr/                   # Hyprland window rules, monitor configs & keybindings
│   ├── pipewire/               # Low-latency PipeWire audio daemon profiles
│   ├── systemd/user/           # Waybar & Swaybg systemd service definitions
│   ├── waybar/                 # Waybar status bar layout, modules & CSS styling
│   ├── wireplumber/            # WirePlumber hardware arbitration policies
│   ├── wofi/                   # Application launcher themes & menu layouts
│   └── xdg-desktop-portal/     # Screen-sharing & Wayland portal configurations
├── bin/                        # Omarchy CLI utilities, audio toggles & display scripts
├── system/                     # Session desktop entry, system profile & environment exports
├── install.sh                  # One-line web and local installer script
├── uninstall.sh                # Clean uninstaller and configuration restorer
├── LICENSE                     # MIT Open Source License
└── README.md                   # Operating System documentation & specifications
```

---

## 🤝 Contributing & Community

Contributions are warmly welcomed! Help make Omarchy for Ubuntu even better:
1. **Report Issues**: Found a bug or hardware quirk? Open a report on our [Issues page](https://github.com/apravint/omarchy-ubuntu/issues).
2. **Suggest Enhancements**: Propose new features or theme ideas via [Feature Requests](https://github.com/apravint/omarchy-ubuntu/issues/new?template=feature_request.md).
3. **Submit Pull Requests**: Fork the repository, create a descriptive feature branch, and submit a PR for review.

---

## 📄 License & Attribution

- **License**: Released under the open-source **[MIT License](LICENSE)**.
- **Core Technologies**:
  - Base OS: [Ubuntu LTS](https://ubuntu.com) by Canonical
  - Compositor: [Hyprland](https://hyprland.org) by Vaxry & contributors
  - Status Bar: [Waybar](https://github.com/Alexays/Waybar) by Alexays
  - Audio Engine: [PipeWire](https://pipewire.org) & [WirePlumber](https://gitlab.freedesktop.org/pipewire/wireplumber)
  - Upstream Theme Suite: [Omarchy Core](https://github.com/omacom/omarchy)

<div align="center">

**Built with ❤️ for the Linux & Wayland Community.**  
*Experience authentic tiling desktop fluidity on the solid foundation of Ubuntu.*

</div>
