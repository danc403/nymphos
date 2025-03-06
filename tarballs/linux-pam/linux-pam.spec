Name:       linux-pam
Version:    1.7.0
Release:    1%{?dist}
Summary:    Pluggable Authentication Modules for Linux

License:    BSD-3-Clause
URL:        https://github.com/linux-pam/linux-pam
Source0:    linux-pam-%{version}.tar.gz

%package devel
Summary:    Development files for linux-pam
Requires:   linux-pam = %{version}-%{release}

%description
Linux-PAM (Pluggable Authentication Modules for Linux) is a suite of
shared libraries that enable local system administrators to choose
how applications authenticate users.

%description devel
This package contains the development files for linux-pam.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --sysconfdir=/etc
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_libdir}/libpam.so.*
%{_libdir}/libpam_misc.so.*
%{_libdir}/libpam_modules.so.*
%{_sbindir}/pam_tally
%{_sbindir}/pam_tally2
%{_mandir}/man8/pam_tally.8*
%{_mandir}/man8/pam_tally2.8*
/etc/pam.d/

%files devel
%{_includedir}/security/
%{_libdir}/libpam.so
%{_libdir}/libpam_misc.so
%{_libdir}/libpam.a
%{_libdir}/libpam_misc.a
%{_libdir}/pkgconfig/pam.pc

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
