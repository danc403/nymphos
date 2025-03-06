Name:       dhcpcd
Version:    10.2.0
Release:    1%{?dist}
Summary:    A DHCP client

License:    BSD-2-Clause
URL:        https://roy.marples.name/projects/dhcpcd
Source0:    dhcpcd-%{version}.tar.gz

BuildRequires:  pkg-config

%description
dhcpcd is an implementation of the DHCP client specified in RFC 2131.
dhcpcd is a daemon that is used to automatically configure network
interfaces.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --sysconfdir=/etc
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_sbindir}/dhcpcd
%{_mandir}/man8/dhcpcd.8*
/etc/dhcpcd.conf

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
