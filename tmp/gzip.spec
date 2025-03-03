content: Name:           gzip
Version:        1.12
Release:        1%{?dist}
Summary:        GNU compression utility (GNU zip) with Lempel-Ziv coding. License:        GPLv3+


URL:            https://www.gnu.org/software/gzip/

Source0:        %{name}-%{version}.tar.xz

BuildRequires:  gettext


%description
Gzip is used to compress files.  Gzip reduces the size of the named files,
using Lempel-Ziv coding.  Whenever possible, each file is replaced by one
with the extension .gz, while keeping the same ownership modes, access and
modification times.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/gzip
%{_bindir}/gunzip
%{_bindir}/zcat
%{_mandir}/man1/gzip.1.*
%{_mandir}/man1/gunzip.1.*
%{_mandir}/man1/zcat.1.*
%{_infodir}/gzip.info*

%changelog
* %{date} Dan Carpenter DanC403@gmail.com - 1.12-1
- Initial package build.

filename: gzip.spec
