
Name:           nano
Version:        6.4
Release:        1%{?dist}
Summary:        Basic nano utilities for Nymph Linux.

License:        GPLv3+
URL:            <upstream_url>
Source0:        tarballs/nano/nano-6.4.tar.xz

BuildArch:      x86_64

BuildRequires:  glibc
BuildRequires: ncurses
Requires:       glibc
Requires: ncurses

%description
This package provides the core nano utilities for the Nymph Linux distribution.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
%license COPYING
%doc README
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Sat Mar 01 2025 Dan Carpenter <danc403@gmail.com> - 6.4-1
- Initial package for Nymph Linux.
