Name:       libseccomp
Version:    2.6.0
Release:    1%{?dist}
Summary:    Library for working with seccomp-bpf

License:    LGPLv2.1+
URL:        https://github.com/seccomp/libseccomp
Source0:    libseccomp-%{version}.tar.gz

%package devel
Summary:    Development files for libseccomp
Requires:   libseccomp = %{version}-%{release}

%description
Libseccomp is a library that provides an easy-to-use interface to the
seccomp-bpf system call filtering mechanism in the Linux kernel.

%description devel
This package contains the development files for libseccomp.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_libdir}/libseccomp.so.*

%files devel
%{_includedir}/seccomp.h
%{_libdir}/libseccomp.so
%{_libdir}/libseccomp.a
%{_libdir}/pkgconfig/libseccomp.pc

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
