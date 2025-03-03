spec_content: Name:           diffutils
Version:        3.9
Release:        1%{?dist}
Summary:        GNU diff utilities - compare files line by line
License:        GPLv3+
URL:            https://www.gnu.org/software/diffutils/

Source0:        %{name}-%{version}.tar.xz

BuildRequires:  gettext

%description
The diffutils package contains programs that find the differences
between files.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

# Remove libtool archives
find %{buildroot} -name '*.la' -delete

%files
%{_bindir}/cmp
%{_bindir}/diff
%{_bindir}/diff3
%{_bindir}/sdiff
%{_mandir}/man1/cmp.1*
%{_mandir}/man1/diff.1*
%{_mandir}/man1/diff3.1*
%{_mandir}/man1/sdiff.1*
%{_infodir}/diffutils.info*
%{_datadir}/locale/*/LC_MESSAGES/diffutils.mo
%{_datadir}/gettext/its/diffutils.its

%changelog
* %{date} Dan Carpenter <DanC403@gmail.com> - 3.9-1
- Initial package build

package_name: diffutils
