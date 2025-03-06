Name:       gtk3
Version:    3.24.48
Release:    1%{?dist}
Summary:    The GTK+ toolkit version 3

License:    LGPLv2+
URL:        https://www.gtk.org/
Source0:    gtk+-%{version}.tar.xz

BuildRequires:  glib2-devel
BuildRequires:  pango-devel
BuildRequires:  cairo-devel
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  atk-devel
BuildRequires:  libx11-devel
BuildRequires:  libxext-devel
BuildRequires:  libxrandr-devel
BuildRequires:  libxinerama-devel
BuildRequires:  libxi-devel
BuildRequires:  libxcursor-devel
BuildRequires:  libxdamage-devel
BuildRequires:  libepoxy-devel
BuildRequires:  wayland-devel # If you have wayland support
BuildRequires:  libinput-devel # If you have libinput support

%description
GTK+ is a highly usable, feature rich toolkit for creating graphical
user interfaces which offers cross platform compatibility.

%package devel
Summary:    Development files for GTK+ 3
Requires:   gtk3 = %{version}-%{release}

%prep
%setup -q -n gtk+-%{version}

%build
./configure --prefix=%{_prefix} --disable-introspection --disable-wayland --disable-libinput #Adjust options as needed.
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_libdir}/libgtk-3.so.*
%{_libdir}/libgdk-3.so.*
%{_libdir}/libgailutil-3.so.*
%{_libdir}/libgail-3.so.*
%{_libdir}/gtk-3.0/
%{_datadir}/themes/
%{_datadir}/icons/
%{_datadir}/gtk-3.0/
%{_datadir}/applications/gtk3-demo.desktop
%{_bindir}/gtk3-demo

%files devel
%{_includedir}/gtk-3.0/
%{_libdir}/libgtk-3.so
%{_libdir}/libgdk-3.so
%{_libdir}/libgailutil-3.so
%{_libdir}/libgail-3.so
%{_libdir}/pkgconfig/gtk+-3.0.pc
%{_libdir}/pkgconfig/gdk-3.0.pc
%{_libdir}/pkgconfig/gail-3.0.pc
%{_libdir}/pkgconfig/gailutil-3.0.pc

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file for GTK3.
