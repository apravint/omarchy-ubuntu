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
    fonts-jetbrains-mono \
    python3 \
    git \
    socat

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
mkdir -p "$HOME/.config" "$HOME/.local/bin"

# Backup existing configs if they exist and are not symlinks
for dir in hypr waybar wofi; do
    if [ -d "$HOME/.config/$dir" ] && [ ! -d "$HOME/.config/$dir.bak" ]; then
        echo "Backing up existing ~/.config/$dir to ~/.config/$dir.bak..."
        cp -r "$HOME/.config/$dir" "$HOME/.config/$dir.bak"
    fi
done

# Copy configurations
cp -r "$REPO_DIR/config/"* "$HOME/.config/"

# Copy scripts & make executable
cp "$REPO_DIR/bin/"* "$HOME/.local/bin/"
chmod +x "$HOME/.local/bin/"omarchy-*

echo -e "\n${YELLOW}[5/6] Initializing default Omarchy theme...${NC}"
export OMARCHY_PATH=/usr/share/omarchy
omarchy theme set "Tokyo Night" || true
"$HOME/.local/bin/omarchy-update-waybar-theme" || true

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
echo -e "  • ${GREEN}Super + Space${NC}                 : Wofi Application Launcher"
echo -e "  • ${GREEN}Super + Return${NC}                : Terminal (Alacritty)"
echo -e "  • ${GREEN}Super + V${NC}                     : Clipboard History Manager"
echo -e "  • ${GREEN}Super + Ctrl + Shift + Space${NC}  : Omarchy 22-Theme Switcher"
echo -e "  • ${GREEN}Super + ` (Grave)${NC} / ${GREEN}Super + S${NC} : Toggle Scratchpad"
echo -e "  • ${GREEN}Super + Escape${NC}                : Power Menu (Lock, Sleep, Logout, Shutdown)"
echo -e "  • ${GREEN}Super + Shift + S${NC}             : Screenshot Snipping Tool"
