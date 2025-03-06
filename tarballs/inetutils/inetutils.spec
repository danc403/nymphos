Name:       inetutils
Version:    2.3
Release:    1%{?dist}
Summary:    A collection of basic network utilities

License:    GPLv3+
URL:        https://www.gnu.org/software/inetutils/
Source0:    %{name}-%{version}.tar.xz

%description
The inetutils package contains a collection of basic network utilities,
including ftp, telnet, ping, and hostname.

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
%{_mandir}/man8/*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> %{version}-%{release}
- Initial build.
