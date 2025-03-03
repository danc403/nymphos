name: lightdm
version: 1.32.0
release: 1%{?dist}
summary: A lightweight display manager
License: GPLv2+
URL: https://github.com/canonical/lightdm
Source0: %{name}-%{version}.tar.xz
BuildRequires:
  - gtk3-devel
  - glib2-devel
  - accountsservice-devel
  - libgcrypt-devel
  - pam-devel
  - libX11-devel
  - libXau-devel
  - libXdmcp-devel
  - libxcb-devel
  - xorg-server-devel
Requires:
  - gtk3
  - glib2
  - accountsservice
  - pam
  - libX11
  - dbus
  - systemd
Conflicts:
  - systemd
Provides:
  - config(lightdm)
Obsoletes:
  - config(lightdm)
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Autoreqprov: 0
Autoreq: 0
Description: LightDM is a cross-desktop display manager. Its main features include a well-defined greeter API, support for multiple display technologies (X11, Mir, Wayland, etc.), and a pluggable authentication framework.
Pre: getent passwd lightdm >/dev/null || useradd -r -d /var/lib/lightdm -s /bin/false lightdm
Postun: /bin/systemctl disable --now lightdm.service
Post: /bin/systemctl enable lightdm.service
Preun: if [ $1 = 0 ]; then
  /bin/systemctl stop lightdm.service
fi
Configure: %configure --sysconfdir=/etc
Build:
  - %configure
  - make %{?_smp_mflags}
Install:
  - make install DESTDIR=%{buildroot}
Files:
  - /etc/lightdm/*
  - /usr/bin/lightdm
  - /usr/share/lightdm/*
  - /usr/share/doc/%{name}-%{version}/
  - /usr/share/licenses/%{name}-%{version}/LICENSE
  - /usr/lib64/lightdm/*
  - %dir /run/lightdm
  - %exclude /usr/share/man/*
Changelog:
  -
    date: * Tue Oct 24 2023
    name: Dan Carpenter
    email: DanC403@gmail.com
    changes: - Initial RPM build
