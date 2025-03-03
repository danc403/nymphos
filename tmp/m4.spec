spec_content: %define debug_package %{nil}

Name:           m4
Version:        1.4.19
Release:        1%{?dist}
Summary:        GNU m4 is an implementation of the traditional UNIX macro processor - GPL

License:        GPLv3+
URL:            https://www.gnu.org/software/m4/
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  texinfo

Requires:       coreutils

%description
The GNU m4 is an implementation of the traditional UNIX macro processor.  It
is mostly SVR4 compliant, and has some extensions to handle things like
builtins that can dynamically load other shared objects.


%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%check
make check

%files
%{_bindir}/m4
%{_infodir}/m4.info*
%{_mandir}/man1/m4.1*
%{_datadir}/aclocal/m4.m4
%{_datadir}/m4/
%{_prefix}/share/doc/%{name}/ChangeLog
%{_prefix}/share/doc/%{name}/NEWS
%{_prefix}/share/doc/%{name}/README
%{_prefix}/share/doc/%{name}/COPYING

%changelog
* %{DATE} Dan Carpenter DanC403@gmail.com - 1.4.19-1
- Initial package build.

