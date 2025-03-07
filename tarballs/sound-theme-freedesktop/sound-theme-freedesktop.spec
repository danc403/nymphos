Name:           sound-theme-freedesktop
Version:        0.8
Release:        1%{?dist}
Summary:        Freedesktop.org sound theme

License:        LGPLv2+
Source0:        sound-theme-freedesktop-%{version}.tar.bz2
BuildArch:      noarch

%description
This package provides the Freedesktop.org sound theme,
which is a set of standard sound files for desktop environments.

%install
mkdir -p %{buildroot}/usr/share/sounds/freedesktop
tar -xjvf %{SOURCE0} -C %{buildroot}/usr/share/sounds/freedesktop --strip-components=1

%files
/usr/share/sounds/freedesktop/

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - 0.8-1
- Initial package creation.
