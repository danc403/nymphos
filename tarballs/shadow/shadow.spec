Name:       shadow
Version:    4.14.3
Release:    1%{?dist}
Summary:    Utilities to administer user accounts

License:    BSD-3-Clause
URL:        https://github.com/shadow-maint/shadow
Source0:    shadow-%{version}.tar.xz

BuildRequires:  pam-devel
BuildRequires:  libcap-devel
BuildRequires:  openssl-devel

%description
The shadow utilities provide a set of tools for managing user accounts,
including password management, group management, and account locking.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --sysconfdir=/etc
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_sbindir}/chage
%{_sbindir}/chfn
%{_sbindir}/chpasswd
%{_sbindir}/chsh
%{_sbindir}/expiry
%{_sbindir}/gpasswd
%{_sbindir}/grpck
%{_sbindir}/groupadd
%{_sbindir}/groupdel
%{_sbindir}/groupmems
%{_sbindir}/groupmod
%{_sbindir}/login
%{_sbindir}/newgrp
%{_sbindir}/passwd
%{_sbindir}/pwck
%{_sbindir}/sg
%{_sbindir}/su
%{_sbindir}/useradd
%{_sbindir}/userdel
%{_sbindir}/usermod
%{_sbindir}/vigr
%{_sbindir}/vipw
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/*
/etc/login.defs
/etc/default/useradd

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
