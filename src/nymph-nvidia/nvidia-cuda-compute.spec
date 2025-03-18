%global debug_package %{nil}
%global __brp_strip %{nil}
%global __brp_ldconfig %{nil}
%define _build_id_links none

Name:           nvidia-driver-compute
Version:        570.124.06
Release:        1%{?dist}
Summary:        NVIDIA compute driver packages (proprietary and open-source kernel)
License:        NVIDIA Proprietary / Open Source (GPLv2, etc.)
URL:            http://www.nvidia.com / [Open Source Project URL]
ExclusiveArch:  x86_64

Source0:        %{name}-%{version}-x86_64.tar.xz
Source1:        nvidia.conf # If you need this file, otherwise remove
Source4:        license
Source5:        changelog
Source6:        readme

BuildRequires:  dkms
BuildRequires:  make # Added for DKMS
BuildRequires:  kernel-devel # Added for DKMS (check if needed)

%package proprietary
Summary:        NVIDIA proprietary driver for CUDA compute (no display)
Requires:       %{name}-compute-libs = %{version}-%{release}
Requires:       nvidia-driver-proprietary-dkms
Requires:       nvidia-kmod-common
Requires:       nvidia-persistenced

Conflicts:      nvidia-driver-open

# Optional: Obsoletes using the version macro
Obsoletes:      nvidia-driver-open < %{version}-%{release}

%description proprietary
This package provides the NVIDIA proprietary driver and CUDA runtime libraries for
compute-only systems.

%package open
Summary:        Open-source kernel module support for NVIDIA compute
Requires:       %{name}-compute-libs = %{version}-%{release}
Requires:       nvidia-driver-open-dkms
Requires:       nvidia-kmod-common
Requires:       nvidia-persistenced

Conflicts:      nvidia-driver-proprietary

# Optional: Obsoletes using the version macro
Obsoletes:      nvidia-driver-proprietary < %{version}-%{release}

%description open
This package provides support for the open-source kernel module for NVIDIA compute.

%package libs
Summary:        Shared libraries for NVIDIA compute driver
Requires:       libnvidia-ml
Requires:       libnvidia-cfg

%description libs
This package provides the shared libraries for the NVIDIA compute driver.

%package proprietary-dkms
Summary:        DKMS support for NVIDIA proprietary compute driver
Requires:       dkms
Requires:       %{name}-compute-proprietary = %{version}-%{release}
Requires:       kernel-devel # Added for DKMS (check if needed)

%description proprietary-dkms
This package provides DKMS support for the NVIDIA proprietary compute driver.

%package open-dkms
Summary:        DKMS support for NVIDIA open-source compute kernel module
Requires:       dkms
Requires:       %{name}-compute-open = %{version}-%{release}
Requires:       kernel-devel # Added for DKMS (check if needed)

%description open-dkms
This package provides DKMS support for the NVIDIA open-source compute kernel module.

%package -n libnvidia-ml
Summary:        NVIDIA Management Library (NVML)

%description -n libnvidia-ml
Provides the NVIDIA Management Library (NVML).

%package -n libnvidia-cfg
Summary:        NVIDIA Config public interface (nvcfg)

%description -n libnvidia-cfg
Provides the NVIDIA Config public interface (nvcfg).

%prep
# Extract source
%setup -q -n %{name}-%{version}-x86_64

# Remove all the X org dependencies
rm -f libnvidia-pkcs11-openssl3.so.%{version}

# Create symlinks for shared objects
ldconfig -vn .
ln -sf libnvidia-encode.so.%{version} libnvidia-encode.so
ln -sf libnvcuvid.so.%{version} libnvcuvid.so
ln -sf libcuda.so.%{version} libcuda.so

%build
# No explicit build steps needed for pre-built userspace and DKMS will build modules

%install
# Install proprietary driver files
pushd %{builddir}/%{name}-%{version}-x86_64 # Use %{builddir} for clarity

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_datadir}/nvidia
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}/etc/modules-load.d
mkdir -p %{buildroot}%{_docdir}/%{name}

# Install binaries and libraries
install -m 0755 bin/* %{buildroot}%{_bindir}/
install -m 0755 sbin/* %{buildroot}%{_sbindir}/
install -m 0644 lib/* %{buildroot}%{_libdir}/
install -m 0644 share/nvoptix.bin %{buildroot}%{_datadir}/nvidia/
install -m 0644 share/sandboxutils-filelist.json %{buildroot}%{_datadir}/nvidia/
install -m 0644 man/* %{buildroot}%{_mandir}/man1/

# Install other files (if they exist and are needed)
# Example:
# install -m 0644 %{SOURCE1} %{buildroot}/etc/modules-load.d/nvidia.conf
install -m 0644 %{SOURCE4} %{buildroot}/license # Adjust path if needed
install -m 0644 %{SOURCE5} %{buildroot}%{_docdir}/%{name}/
install -m 0644 %{SOURCE6} %{buildroot}%{_docdir}/%{name}/

popd

# Install DKMS files for proprietary kernel
mkdir -p %{buildroot}/usr/src/nvidia-driver-proprietary-%{version}
cp -r %{builddir}/%{name}-%{version}-x86_64/kernel %{buildroot}/usr/src/nvidia-driver-proprietary-%{version}/
cat <<EOF > %{buildroot}/usr/src/nvidia-driver-proprietary-%{version}/dkms.conf
PACKAGE_NAME="nvidia-driver-proprietary"
PACKAGE_VERSION="%{version}"
MAKE[0]="make KERNELDIR=\$kernel_source_dir"
CLEAN="make clean KERNELDIR=\$kernel_source_dir"
BUILT_MODULE_NAME[0]="nvidia"
BUILT_MODULE_LOCATION[0]="kernel"
DEST_MODULE_LOCATION[0]="/updates"
AUTOINSTALL="yes"
EOF

# Install DKMS for open-source kernel
mkdir -p %{buildroot}/usr/src/nvidia-driver-open-%{version}
cp -r %{builddir}/%{name}-%{version}-x86_64/kernel-open %{buildroot}/usr/src/nvidia-driver-open-%{version}/
cat <<EOF > %{buildroot}/usr/src/nvidia-driver-open-%{version}/dkms.conf
PACKAGE_NAME="nvidia-driver-open"
PACKAGE_VERSION="%{version}"
MAKE[0]="make -C \$kernel_source_dir SUBDIRS=\$dkms_tree/nvidia-driver-open/%{version}/kernel-open"
CLEAN="make -C \$kernel_source_dir SUBDIRS=\$dkms_tree/nvidia-driver-open/%{version}/kernel-open clean"
BUILT_MODULE_NAME[0]="nvidia_open"  # Replace with the actual open-source module name if different
BUILT_MODULE_LOCATION[0]="kernel-open"
DEST_MODULE_LOCATION[0]="/updates"
AUTOINSTALL="yes"
EOF

%post proprietary-dkms
dkms add -m nvidia-driver-proprietary -v %{version}
dkms build -m nvidia-driver-proprietary -v %{version}
dkms install -m nvidia-driver-proprietary -v %{version}
# Enable OpenRC service for proprietary driver
if [ -f /etc/init.d/nvidia-persistenced ]; then
    rc-update add nvidia-persistenced default
fi

%preun proprietary-dkms
if [ $1 = 0 ]; then
    dkms remove -f nvidia-driver-proprietary -v %{version} --all
fi
# Disable OpenRC service for proprietary driver
if [ -f /etc/init.d/nvidia-persistenced ]; then
    rc-update del nvidia-persistenced default
fi

%post open-dkms
dkms add -m nvidia-driver-open -v %{version}
dkms build -m nvidia-driver-open -v %{version}
dkms install -m nvidia-driver-open -v %{version}
# Enable OpenRC service for open-source driver
if [ -f /etc/init.d/nvidia-persistenced ]; then
    rc-update add nvidia-persistenced default
fi

%preun open-dkms
if [ $1 = 0 ]; then
    dkms remove -f nvidia-driver-open -v %{version} --all
fi
# Disable OpenRC service for open-source driver
if [ -f /etc/init.d/nvidia-persistenced ]; then
    rc-update del nvidia-persistenced default
fi

%files proprietary
%license license
%doc changelog readme %{_docdir}/%{name}/*
%{_bindir}/*
%{_sbindir}/nvidia-persistenced
%{_datadir}/nvidia/nvoptix.bin
%{_datadir}/nvidia/sandboxutils-filelist.json
%{_mandir}/man1/*
/etc/modules-load.d/nvidia.conf # If truly needed here
# Udev rules are managed by DKMS, so we don't package them here

%files open
%license license
%doc changelog readme %{_docdir}/%{name}/*
%{_bindir}/*
# Include open-specific sbindir files
%{_mandir}/man1/*
/etc/modules-load.d/nvidia.conf # If truly needed here
# Udev rules are managed by DKMS, so we don't package them here

%files libs
%{_libdir}/libcuda.so
%{_libdir}/libcuda.so.1
%{_libdir}/libcuda.so.%{version}
%{_libdir}/libnvcuvid.so
%{_libdir}/libnvcuvid.so.1
%{_libdir}/libnvcuvid.so.%{version}
%{_libdir}/libnvidia-encode.so
%{_libdir}/libnvidia-encode.so.1
%{_libdir}/libnvidia-encode.so.%{version}
%{_libdir}/libnvidia-allocator.so.1
%{_libdir}/libnvidia-allocator.so.%{version}
# Add other compute-related libraries as needed:
# %{_libdir}/libnvidia-opencl.so.1
# %{_libdir}/libnvidia-opencl.so.%{version}
# %{_libdir}/libnvidia-nvvm.so.4
# %{_libdir}/libnvidia-nvvm.so.%{version}

%files proprietary-dkms
/usr/src/nvidia-driver-proprietary-%{version}/dkms.conf
/usr/src/nvidia-driver-proprietary-%{version}/kernel

%files open-dkms
/usr/src/nvidia-driver-open-%{version}/dkms.conf
/usr/src/nvidia-driver-open-%{version}/kernel-open

%files -n libnvidia-ml
%{_libdir}/libnvidia-ml.so.1
%{_libdir}/libnvidia-ml.so.%{version}

%files -n libnvidia-cfg
%{_libdir}/libnvidia-cfg.so.1
%{_libdir}/libnvidia-cfg.so.%{version}

%changelog
* Mon Mar 17 2025 Dan Carpenter <danc403@gmail.com> - 570.124.04-1
- Builds separate RPM packages for proprietary and open-source kernel modules.
- Generates DKMS configuration files within the spec.
- Introduced a common `libs` package for shared libraries.
- Removed manual handling of udev rules as DKMS will manage them.
- Added support for enabling/disabling the nvidia-persistenced service on OpenRC systems.
- Adapted `%install` section to match the directory structure of the provided tarball.
