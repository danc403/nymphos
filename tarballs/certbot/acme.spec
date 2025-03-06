Name:       acme.sh
Version:    2.11.1
Release:    1%{?dist}
Summary:    A pure Unix shell script implementing ACME client protocol

License:    MIT
URL:        https://github.com/acmesh-official/acme.sh
Source0:    acme-%{version}.tar.gz

%description
acme.sh is a pure Unix shell script implementing ACME client protocol.

%install
install -Dm755 acme.sh %{buildroot}%{_bindir}/acme.sh
install -Dm644 *.sh %{buildroot}%{_datadir}/acme.sh/

%files
%{_bindir}/acme.sh
%{_datadir}/acme.sh/

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
