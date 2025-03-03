
Name:           gzip
Version:        1.12
Release:        1%{?dist}
Summary:        Basic gzip utilities for Nymph Linux.

License:        GPLv3+
URL:            <upstream_url>
Source0:        tarballs/gzip/gzip-1.12.tar.xz

BuildArch:      x86_64

BuildRequires:  glibc
BuildRequires: zlib
Requires:       glibc
Requires: zlib

%description
This package provides the core gzip utilities for the Nymph Linux distribution.

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
* Sat Mar 01 2025 Dan Carpenter <danc403@gmail.com> - 1.12-1
- Initial package for Nymph Linux.
