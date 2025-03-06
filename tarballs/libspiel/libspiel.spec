Name:       libspiel
Version:    SPIEL_1_0_3
Release:    1%{?dist}
Summary:    A library for speech synthesis

License:    LGPLv2.1+
URL:        https://github.com/brailletec/libspiel
Source0:    libspiel-%{version}.tar.gz

%package devel
Summary:    Development files for libspiel
Requires:   libspiel = %{version}-%{release}

%description
Libspiel is a library for speech synthesis. It provides a simple API
for generating speech from text.

%description devel
This package contains the development files for libspiel.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_libdir}/libspiel.so.*

%files devel
%{_includedir}/spiel/
%{_libdir}/libspiel.so
%{_libdir}/libspiel.a
%{_libdir}/pkgconfig/spiel.pc

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
