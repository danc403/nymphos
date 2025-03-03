
Name:           xz
Version:        5.4.1
Release:        1%{?dist}
Summary:        Basic xz utilities for Nymph Linux.

License:        GPLv3+
URL:            <upstream_url>
Source0:        tarballs/xz/xz-5.4.1.tar.xz

BuildArch:      x86_64

BuildRequires:  glibc
BuildRequires: liblzma
Requires:       glibc
Requires: liblzma

%description
This package provides the core xz utilities for the Nymph Linux distribution.

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
* Sat Mar 01 2025 Dan Carpenter <danc403@gmail.com> - 5.4.1-1
- Initial package for Nymph Linux.
