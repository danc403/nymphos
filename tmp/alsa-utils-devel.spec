content: Name:           alsa-utils-devel
Version:        1.2.10
Release:        1%{?dist}
Summary:        Development files for alsa-utils

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

Requires:       alsa-utils = %{version}-%{release}

%description
The alsa-utils-devel package contains the header files and
static libraries necessary for developing applications that use
the alsa-utils.

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

%files
%{_includedir}/alsa/*
%{_libdir}/libalsautils.so
%{_libdir}/pkgconfig/alsautils.pc

%changelog
* Tue Oct 24 2023 Dan Carpenter DanC403@gmail.com - 1.2.10-1
- Initial package build

