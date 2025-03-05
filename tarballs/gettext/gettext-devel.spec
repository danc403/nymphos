Name: gettext-devel
Version: 0.21.1
Release: 1%{?dist}
Summary: Development files for GNU gettext
License: GPLv3+
URL: https://www.gnu.org/software/gettext/
Source0: gettext-0.21.1.tar.xz
BuildRequires:
  - autoconf
  - automake
  - libtool
  - pkgconfig
  - glibc-devel
Requires:
  - gettext = %{version}-%{release}

%description
Development files for GNU gettext.

%prep
%setup -q

%build
./configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
/usr/include/libintl.h
/usr/lib/libintl.so
/usr/lib/pkgconfig/gettext-runtime.pc
/usr/lib/pkgconfig/libintl.pc

%changelog
* %{__date} Dan Carpenter <DanC403@gmail.com> - %{version}-1
- Initial RPM build of gettext-devel.
