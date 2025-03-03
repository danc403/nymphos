content: Name:           alsa-utils
Version:        1.2.10
Release:        1%{?dist}
Summary:        Advanced Linux Sound Architecture (ALSA) utilities

License:        GPLv2+
URL:            https://www.alsa-project.org/

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gettext
BuildRequires:  alsa-lib-devel
BuildRequires:  ncurses-devel
BuildRequires:  libcap-devel

Requires:       alsa-lib
Requires:       ncurses
Requires:       libcap

%description
The alsa-utils package contains utilities for configuring and using
the Advanced Linux Sound Architecture (ALSA) subsystem.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} \
            --sysconfdir=%{_sysconfdir} \
            --localstatedir=%{_localstatedir} \
            --with-alsaconfdir=%{_sysconfdir}/alsa \
            --with-curses=ncurses
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# Remove static libraries
rm -f %{buildroot}%{_libdir}/*.a

%files
%license COPYING
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man1/*
%{_mandir}/man8/*
%config(noreplace) %{_sysconfdir}/alsa/*

%changelog
* Tue Oct 24 2023 Dan Carpenter DanC403@gmail.com - 1.2.10-1
- Initial package build

