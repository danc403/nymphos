Name: readline-devel
Version: 8.2
Release: 1%{?dist}
Summary: Development files for GNU readline library
License: GPLv3+
URL: https://tiswww.cwru.edu/php/chet/readline/rltop.html
Source0: readline-8.2.tar.gz
BuildRequires:
  - autoconf
  - automake
  - libtool
  - pkgconfig
  - ncurses-devel
Requires:
  - readline = %{version}-%{release}

%description
Development files for the GNU readline library.

%prep
%setup -q

%build
./configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
/usr/include/readline/
/usr/lib/libreadline.so
/usr/lib/libhistory.so
/usr/lib/pkgconfig/readline.pc

%changelog
* %{__date} Dan Carpenter <DanC403@gmail.com> - %{version}-1
- Initial RPM build of readline-devel.
