Name:           libogg
Version:        1.3.5
Release:        1%{?dist}
Summary:        Ogg bitstream library
License:        BSD
URL:            https://www.xiph.org/ogg/
Source0:        %{name}-%{version}.tar.xz

%description
Ogg is a bitstream format for multiplexing a number of independent digital streams for audio, video, text (such as subtitles), and metadata.

%package devel
Summary:        Development files for libogg
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains the development files for libogg.

%prep
%autosetup -n %{name}-%{version}

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
%{_libdir}/libogg.so.*
%{_bindir}/oggz-validate
%{_mandir}/man1/oggz-validate.1*

%files devel
%{_includedir}/ogg/
%{_libdir}/libogg.a
%{_libdir}/pkgconfig/ogg.pc

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial package.
