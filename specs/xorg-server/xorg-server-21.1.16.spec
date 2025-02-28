# specs/xorg-server/xorg-server-21.1.16.spec
Name:           xorg-server
Version:        21.1.16
Release:        1%{?dist}
Summary:        X.Org X server
License:        MIT
URL:            https://www.x.org/
Source0:        xorg-server-21.1.16.tar.xz

BuildRequires:  autoconf, automake, libtool, pkgconfig, libX11-devel, libXext-devel, libXrender-devel, libXfixes-devel, libXi-devel, libXrandr-devel, libXcursor-devel, libXdamage-devel, libudev-devel, libmtdev-devel, libinput-devel, libepoxy-devel, pixman-devel, xproto-devel, inputproto-devel, renderproto-devel, fixesproto-devel, damageproto-devel, randrproto-devel, xcursorproto-devel, videoproto-devel, presentproto-devel, dri2proto-devel, dri3proto-devel, syncproto-devel, kbproto-devel, fontsproto-devel, resourceproto-devel, compositeproto-devel, recordproto-devel, selinux-policy-devel

%description
The X.Org X server is the core component of the X Window System.

%prep
%setup -q

%build
autoreconf -fi
%configure --disable-static --enable-dri --enable-glamor --enable-suid --with-systemd=no --with-udev-rules-dir=/lib/udev/rules.d/
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

#remove systemd files
rm -rf %{buildroot}%{_libdir}/systemd

%files
%{_bindir}/Xorg
%{_libdir}/xorg/
%{_datadir}/X11/
%{_mandir}/man1/Xorg.1*
%{_mandir}/man5/xorg.conf.5*
%{_mandir}/man7/xorg-server.7*
%{_mandir}/man7/xorg.7*
%{_mandir}/man4/vga.4*
%{_mandir}/man4/vesa.4*
%{_mandir}/man4/fbdev.4*
%{_mandir}/man4/modesetting.4*
%{_mandir}/man4/intel.4*
%{_mandir}/man4/amdgpu.4*
%{_mandir}/man4/nouveau.4*

%changelog
* Fri Nov 24 2023 User <user@example.com> - 21.1.16-1
- Initial package.
