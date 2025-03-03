# -*- mode: rpm-spec -*-

Name:       python3.13-devel
Version:    3.13.2
Release:    1%{?dist}
Summary:    Header files, libraries and development tools for developing Python 3.13 modules
License:    Python-2.0
URL:        https://www.python.org/
Source0:    Python-%{version}.tar.xz
Requires:     python3.13 = %{version} # Match the main python package name
BuildRequires: pkg-config
Prefix:     /usr
BuildRoot:  %{_tmppdir}/%{name}-%{version}-%{release}-root

%description
The python3.13-devel package contains the header files and libraries you need to develop Python 3.13 modules that extend the Python programming language.

%build
%configure --enable-shared
make

%install
make install DESTDIR=%{buildroot}

%files
/usr/include/python3.13/*
/usr/lib64/libpython3.so # This could be a symlink, verify its actual path
/usr/lib64/pkgconfig/python3.pc
/usr/lib64/pkgconfig/python3-embed.pc
/usr/lib64/python3.13/config-3.13-linux-x86_64-gnu/Makefile

%changelog
* %{DATE} Dan Carpenter DanC403@gmail.com - 3.13.2-1
- Initial build.
- Adjusted requires to match the main python package name.
- Adjusted package name to be version specific.
