Name:           kernel
Version:        6.5.0
Release:        1%{?dist}
Summary:        The Linux Kernel

License:        GPLv2
URL:            https://www.kernel.org/
Source0:        https://cdn.kernel.org/pub/linux/kernel/v6.x/linux-%{version}.tar.xz
BuildRequires:  bc, bison, flex, gcc, ncurses-devel, openssl-devel, perl, elfutils-libelf-devel, zlib-devel, libasan, libubsan, audit-libs-devel, libcap-devel, libelf-devel, libblkid-devel, libsodium-devel, libzstd-devel, liblz4-devel, liblzma-devel, xz-devel, bzip2-devel, binutils, make, patch, python3
BuildRequires:  openrc, openrc-devel, libuuid-devel, libselinux-devel, libsepol-devel, libacl-devel, libattr-devel, libpciaccess-devel, libdrm-devel, libgcrypt-devel, libgpg-error-devel, libcap-ng-devel, libunwind-devel, libmpc-devel, libmpfr-devel, libgmp-devel, libnuma-devel, libaio-devel, libibverbs-devel, librdmacm-devel, libibumad-devel, libibcm-devel, libfabric-devel, libibverbs-utils, libibcm-utils, libibumad-utils, librdmacm-utils, libfabric-utils, libibverbs-devel-static, libibcm-devel-static, libibumad-devel-static, librdmacm-devel-static, libfabric-devel-static, libibverbs-utils-static, libibcm-utils-static, libibumad-utils-static, librdmacm-utils-static, libfabric-utils-static

Patch0:         %{name}-generic.patch

ExclusiveArch:  x86_64
BuildArch:      x86_64

%description
The Linux Kernel.

%prep
%setup -q
%patch0 -p1

%build
make mrproper
cp /boot/config-$(uname -r) .config
make oldconfig
make %{?_smp_mflags} bzImage modules

# Generate extlinux image
make %{?_smp_mflags} bzImage EXT2_FS=y EXT3_FS=y EXT4_FS=y

%install
rm -rf %{buildroot}

make %{?_smp_mflags} modules_install install INSTALL_MOD_PATH=%{buildroot}

# Install the kernel and modules
install -D -m 0644 System.map %{buildroot}/boot/System.map-%{version}
install -D -m 0644 vmlinux %{buildroot}/boot/vmlinux-%{version}
install -D -m 0644 arch/x86/boot/bzImage %{buildroot}/boot/vmlinuz-%{version}
install -D -m 0644 arch/x86/boot/bzImage %{buildroot}/boot/extlinux/bzImage-%{version}

# Remove any unnecessary files from the module installation
find %{buildroot}/lib/modules/%{version} -type f -name "*.ko.cmd" -exec rm -f {} \;
find %{buildroot}/lib/modules/%{version} -type f -name "*.mod.c" -exec rm -f {} \;
find %{buildroot}/lib/modules/%{version} -type f -name "*.mod.o" -exec rm -f {} \;

%files
/boot/vmlinuz-%{version}
/boot/extlinux/bzImage-%{version}
/boot/System.map-%{version}
/boot/vmlinux-%{version}
/lib/modules/%{version}

%changelog
* Sun Oct 01 2023 Your Name <your.email@example.com> - 6.5.0-1
- Initial build of Linux Kernel 6.5.0 for x86_64 with OpenRC and extlinux support
