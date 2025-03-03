spec_content: Name:           ncurses
Version:        6.4
Release:        1%{?dist}
Summary:        NCURSES (new curses) is a library of functions that facilitate the writing of text-based user interfaces. MIT License

License:        MIT
URL:            https://invisible-island.net/ncurses/

Source0:        %{name}-%{version}.tar.gz

BuildRequires:  pkgconfig(autoconf)
BuildRequires:  pkgconfig(automake)
BuildRequires:  pkgconfig(libtool)

Requires:       bash
Requires:       coreutils
Requires:       gzip
Requires:       less

%description
NCURSES (new curses) is a library of functions that facilitate the
writing of text-based user interfaces.  It provides a character-based
windowing capability, supporting overlapping windows, colors, and
keypad handling, among other things.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --with-shared --with-normal --with-widec --with-cxx-shared --without-debug
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

#Remove the static library
rm -f %{buildroot}%{_libdir}/lib*.a

%files
%{_bindir}/captoinfo
%{_bindir}/clear
%{_bindir}/infocmp
%{_bindir}/ncurses*-config
%{_bindir}/reset
%{_bindir}/tic
%{_bindir}/toe
%{_bindir}/tput
%{_mandir}/man1/*
%{_libdir}/libncursesw.so.*
%{_libdir}/libformw.so.*
%{_libdir}/libmenuw.so.*
%{_libdir}/libpanelw.so.*
%{_libdir}/libticw.so.*
%{_libdir}/libncurses.so.*
%{_libdir}/libform.so.*
%{_libdir}/libmenu.so.*
%{_libdir}/libpanel.so.*
%{_libdir}/libtic.so.*
%{_datadir}/terminfo/*
%{_datadir}/ncurses/*
%license COPYING

%changelog
* %{date} Dan Carpenter DanC403@gmail.com - %{version}-1
- Initial package build.

package_name: ncurses
