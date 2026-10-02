#!/usr/bin/env bash
# ==============================================================================
# Omarchy for Ubuntu - Uninstaller
# https://github.com/apravint/omarchy-ubuntu
# ==============================================================================
set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${YELLOW}======================================================${NC}"
echo -e "${RED}       Omarchy for Ubuntu - Uninstallation${NC}"
echo -e "${YELLOW}======================================================${NC}"

read -p "Are you sure you want to uninstall Omarchy from Ubuntu? (y/N): " -r CONFIRM
if [[ ! "$CONFIRM" =~ ^[Yy]$ ]]; then
    echo "Aborted."
    exit 0
fi

echo -e "\n${YELLOW}[1/3] Removing session entries...${NC}"
sudo rm -f /usr/share/wayland-sessions/omarchy.desktop
sudo rm -f /etc/omarchy.conf /etc/profile.d/omarchy.sh

echo -e "\n${YELLOW}[2/3] Removing local helper scripts...${NC}"
rm -f "$HOME/.local/bin"/omarchy-*

echo -e "\n${YELLOW}[3/3] Restoring original configuration backups...${NC}"
for dir in hypr waybar wofi; do
    if [ -d "$HOME/.config/$dir.bak" ]; then
        echo "Restoring ~/.config/$dir from ~/.config/$dir.bak..."
        rm -rf "$HOME/.config/$dir"
        mv "$HOME/.config/$dir.bak" "$HOME/.config/$dir"
    fi
done

echo -e "\n${GREEN}✔ Omarchy session removed and backups restored successfully!${NC}"
echo -e "Your primary desktop session (GNOME / KDE) is ready for your next login."
