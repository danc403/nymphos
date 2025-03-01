Name:       geany
Version:    2.0
Release:    1%{?dist}
Summary:    A fast and lightweight text editor

License:    GPL-2.0-or-later
URL:        https://www.geany.org/
Source0:    %{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  gtk3-devel
BuildRequires:  gtksourceview3-devel
BuildRequires:  enchant2-devel
BuildRequires:  libxml2-devel
BuildRequires:  libnotify-devel
BuildRequires:  cairo-devel
BuildRequires:  pango-devel
BuildRequires:  atk-devel
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  gudev-devel
BuildRequires:  libcanberra-gtk3-devel
BuildRequires:  libpeas-devel
BuildRequires:  pkgconfig

%description
Geany is a fast and lightweight text editor. It uses the GTK+ toolkit and
the Scintilla editing component. It supports many filetypes and includes
features such as syntax highlighting, code folding, code completion, and
build system integration.

%prep
%setup -q

%build
autoreconf -fiv
%configure --prefix=/usr --sysconfdir=/etc --localstatedir=/var
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
%{_bindir}/geany
%{_datadir}/geany/
%{_mandir}/man1/geany.1*

%changelog
* Mon Nov 20 2023 Your Name <your.email@example.com> - 2.0-1
- Initial build for x86_64 and OpenRC.
