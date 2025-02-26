Name: dracut
Version: <version> # Replace with actual version
Release: 1%{?dist} # For RPM-based systems
Summary: Event-driven initramfs infrastructure
License: GPLv2+
URL: https://github.com/dracutdevs/dracut
Source0: dracut-<version>.tar.gz # Replace with source tarball
BuildRequires: make, gcc, bash # Adjust as needed

%description
Dracut is an event-driven initramfs infrastructure.

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

%files
/usr/lib/dracut/* # Adjust as needed
/usr/bin/dracut
/etc/dracut.conf.d/*

%changelog
* <date> <your name> <email> - <version>-1
- Initial build.
