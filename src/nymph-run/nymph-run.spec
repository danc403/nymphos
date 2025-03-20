Name:           nymph-run
Version:        1.0
Release:        1%{?dist}
Summary:        A simple run dialog for executing commands

License:        GPLv3+
URL:            https://example.com/nymph-run  (Replace with your actual project URL if you have one)
Source0:        %{name}-%{version}.tar.xz

BuildRequires:  vala
BuildRequires:  gtk3-devel
BuildRequires:  glib2-devel

Requires:       gtk3

%description
Nymph Run is a simple application that provides a run dialog,
allowing users to execute commands quickly.

%prep
%autosetup

%build
make

%install
make install PREFIX=%{buildroot}%{_prefix}

#Remove the default desktop file installation path from share/applications, instead it should be in /usr/share/applications, not /usr/local/share/applications.
rm -f %{buildroot}/usr/local/share/applications/nymph-run.desktop
install -D -m 0644 nymph-run.desktop %{buildroot}%{_datadir}/applications/nymph-run.desktop

%files
%{_bindir}/nymph-run
%{_datadir}/applications/nymph-run.desktop

%changelog
* Mon Oct 23 2023 Your Name <your.email@example.com> - 1.0-1
- Initial package.
