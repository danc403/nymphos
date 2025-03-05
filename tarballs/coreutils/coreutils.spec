Name: coreutils
Version: 9.3
Release: 1%{?dist}
Summary: Basic file, shell, and text manipulation utilities
License: GPLv3+
URL: https://www.gnu.org/software/coreutils/
Source0: %{name}-%{version}.tar.xz
BuildRequires:
  - autoconf
  - automake
  - libtool
  - pkgconfig
  - gettext
  - gmp-devel
  - acl-devel
  - attr-devel
Requires:
  - gmp
  - acl
  - attr

%description
The GNU Core Utilities are the basic file, shell, and text manipulation
utilities which are expected to exist on every operating system.

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
/usr/sbin/*
/usr/share/man/man1/*
/usr/share/man/man8/*
/usr/share/locale/*/LC_MESSAGES/coreutils.mo

%changelog
* %{__date} Dan Carpenter <DanC403@gmail.com> - %{version}-1
- Initial RPM build of coreutils.
