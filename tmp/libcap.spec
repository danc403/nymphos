%global dist .el8

Name:           libcap
Version:        2.73
Release:        1%{?dist}
Summary:        POSIX 1003.1e capabilities library
License:        BSD
URL:            https://sites.google.com/site/fullycapabilities/
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
Requires:       glibc
BuildRoot:      %{_tmppdir}/%{name}-%{version}-build
BuildArch:      x86_64

%description
This is a library for getting and setting POSIX 1003.1e capabilities.

%prep
%setup -q

%build
autoreconf -fvi
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README
%{_libdir}/libcap.so.*
%{_bindir}/capsh
%{_bindir}/getcap
%{_bindir}/setcap
%{_mandir}/man1/capsh.1*
%{_mandir}/man1/getcap.1*
%{_mandir}/man1/setcap.1*
%{_mandir}/man3/cap_*.3*
%{_mandir}/man5/cap.5*
%{_mandir}/man8/filecap.8*
%{_mandir}/man8/getpcaps.8*
%license LICENSE

%changelog
* Tue Oct 24 2023 Dan Carpenter <DanC403@gmail.com> - 2.73-1
- Initial package build
