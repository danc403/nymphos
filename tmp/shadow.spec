%global dist .el8

Name:           shadow
Version:        4.17.2
Release:        1%{?dist}
Summary:        Shadow password suite
License:        BSD-3-Clause
URL:            https://github.com/shadow-maint/shadow
Source0:        shadow-%{version}.tar.xz
Requires:       bash
Requires:       coreutils
Requires:       cracklib
Requires:       grep
Requires:       libcap-ng
Requires:       perl
Requires:       util-linux
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bzip2
BuildRequires:  gettext
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkg-config

%description
The shadow package contains the shadow utilities which include
passwd, su, groups, shadowconfig, pwck, grpck, usermod, groupmod,
useradd, groupadd, userdel, groupdel, newusers, newgrp, chfn, chsh, id,
lastlog, and vigr.

%prep
%setup -q

%build
./configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} SBINDIR=/usr/bin MANDIR=/usr/share/man
rm -f %{buildroot}/usr/bin/su %{buildroot}/usr/bin/chsh %{buildroot}/usr/bin/chfn

%files
%defattr(-,root,root,-)
%license COPYING
/usr/bin/*
/etc/*
/usr/share/man/*
/usr/share/doc/shadow-%{version}/*

%changelog
* Tue Feb 24 2025 Dan Carpenter <DanC403@gmail.com> - 4.17.2-1
- Initial build
