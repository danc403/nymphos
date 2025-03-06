Name:       pciutils
Version:    3.9.0
Release:    1%{?dist}
Summary:    PCI utilities

License:    GPLv2+
URL:        https://mj.ucw.cz/sw/pciutils/
Source0:    %{name}-%{version}.tar.xz

%description
The pciutils package contains utilities for inspecting and configuring
PCI devices.

%prep
%setup -q -n %{name}-%{version}

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_sbindir}/lspci
%{_sbindir}/setpci
%{_sbindir}/update-pciids
%{_mandir}/man8/lspci.8*
%{_mandir}/man8/setpci.8*
%{_mandir}/man8/update-pciids.8*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> %{version}-%{release}
- Initial build.
