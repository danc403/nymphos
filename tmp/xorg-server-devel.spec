name: xorg-server-devel
version: 21.1.16
release: 1%{?dist}
summary: Development files for the X Window System display server
license: MIT
url: https://xorg.freedesktop.org/
source0: xorg-server-%{version}.tar.xz
buildrequires:
  - autoconf
  - automake
  - libtool
  - pkg-config
  - gcc
  - make
  - xproto
  - renderproto
  - inputproto
  - videoproto
  - dri2proto
  - dri3proto
  - presentproto
  - damageproto
  - fixesproto
  - glproto
  - xextproto
  - xf86driproto
  - xf86vidmodeproto
  - kbproto
  - fontsproto
  - bigreqsproto
  - randrproto
  - recordproto
  - compositeproto
  - xcmiscproto
  - xkeyboard-config
  - libXi-devel
  - libXrandr-devel
  - libXcursor-devel
  - libXinerama-devel
  - libXdamage-devel
  - libXcomposite-devel
  - libXfixes-devel
  - libXext-devel
  - libXdmcp-devel
  - libXtst-devel
  - libxcb-devel
  - libXfont2-devel
  - mesa-libGL-devel
  - mesa-libEGL-devel
  - pixman-devel
  - libudev-devel
  - systemd-devel
  - dbus-devel
requires:
  - xorg-server = %{version}-%{release}
description: This package contains the header files and static libraries needed to develop applications that use the X Window System display server.
prep:
  - %autosetup
build:
  - %configure %{?configure_options}
  - %make_build
install:
  - %make_install
files:
  - /usr/include/xorg/*
  - /usr/lib64/pkgconfig/xorg-server.pc
changelog:
  -
    date: 2024-01-01
    name: Dan Carpenter
    email: DanC403@gmail.com
    changes: ['Initial build for version 21.1.16.']
