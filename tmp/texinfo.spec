content: Name:           texinfo
Version:        7.0
Release:        1%{?dist}
Summary:        GNU documentation system for on-line information and printed output
License:        GPLv3+
URL:            https://www.gnu.org/software/texinfo/

Source0:        %{name}-%{version}.tar.xz

BuildRequires:  make
BuildRequires:  gettext
BuildRequires:  perl

Requires:       coreutils
Requires:       gawk
Requires:       perl
Requires:       xz


%description
Texinfo is a documentation system that uses a single source file
to produce both on-line information and printed output.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# Remove libtool archives
find %{buildroot} -name \*.la -delete

%files
%{_bindir}/*
%{_infodir}/*
%{_mandir}/man1/*
%{_datadir}/texinfo/*
%{_datadir}/gettext/*
%{_libexecdir}/texinfo/*
%license COPYING

%changelog
* %{date} Dan Carpenter DanC403@gmail.com - 7.0-1
- Initial package build.

filename: texinfo.spec
