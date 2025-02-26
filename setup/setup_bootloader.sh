#!/bin/bash

# Script to set up Syslinux/extlinux bootloader (from scratch)

# Mount point for boot partition (adjust if needed)
BOOT_MOUNT="/boot"

# Kernel and initramfs locations (adjust if needed)
KERNEL_IMAGE="/boot/vmlinuz"
INITRAMFS_IMAGE="/boot/initramfs.img"

# Bootloader configuration file
EXTLINUX_CONF="$BOOT_MOUNT/extlinux/extlinux.conf"

# Syslinux/extlinux binaries (adjust paths if needed)
SYSLINUX_BIN="/usr/lib/syslinux/extlinux.bin"
LDLINUX_SYS="/usr/lib/syslinux/ldlinux.sys"
LIBUTIL_C32="/usr/lib/syslinux/libutil.c32"
MENU_C32="/usr/lib/syslinux/menu.c32"
LIBCOM32_C32="/usr/lib/syslinux/libcom32.c32"
LIBPCI_C32="/usr/lib/syslinux/libpci.c32"
LIBMENU_C32="/usr/lib/syslinux/libmenu.c32"

# Create extlinux directory if it doesn't exist.
mkdir -p "$BOOT_MOUNT/extlinux"

# Copy Syslinux/extlinux binaries
cp "$SYSLINUX_BIN" "$BOOT_MOUNT/extlinux/"
cp "$LDLINUX_SYS" "$BOOT_MOUNT/extlinux/"
cp "$LIBUTIL_C32" "$BOOT_MOUNT/extlinux/"
cp "$MENU_C32" "$BOOT_MOUNT/extlinux/"
cp "$LIBCOM32_C32" "$BOOT_MOUNT/extlinux/"
cp "$LIBPCI_C32" "$BOOT_MOUNT/extlinux/"
cp "$LIBMENU_C32" "$BOOT_MOUNT/extlinux/"

# Create extlinux configuration file
cat <<EOF > "$EXTLINUX_CONF"
DEFAULT linux
LABEL linux
KERNEL $KERNEL_IMAGE
APPEND initrd=$INITRAMFS_IMAGE root=/dev/sda1 rw #adjust sda1 to your root partition.
EOF

# Install bootloader to boot device (adjust /dev/sda to your boot device)
extlinux --install "$BOOT_MOUNT/extlinux"
install-mbr /dev/sda #be very careful with this command.

echo "Syslinux/extlinux bootloader setup complete."
