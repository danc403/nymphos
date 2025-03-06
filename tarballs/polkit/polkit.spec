Name:       polkit
Version:    0.120
Release:    1%{?dist}
Summary:    Application toolkit for controlling system-wide privileges

License:    GPLv2+
URL:        https://gitlab.freedesktop.org/polkit/polkit
Source0:    polkit-%{version}.tar.xz

BuildRequires:  glib2-devel
BuildRequires:  js-devel
BuildRequires:  libcap-devel

%description
PolicyKit (polkit) is an application-level toolkit for defining and
handling authorizations. It allows non-privileged processes to execute
privileged processes.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --sysconfdir=/etc
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_sbindir}/pkaction
%{_sbindir}/pkcheck
%{_sbindir}/pkexec
%{_libdir}/libpolkit-agent-1.so.*
%{_libdir}/libpolkit-gobject-1.so.*
%{_mandir}/man1/pkaction.1*
%{_mandir}/man1/pkcheck.1*
%{_mandir}/man1/pkexec.1*
/etc/polkit-1/

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - %{version}-%{release}
- Initial spec file.
