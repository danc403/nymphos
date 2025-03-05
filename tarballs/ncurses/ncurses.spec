Name: ncurses
Version: 6.4
Release: 1%{?dist}
Summary: Terminal handling library
License: MIT
URL: https://invisible-island.net/ncurses/
Source0: %{name}-%{version}.tar.gz
BuildRequires:
  - autoconf
  - automake
  - libtool
  - pkgconfig
Requires:
  - zlib

%description
The ncurses library provides terminal-independent screen management
and cursor optimization.

%prep
%setup -q

%build
./configure --with-shared --without-debug --without-ada --enable-widec --enable-pc-files
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
%doc README NEWS CHANGES
/usr/lib/libncurses.so.*
/usr/lib/libpanel.so.*
/usr/lib/libform.so.*
/usr/lib/libmenu.so.*
/usr/lib/libtic.so.*
/usr/bin/tic
/usr/bin/infocmp
/usr/bin/toe
/usr/share/man/man1/tic.1*
/usr/share/man/man1/infocmp.1*
/usr/share/man/man1/toe.1*
/usr/share/man/man3/ncurses.3*

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%changelog
* %{__date} Dan Carpenter <DanC403@gmail.com> - %{version}-1
- Initial RPM build of ncurses.
