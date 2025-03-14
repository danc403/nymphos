# Installing extlinux (syslinux) as a Bootloader on Nymph-OS

Extlinux is a variant of syslinux, a bootloader commonly used for live CDs and various applications. While not as prevalent as GRUB for desktop and laptop installations, extlinux is a robust and reliable option. Its simplicity, proven track record, and support for essential features make it a viable choice. These features include:

* A straightforward configuration file located in the `/boot` partition.
* The ability to chain-load Windows on systems with a Windows partition.
* Support for graphical menus with image backgrounds.

This document provides a step-by-step guide to installing and configuring extlinux on Nymph-OS.

## Installing extlinux

Begin by installing the `extlinux` and `syslinux-common` packages using `microdnf`.

**For Nymph-OS:**

```bash
sudo microdnf install extlinux syslinux-common

On Nymph-OS, this installation creates the /boot/extlinux directory, containing configuration files such as extlinux.conf (the main bootloader configuration) and linux.cfg (kernel boot stanzas).
Note: It's highly recommended to use a separate /boot partition, especially for multi-boot systems. This isolates boot files from individual Linux distributions, preventing potential data loss or conflicts. If /boot resides on the same filesystem as /, adjustments to these instructions may be necessary.

Installing the Bootloader
The package installation provides the necessary files, but it doesn't automatically configure the system to boot with extlinux. The following steps are required:

1. 
Install extlinux files to the /boot partition:
Bash
sudo extlinux --install /boot/extlinux

This command installs essential files into /boot/extlinux and potentially writes to the first sector of the /boot partition.

2. 
Ensure the /boot partition is bootable:
Use fdisk to check the bootable flag:
Bash
sudo fdisk -l /dev/sda

(Replace /dev/sda with your disk identifier.)
A * in the "Boot" column indicates a bootable partition. If the /boot partition (or the partition where /boot resides) is not marked bootable, use gparted or fdisk to set the bootable flag.

3. 
Replace the MBR (Master Boot Record) if necessary:
If GRUB was previously installed, it may have overwritten the MBR. Replace it with the extlinux MBR:
Bash
sudo dd if=/usr/lib/extlinux/mbr.bin of=/dev/sda bs=440 count=1 conv=notrunc

(Replace /dev/sda with your disk identifier.)
This command only modifies the boot block portion of the disk.

Setting up Menus
Extlinux requires additional files for menu display. Install these files:
Bash
sudo cp /usr/lib/syslinux/*menu* /boot/extlinux
sudo cp /usr/lib/syslinux/chain.c32 /boot/extlinux # For Windows or other OS chaining

Enable the menu in /boot/extlinux.conf:
ui vesamenu.c32

Add menu entries for Linux and other operating systems.

Linux Example:
label nymph
    menu label Nymph-OS, kernel {your kernel version here}
    kernel /vmlinuz-{your kernel version here}
    append initrd=/initrd.img-{your kernel version here} root=UUID={your root UUID here} ro quiet

Note: Replace {your kernel version here} and {your root UUID here} with the actual values for your Nymph-OS system. You can find your root UUID with the command blkid.

Windows Example:
LABEL Windows
KERNEL chain.c32
APPEND hd0 1

Reboot to view the extlinux menu.

Image Backgrounds in Menus
Extlinux supports image backgrounds in menus.
1. 
Prepare an image:
• Use a 640x480 image (JPG or PNG).
• For JPG, ensure "progressive" is disabled.
• Copy the image to /boot/extlinux/.
2. 
Add the background to extlinux.conf:
menu background splash.png
If JPG issues occur, use convert from ImageMagick:
Bash
convert orig.jpg splash.jpg
convert orig.jpg splash.png

Choose images with even colors for better menu text visibility.
Further Reading
• Refer to the extlinux and syslinux man pages.
• The text files within the syslinux git repository, especially menu.txt, are valuable resources.
