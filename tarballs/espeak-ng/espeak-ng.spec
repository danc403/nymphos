
Name:           espeak-ng
Version:        1.52.0
Release:        1%{?dist}
Summary:        Compact open source software speech synthesizer

License:        GPLv3+
URL:            http://espeak.sourceforge.net/
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  alsa-lib-devel

%description
eSpeak NG is an open source speech synthesizer that supports many languages.
It is compact and can be used as a command line tool or as a library.

%package devel
Summary:        Development files for espeak-ng
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains the development files for espeak-ng.

%prep
%autosetup -n %{name}-%{version}

%build
autoreconf -fiv
%configure --disable-static --enable-shared --with-pic --with-alsa
%make_build

%install
%make_install

%check
%make_check

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%license COPYING
%{_bindir}/espeak-ng
%{_libdir}/libespeak-ng.so.*
%{_datadir}/espeak-ng/

%files devel
%{_includedir}/espeak-ng/
%{_libdir}/libespeak-ng.a
%{_libdir}/libespeak-ng.so
%{_libdir}/pkgconfig/espeak-ng.pc

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-1
- Initial package.
