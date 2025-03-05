Name: readline
Version: 8.2
Release: 1%{?dist}
Summary: GNU readline library
License: GPLv3+
URL: https://tiswww.cwru.edu/php/chet/readline/rltop.html
Source0: %{name}-%{version}.tar.gz
BuildRequires:
  - autoconf
  - automake
  - libtool
  - pkgconfig
  - ncurses-devel
Requires:
  - ncurses

%description
The GNU readline library provides a set of functions for use by
applications that allow users to edit command lines as they are
typed in. Both Emacs and vi editing modes are available.

%prep
%setup -q

%build
./configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
%doc README NEWS CHANGES
/usr/lib/libreadline.so.*
/usr/lib/libhistory.so.*
/usr/share/man/man3/readline.3*
/usr/share/man/man3/history.3*

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%changelog
* %{__date} Dan Carpenter <DanC403@gmail.com> - %{version}-1
- Initial RPM build of readline.
