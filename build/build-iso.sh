#!/usr/bin/env bash
# ==============================================================================
# Omarchy for Ubuntu - Automated Live ISO Builder
# Builds a bootable hybrid UEFI/BIOS Live ISO based on Ubuntu LTS
# ==============================================================================
set -euo pipefail

# Auto-detect latest Ubuntu version from host or environment
HOST_CODENAME="$(. /etc/os-release 2>/dev/null && echo "${UBUNTU_CODENAME:-}" || echo "")"
HOST_VERSION="$(. /etc/os-release 2>/dev/null && echo "${VERSION_ID:-}" || echo "")"

CODENAME="${UBUNTU_CODENAME:-${HOST_CODENAME:-noble}}"
DISTRO_VERSION="${DISTRO_VERSION:-${HOST_VERSION:-24.04}}"
DISTRO_NAME="omarchy-ubuntu"
ARCH="amd64"
ROOTFS_DIR="/tmp/omarchy-rootfs"
ISO_DIR="/tmp/omarchy-iso"
OUTPUT_DIR="${PWD}/out"
ISO_NAME="${DISTRO_NAME}-${DISTRO_VERSION}-${ARCH}.iso"

# Colors for logging
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

log_info() { echo -e "${BLUE}[INFO]${NC} $1"; }
log_step() { echo -e "${GREEN}[STEP]${NC} $1"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
log_err()  { echo -e "${RED}[ERROR]${NC} $1"; }

if [ "$(id -u)" -ne 0 ]; then
    log_err "This script must be run as root (sudo)."
    exit 1
fi

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# ------------------------------------------------------------------------------
# 1. Install Build Dependencies on Host
# ------------------------------------------------------------------------------
log_step "Installing ISO build tools on host system..."
apt update -y
apt install -y \
    binutils \
    debootstrap \
    squashfs-tools \
    xorriso \
    grub-pc-bin \
    grub-efi-amd64-bin \
    mtools \
    dosfstools \
    isolinux \
    syslinux-utils \
    zstd

# ------------------------------------------------------------------------------
# 2. Prepare Clean Directories
# ------------------------------------------------------------------------------
log_step "Cleaning old build directories..."
umount -lf "${ROOTFS_DIR}/dev/pts" 2>/dev/null || true
umount -lf "${ROOTFS_DIR}/dev" 2>/dev/null || true
umount -lf "${ROOTFS_DIR}/proc" 2>/dev/null || true
umount -lf "${ROOTFS_DIR}/sys" 2>/dev/null || true
rm -rf "${ROOTFS_DIR}" "${ISO_DIR}" "${OUTPUT_DIR}"
mkdir -p "${ROOTFS_DIR}" "${ISO_DIR}/casper" "${ISO_DIR}/boot/grub" "${OUTPUT_DIR}"

# ------------------------------------------------------------------------------
# 3. Bootstrap Base Ubuntu System
# ------------------------------------------------------------------------------
log_step "Bootstrapping minimal Ubuntu ${CODENAME} (${ARCH})..."
debootstrap --arch="${ARCH}" --variant=minbase "${CODENAME}" "${ROOTFS_DIR}" http://archive.ubuntu.com/ubuntu/

# Mount virtual filesystems for chroot
mount --bind /dev "${ROOTFS_DIR}/dev"
mount --bind /dev/pts "${ROOTFS_DIR}/dev/pts"
mount -t proc proc "${ROOTFS_DIR}/proc"
mount -t sysfs sysfs "${ROOTFS_DIR}/sys"

# Ensure cleanup on trap
cleanup() {
    log_info "Cleaning up mounted virtual filesystems..."
    umount -lf "${ROOTFS_DIR}/dev/pts" 2>/dev/null || true
    umount -lf "${ROOTFS_DIR}/dev" 2>/dev/null || true
    umount -lf "${ROOTFS_DIR}/proc" 2>/dev/null || true
    umount -lf "${ROOTFS_DIR}/sys" 2>/dev/null || true
}
trap cleanup EXIT

# ------------------------------------------------------------------------------
# 4. Configure System Inside Chroot
# ------------------------------------------------------------------------------
log_step "Configuring packages, kernel, live-boot and desktop environment in chroot..."

# Setup apt sources with universe & multiverse
cat << EOF > "${ROOTFS_DIR}/etc/apt/sources.list"
deb http://archive.ubuntu.com/ubuntu/ ${CODENAME} main restricted universe multiverse
deb http://archive.ubuntu.com/ubuntu/ ${CODENAME}-updates main restricted universe multiverse
deb http://archive.ubuntu.com/ubuntu/ ${CODENAME}-security main restricted universe multiverse
EOF

# Setup hostname and hosts
echo "omarchy" > "${ROOTFS_DIR}/etc/hostname"
cat << EOF > "${ROOTFS_DIR}/etc/hosts"
127.0.0.1   localhost
127.0.1.1   omarchy
::1         localhost ip6-localhost ip6-loopback
EOF

# Install packages inside chroot
chroot "${ROOTFS_DIR}" /bin/bash << 'CHROOT_EOF'
export DEBIAN_FRONTEND=noninteractive
apt update -y

# Kernel & Live Boot Essentials
apt install -y --no-install-recommends \
    linux-generic \
    casper \
    lupin-casper \
    discover \
    laptop-detect \
    os-prober \
    network-manager \
    net-tools \
    wireless-tools \
    wpasupplicant \
    sudo \
    curl \
    git \
    wget \
    nano \
    vim \
    ca-certificates \
    software-properties-common

# Audio, Bluetooth & Display Server
apt install -y --no-install-recommends \
    pipewire \
    wireplumber \
    pipewire-pulse \
    pipewire-alsa \
    libspa-0.2-bluetooth \
    bluez \
    blueman \
    pavucontrol \
    sddm

# Enable Universe / Multiverse
add-apt-repository -y universe || true
add-apt-repository -y multiverse || true
apt update -y

# On Ubuntu 24.04 (noble), Hyprland is available via ppa:cpp-core/hyprland or universe in 24.10+/26.04+
if ! apt-cache show hyprland >/dev/null 2>&1; then
    add-apt-repository -y ppa:cpp-core/hyprland || true
    apt update -y || true
fi

# Hyprland & Wayland Desktop Stack
apt install -y \
    hyprland \
    waybar \
    swaybg \
    swaylock \
    mako-notifier \
    wofi \
    alacritty \
    grim \
    slurp \
    wl-clipboard \
    cliphist \
    playerctl \
    fonts-jetbrains-mono \
    fonts-font-awesome \
    pavucontrol \
    btop \
    jq || true

# Setup default live user: 'omarchy' with passwordless sudo
mkdir -p /etc/sudoers.d
groupadd -f sudo
groupadd -f audio
groupadd -f video

useradd -m -s /bin/bash -G sudo,audio,video omarchy || true
echo "omarchy:omarchy" | chpasswd || true
echo "omarchy ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/omarchy
chmod 0440 /etc/sudoers.d/omarchy

# Enable essential systemd services
systemctl enable NetworkManager.service 2>/dev/null || true
systemctl enable bluetooth.service 2>/dev/null || true
systemctl enable sddm.service 2>/dev/null || true

# Clean apt cache
apt autoremove -y
apt clean
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
CHROOT_EOF

# ------------------------------------------------------------------------------
# 5. Inject Omarchy Desktop Configurations & Scripts
# ------------------------------------------------------------------------------
log_step "Injecting Omarchy scripts, systemd units, and skeleton user configs..."

# Copy Omarchy system-wide binaries
mkdir -p "${ROOTFS_DIR}/usr/local/bin" "${ROOTFS_DIR}/usr/share/wayland-sessions"
cp -r "${REPO_ROOT}/bin/"* "${ROOTFS_DIR}/usr/local/bin/"
chmod +x "${ROOTFS_DIR}/usr/local/bin/"*

# Copy skeleton configs so every user (and live user) gets them
mkdir -p "${ROOTFS_DIR}/etc/skel/.config" "${ROOTFS_DIR}/etc/skel/.local/bin"
cp -r "${REPO_ROOT}/config/"* "${ROOTFS_DIR}/etc/skel/.config/"
cp -r "${REPO_ROOT}/bin/"* "${ROOTFS_DIR}/etc/skel/.local/bin/"

# Also copy into the live user's home directly
mkdir -p "${ROOTFS_DIR}/home/omarchy/.config" "${ROOTFS_DIR}/home/omarchy/.local/bin"
cp -r "${REPO_ROOT}/config/"* "${ROOTFS_DIR}/home/omarchy/.config/"
cp -r "${REPO_ROOT}/bin/"* "${ROOTFS_DIR}/home/omarchy/.local/bin/"

# Copy systemd units
mkdir -p "${ROOTFS_DIR}/etc/skel/.config/systemd/user" "${ROOTFS_DIR}/home/omarchy/.config/systemd/user"
cp -r "${REPO_ROOT}/config/systemd/user/"* "${ROOTFS_DIR}/etc/skel/.config/systemd/user/" 2>/dev/null || true
cp -r "${REPO_ROOT}/config/systemd/user/"* "${ROOTFS_DIR}/home/omarchy/.config/systemd/user/" 2>/dev/null || true

# Fix permissions
chroot "${ROOTFS_DIR}" chown -R omarchy:omarchy /home/omarchy 2>/dev/null || true

# Copy Wayland session desktop entry
if [ -f "${REPO_ROOT}/system/omarchy.desktop" ]; then
    cp "${REPO_ROOT}/system/omarchy.desktop" "${ROOTFS_DIR}/usr/share/wayland-sessions/omarchy.desktop"
fi

# Set custom OS Release Branding
cat << EOF > "${ROOTFS_DIR}/etc/os-release"
NAME="Omarchy for Ubuntu"
VERSION="${DISTRO_VERSION} LTS (${CODENAME})"
ID=omarchy-ubuntu
ID_LIKE="ubuntu debian"
PRETTY_NAME="Omarchy for Ubuntu ${DISTRO_VERSION} LTS (${CODENAME})"
VERSION_ID="${DISTRO_VERSION}"
HOME_URL="https://github.com/apravint/omarchy-ubuntu"
SUPPORT_URL="https://github.com/apravint/omarchy-ubuntu/issues"
BUG_REPORT_URL="https://github.com/apravint/omarchy-ubuntu/issues"
PRIVACY_POLICY_URL="https://github.com/apravint/omarchy-ubuntu"
UBUNTU_CODENAME=${CODENAME}
EOF

# Copy kernel & initrd into casper directory for ISO booting
log_step "Extracting kernel and initrd for live boot..."
cp "${ROOTFS_DIR}"/boot/vmlinuz-* "${ISO_DIR}/casper/vmlinuz"
cp "${ROOTFS_DIR}"/boot/initrd.img-* "${ISO_DIR}/casper/initrd"

# ------------------------------------------------------------------------------
# 6. Compress Root Filesystem into SquashFS
# ------------------------------------------------------------------------------
log_step "Compressing root filesystem into filesystem.squashfs (this may take a few minutes)..."
# Unmount virtual mounts before squashing
umount -lf "${ROOTFS_DIR}/dev/pts" 2>/dev/null || true
umount -lf "${ROOTFS_DIR}/dev" 2>/dev/null || true
umount -lf "${ROOTFS_DIR}/proc" 2>/dev/null || true
umount -lf "${ROOTFS_DIR}/sys" 2>/dev/null || true

mksquashfs "${ROOTFS_DIR}" "${ISO_DIR}/casper/filesystem.squashfs" \
    -comp zstd -Xcompression-level 15 \
    -e boot

# Generate filesystem size metadata for casper
printf $(du -sx --block-size=1 "${ROOTFS_DIR}" | cut -f1) > "${ISO_DIR}/casper/filesystem.size"

# ------------------------------------------------------------------------------
# 7. Configure GRUB Bootloader for BIOS & UEFI Hybrid Boot
# ------------------------------------------------------------------------------
log_step "Creating GRUB boot menu..."
cat << 'EOF' > "${ISO_DIR}/boot/grub/grub.cfg"
set default="0"
set timeout=5

insmod part_gpt
insmod part_msdos
insmod fat
insmod iso9660
insmod all_video
insmod font

set menu_color_normal=white/black
set menu_color_highlight=black/light-cyan

menuentry "🚀 Start Omarchy for Ubuntu Live (Default)" {
    set gfxpayload=keep
    linux /casper/vmlinuz boot=casper quiet splash ---
    initrd /casper/initrd
}

menuentry "🛡️ Start Omarchy for Ubuntu Live (Safe Graphics)" {
    set gfxpayload=keep
    linux /casper/vmlinuz boot=casper nomodeset quiet splash ---
    initrd /casper/initrd
}

menuentry "🔍 Check Disc for Defects" {
    linux /casper/vmlinuz boot=casper integrity-check quiet splash ---
    initrd /casper/initrd
}

menuentry "⚡ Reboot System" {
    reboot
}

menuentry "⏻ Power Off System" {
    halt
}
EOF

# ------------------------------------------------------------------------------
# 8. Generate Hybrid UEFI/BIOS Bootable ISO
# ------------------------------------------------------------------------------
log_step "Generating hybrid UEFI/BIOS bootable ISO image..."
grub-mkrescue -o "${OUTPUT_DIR}/${ISO_NAME}" "${ISO_DIR}" \
    -- -volid "OMARCHY"

# ------------------------------------------------------------------------------
# 9. Compute Checksums & Finish
# ------------------------------------------------------------------------------
log_step "Calculating SHA256 checksum..."
cd "${OUTPUT_DIR}"
sha256sum "${ISO_NAME}" > "sha256sum.txt"

echo -e "\n${BLUE}======================================================${NC}"
echo -e "${GREEN}🎉 ISO Build Completed Successfully!${NC}"
echo -e "${BLUE}======================================================${NC}"
echo -e "ISO File : ${GREEN}${OUTPUT_DIR}/${ISO_NAME}${NC}"
echo -e "Size     : $(du -h "${OUTPUT_DIR}/${ISO_NAME}" | cut -f1)"
echo -e "Checksum : $(cat "${OUTPUT_DIR}/sha256sum.txt")"
echo -e "${BLUE}======================================================${NC}"
