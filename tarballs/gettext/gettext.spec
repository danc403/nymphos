Name: gettext
Version: 0.21.1
Release: 1%{?dist}
Summary: GNU internationalization and localization library
License: GPLv3+
URL: https://www.gnu.org/software/gettext/
Source0: %{name}-%{version}.tar.xz
BuildRequires:
  - autoconf
  - automake
  - libtool
  - pkgconfig
  - glibc-devel
Requires:
  - glibc

%description
GNU gettext is an internationalization and localization system commonly
used for writing multilingual programs.

%prep
%setup -q

%build
./configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
%doc README NEWS AUTHORS ChangeLog
/usr/bin/*
/usr/lib/libintl.so.*
/usr/share/man/man1/*
/usr/share/man/man3/libintl.3*
/usr/share/gettext/

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%changelog
* %{__date} Dan Carpenter <DanC403@gmail.com> - %{version}-1
- Initial RPM build of gettext.
