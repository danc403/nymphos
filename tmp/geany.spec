name: geany
version: 2.0
release: 1%{?dist}
summary: A small and lightweight IDE - Geany
license: GPL-2.0-or-later
url: https://www.geany.org/
source0: %{name}-%{version}.tar.gz
buildrequires:
  - gtk3-devel
  - glib2-devel
  - vte3-devel
  - pcre-devel
  - gcc
  - make
  - pkg-config
  - gettext
requires:
  - gtk3
  - glib2
  - vte3
  - pcre
  - desktop-file-utils
description: Geany is a small and lightweight Integrated Development Environment. It supports many filetypes and languages and provides basic code completion and syntax highlighting.
prep:
  - %setup -q
build:
  - %configure
  - %make_build
install:
  - %make_install
  - %find_lang %{name}
files:
  - %{_bindir}/%{name}
  - %{_datadir}/%{name}/*
  - %{_datadir}/applications/%{name}.desktop
  - %{_datadir}/icons/hicolor/*/*/%{name}.png
  - %{_mandir}/man1/%{name}.1*
  - %{_datadir}/locale/*/%{name}.mo
  - %license COPYING
changelog:
  - * %{DATE} Dan Carpenter <DanC403@gmail.com> - 2.0-1
  - - Initial RPM build.
