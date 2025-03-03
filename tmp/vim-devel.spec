name: vim-devel
version: 9.0.1635
release: 1%{?dist}
summary: Development files for Vim.
license: Vim
url: https://www.vim.org/
source0: %{name}-%{version}.tar.gz
requires:
  - vim = %{version}-%{release}
description: This package contains the development files for Vim.
build:
  - %configure
  - %make_build
install:
  - %make_install
files:
  - /usr/include/vim/*
changelog:
  - * %{date} Dan Carpenter <DanC403@gmail.com> - %{version}-1
  - - Initial build.
