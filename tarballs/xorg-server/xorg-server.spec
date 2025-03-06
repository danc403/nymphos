Name:       xorg-server
Version:    21.1.16
Release:    1%{?dist}
Summary:    Xorg X server

License:    MIT
URL:        https://www.x.org/wiki/Xorg/
Source0:    xorg-server-%{version}.tar.xz

BuildRequires:  libxkbfile-devel
BuildRequires:  libxfont2-devel
BuildRequires:  libxshmfence-devel
BuildRequires:  libxcb-devel
BuildRequires:  libxcb-dri2-devel
BuildRequires:  libxcb-dri3-devel
BuildRequires:  libxcb-glx-devel
BuildRequires:  libxcb-present-devel
BuildRequires:  libxcb-randr-devel
BuildRequires:  libxcb-shape-devel
BuildRequires:  libxcb-sync-devel
BuildRequires:  libxcb-xfixes-devel
BuildRequires:  libxcb-xkb-devel
BuildRequires:  libxcb-xv-devel
BuildRequires:  libxcb-xinput-devel
BuildRequires:  libxcvt-devel
BuildRequires:  libudev-devel
BuildRequires:  pixman-devel
BuildRequires:  libepoxy-devel
BuildRequires:  libpciaccess-devel
BuildRequires:  libunwind-devel
BuildRequires:  libtirpc-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libEGL-devel

%description
The Xorg X server is the core of the X Window System. It provides the
basic display services to graphical applications.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --enable-dri3 --enable-glamor --enable-xkb
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/Xorg
%{_libdir}/xorg/
%{_mandir}/man1/Xorg.1*

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
