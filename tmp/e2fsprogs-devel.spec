name: e2fsprogs-devel
version: 1.47.2
release: 1%{?dist}
summary: Development files for e2fsprogs
License: GPLv2+
URL: https://e2fsprogs.sourceforge.net/
Source0: %{name}-%{version}.tar.gz
Requires: libuuid-devel
BuildRequires: libuuid-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
%description: This package contains the header files and libraries needed to develop programs that use the e2fsprogs library.
%prep: %setup -q
%build: %configure
make %{?_smp_mflags}: None
%install: make install DESTDIR=%{buildroot}
%files:
  - /usr/include/*
  - /usr/lib64/lib*.so
  - /usr/lib64/pkgconfig/*
%changelog:
  - * Tue Oct 24 2023 Dan Carpenter DanC403@gmail.com - 1.47.2-1
  - - Initial build
