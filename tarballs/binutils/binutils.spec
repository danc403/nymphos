Name:       binutils
Version:    2.40
Release:    1%{?dist}
Summary:    A set of binary utilities

License:    GPLv3+
URL:        https://www.gnu.org/software/binutils/
Source0:    %{name}-%{version}.tar.xz

BuildRequires:  zlib-devel

%description
The GNU Binutils package contains a collection of utilities for manipulating
binary files. These include ld, the GNU linker, and as, the GNU assembler.

%prep
%setup -q -n %{name}-%{version}

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/*
%{_libdir}/*
%{_includedir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_mandir}/man5/*
%{_mandir}/man7/*

%package devel
Summary:    Development files for binutils
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains the development files for binutils.

%files devel
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.la

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> %{version}-%{release}
- Initial build.
