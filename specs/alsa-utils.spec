Name:       alsa-utils
Version:    1.2.10
Release:    1%{?dist}
Summary:    ALSA utilities

License:    GPL-2.0-or-later
URL:        https://www.alsa-project.org/
Source0:    %{name}-%{version}.tar.bz2

BuildRequires:  alsa-lib-devel
BuildRequires:  libattr-devel
BuildRequires:  libcap-devel
BuildRequires:  libconfuse-devel
BuildRequires:  glib2-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  libusb-devel
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig

%description
alsa-utils provides a collection of command-line tools for configuring and
testing the Advanced Linux Sound Architecture (ALSA).

%prep
%setup -q

%build
./configure --prefix=/usr
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*

%changelog
* Mon Nov 20 2023 Your Name <your.email@example.com> - 1.2.10-1
- Initial build for x86_64 and OpenRC.
