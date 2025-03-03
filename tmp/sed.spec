spec_content: Name:           sed
Version:        4.9
Release:        1%{?dist}
Summary:        The GNU Stream EDitor - a line-oriented text editor.
License:        GPLv3+
URL:            https://www.gnu.org/software/sed/

Source0:        %{name}-%{version}.tar.xz

BuildRequires:  gettext
BuildRequires:  texinfo

%description
Sed is a stream editor.  A stream editor is used to perform basic
text transformations on an input stream (a file or input from a
pipeline).

%prep
%autosetup

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# Remove libtool archives
find %{buildroot} -name '*.la' -delete

%files
%{_bindir}/sed
%{_infodir}/sed.info*
%{_mandir}/man1/sed.1.*
%{_datadir}/locale/*/LC_MESSAGES/sed.mo
%{_datadir}/doc/%{name}/
%{_mandir}/man7/regex.7*

%changelog
* %{date} Dan Carpenter <DanC403@gmail.com> - 4.9-1
- Initial package build.

