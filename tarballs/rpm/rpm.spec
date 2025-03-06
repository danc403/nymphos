Name:       rpm
Version:    4.20.1
Release:    1%{?dist}
Summary:    The RPM Package Manager

License:    GPLv2+
URL:        https://rpm.org/
Source0:    rpm-%{version}.tar.bz2

BuildRequires:  lua-devel
BuildRequires:  popt-devel
BuildRequires:  file-devel
BuildRequires:  zlib-devel
BuildRequires:  bzip2-devel
BuildRequires:  xz-devel
BuildRequires:  openssl-devel
BuildRequires:  db-devel
BuildRequires:  libarchive-devel
BuildRequires:  libmagic-devel
BuildRequires:  python3-devel

%package devel
Summary:    Development files for rpm
Requires:   rpm = %{version}-%{release}

%description
The RPM Package Manager (RPM) is a powerful command line driven package
management system capable of installing, uninstalling, verifying,
querying, and updating computer software packages.

%description devel
This package contains the development files for rpm.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/rpm
%{_bindir}/rpmbuild
%{_bindir}/rpmsign
%{_bindir}/rpm2cpio
%{_libdir}/librpm.so.*
%{_libdir}/librpmbuild.so.*
%{_mandir}/man1/rpm.1*
%{_mandir}/man1/rpmbuild.1*
%{_mandir}/man1/rpmsign.1*
%{_mandir}/man1/rpm2cpio.1*
%{_mandir}/man3/rpmio.3*

%files devel
%{_includedir}/rpm/
%{_libdir}/librpm.so
%{_libdir}/librpmbuild.so
%{_libdir}/librpm.a
%{_libdir}/librpmbuild.a
%{_libdir}/pkgconfig/rpm.pc

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
