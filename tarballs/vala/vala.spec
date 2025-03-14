Name:           vala
Version:        0.56.17
Release:        1%{?dist}
Summary:        The Vala Compiler

License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/GNOME/vala
# Source0:        https://download.gnome.org/sources/vala/%{version:0.56}/vala-%{version}.tar.gz
Source0:        vala-%{version}.tar.gz # Expect tarball in the same directory

BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  glib2-devel >= 2.56
BuildRequires:  gobject-introspection-devel
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  graphviz-devel >= 2.16
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  help2man

%global __date    %(date +%%Y-%%m-%%d)
%global _version_release %{version}-%{release}

%package devel
Summary:        Development files for the Vala compiler
Requires:       %{name} = %{_version_release}

%description
The Vala compiler is a compiler for the Vala programming language.

%package devel
Summary:        Development files for the Vala compiler
Requires:       %{name} = %{_version_release}

%description devel
This package contains the development files for the Vala compiler.

%prep
%autosetup -p1

%build
# Check if valac is in PATH
if ! which valac >/dev/null 2>&1; then
  # Bootstrap
  touch */*.stamp
  ./configure --prefix=%{_builddir}/vala-bootstrap
  make -C compiler
  export VALAC=%{_builddir}/vala-bootstrap/compiler/valac
else
  export VALAC=valac
fi

# Build the main package
%{VALAC} ./configure --prefix=%{_prefix}
make %{?_smp_flags}

%install
make install DESTDIR=%{buildroot}

# Install valadoc documentation
# make install-valadoc DESTDIR=%{buildroot} # Skip valadoc

# Install man pages
make install-man DESTDIR=%{buildroot}

# Install README
install -Dm0644 README %{buildroot}%{_docdir}/%{name}/README

%check
make check

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%{_bindir}/valac
%{_bindir}/vapigen
%{_mandir}/man1/valac.1*
%{_mandir}/man1/vapigen.1*
%{_datadir}/vala/
# %{_datadir}/valadoc/ # Skip valadoc
%{_docdir}/%{name}/README

%files devel
%{_includedir}/vala-0.56/
%{_libdir}/libvala-0.56.so
%{_libdir}/libvapi-0.56.so
%{_libdir}/pkgconfig/vala-0.56.pc
%{_libdir}/pkgconfig/vapi-0.56.pc

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/vala-bootstrap

%changelog
* Thu Mar 13 2025 Dan Carpenter <danc403@gmail.com> - %{_version_release}
-   Use local tarball.
-   Skip building valadoc.
-   Use spec file macros for date and version-release.
