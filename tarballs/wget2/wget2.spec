Name:       wget2
Version:    2.2.0
Release:    1%{?dist}
Summary:    A network utility to retrieve files from the Web (version 2)

License:    GPLv3+
URL:        https://gitlab.gnu.org/gnuwget/wget2
Source0:    wget2-%{version}.tar.gz

BuildRequires:  openssl-devel
BuildRequires:  libunistring-devel
BuildRequires:  gnutls-devel

%description
GNU Wget2 is a network utility to retrieve files from the Web. It is a
complete rewrite of GNU Wget, with improvements in performance,
security, and features.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --sysconfdir=/etc
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/wget
%{_mandir}/man1/wget.1*
/etc/wgetrc

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file for wget2.
