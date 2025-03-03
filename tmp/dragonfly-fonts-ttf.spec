name: dragonfly-fonts-ttf
version: 0
release: 1%{?dist}
summary: Dragonfly TTF Fonts
license: OFL
url: https://example.com/dragonfly-fonts-ttf
source0: dragonfly-fonts-ttf.tar.xz
buildarch: noarch
requires:
  - fontconfig
buildrequires:
  - fontconfig
description: Dragonfly TTF Fonts.
prep:
  - %setup -q
build:
  - 
install:
  - mkdir -p %{buildroot}%{_datadir}/fonts
  - cp -r * %{buildroot}%{_datadir}/fonts/
  - mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.d
  - fc-cache -f -v
files:
  - %{_datadir}/fonts/*
  - %license LICENSE
changelog:
  - * Wed Oct 25 2023 Dan Carpenter DanC403@gmail.com - 0-1
  - - Initial package build
