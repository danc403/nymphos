spec_content: Name:           ncurses-devel
Version:        6.4
Release:        1%{?dist}
Summary:        Development files for ncurses. MIT License

License:        MIT
URL:            https://invisible-island.net/ncurses/

Source0:        ncurses-%{version}.tar.gz

BuildRequires:  ncurses
Requires:       ncurses = %{version}-%{release}

%description
This package contains the header files and libraries needed to develop
applications that use the ncurses library.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --with-shared --with-normal --with-widec --with-cxx-shared --without-debug
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/lib*.so

%license COPYING

%changelog
* %{date} Dan Carpenter DanC403@gmail.com - %{version}-1
- Initial package build.

package_name: ncurses-devel
