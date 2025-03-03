spec_content: %define debug_package %{nil}

Name:           coreutils
Version:        9.3
Release:        1%{?dist}
Summary:        GNU core utilities  (License: GPLv3+)

License:        GPLv3+
URL:            https://www.gnu.org/software/coreutils/

Source0:        %{name}-%{version}.tar.xz

BuildRequires:  gmp-devel
BuildRequires:  libcap-devel
BuildRequires:  texinfo

Requires:       bash
Requires:       acl
Requires:       attr
Requires:       glibc
Requires:       libcgroup
Requires:       libselinux
Requires:       coreutils-common = %{version}-%{release}

%description
The GNU Core Utilities are the basic file, shell and text manipulation
utilities of the GNU operating system.  These utilities are expected
to be available on every operating system.

%package common
Summary: Common files for coreutils

%description common
This package contains common files for coreutils.

%prep
%autosetup

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# Remove static libraries
rm -f %{buildroot}%{_libdir}/*.a

# Remove executable doc files
find %{buildroot}%{_docdir}/coreutils -type f -executable -print -delete

# Remove empty directories
find %{buildroot} -depth -type d -empty -print -delete

%files
%license COPYING
%{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/*
%exclude %{_bindir}/[[
%exclude %{_bindir}/test

%files common
%{_sbindir}/*
%attr(0755,root,root) %dir %{_libexecdir}
%{_libexecdir}/coreutils

%changelog
* %{date} Dan Carpenter DanC403@gmail.com - 9.3-1
- Initial package build.

