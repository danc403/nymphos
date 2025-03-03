name: vim
version: 9.0.1635
release: 1%{?dist}
summary: Vi Improved, a programmers text editor.
license: Vim
url: https://www.vim.org/
source0: %{name}-%{version}.tar.gz
buildrequires:
  - ncurses-devel
  - perl
  - python3-devel
  - gtk2-devel
  - gtk3-devel
  - libX11-devel
  - libXt-devel
requires:
  - ncurses
  - perl
  - python3
  - gtk2
  - gtk3
  - libX11
  - libXt
description: Vim is an advanced text editor that provides syntax highlighting,
multiple undo, split screen editing, command line editing, filename
completion, and a complete online help system.  It supports a variety
of languages and file formats.
build:
  - %configure
  - %make_build
install:
  - %make_install
files:
  - /usr/bin/vim
  - /usr/bin/vimdiff
  - /usr/bin/rvim
  - /usr/bin/ex
  - /usr/bin/view
  - /usr/share/vim
  - /usr/share/applications/vim.desktop
  - /usr/share/man/man1/vim.1.gz
  - /usr/share/man/man1/vimdiff.1.gz
  - /usr/share/man/man1/rvim.1.gz
  - /usr/share/man/man1/ex.1.gz
  - /usr/share/man/man1/view.1.gz
  - /usr/share/doc/vim-%{version}/
  - /usr/share/licenses/vim-%{version}/LICENSE
changelog:
  - * %{date} Dan Carpenter <DanC403@gmail.com> - %{version}-1
  - - Initial build.
