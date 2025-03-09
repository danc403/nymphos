Name:           lame
Version:        3.100
Release:        1%{?dist}
Summary:        LAME Ain't an MP3 Encoder
License:        LGPLv2+
URL:            https://lame.sourceforge.io/
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  ncurses-devel

%description
LAME is an MP3 encoder licensed under the LGPL. It is considered by many to be the best MP3 encoder at mid-high bitrates and VBR, generally better than all other encoders except for those too slow for practical use.

%package devel
Summary:        Development files for LAME
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains the development files for LAME.

%prep
%autosetup -n lame-%{version}

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license LICENSE
%{_bindir}/lame
%{_libdir}/libmp3lame.so.*
%{_mandir}/man1/lame.1*

%files devel
%{_includedir}/lame/
%{_libdir}/libmp3lame.a
%{_libdir}/pkgconfig/lame.pc

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial package.
