content: Name:           polkit-devel
Version:        1.23
Release:        1%{?dist}
Summary:        Development files for polkit

License:        BSD
URL:            https://www.freedesktop.org/software/polkit/

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  glib2-devel

Requires:       polkit = %{version}-%{release}

%description
Development files for polkit.

%prep
%autosetup

%build
./autogen.sh
%configure --disable-static --with-console-helper-group=wheel
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_includedir}/polkit-1
%{_libdir}/libpolkit*.so
%{_libdir}/pkgconfig/polkit-1.pc

%changelog
* %{_isodate} Dan Carpenter <DanC403@gmail.com> - 1.23-1
- Initial build

filename: polkit-devel.spec
