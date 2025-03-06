Name:       gtk4
Version:    4.9.4
Release:    1%{?dist}
Summary:    GTK graphical user interface library

License:    LGPLv2.1+
URL:        https://www.gtk.org/
Source0:    gtk-%{version}.tar.xz

BuildRequires:  glib2-devel
BuildRequires:  cairo-devel
BuildRequires:  pango-devel
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  libepoxy-devel
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols
BuildRequires:  libxrandr-devel
BuildRequires:  libxinerama-devel
BuildRequires:  libxcursor-devel
BuildRequires:  libxcomposite-devel
BuildRequires:  libxdamage-devel
BuildRequires:  libxfixes-devel
BuildRequires:  libxi-devel
BuildRequires:  libxrender-devel
BuildRequires:  libxext-devel
BuildRequires:  libinput-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  at-spi2-core-devel
BuildRequires:  at-spi2-atk-devel
BuildRequires:  libcolord-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libtiff-devel
BuildRequires:  libpng-devel
BuildRequires:  libwebp-devel
BuildRequires:  libwmf-devel
BuildRequires:  fontconfig-devel

%package devel
Summary:    Development files for GTK4
Requires:   gtk4 = %{version}-%{release}

%description
GTK is a multi-platform toolkit for creating graphical user interfaces.

%description devel
This package contains the development files for GTK4.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --enable-x11-backend --enable-wayland-backend
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_libdir}/libgtk-4.so.*
%{_libdir}/libgdk-4.so.*
%{_libdir}/libgsk-4.so.*
%{_bindir}/gtk4-demo
%{_bindir}/gtk4-builder-tool
%{_datadir}/gtk-4.0/
%{_mandir}/man1/gtk4-demo.1*
%{_mandir}/man1/gtk4-builder-tool.1*

%files devel
%{_includedir}/gtk-4.0/
%{_libdir}/libgtk-4.so
%{_libdir}/libgdk-4.so
%{_libdir}/libgsk-4.so
%{_libdir}/libgtk-4.a
%{_libdir}/libgdk-4.a
%{_libdir}/libgsk-4.a
%{_libdir}/pkgconfig/gtk4.pc
%{_libdir}/pkgconfig/gdk-4.pc
%{_libdir}/pkgconfig/gsk-4.pc

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
