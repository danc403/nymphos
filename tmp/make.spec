content:
  - Name:           make
  - Version:        4.4.1
  - Release:        1%{?dist}
  - Summary:        A GNU tool which simplifies the build process
  - 
  - License:        GPLv3+
  - URL:            https://www.gnu.org/software/make/
  - 
  - Source0:        %{name}-%{version}.tar.gz
  - 
  - BuildRequires:  texinfo
  - 
  - Provides:       make
  - Conflicts:      bsdmake
  - 
  - %description
  - GNU Make is a program that simplifies the build process for software.
  - 
  - %prep
  - %setup -q
  - 
  - %build
  - ./configure
  - make %{?_smp_mflags}
  - 
  - %install
  - make install DESTDIR=%{buildroot}
  - 
  - %files
  - %license COPYING
  - %doc README NEWS AUTHORS THANKS
  - /usr/bin/make
  - /usr/share/man/man1/make.1*
  - /usr/share/info/*
  - 
  - %changelog
  - * %{date} Dan Carpenter <DanC403@gmail.com> - 4.4.1-1
  - - Initial package build
