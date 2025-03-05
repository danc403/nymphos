Name: dracut-devel
Version: 059
Release: 1%{?dist}
Summary: Development files for dracut
License: GPLv2+
URL: https://github.com/dracutdevs/dracut
Source0: %{name}.tar.gz
BuildRequires:
  - make
  - automake
  - autoconf
  - gettext
  - pkg-config
  - util-linux
  - bash
  - coreutils
  - eudev
Requires:
  - dracut = %{version}-%{release}

%description
Development files for dracut.

%prep
%autosetup

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
%doc README
/usr/include/dracut/
/usr/lib/pkgconfig/dracut.pc

%changelog
* Sat Mar 1 2025 Dan Carpenter <DanC403@gmail.com> - 059-1
- Initial RPM build of dracut-devel.
