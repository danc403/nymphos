Name: ncurses-devel
Version: 6.4
Release: 1%{?dist}
Summary: Development files for ncurses
License: MIT
URL: https://invisible-island.net/ncurses/
Source0: ncurses-6.4.tar.gz
BuildRequires:
  - autoconf
  - automake
  - libtool
  - pkgconfig
Requires:
  - ncurses = %{version}-%{release}

%description
Development files for ncurses.

%prep
%setup -q

%build
./configure --with-shared --without-debug --without-ada --enable-widec --enable-pc-files
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
/usr/include/ncursesw/
/usr/lib/libncursesw.so
/usr/lib/libpanelw.so
/usr/lib/libformw.so
/usr/lib/libmenuw.so
/usr/lib/libticw.so
/usr/lib/pkgconfig/ncursesw.pc
/usr/lib/pkgconfig/formw.pc
/usr/lib/pkgconfig/menuw.pc
/usr/lib/pkgconfig/panelw.pc
/usr/lib/pkgconfig/ticw.pc

%changelog
* %{__date} Dan Carpenter <DanC403@gmail.com> - %{version}-1
- Initial RPM build of ncurses-devel.
