Name:           x264
Version:        0.164.r3194
Release:        1%{?dist}
Summary:        x264 video encoder
License:        GPLv2+
URL:            https://www.videolan.org/developers/x264.html
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  yasm

%description
x264 is a free software library and application for encoding video streams into the H.264/MPEG-4 AVC compression format.

%package devel
Summary:        Development files for x264
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains the development files for x264.

%prep
%autosetup -n %{name}-%{version}

%build
./configure --prefix=%{_prefix} --libdir=%{_libdir} --includedir=%{_includedir}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
%{_bindir}/x264
%{_libdir}/libx264.so.*
%{_mandir}/man1/x264.1*

%files devel
%{_includedir}/x264.h
%{_libdir}/libx264.a
%{_libdir}/pkgconfig/x264.pc

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial package.
