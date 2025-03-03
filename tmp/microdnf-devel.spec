content: Name:           microdnf-devel
Version:        3.10.1
Release:        1%{?dist}
Summary:        Development files for microdnf

License:        GPLv2+
URL:            https://github.com/rpm-software-management/microdnf

Source0:        %{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkg-config
BuildRequires:  python3-devel
BuildRequires:  rpm-devel
BuildRequires:  libcomps-devel

Requires:       microdnf = %{version}-%{release}

%description
This package contains the header files and libraries needed to develop
applications that use microdnf.

%prep
%setup -q

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# remove binaries and man pages for the -devel package.
rm -f %{buildroot}%{_bindir}/microdnf
rm -f %{buildroot}%{_mandir}/man8/microdnf.8.gz
rm -f %{buildroot}%{_sysconfdir}/microdnf.conf
rm -f %{buildroot}%{_datadir}/bash-completion/completions/microdnf
rm -f %{buildroot}%{_datadir}/zsh/site-functions/_microdnf
rm -rf %{buildroot}%{_datadir}/microdnf/

%files
%{_includedir}/*
%{_libdir}/libmicrodnf*.so
%{_libdir}/pkgconfig/microdnf.pc

%changelog
* %{date} Dan Carpenter DanC403@gmail.com - 3.10.1-1
- Initial package build.

