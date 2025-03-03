
Name:           coreutils
Version:        9.3
Release:        1%{?dist}
Summary:        Basic coreutils utilities for Nymph Linux.

License:        GPLv3+
URL:            <upstream_url>
Source0:        tarballs/coreutils/coreutils-9.3.tar.xz

BuildArch:      x86_64

BuildRequires:  glibc
Requires:       glibc

%description
This package provides the core coreutils utilities for the Nymph Linux distribution.

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
* Sat Mar 01 2025 Dan Carpenter <danc403@gmail.com> - 9.3-1
- Initial package for Nymph Linux.
