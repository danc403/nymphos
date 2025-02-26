Name: openrc
Version: <version> # Replace with actual version
Release: 1%{?dist} # For RPM-based systems
Summary: Service manager for Linux
License: GPLv2+
URL: https://github.com/OpenRC/openrc
Source0: openrc-<version>.tar.bz2 # Replace with source tarball
BuildRequires: make, gcc, bash # Adjust as needed

%description
OpenRC is a dependency-based init system that works with the system's init program, normally /sbin/init.

%prep
%setup -q -n openrc-<version>

%build
make # Add any specific flags if needed.

%install
make install PREFIX=%{buildroot}/usr # Adjust PREFIX as needed

# Create announce_login init script
mkdir -p %{buildroot}/etc/init.d
cat <<EOF > %{buildroot}/etc/init.d/announce_login
#!/sbin/openrc-run
command="/usr/local/bin/speakup_boot.sh"
command_args="Login prompt"
depend() {
        need ttyd
}
start() {
        ebegin "Announcing login prompt"
        \${command} "\${command_args}"
        eend \$?
}
EOF
chmod +x %{buildroot}/etc/init.d/announce_login

%files
/usr/sbin/*
/etc/init.d/*
/usr/lib/openrc/*
/usr/share/openrc/*
/usr/local/bin/speakup_boot.sh

%changelog
* <date> <your name> <email> - <version>-1
- Initial build with login announcement.
