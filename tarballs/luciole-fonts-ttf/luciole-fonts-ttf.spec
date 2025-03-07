Name:       luciole-fonts-ttf
Version:    1.0
Release:    1%{?dist}
Summary:    Luciole TrueType fonts

License:    OFL
URL:        https://www.luciole-vision.com/luciole-en.html # Replace with actual URL
Source0:    luciole-fonts-ttf.tar.xz

%description
The Luciole fonts are a TrueType font family designed with accessibility in mind.

%files
%{_datadir}/fonts/ttf/Luciole-Regular.ttf
%{_datadir}/fonts/ttf/Luciole-Bold.ttf

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
