Name: bash
Version: 5.2.15
Release: 1%{?dist}
Summary: The GNU Bourne Again shell
License: GPLv3+
URL: https://www.gnu.org/software/bash/
Source0: %{name}-%{version}.tar.gz
BuildRequires:
  - autoconf
  - automake
  - libtool
  - pkgconfig
  - readline-devel
  - ncurses-devel
  - gettext
Requires:
  - readline
  - ncurses

%description
Bash is an sh-compatible command language interpreter that executes
commands read from the standard input or from a file. Bash also
incorporates useful features from the Korn and C shells (ksh and csh).

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
/bin/bash
/etc/profile
/etc/bash.bashrc
/usr/share/man/man1/bash.1*
/usr/share/man/man1/sh.1*
/usr/share/doc/bash/

%changelog
* %{__date} Dan Carpenter <DanC403@gmail.com> - %{version}-1
- Initial RPM build of bash.
