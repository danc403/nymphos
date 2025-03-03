name: luciole-fonts-ttf
version: 0
release: 1%{?dist}
summary: Luciole Fonts TTF - A set of TrueType fonts
license: OFL
url: https://example.com/luciole-fonts-ttf
source0: %{name}.tar.xz
buildarch: noarch
requires:
  - fontconfig
buildrequires:
  - fontconfig
description: Luciole Fonts TTF is a set of TrueType fonts.
prep:
  - %setup -q
build:
  - 
install:
  - mkdir -p %{buildroot}%{_datadir}/fonts
  - cp -r *.ttf %{buildroot}%{_datadir}/fonts/
  - mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.d
  - echo '<?xml version="1.0"?>' > %{buildroot}%{_datadir}/fontconfig/conf.d/50-luciole.conf
  - echo '<fontconfig>' >> %{buildroot}%{_datadir}/fontconfig/conf.d/50-luciole.conf
  - echo ' <match target="pattern">' >> %{buildroot}%{_datadir}/fontconfig/conf.d/50-luciole.conf
  - echo '  <test qual="any" name="family"><string>sans-serif</string></test>' >> %{buildroot}%{_datadir}/fontconfig/conf.d/50-luciole.conf
  - echo '  <edit name="family" mode="prepend" binding="strong"><string>Luciole</string></edit>' >> %{buildroot}%{_datadir}/fontconfig/conf.d/50-luciole.conf
  - echo ' </match>' >> %{buildroot}%{_datadir}/fontconfig/conf.d/50-luciole.conf
  - echo ' <match target="pattern">' >> %{buildroot}%{_datadir}/fontconfig/conf.d/50-luciole.conf
  - echo '  <test qual="any" name="family"><string>serif</string></test>' >> %{buildroot}%{_datadir}/fontconfig/conf.d/50-luciole.conf
  - echo '  <edit name="family" mode="prepend" binding="strong"><string>Luciole</string></edit>' >> %{buildroot}%{_datadir}/fontconfig/conf.d/50-luciole.conf
  - echo ' </match>' >> %{buildroot}%{_datadir}/fontconfig/conf.d/50-luciole.conf
  - echo ' <match target="pattern">' >> %{buildroot}%{_datadir}/fontconfig/conf.d/50-luciole.conf
  - echo '  <test qual="any" name="family"><string>monospace</string></test>' >> %{buildroot}%{_datadir}/fontconfig/conf.d/50-luciole.conf
  - echo '  <edit name="family" mode="prepend" binding="strong"><string>Luciole</string></edit>' >> %{buildroot}%{_datadir}/fontconfig/conf.d/50-luciole.conf
  - echo ' </match>' >> %{buildroot}%{_datadir}/fontconfig/conf.d/50-luciole.conf
  - echo '</fontconfig>' >> %{buildroot}%{_datadir}/fontconfig/conf.d/50-luciole.conf
  - /usr/bin/fc-cache -fvs %{buildroot}%{_datadir}/fonts
files:
  - %{_datadir}/fonts/*
  - %{_datadir}/fontconfig/conf.d/50-luciole.conf
  - %license
changelog:
  - * Mon Oct 28 2024 Dan Carpenter DanC403@gmail.com - 0-1
  - - Initial package build.
