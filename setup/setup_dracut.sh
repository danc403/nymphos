#!/bin/bash

# Script to configure Dracut for accessibility

# Configuration file location
DRACUT_CONF_DIR="/etc/dracut.conf.d"
ACCESSIBILITY_CONF="$DRACUT_CONF_DIR/accessibility.conf"

# Kernel version (replace with your actual kernel version)
KERNEL_VERSION="$(uname -r)"

# Create Dracut configuration directory if it doesn't exist
mkdir -p "$DRACUT_CONF_DIR"

# Create accessibility configuration file
cat <<EOF > "$ACCESSIBILITY_CONF"
add_drivers+=" ahci nvme e1000e r8169 ext4 speakup snd_hda_intel snd_soc_sof_intel_pci"
add_modules+=" speakup espeak"
console_font="ter-v32b" # Example: Terminus bold 32-pixel font
EOF

# Regenerate initramfs
dracut -f /boot/initramfs.img "$KERNEL_VERSION"

echo "Dracut accessibility setup complete."
