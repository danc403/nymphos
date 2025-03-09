Name:           x265
Version:        4.1
Release:        1%{?dist}
Summary:        HEVC (H.265) video encoder
License:        GPLv2+
URL:            https://bitbucket.org/multicoreware/x265/
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake

%description
x265 is a free software library and application for encoding video streams into the High Efficiency Video Coding (HEVC/H.265) compression format.

%package devel
Summary:        Development files for x265
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains the development files for x265.

%prep
%autosetup -n %{name}-%{version}

%build
%cmake -G "Unix Makefiles"
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
%{_bindir}/x265
%{_libdir}/libx265.so.*

%files devel
%{_includedir}/x265/
%{_libdir}/libx265.a
%{_libdir}/pkgconfig/x265.pc

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial package.
