Name:       fontconfig
Version:    2.15.0
Release:    1%{?dist}
Summary:    A library for configuring and customizing font access

License:    MIT
URL:        https://www.freedesktop.org/wiki/Software/fontconfig/
Source0:    fontconfig-%{version}.tar.xz

BuildRequires:  libxml2-devel

%package devel
Summary:    Development files for fontconfig
Requires:   fontconfig = %{version}-%{release}

%description
Fontconfig is a library designed to provide system-wide font configuration,
customization and application access.

%description devel
This package contains the development files for fontconfig.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_libdir}/libfontconfig.so.*
%{_bindir}/fc-*
%{_mandir}/man1/fc-*.1*
/etc/fonts/

%files devel
%{_includedir}/fontconfig/
%{_libdir}/libfontconfig.so
%{_libdir}/libfontconfig.a
%{_libdir}/pkgconfig/fontconfig.pc

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
