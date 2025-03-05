%global dist .el8

Name:           linux-devel
Version:        6.5.0
Release:        1%{?dist}
Summary:        Development files for the Linux Kernel
License:        GPLv2
URL:            https://www.kernel.org/
Source0:        https://cdn.kernel.org/pub/linux/kernel/v6.x/linux-%{version}.tar.xz
Requires:       linux = %{version}-%{release}
BuildRequires:  linux = %{version}-%{release}

%description
This package contains the header files needed for developing
kernel modules against the Linux Kernel.

%prep
%setup -q -n linux-%{version}

%build
# No build required for devel package

%install
# Headers are installed by the base linux package

%files
%defattr(-,root,root,-)
%{_includedir}/linux/
%{_includedir}/asm/
%{_includedir}/asm-generic/
%{_includedir}/scsi/
%{_libdir}/modules/%{version}/build/include/
%{_libdir}/modules/%{version}/source/include/

%changelog
* Sat Mar 01 2025 Dan Carpenter <danc403@gmail.com> - 6.5.0-1
- Initial build of Linux Kernel 6.5.0 development files for x86_64
