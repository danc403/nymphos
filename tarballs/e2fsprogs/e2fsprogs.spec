Name:       e2fsprogs
Version:    1.47.2
Release:    1%{?dist}
Summary:    Ext2/ext3/ext4 file system utilities

License:    GPLv2+
URL:        https://e2fsprogs.sourceforge.net/
Source0:    %{name}-%{version}.tar.gz

BuildRequires:  util-linux-devel
BuildRequires:  zlib-devel
BuildRequires:  e2fsprogs-libs-devel

%description
The e2fsprogs package contains utilities for creating, checking,
modifying, and correcting ext2, ext3, and ext4 file systems.

%prep
%setup -q -n %{name}-%{version}

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_sbindir}/*
%{_bindir}/*
%{_libdir}/libext2fs.so.*
%{_libdir}/libblkid.so.* # from util-linux
%{_libdir}/libcom_err.so.*
%{_libdir}/libss.so.*
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/*

%package libs
Summary:    Ext2/ext3/ext4 shared libraries
Requires:   %{name} = %{version}-%{release}

%description libs
This package contains the shared libraries for e2fsprogs.

%files libs
%{_libdir}/libext2fs.so.*
%{_libdir}/libblkid.so.*
%{_libdir}/libcom_err.so.*
%{_libdir}/libss.so.*

%package devel
Summary:    Development files for e2fsprogs
Requires:   %{name}-libs = %{version}-%{release}

%description devel
This package contains the development files for e2fsprogs.

%files devel
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> %{version}-%{release}
- Initial build.
