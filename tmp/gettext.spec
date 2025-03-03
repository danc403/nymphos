spec_content: %global commit 5157e12d33e42c18083908b044e913a891966468

Name:       gettext
Version:    0.21.1
Release:    1%{?dist}
Summary:    GNU internationalization library and tools
License:    GPLv3+
URL:        https://www.gnu.org/software/gettext/

Source0:    %{name}-%{version}.tar.xz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  gettext
BuildRequires:  libtool
BuildRequires:  perl
BuildRequires:  texinfo
BuildRequires:  pkgconfig
Requires:       glibc

%description
gettext is a set of tools providing a framework to help other GNU
software produce multi-lingual messages.

%prep
%autosetup

%build
./configure --prefix=%{_prefix} \
            --disable-static \
            --enable-shared
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# remove libtool archives
find %{buildroot} -name '*.la' -delete

%files
%license COPYING.LIB
%{_bindir}/*
%{_libdir}/*.so*
%{_datadir}/gettext/*
%{_datadir}/locale/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_infodir}/*

%changelog
* %{date} Dan Carpenter DanC403@gmail.com - 0.21.1-1
- Initial package build

package_name: gettext
