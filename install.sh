#!/usr/bin/env bash
# ==============================================================================
# Omarchy for Ubuntu - Automated Installer
# Experience authentic Omarchy (Hyprland + Themes + Waybar) on Ubuntu
# https://github.com/apravint/omarchy-ubuntu
# ==============================================================================
set -e

REPO_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}======================================================${NC}"
echo -e "${GREEN}     Omarchy for Ubuntu - Setup & Installation${NC}"
echo -e "${BLUE}======================================================${NC}"

# Check for sudo/root
if ! sudo -v &>/dev/null; then
    echo -e "${RED}Error: sudo access is required to install system packages.${NC}"
    exit 1
fi

echo -e "\n${YELLOW}[1/6] Installing required Wayland & Hyprland packages...${NC}"
sudo apt update
sudo apt install -y \
    hyprland \
    waybar \
    wofi \
    swaybg \
    swaylock \
    mako-notifier \
    grim \
    slurp \
    wl-clipboard \
    cliphist \
    playerctl \
    alacritty \
    btop \
    gawk \
    fonts-jetbrains-mono \
    wf-recorder \
    hyprpicker \
    tesseract-ocr \
    ripgrep \
    fd-find \
    tmux \
    fzf \
    zoxide \
    eza \
    bat \
    jq \
    curl \
    wlsunset \
    python3 \
    python3-pip \
    python3-gi \
    gir1.2-gtk-3.0 \
    pavucontrol \
    blueman \
    network-manager-gnome \
    polkit-kde-agent-1 \
    git \
    socat

# Install Ollama & OpenClaw Agentic Stack
if ! command -v ollama >/dev/null 2>&1; then
    echo "Installing Ollama Local LLM Engine..."
    curl -fsSL https://ollama.com/install.sh | sh || true
fi
if command -v pip3 >/dev/null 2>&1; then
    echo "Installing OpenClaw Agent Framework..."
    pip3 install openclaw 2>/dev/null || true
fi

echo -e "\n${YELLOW}[2/6] Installing Omarchy core repository & theme suite...${NC}"
if [ ! -d "/usr/share/omarchy" ]; then
    echo "Cloning official Omarchy repository..."
    sudo git clone --branch quattro https://github.com/omacom/omarchy.git /usr/share/omarchy
else
    echo "Updating existing Omarchy repository..."
    sudo git -C /usr/share/omarchy pull --ff-only || true
fi

# Ensure git safe.directory
sudo git config --system --add safe.directory /usr/share/omarchy || true

# Symlink omarchy binaries
echo "Linking Omarchy CLI binaries..."
sudo ln -sf /usr/share/omarchy/bin/* /usr/local/bin/
sudo ln -sf /usr/share/omarchy/bin/* /usr/bin/
sudo cp -a "$REPO_DIR/bin/"* /usr/local/bin/
sudo chmod +x /usr/local/bin/*

if [ -f "$REPO_DIR/system/sudoers.d/omarchy-theme-browser" ]; then
    sudo cp "$REPO_DIR/system/sudoers.d/omarchy-theme-browser" /etc/sudoers.d/omarchy-theme-browser
    sudo chmod 0440 /etc/sudoers.d/omarchy-theme-browser
fi

echo -e "\n${YELLOW}[3/6] Configuring system environment & session entries...${NC}"
# System-wide OMARCHY_PATH
sudo cp "$REPO_DIR/system/omarchy.conf" /etc/omarchy.conf
sudo cp "$REPO_DIR/system/omarchy.sh" /etc/profile.d/omarchy.sh
if ! grep -q "OMARCHY_PATH" /etc/environment 2>/dev/null; then
    echo "OMARCHY_PATH=/usr/share/omarchy" | sudo tee -a /etc/environment >/dev/null
fi

# Install Wayland session
sudo cp "$REPO_DIR/system/omarchy.desktop" /usr/share/wayland-sessions/omarchy.desktop

echo -e "\n${YELLOW}[4/6] Installing user dotfiles & scripts...${NC}"
mkdir -p "$HOME/.config" "$HOME/.local/bin" "$HOME/.config/omarchy/hooks"

# Backup existing configs if they exist and are not symlinks
for dir in hypr waybar wofi mako; do
    if [ -d "$HOME/.config/$dir" ] && [ ! -d "$HOME/.config/$dir.bak" ]; then
        echo "Backing up existing ~/.config/$dir to ~/.config/$dir.bak..."
        cp -r "$HOME/.config/$dir" "$HOME/.config/$dir.bak"
    fi
done

# Copy configurations
cp -r "$REPO_DIR/config/"* "$HOME/.config/"

# Copy scripts & make executable
cp "$REPO_DIR/bin/"* "$HOME/.local/bin/"
chmod +x "$HOME/.local/bin/"*

# Copy Omarchy desktop webapps and icons
mkdir -p "$HOME/.local/share/applications" "$HOME/.local/share/icons/hicolor/128x128/apps"
cp "$REPO_DIR/applications/"*.desktop "$HOME/.local/share/applications/" 2>/dev/null || true
cp "$REPO_DIR/applications/icons/"*.png "$HOME/.local/share/icons/hicolor/128x128/apps/" 2>/dev/null || true

# Symlink Debian-specific binary names if needed
ln -sf /usr/bin/batcat "$HOME/.local/bin/bat" 2>/dev/null || true
ln -sf /usr/bin/fdfind "$HOME/.local/bin/fd" 2>/dev/null || true

# Setup theme-set hook
cat << 'EOF' > "$HOME/.config/omarchy/hooks/theme-set"
#!/usr/bin/env bash
set -euo pipefail
THEME_NAME="${1:-$(cat "$HOME/.local/state/omarchy/current/theme.name" 2>/dev/null || echo "Unknown")}"
if [[ -x "$HOME/.local/bin/omarchy-theme-sync-all" ]]; then
    "$HOME/.local/bin/omarchy-theme-sync-all" || true
fi
if command -v notify-send >/dev/null 2>&1; then
    notify-send -a "Omarchy" "Theme Changed" "Active Theme: $THEME_NAME" -t 3000 2>/dev/null || true
fi
EOF
chmod +x "$HOME/.config/omarchy/hooks/theme-set"

# Configure Omarchy Shell Environment in ~/.bashrc
if ! grep -q "OMARCHY_PATH" "$HOME/.bashrc" 2>/dev/null; then
    cat << 'EOF' >> "$HOME/.bashrc"

# Omarchy Environment & Shell Tools
export OMARCHY_PATH=/usr/share/omarchy
export EDITOR=nvim
export VISUAL=nvim
if [[ -f "$OMARCHY_PATH/default/bash/rc" ]]; then
    source "$OMARCHY_PATH/default/bash/rc"
fi
if [[ -f /usr/share/doc/fzf/examples/key-bindings.bash ]]; then
    source /usr/share/doc/fzf/examples/key-bindings.bash
fi
if [[ -f /usr/share/doc/fzf/examples/completion.bash ]]; then
    source /usr/share/doc/fzf/examples/completion.bash
fi
EOF
fi

echo -e "\n${YELLOW}[5/6] Initializing default Omarchy theme & Self-Healing Timer...${NC}"
export OMARCHY_PATH=/usr/share/omarchy
omarchy theme set "Tokyo Night" || true
"$HOME/.local/bin/omarchy-theme-sync-all" || true
systemctl --user enable --now omarchy-agentd.service 2>/dev/null || true
systemctl --user enable --now omarchy-healthd.timer 2>/dev/null || true

# Unmute audio sinks so sound works out of the box
for sink in $(pactl list sinks short 2>/dev/null | awk '{print $2}'); do
    pactl set-sink-mute "$sink" 0 2>/dev/null || true
    pactl set-sink-volume "$sink" 100% 2>/dev/null || true
done

echo -e "\n${YELLOW}[6/6] Verifying Hyprland configuration...${NC}"
if hyprland --verify-config --config "$HOME/.config/hypr/hyprland.conf" >/dev/null 2>&1; then
    echo -e "${GREEN}Hyprland configuration verified: OK!${NC}"
else
    echo -e "${YELLOW}Warning: Hyprland configuration check had warnings, but file was installed successfully.${NC}"
fi

echo -e "\n${BLUE}======================================================${NC}"
echo -e "${GREEN}🎉 Installation Complete!${NC}"
echo -e "${BLUE}======================================================${NC}"
echo -e "To start using Omarchy:"
echo -e "1. Log out of your current session."
echo -e "2. In the display manager (login screen), select ${GREEN}Omarchy${NC} from the session menu."
echo -e "3. Log in and enjoy authentic Omarchy tiling!"
echo -e "\n${YELLOW}Useful Shortcuts:${NC}"
echo -e "  • ${GREEN}Super + A${NC}                     : 🤖 Launch Omarchy Agentic OS Assistant"
echo -e "  • ${GREEN}Super + Shift + A${NC}               : 💬 Launch Agent Interactive Sidecar Window"
echo -e "  • ${GREEN}Super + Ctrl + H${NC}                : 🛡️ Instant OS Self-Healing & Service Audit"
echo -e "  • ${GREEN}Super + Space${NC}                 : Wofi Application Launcher"
echo -e "  • ${GREEN}Super + Return${NC}                : Terminal (Alacritty)"
echo -e "  • ${GREEN}Super + Alt + Return${NC}          : Tmux Terminal Session"
echo -e "  • ${GREEN}Super + K${NC}                     : Keybindings Cheat Sheet Menu"
echo -e "  • ${GREEN}Super + V${NC}                     : Clipboard History Manager"
echo -e "  • ${GREEN}Super + Ctrl + Shift + Space${NC}  : Omarchy 22-Theme Switcher"
echo -e "  • ${GREEN}Super + Ctrl + Space${NC}          : Next Background in Active Theme"
echo -e "  • ${GREEN}Super + \` (Grave)${NC} / ${GREEN}Super + S${NC} : Toggle Scratchpad"
echo -e "  • ${GREEN}Super + Ctrl + T${NC}              : Activity Monitor (btop)"
echo -e "  • ${GREEN}Super + Escape${NC}                : Power Menu (Lock, Sleep, Logout, Shutdown)"
echo -e "  • ${GREEN}Super + Shift + S${NC}             : Screenshot Snipping Tool"
echo -e "  • ${GREEN}Super + Ctrl + Print${NC}          : OCR Text Extraction to Clipboard"
echo -e "  • ${GREEN}Super + Ctrl + R${NC}              : Set Reminder (Timer + Message)"
echo -e "  • ${GREEN}Super + Ctrl + Alt + T / W / B${NC}: Date/Time, Weather & Battery Notices"
echo -e "  • ${GREEN}Super + Ctrl + D${NC}              : Display & Monitor Settings GUI"
echo -e "  • ${GREEN}Super + Alt + D${NC}               : Instant Dictionary Definition Lookup"

