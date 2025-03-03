content: Name:           linux-pam-devel
Version:        1.7.0
Release:        1%{?dist}
Summary:        Development files for linux-pam

License:        BSD-3-Clause
URL:            http://www.linux-pam.org/

Source0:        %{name:linux-pam}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
Requires:       linux-pam = %{version}-%{release}

%description
This package contains the header files and libraries needed to develop
applications that use the Pluggable Authentication Modules (PAM) library.

%prep
%autosetup -n linux-pam-%{version}

%build
./configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir} --localstatedir=%{_localstatedir} --enable-audit --enable-shadow --enable-cracklib --enable-dbus
make

%install
make install DESTDIR=%{buildroot}


%files
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*

%changelog
* %{?date:%Y-%m-%d} Dan Carpenter DanC403@gmail.com 1.7.0-1
- Initial RPM release.

filename: linux-pam-devel.spec
