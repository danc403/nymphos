Name: linux-firmware
Version: 20250211 # Get the latest version from kernel.org or your distribution
Release: 1%{?dist}
Summary: Firmware files for Linux
License: GPLv2+
URL: https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git
Source0: %{name}-%{version}.tar.gz # Create a tarball from the git repo.
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
This package contains firmware files used by various hardware devices in Linux.

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/lib/firmware
cp -r * %{buildroot}/lib/firmware/

%clean
rm -rf %{buildroot}

%files
/lib/firmware/

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial package build.
