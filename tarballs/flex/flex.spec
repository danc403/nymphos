Name:       flex
Version:    2.6.4
Release:    1%{?dist}
Summary:    A fast lexical analyzer generator

License:    BSD-3-Clause
URL:        https://github.com/westes/flex
Source0:    flex-%{version}.tar.gz

%description
Flex is a tool for generating scanners: programs which recognize lexical
patterns in text. Flex reads the given input files, or its standard input
if no file names are given, for a description of a scanner to generate.
The description is in the form of pairs of regular expressions and C code,
called rules. Then it generates as output a C source file, `lex.yy.c', which
defines a routine `yylex()'. This file is compiled and linked with the
`-lfl' library to produce an executable. When the executable is run, it
analyzes its standard input for occurrences of the regular expressions.

%package devel
Summary:    Development files for flex
Requires:   flex = %{version}-%{release}

%description devel
This package contains the development files for flex.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/flex
%{_mandir}/man1/flex.1*

%files devel
%{_libdir}/libfl.a
%{_includedir}/FlexLexer.h

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
