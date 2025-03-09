Name:           libxml2
Version:        2.12.10
Release:        1%{?dist}
Summary:        XML parsing library
License:        MIT
URL:            http://www.xmlsoft.org/
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  zlib-devel libicu-devel

%description
libxml2 is the XML C parser and toolkit developed for the Gnome project (but usable outside of the Gnome platform), providing an API to parse XML and HTML documents.

%package devel
Summary:        Development files for libxml2
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains the development files for libxml2.

%prep
%autosetup -n %{name}-%{version}

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
%{_libdir}/libxml2.so.*
%{_bindir}/xmlcatalog
%{_bindir}/xmllint
%{_mandir}/man1/xmlcatalog.1*
%{_mandir}/man1/xmllint.1*

%files devel
%{_includedir}/libxml/
%{_libdir}/libxml2.a
%{_libdir}/pkgconfig/libxml-2.0.pc

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial package.
