Name: python3-devel
Version: 3.13.2
Release: 1%{?dist}
Summary: Header files and static libraries for Python 3
License: PSF-2.0
URL: https://www.python.org/
Source0: python-3.13.2.tar.xz
BuildRequires:
  - autoconf
  - automake
  - libtool
  - pkgconfig
  - zlib-devel
  - bzip2-devel
  - xz-devel
  - openssl-devel
  - libffi-devel
  - readline-devel
  - ncurses-devel
  - libxcrypt-devel
Requires:
  - python3 = %{version}-%{release}

%description
Header files and static libraries for Python 3 development.

%prep
%setup -q

%build
./configure --enable-optimizations --enable-shared --with-system-ffi --with-computed-gotos
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license LICENSE
/usr/include/python3.%{version}/
/usr/lib/libpython3.%{version}.so
/usr/lib/libpython3.%{version}.a
/usr/lib/pkgconfig/python3.pc
/usr/lib/pkgconfig/python3-embed.pc

%changelog
* %{__date} Dan Carpenter <DanC403@gmail.com> - %{version}-1
- Initial RPM build of python3-devel.
