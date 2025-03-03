spec: Name:           util-linux-devel
Version:        2.39
Release:        1%{?dist}
Summary:        Development files for util-linux

License:        GPLv2+
URL:            https://www.kernel.org/pub/linux/utils/util-linux/

Source0:        %{name}.tar.xz

Requires:       util-linux = %{version}-%{release}

%description
Development files (header files, static libraries, etc.)
for the util-linux package.

%prep
# Dummy prep section

%build
# Dummy build section

%install
# Dummy install section

%files
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*

%changelog
* %{date} Dan Carpenter DanC403@gmail.com - 2.39-1
- Initial package build.

name: util-linux-devel
