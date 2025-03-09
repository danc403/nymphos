Name:           freetype
Version:        2.9.1
Release:        1%{?dist}
Summary:        A free, high-quality, and portable font engine.
License:        FTL or GPLv2
URL:            https://www.freetype.org/
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  bzip2-devel zlib-devel libpng-devel

%description
FreeType 2 is a software library to render fonts. It is written in C, designed to be small, efficient, highly customizable, and portable while capable of producing high-quality output (glyph images). It can be used in graphics libraries, display servers, font conversion tools, text image generation tools, and many other products.

%package devel
Summary:        Development files for FreeType
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains the development files for FreeType.

%prep
%autosetup -n freetype-%{version}

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license docs/FTL.TXT docs/GPLv2.TXT
%{_libdir}/libfreetype.so.*
%{_bindir}/freetype-config
%{_mandir}/man1/freetype-config.1*

%files devel
%{_includedir}/freetype2/
%{_libdir}/libfreetype.a
%{_libdir}/pkgconfig/freetype2.pc

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial package.
