content: Name:           grep
Version:        3.9
Release:        1%{?dist}
Summary:        A GNU utility to search files for character patterns. GPL

License:        GPLv3+
URL:            https://www.gnu.org/software/grep/

Source0:        %{name}-%{version}.tar.xz

BuildRequires:  gettext

#Runtime Dependencies
Requires:       glibc


%description
The grep program searches the named input FILEs (or standard input if no files are named,
or the file name - is given) for lines containing a match to the given PATTERN.
By default, grep prints the matching lines.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/grep
%{_mandir}/man1/grep.1*
%{_infodir}/grep.info*

%changelog
* %{DATE} Dan Carpenter DanC403@gmail.com - 3.9-1
- Initial package build.

