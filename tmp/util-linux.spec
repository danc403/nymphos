spec: %global debug_package %{nil}

Name:           util-linux
Version:        2.39
Release:        1%{?dist}
Summary:        A collection of basic system utilities - GPL

License:        GPLv2+
URL:            https://www.kernel.org/pub/linux/utils/util-linux/

Source0:        %{name}-%{version}.tar.xz

BuildRequires:  ncurses-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(mount)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(readline)
BuildRequires:  gettext
BuildRequires:  automake
BuildRequires:  autoconf

Requires:       ncurses
Requires:       zlib
Requires:       coreutils
Requires:       bash

%description
The util-linux package contains a collection of basic system utilities.
These utilities are essential for the operation of a Linux system.

%prep
%autosetup

%build
./configure --prefix=%{_prefix} --libdir=%{_libdir} --sbindir=%{_sbindir} --disable-rpath --enable-fsck
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# Clean up unneeded files
rm -rf %{buildroot}%{_infodir}

%files
%{_bindir}/*
%{_sbindir}/*
%{_libdir}/*
%{_mandir}/man?/*
%{_sysconfdir}/*
%{_prefix}/share/locale/*
%{_prefix}/share/man/*
%{_prefix}/share/vim/*
%{_prefix}/share/bash-completion/*

%changelog
* %{date} Dan Carpenter DanC403@gmail.com - 2.39-1
- Initial package build.

name: util-linux
