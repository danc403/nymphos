Name:           apr
Version:        1.6.5
Release:        1%{?dist}
Summary:        Apache Portable Runtime Library

License:        Apache-2.0
URL:            https://apr.apache.org/
Source0:        apr-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%description
The Apache Portable Runtime (APR) library provides a portable
interface to operating system functionality.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --disable-shared
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_libdir}/libapr-1.a
%{_includedir}/apr-1/
%{_bindir}/apu-config
%{_mandir}/man1/apu-config.1*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - 1.6.5-1
- Initial build for custom distribution.
