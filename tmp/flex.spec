content: Name:           flex
Version:        2.6.4
Release:        1%{?dist}
Summary:        A fast lexical analyzer generator
License:        BSD-3-Clause
URL:            https://github.com/westes/flex

Source0:        %{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison

#Runtime deps
Requires:       coreutils
Requires:       grep


%description
Flex is a tool for generating scanners: programs which recognize
lexical patterns in text.  Flex reads the given input files, or its
standard input if no file names are given, for a description of the
scanner to generate.  The description is in the form of pairs of
regular expressions and C code.  Flex generates as output a C source
file, lex.yy.c, which defines a routine yylex().  This file is
compiled and linked with the -ll library to produce an executable.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

#Move man page
mv %{buildroot}/%{_mandir}/man1/flex.1 %{buildroot}/%{_mandir}/man1/%{name}.1

%files
%{_bindir}/flex
%{_mandir}/man1/%{name}.1*
%{_infodir}/flex.info*
%{_datadir}/aclocal/flex.m4
%{_datadir}/flex/*
%license LICENSE

%changelog
* %{date} Dan Carpenter DanC403@gmail.com - 2.6.4-1
- Initial package build

