content: Name:           flex-devel
Version:        2.6.4
Release:        1%{?dist}
Summary:        Development files for flex

License:        BSD-3-Clause
URL:            https://github.com/westes/flex

Requires:       flex = %{version}-%{release}

%description
This package contains the header files and libraries needed to develop
applications that use flex.

%files
%{_includedir}/FlexLexer.h

