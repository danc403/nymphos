Name: dkms
Version: 3.1.6
Release: 1%{?dist}
Summary: Dynamic Kernel Module System
License: GPLv2
URL: https://github.com/dell/dkms
Source0: %{name}-%{version}.tar.gz

BuildRequires: gcc, make, automake, autoconf, kernel-devel, kernel-headers, openssl
Requires: kernel-devel, kernel-headers, openssl

%description
DKMS enables kernel modules to be built and installed automatically when a new kernel is installed.

%prep
%setup -q

%build
make

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
%{_sbindir}/dkms
%{_mandir}/man8/dkms.8*
/usr/src/
/etc/dkms/
/var/lib/dkms/

%post
# add post install scripts here if needed.

%postun
# add post uninstall scripts here if needed.

%changelog
* %{__date} Dan Carpenter <danc403@gmail.com> - 2.1.6-1
- Initial RPM package.
