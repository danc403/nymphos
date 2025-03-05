Name: libffi
Version: 3.4.4
Release: 1%{?dist}
Summary: Foreign Function Interface library
License: MIT
URL: https://sourceware.org/libffi/
Source0: %{name}-%{version}.tar.gz

%description
The libffi library provides a portable, high level programming interface
to various calling conventions. This allows a programmer to call any
function specified by a call description.

%prep
%setup -q

%build
./configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license LICENSE
%doc README.md
/usr/lib/libffi.so.*
/usr/share/man/man3/ffi.3*

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%changelog
* %{__date} Dan Carpenter <DanC403@gmail.com> - %{version}-1
- Initial RPM build of libffi.
