
Name:           grep
Version:        3.9
Release:        1%{?dist}
Summary:        Basic grep utilities for Nymph Linux.

License:        GPLv3+
URL:            <upstream_url>
Source0:        tarballs/grep/grep-3.9.tar.xz

BuildArch:      x86_64

BuildRequires:  glibc
Requires:       glibc

%description
This package provides the core grep utilities for the Nymph Linux distribution.

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
* <date> Your Name <your.email@example.com> - 3.9-1
- Initial package for Nymph Linux.
