Name:       usbutils
Version:    017
Release:    1%{?dist}
Summary:    USB utilities

License:    GPLv2+
URL:        https://sourceforge.net/projects/usbutils/
Source0:    %{name}-%{version}.tar.xz

%description
The usbutils package contains utilities for inspecting USB devices.

%prep
%setup -q -n %{name}-%{version}

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_sbindir}/lsusb
%{_sbindir}/usb-devices
%{_mandir}/man8/lsusb.8*
%{_mandir}/man8/usb-devices.8*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> %{version}-%{release}
- Initial build.
