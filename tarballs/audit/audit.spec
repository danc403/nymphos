Name:       audit
Version:    3.0.9
Release:    1%{?dist}
Summary:    User space tools to manage the Linux audit system

License:    GPLv2+
URL:        https://people.redhat.com/sgrubb/audit/
Source0:    audit-%{version}.tar.gz

BuildRequires:  libcap-ng-devel
BuildRequires:  libnl3-devel

%description
The audit package contains the user space tools for managing and
searching the audit subsystem of the Linux kernel.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_sbindir}/audit*
%{_bindir}/ausearch
%{_bindir}/autrace
%{_mandir}/man8/audit*.8*
%{_mandir}/man1/ausearch.1*
%{_mandir}/man1/autrace.1*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
