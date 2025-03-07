Name:       dragonfly-fonts-ttf
Version:    1.0
Release:    1%{?dist}
Summary:    Dragonfly TrueType fonts

License:    OFL
URL:        https://www.1001freefonts.com/dragonfly.font # Replace with actual URL
Source0:    dragonfly-fonts-ttf.tar.xz

%description
The Dragonfly fonts are a TrueType font family designed with accessibility in mind.

%files
%{_datadir}/fonts/ttf/Dragonfly-Regular.ttf
%{_datadir}/fonts/ttf/Dragonfly-Bold.ttf

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
