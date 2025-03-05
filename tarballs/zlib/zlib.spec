Name: zlib
Version: 1.3.1
Release: 1%{?dist}
Summary: A massively spiffy yet delicately unobtrusive compression library
License: Zlib
URL: https://www.zlib.net/
Source0: %{name}-%{version}.tar.gz

%description
zlib is a general-purpose lossless data-compression library.

%prep
%setup -q

%build
./configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license zlib.h
%doc README.md FAQ
/usr/lib/libz.so.*
/usr/share/man/man3/zlib.3*

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%changelog
* %{__date} Dan Carpenter <DanC403@gmail.com> - %{version}-1
- Initial RPM build of zlib.
