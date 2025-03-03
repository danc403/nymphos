Name:       rpm
Version:    4.20.1
Release:    1%{?dist}
Summary:    The RPM Package Manager

License:    GPLv2+
URL:        https://rpm.org/
Source0:    %{name}-%{version}.tar.bz2

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  libarchive-devel
BuildRequires:  lua-devel
BuildRequires:  openssl-devel
BuildRequires:  popt-devel
BuildRequires:  sqlite-devel
BuildRequires:  zlib-devel

%description
RPM is a powerful command line driven package management system
capable of installing, uninstalling, verifying, querying, and updating
computer software packages.

%prep
%setup -q

%build
autoreconf -fiv
%configure --prefix=/usr --sysconfdir=/etc --localstatedir=/var
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
%{_bindir}/rpm
%{_bindir}/rpmbuild
%{_bindir}/rpmsign
%{_bindir}/rpmverify
%{_bindir}/rpm2cpio
%{_bindir}/cpio2rpm
%{_mandir}/man1/rpm*
%{_mandir}/man8/rpm*
%{_libdir}/librpm*
%{_libdir}/rpm/macros.*
%{_includedir}/rpm/rpm*
%{_sysconfdir}/rpm/macros
%{_sysconfdir}/rpm/platform
%{_sysconfdir}/rpm/redhat
%{_sysconfdir}/rpm/rpmrc

%changelog
* Sat Mar 01 2025 Dan Carpenter <danc403@gmail.com> - 4.20.1-1
- Initial build for MicroRC and Microdnf.
