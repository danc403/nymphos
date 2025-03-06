Name:           mod_fcgid
Version:        2.3.9
Release:        1%{?dist}
Summary:        FastCGI interface module for Apache HTTP Server

License:        Apache-2.0
URL:            http://httpd.apache.org/mod_fcgid/
Source0:        mod_fcgid-%{version}.tar.gz

BuildRequires:  httpd-devel
BuildRequires:  apr-devel
BuildRequires:  apr-util-devel
BuildRequires:  gcc
BuildRequires:  make

%description
mod_fcgid is an Apache HTTP Server module that provides a FastCGI
interface, allowing Apache to run external applications more efficiently.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure.apxs
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_libdir}/httpd/modules/mod_fcgid.so
%{_mandir}/man8/mod_fcgid.8*
%doc CHANGES README

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - 2.3.9-1
- Initial build for custom distribution.
