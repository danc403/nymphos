Name:       iproute2
Version:    6.1.0
Release:    1%{?dist}
Summary:    Linux routing utilities

License:    GPL-2.0-or-later
URL:        https://www.kernel.org/pub/linux/utils/net/iproute2/
Source0:    %{name}-%{version}.tar.xz

BuildRequires:  libmnl-devel
BuildRequires:  libxtables-devel

%description
The iproute2 package contains utilities for controlling TCP/IP networking
and traffic control in Linux.

%prep
%setup -q -n %{name}-%{version}

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_sbindir}/*
%{_mandir}/man8/*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> %{version}-%{release}
- Initial build.
