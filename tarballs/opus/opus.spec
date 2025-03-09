Name:           opus
Version:        1.5.1
Release:        1%{?dist}
Summary:        Opus audio codec
License:        BSD
URL:            https://www.opus-codec.org/
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  libogg-devel

%description
Opus is a totally open, royalty-free, highly versatile audio codec. Opus is unmatched for interactive speech and music transmission over the Internet, but is also intended for storage and streaming applications.

%package devel
Summary:        Development files for Opus
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains the development files for Opus.

%prep
%autosetup -n %{name}-%{version}

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
%{_libdir}/libopus.so.*
%{_bindir}/opusenc
%{_bindir}/opusdec
%{_mandir}/man1/opusenc.1*
%{_mandir}/man1/opusdec.1*

%files devel
%{_includedir}/opus/
%{_libdir}/libopus.a
%{_libdir}/pkgconfig/opus.pc

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial package.
