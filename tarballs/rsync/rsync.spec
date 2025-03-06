Name:       rsync
Version:    3.4.1
Release:    1%{?dist}
Summary:    Fast and versatile file synchronization tool

License:    GPLv3+
URL:        https://rsync.samba.org/
Source0:    rsync-%{version}.tar.gz

BuildRequires:  openssl-devel  # Required for rsync daemon encryption

%description
Rsync is a fast and versatile file synchronization tool. It can efficiently
transfer only the differences between two files or directories.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --sysconfdir=/etc
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/rsync
%{_mandir}/man1/rsync.1*
/etc/rsyncd.conf

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
