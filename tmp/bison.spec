content:
  - Name:           bison
  - Version:        3.8
  - Release:        1%{?dist}
  - Summary:        A general-purpose parser generator (GNU Bison)
  - 
  - License:        GPLv3+
  - URL:            https://www.gnu.org/software/bison/
  - 
  - Source0:        %{name}-%{version}.tar.xz
  - 
  - BuildRequires:  m4
  - BuildRequires:  texinfo
  - 
  - Requires:       coreutils
  - 
  - %description
  - GNU Bison is a general-purpose parser generator that converts a grammar
  - description for an LALR(1) context-free grammar into a C program to parse
  - that grammar.
  - 
  - %prep
  - %autosetup
  - 
  - %build
  - %configure
  - make %{?_smp_mflags}
  - 
  - %install
  - make install DESTDIR=%{buildroot}
  - 
  - rm -rf %{buildroot}/usr/share/info
  - 
  - %files
  - %license COPYING
  - %doc NEWS README
  - %{_bindir}/bison
  - %{_mandir}/man1/bison.1*
  - %{_datadir}/bison
  - %{_datadir}/aclocal/bison.m4
  - 
  - %changelog
  - * %{date} Dan Carpenter <DanC403@gmail.com> - 3.8-1
  - - Initial package build
