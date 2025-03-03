content: Name:           bzip2-devel
Version:        1.0.8
Release:        1%{?dist}
Summary:        Development files for bzip2

License:        MIT
URL:            http://www.bzip.org/

Source0:        %{name:bzip2}-%{version}.tar.gz

Requires:       bzip2 = %{version}-%{release}

%description
This package contains the header files and libraries needed to develop
applications that use bzip2.

%prep
%setup -q -n %{name:bzip2}-%{version}

%build
make -f Makefile-libbz2_so
make

%install
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_libdir}
install -m 644 bzlib.h %{buildroot}%{_includedir}/bzlib.h
install -m 644 bzlib.h %{buildroot}%{_includedir}/bzlib.h
install -m 644 libbz2.a %{buildroot}%{_libdir}/libbz2.a


%files
%{_includedir}/bzlib.h
%{_libdir}/libbz2.a

%changelog
* %{date} Dan Carpenter DanC403@gmail.com - 1.0.8-1
- Initial package build.

