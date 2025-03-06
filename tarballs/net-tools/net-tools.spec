Name:       net-tools
Version:    2.10
Release:    1%{?dist}
Summary:    Basic networking tools

License:    GPL-2.0-or-later
URL:        https://sourceforge.net/projects/net-tools/
Source0:    %{name}-%{version}.tar.xz

%description
The net-tools package contains basic networking tools such as ifconfig,
route, netstat, and arp.

%prep
%setup -q -n %{name}-%{version}

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_sbindir}/*
%{_mandir}/man8/*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> %{version}-%{release}
- Initial build.
