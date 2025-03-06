Name:       procps-ng
Version:    4.0.5
Release:    1%{?dist}
Summary:    Utilities for monitoring processes

License:    GPLv2+
URL:        https://gitlab.com/procps-ng/procps
Source0:    %{name}-%{version}.tar.gz

%description
The procps-ng package contains utilities for monitoring processes,
including ps, top, kill, and uptime.

%prep
%setup -q -n %{name}-%{version}

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> %{version}-%{release}
- Initial build.
