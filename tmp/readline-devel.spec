content: Name:           readline-devel
Version:        8.2
Release:        1%{?dist}
Summary:        Development files for the GNU Readline library
License:        GPLv3+
URL:            https://tiswww.case.edu/php/chet/readline/rltop.html

Source0:        readline-%{version}.tar.gz

BuildRequires:  ncurses-devel
Requires:       readline = %{version}-%{release}

%description
This package contains the header files and libraries needed to develop
applications that use the GNU Readline library.

%prep
%setup -q -n %{name}-%{version}

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# Remove libtool archive
rm -f %{buildroot}%{_libdir}/*.la

%files
%{_includedir}/readline/*
%{_libdir}/libreadline.a
%{_libdir}/libhistory.a
%{_libdir}/pkgconfig/readline.pc
%{_mandir}/man3/*

%changelog
* %{_isodate} Dan Carpenter DanC403@gmail.com - 8.2-1
- Initial package build
filename: readline-devel.spec
