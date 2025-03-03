
Name:           tar
Version:        1.34
Release:        1%{?dist}
Summary:        Basic tar utilities for Nymph Linux.

License:        GPLv3+
URL:            <upstream_url>
Source0:        tarballs/tar/tar-1.34.tar.xz

BuildArch:      x86_64

BuildRequires:  glibc
BuildRequires: liblzma
BuildRequires: zlib
BuildRequires: bzip2
Requires:       glibc
Requires: liblzma
Requires: zlib
Requires: bzip2

%description
This package provides the core tar utilities for the Nymph Linux distribution.

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
* Sat Mar 01 2025 Dan Carpenter <danc403@gmail.com> - 1.34-1
- Initial package for Nymph Linux.
