Name:       fontconfig
Version:    2.15.0
Release:    1%{?dist}
Summary:    A library to configure and customize font access

License:    MIT
URL:        https://www.freedesktop.org/software/fontconfig/
Source0:    %{name}-%{version}.tar.xz

BuildRequires:  pkgconfig
BuildRequires:  libXrender-devel
BuildRequires:  libXft-devel
BuildRequires:  freetype-devel
BuildRequires:  expat-devel

%description
Fontconfig is a library designed to provide system-wide font configuration,
customization, and application access.

%prep
%setup -q

%build
./configure --prefix=/usr --sysconfdir=/etc --localstatedir=/var
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
%{_bindir}/*
%{_libdir}/libfontconfig.so.*
%{_libdir}/pkgconfig/fontconfig.pc
%{_datadir}/fontconfig/
%{_sysconfdir}/fontconfig/
%{_mandir}/man1/*
%{_mandir}/man5/*

%changelog
* Sat Mar 01 2025 Dan Carpenter <danc403@gmail.com> - 2.15.0-1
- Initial build for x86_64 and OpenRC.
