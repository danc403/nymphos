Name:       sudo
Version:    1.9.15
Release:    1%{?dist}
Summary:    Allow limited superuser privileges to specific users

License:    ISC
URL:        https://www.sudo.ws/
Source0:    sudo-%{version}.tar.gz

BuildRequires:  pam-devel
BuildRequires:  openssl-devel
BuildRequires:  libselinux-devel # Remove this if not using SELinux
BuildRequires:  audit-libs-devel

%description
Sudo allows a system administrator to give certain users (or groups of
users) the ability to run some (or all) commands as root while logging
all commands and arguments.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --sysconfdir=/etc
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_sbindir}/sudo
%{_sbindir}/sudoreplay
%{_sbindir}/visudo
%{_mandir}/man1/sudo.1*
%{_mandir}/man8/sudoreplay.8*
%{_mandir}/man8/visudo.8*
/etc/sudoers
/etc/sudoers.d/

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
