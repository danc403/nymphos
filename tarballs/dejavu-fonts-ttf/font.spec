Name:       dejavu-fonts-ttf
Version:    2.37
Release:    1%{?dist}
Summary:    DejaVu TrueType fonts

License:    Bitstream Vera License and Public Domain
URL:        https://dejavu-fonts.github.io/
Source0:    dejavu-fonts-ttf-%{version}.tar.bz2

%description
The DejaVu fonts are a font family based on the Vera Fonts.
Its purpose is to provide a wider range of characters while
maintaining the original look and feel.

%files
%{_datadir}/fonts/ttf/DejaVuSans.ttf
%{_datadir}/fonts/ttf/DejaVuSans-Bold.ttf
%{_datadir}/fonts/ttf/DejaVuSans-Oblique.ttf
%{_datadir}/fonts/ttf/DejaVuSans-BoldOblique.ttf
%{_datadir}/fonts/ttf/DejaVuSansMono.ttf
%{_datadir}/fonts/ttf/DejaVuSansMono-Bold.ttf
%{_datadir}/fonts/ttf/DejaVuSansMono-Oblique.ttf
%{_datadir}/fonts/ttf/DejaVuSansMono-BoldOblique.ttf
%{_datadir}/fonts/ttf/DejaVuSerif.ttf
%{_datadir}/fonts/ttf/DejaVuSerif-Bold.ttf
%{_datadir}/fonts/ttf/DejaVuSerif-Italic.ttf
%{_datadir}/fonts/ttf/DejaVuSerif-BoldItalic.ttf

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
