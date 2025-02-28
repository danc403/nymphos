
Name:           vim-tiny
Version:        9.0.1635
Release:        1%{?dist}
Summary:        Basic vim-tiny utilities for Nymph Linux.

License:        GPLv3+
URL:            <upstream_url>
Source0:        tarballs/vim-tiny/vim-9.0.1635.tar.gz

BuildArch:      x86_64

BuildRequires:  glibc
BuildRequires: ncurses
Requires:       glibc
Requires: ncurses

%description
This package provides the core vim-tiny utilities for the Nymph Linux distribution.

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
* <date> Your Name <your.email@example.com> - 9.0.1635-1
- Initial package for Nymph Linux.
