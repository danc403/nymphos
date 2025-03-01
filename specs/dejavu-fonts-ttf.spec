Name:       dejavu-fonts-ttf
Version:    2.37
Release:    1%{?dist}
Summary:    DejaVu TrueType fonts

License:    Bitstream-Vera AND Public Domain
URL:        https://dejavu-fonts.github.io/
Source0:    %{name}-%{version}.tar.bz2

BuildRequires:  fontconfig

%description
DejaVu is a family of fonts derived from the Bitstream Vera fonts. They
provide a wider range of characters while maintaining the original look
and feel. This package contains the TrueType font files.

%prep
%setup -q

%build
# No build step required for fonts

%install
install -d %{buildroot}%{_datadir}/fonts/ttf/dejavu
cp -r ttf/* %{buildroot}%{_datadir}/fonts/ttf/dejavu

%files
%{_datadir}/fonts/ttf/dejavu/

%changelog
* Mon Nov 20 2023 Your Name <your.email@example.com> - 2.37-1
- Initial build for x86_64 and OpenRC.
