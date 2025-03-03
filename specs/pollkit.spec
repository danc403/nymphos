Name:       polkit
Version:    1.23
Release:    1%{?dist}
Summary:    PolicyKit

License:    GPL-2.0-or-later
URL:        https://gitlab.freedesktop.org/polkit/polkit
Source0:    %{name}-%{version}.tar.bz2

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  dbus-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libselinux-devel
BuildRequires:  pkgconfig

%description
PolicyKit is a framework for controlling system-wide privileges.

%prep
%setup -q

%build
autoreconf -fiv
%configure --prefix=/usr --sysconfdir=/etc --localstatedir=/var
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
%{_bindir}/*
%{_libdir}/libpolkit*.so.*
%{_libdir}/pkgconfig/polkit-*.pc
%{_datadir}/polkit-1/rules.d/
%{_mandir}/man1/*
%{_mandir}/man5/*

%changelog
* Sat Mar 01 2025 Dan Carpenter <danc403@gmail.com> - 1.23-1
- Initial build for x86_64 and OpenRC.
