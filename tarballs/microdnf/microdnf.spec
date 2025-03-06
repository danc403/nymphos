Name:       microdnf
Version:    3.10.1
Release:    1%{?dist}
Summary:    A lightweight DNF package manager

License:    GPLv2+
URL:        https://github.com/rpm-software-management/microdnf
Source0:    microdnf-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  rpm-devel
BuildRequires:  libsolv-devel
BuildRequires:  libcomps-devel
BuildRequires:  libdnf-devel

%description
Microdnf is a lightweight version of the DNF package manager. It is
intended for use in minimal environments, such as containers.

%prep
%setup -q

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
mkdir -p %{buildroot}/etc/dnf/repos.d
mkdir -p %{buildroot}/var/cache/microdnf

# Create a sample repo file. You will need to change this!
cat <<EOF > %{buildroot}/etc/dnf/repos.d/sample.repo
[sample]
name=Sample Repository
baseurl=file:///path/to/your/repo/
enabled=1
gpgcheck=0
EOF

%files
%{_bindir}/microdnf
%{_mandir}/man8/microdnf.8*
/etc/dnf/
/var/cache/microdnf/

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
