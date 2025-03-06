Name:       sysstat
Version:    12.6.1
Release:    1%{?dist}
Summary:    System performance tools

License:    GPLv2+
URL:        https://github.com/sysstat/sysstat
Source0:    %{name}-%{version}.tar.gz

%description
The sysstat package contains various system performance monitoring tools.

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
%{_mandir}/man8/*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> %{version}-%{release}
- Initial build.
