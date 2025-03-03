content: Name:           xz
Version:        5.4.1
Release:        1%{?dist}
Summary:        XZ Utils - Tools for compressing and decompressing .xz files
License:        LGPLv2+ and GPLv2+
URL:            https://tukaani.org/xz/

Source0:        %{name}-%{version}.tar.xz

BuildRequires:  gettext

# No OpenRC-specific configuration needed, handles systemd internally.
# No LightDM-specific configuration needed.

%description
XZ Utils are the tools to compress and decompress .xz files, which
are useful for smaller downloads.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING COPYING.GPLv2 COPYING.LGPLv2
%{_bindir}/xz
%{_bindir}/xzcat
%{_bindir}/xzdec
%{_bindir}/lzma
%{_bindir}/unxz
%{_mandir}/man1/xz.1*
%{_mandir}/man1/xzcat.1*
%{_mandir}/man1/xzdec.1*
%{_mandir}/man1/lzma.1*
%{_mandir}/man1/unxz.1*
%{_libdir}/liblzma.so*
%{_libdir}/liblzma.*.dylib*

%changelog
* %{today} Dan Carpenter DanC403@gmail.com - 5.4.1-1
- Initial package build

filename: xz.spec
