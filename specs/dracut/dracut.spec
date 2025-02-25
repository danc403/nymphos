Name: dracut
Version: <version> # Replace with actual version
Release: 1%{?dist} # For RPM-based systems
Summary: Event-driven initramfs infrastructure with accessibility features.
License: GPLv2+
URL: https://github.com/dracutdevs/dracut
Source0: dracut-<version>.tar.gz # Replace with source tarball
BuildRequires: make, gcc, bash # Adjust as needed

%description
Dracut is an event-driven initramfs infrastructure with accessibility features.

%prep
%setup -q -n dracut-<version>

%build
make # Add any specific flags if needed.

%install
make install PREFIX=%{buildroot}/usr # Adjust PREFIX as needed

# Create accessibility configuration file
mkdir -p %{buildroot}/etc/dracut.conf.d
cat <<EOF > %{buildroot}/etc/dracut.conf.d/accessibility.conf
add_drivers+=" ahci nvme e1000e r8169 ext4 speakup snd_hda_intel snd_soc_sof_intel_pci"
add_modules+=" speakup espeak"
console_font="ter-v32b" # Example: Terminus bold 32-pixel font
EOF

# Create speakup_boot.sh script
mkdir -p %{buildroot}/usr/local/bin
cat <<EOF > %{buildroot}/usr/local/bin/speakup_boot.sh
#!/bin/bash
MESSAGE="$1"
if [ -n "\$MESSAGE" ]; then
  echo "\$MESSAGE" > /dev/console #or /dev/tts/0
fi
EOF
chmod +x %{buildroot}/usr/local/bin/speakup_boot.sh

# Dracut module for Speakup messages
mkdir -p %{buildroot}/usr/lib/dracut/modules.d/99speakup
cat <<EOF > %{buildroot}/usr/lib/dracut/modules.d/99speakup/module-setup.sh
#!/bin/bash
check() {
  return 0
}
depends() {
  return 0
}
install() {
  inst_hook pre-trigger 00\$hookdir/speakup_pre_trigger.sh
  inst_hook pre-udev 10\$hookdir/speakup_pre_udev.sh
  inst_hook pre-mount 20\$hookdir/speakup_pre_mount.sh
  inst_hook pre-pivot 30\$hookdir/speakup_pre_pivot.sh
  inst_hook pre-shutdown 40\$hookdir/speakup_pre_shutdown.sh
}
EOF
chmod +x %{buildroot}/usr/lib/dracut/modules.d/99speakup/module-setup.sh

cat <<EOF > %{buildroot}/usr/lib/dracut/modules.d/99speakup/speakup_pre_trigger.sh
#!/bin/bash
/usr/local/bin/speakup_boot.sh "Starting Dracut"
/usr/local/bin/speakup_boot.sh "Detecting hardware"
EOF
chmod +x %{buildroot}/usr/lib/dracut/modules.d/99speakup/speakup_pre_trigger.sh

cat <<EOF > %{buildroot}/usr/lib/dracut/modules.d/99speakup/speakup_pre_udev.sh
#!/bin/bash
/usr/local/bin/speakup_boot.sh "Starting device detection"
EOF
chmod +x %{buildroot}/usr/lib/dracut/modules.d/99speakup/speakup_pre_udev.sh

cat <<EOF > %{buildroot}/usr/lib/dracut/modules.d/99speakup/speakup_pre_mount.sh
#!/bin/bash
/usr/local/bin/speakup_boot.sh "Mounting root filesystem"
EOF
chmod +x %{buildroot}/usr/lib/dracut/modules.d/99speakup/speakup_pre_mount.sh

cat <<EOF > %{buildroot}/usr/lib/dracut/modules.d/99speakup/speakup_pre_pivot.sh
#!/bin/bash
/usr/local/bin/speakup_boot.sh "Switching to main system"
EOF
chmod +x %{buildroot}/usr/lib/dracut/modules.d/99speakup/speakup_pre_pivot.sh

cat <<EOF > %{buildroot}/usr/lib/dracut/modules.d/99speakup/speakup_pre_shutdown.sh
#!/bin/bash
/usr/local/bin/speakup_boot.sh "System shutting down"
EOF
chmod +x %{buildroot}/usr/lib/dracut/modules.d/99speakup/speakup_pre_shutdown.sh

%files
/usr/lib/dracut/*
/usr/bin/dracut
/etc/dracut.conf.d/*
/usr/local/bin/speakup_boot.sh
/usr/lib/dracut/modules.d/99speakup/

%changelog
* <date> <your name> <email> - <version>-1
- Initial build with Speakup messages.
