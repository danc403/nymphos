name: lightdm-devel
version: 1.32.0
release: 1%{?dist}
summary: Development files for lightdm
License: GPLv2+
URL: https://github.com/canonical/lightdm
Source0: %{name:lightdm}-%{version}.tar.xz
Requires:
  - lightdm = %{version}-%{release}
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
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Description: This package contains header files and libraries needed to develop applications that use lightdm.
Build:
  - make %{?_smp_mflags}
Install:
  - make install DESTDIR=%{buildroot}
Files:
  - /usr/include/lightdm-1/*
  - /usr/lib64/liblightdm-gobject-1.so
  - /usr/lib64/pkgconfig/lightdm-gobject-1.0.pc
Changelog:
  -
    date: * Tue Oct 24 2023
    name: Dan Carpenter
    email: DanC403@gmail.com
    changes: - Initial RPM build
