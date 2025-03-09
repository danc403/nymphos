Name:           libvorbis
Version:        1.3.7
Release:        1%{?dist}
Summary:        Vorbis audio codec library
License:        BSD
URL:            https://www.xiph.org/vorbis/
Source0:        %{name}-%{version}.tar.xz

BuildRequires:  libogg-devel

%description
libvorbis is the reference implementation of the Vorbis audio codec, a free and open-source lossy audio compression format.

%package devel
Summary:        Development files for libvorbis
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains the development files for libvorbis.

%prep
%autosetup -n %{name}-%{version}

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
%{_libdir}/libvorbis.so.*
%{_libdir}/libvorbisenc.so.*
%{_libdir}/libvorbisfile.so.*

%files devel
%{_includedir}/vorbis/
%{_libdir}/libvorbis.a
%{_libdir}/libvorbisenc.a
%{_libdir}/libvorbisfile.a
%{_libdir}/pkgconfig/vorbis.pc
%{_libdir}/pkgconfig/vorbisenc.pc
%{_libdir}/pkgconfig/vorbisfile.pc

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial package.
