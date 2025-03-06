Name:           apr-util
Version:        1.6.3
Release:        1%{?dist}
Summary:        Apache Portable Runtime Utility Library

License:        Apache-2.0
URL:            https://apr.apache.org/
Source0:        apr-util-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  apr-devel >= 1.6.5

%description
The Apache Portable Runtime Utility (APR-util) library provides
higher-level functions built on top of APR.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --with-apr=%{_prefix} --disable-shared
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_libdir}/libaprutil-1.a
%{_includedir}/apr-1/apr_*.h
%{_bindir}/apu-1-config
%{_mandir}/man1/apu-1-config.1*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - 1.6.3-1
- Initial build for custom distribution.
