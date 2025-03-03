content: Name:           linux-pam
Version:        1.7.0
Release:        1%{?dist}
Summary:        Pluggable Authentication Modules for Linux
License:        BSD-3-Clause
URL:            http://www.linux-pam.org/

Source0:        %{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  openssl-devel
BuildRequires:  cracklib-devel
BuildRequires:  dbus-devel
BuildRequires:  libcap-ng-devel
BuildRequires:  audit-libs-devel

Requires:       shadow-utils
Requires:       cracklib
Requires:       dbus
Requires:       libcap-ng
Requires:       audit
Requires:       openssl

%description
PAM (Pluggable Authentication Modules) is a system of libraries
that handle authentication tasks for applications (services) in
a uniform manner. PAM separates the task of authentication from
the applications, allowing administrators to change authentication
mechanisms without re-compiling applications.

%prep
%autosetup

%build
./configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir} --localstatedir=%{_localstatedir} --enable-audit --enable-shadow --enable-cracklib --enable-dbus
make

%install
make install DESTDIR=%{buildroot}

# OpenRC configuration (example, adjust as needed)
mkdir -p %{buildroot}%{_sysconfdir}/pam.d
#install -m 644 YOUR_PAM_CONFIG %{buildroot}%{_sysconfdir}/pam.d/YOUR_APP

%files
%license COPYING
%{_bindir}/pam_console_apply
%{_libdir}/security/*.so
%{_sysconfdir}/pam.d/*
%{_mandir}/man8/pam_console_apply.8*
%{_mandir}/man5/*.5*
%{_mandir}/man8/*.8*
%{_sbindir}/*
%{_libdir}/*.so*
%{_libdir}/pkgconfig/*
%{_datadir}/aclocal/*
%{_datadir}/augeas/*
%{_datadir}/pam.d/*
%{_datadir}/security/*
%{_prefix}/include/*
%{_prefix}/lib/*
%{_prefix}/sbin/*

%changelog
* %{?date:%Y-%m-%d} Dan Carpenter DanC403@gmail.com 1.7.0-1
- Initial RPM release.

filename: linux-pam.spec
