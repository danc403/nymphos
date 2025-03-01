Name:       lightdm
Version:    1.32.0
Release:    1%{?dist}
Summary:    Lightweight Display Manager

License:    GPL-2.0-or-later
URL:        https://github.com/canonical/lightdm
Source0:    %{name}-%{version}.tar.xz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  dbus-devel
BuildRequires:  libX11-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXft-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXext-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXau-devel
BuildRequires:  libXdmcp-devel
BuildRequires:  pam-devel
BuildRequires:  polkit-devel
BuildRequires:  libnotify-devel
BuildRequires:  avahi-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  pkgconfig

%description
LightDM is a fast and lightweight display manager.

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
%{_libdir}/lightdm/
%{_sysconfdir}/lightdm/
%{_datadir}/lightdm/
%{_mandir}/man1/*
%{_mandir}/man5/*

%changelog
* Mon Nov 20 2023 Your Name <your.email@example.com> - 1.32.0-1
- Initial build for x86_64 and OpenRC.
