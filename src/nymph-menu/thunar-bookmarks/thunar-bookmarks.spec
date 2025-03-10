Name:           thunar-bookmarks
Version:        0.1
Release:        1%{?dist}
Summary:        Thunar bookmarks script
License:        GPLv2+
URL:            https://github.com/your-repo/thunar-bookmarks
Source0:        %{name}-%{version}.tar.xz

BuildRequires:  perl

%description
thunar-bookmarks is a Perl script that provides enhanced bookmark functionality for the Thunar file manager.

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 thunar-bookmarks-0.1/thunar-bookmarks.pl %{buildroot}%{_bindir}/thunar-bookmarks

%files
%{_bindir}/thunar-bookmarks

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial package.
