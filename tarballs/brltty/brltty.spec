
Name:           brltty
Version:        6.7
Release:        1%{?dist}
Summary:        Console-based braille terminal

License:        GPL-2.0-or-later
URL:            https://www.brltty.org/
Source0:        brltty-brltty-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  libusb-1.0-devel

%description
brltty is a console-based braille terminal. It provides access to the console
for blind users by translating text to braille.

%package devel
Summary:        Development files for brltty
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains the development files for brltty.

%prep
%autosetup -n brltty-brltty-%{version}

%build
autoreconf -fiv
%configure --with-usb --enable-braille-driver-autodetection
%make_build

%install
%make_install

%check
%make_check

%post
/sbin/ldconfig
# Add brltty to default runlevel for early startup.
%systemd_post brltty.service

%postun
/sbin/ldconfig
%systemd_preun brltty.service

%files
%license COPYING
%{_bindir}/brltty
%{_mandir}/man1/brltty.1.gz
%{_datadir}/brltty/

%files devel
%{_includedir}/brltty/
%{_libdir}/libbc.so.*
%{_libdir}/libbc.a
%{_libdir}/libbc.so
%{_libdir}/pkgconfig/libbc.pc

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-1
- Initial package.
