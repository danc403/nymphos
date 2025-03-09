Name:           libpng
Version:        1.6.47
Release:        1%{?dist}
Summary:        PNG library
License:        libpng
URL:            http://www.libpng.org/pub/png/libpng.html
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  zlib-devel

%description
libpng is the official Portable Network Graphics (PNG) reference library. It supports almost all PNG features, is extensible, and has been extensively tested for robustness.

%package devel
Summary:        Development files for libpng
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains the development files for libpng.

%prep
%autosetup -n %{name}-%{version}

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license LICENSE
%{_libdir}/libpng16.so.*
%{_bindir}/libpng16-config
%{_mandir}/man1/libpng16-config.1*

%files devel
%{_includedir}/libpng16/
%{_libdir}/libpng16.a
%{_libdir}/pkgconfig/libpng16.pc

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial package.
