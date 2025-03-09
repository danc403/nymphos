Name:           libvpx
Version:        1.15.0
Release:        1%{?dist}
Summary:        VP8/VP9 video codec library
License:        BSD
URL:            https://www.webmproject.org/
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  yasm

%description
libvpx is the official VP8/VP9 codec SDK. It provides an API to encode and decode VP8 and VP9 video streams.

%package devel
Summary:        Development files for libvpx
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains the development files for libvpx.

%prep
%autosetup -n vpx-%{version}

%build
./configure --prefix=%{_prefix} --libdir=%{_libdir} --includedir=%{_includedir}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license LICENSE
%{_libdir}/libvpx.so.*
%{_bindir}/vpxenc
%{_bindir}/vpxdec
%{_mandir}/man1/vpxenc.1*
%{_mandir}/man1/vpxdec.1*

%files devel
%{_includedir}/vpx/
%{_libdir}/libvpx.a
%{_libdir}/pkgconfig/vpx.pc

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial package.
