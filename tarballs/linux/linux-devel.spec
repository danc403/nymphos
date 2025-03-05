%global dist .el8

Name: linux-devel
Version: 6.5.3
Release: 1%{?dist}
Summary: Development files for the Linux Kernel
License: GPLv2
URL: https://www.kernel.org/
Source0: linux-%{version}.tar.xz
Source1: linux.config
BuildRequires: bc, bison, flex, gcc, ncurses-devel, openssl-devel, perl, elfutils-libelf-devel, zlib-devel, libasan, libubsan, audit-libs-devel, libcap-devel, libelf-devel, libblkid-devel, libsodium-devel, libzstd-devel, liblz4-devel, liblzma-devel, xz-devel, bzip2-devel, binutils, make, patch, python3
BuildRequires: openrc, openrc-devel, libuuid-devel, libacl-devel, libattr-devel, libpciaccess-devel, libdrm-devel, libgcrypt-devel, libgpg-error-devel, libcap-ng-devel, libunwind-devel, libmpc-devel, libmpfr-devel, libgmp-devel, libnuma-devel, libaio-devel, libibverbs-devel, librdmacm-devel, libibumad-devel, libibcm-devel, libfabric-devel, libibverbs-utils, libibcm-utils, libibumad-utils, librdmacm-utils, libfabric-utils, libibverbs-devel-static, libibcm-devel-static, libibumad-devel-static, librdmacm-devel-static, libfabric-devel-static, libibverbs-utils-static, libibcm-utils-static, libibumad-utils-static, librdmacm-utils-static, libfabric-utils-static
BuildRequires: syslinux, dracut

#Patch0: %{name}-generic.patch

ExclusiveArch: x86_64
BuildArch: x86_64

%description
Development files for the Linux Kernel.

%prep
%setup -q
#%patch0 -p1

%build
make mrproper
cp %{SOURCE1} .config
make oldconfig
make %{?_smp_mflags} headers_install INSTALL_HDR_PATH=%{buildroot}/usr

%install
rm -rf %{buildroot}
make headers_install INSTALL_HDR_PATH=%{buildroot}/usr

%files
/usr/include/linux/
/usr/include/asm/
/usr/include/asm-generic/
/usr/include/uapi/linux/
/usr/include/uapi/asm/
/usr/include/uapi/asm-generic/
/usr/include/config/

%changelog
* Sat Mar 01 2025 Dan Carpenter <danc403@gmail.com> - 6.5.3-1
- Initial build of Linux Kernel 6.5.3 development files for x86_64 with OpenRC.
