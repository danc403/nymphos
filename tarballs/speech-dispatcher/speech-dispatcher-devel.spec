Name: speech-dispatcher-devel
Version: 0.10.1
Release: 1%{?dist}
Summary: Development files for speech-dispatcher
License: GPL-2.0-or-later
URL: https://freebsoft.org/speechd
Source0: speech-dispatcher-0.10.1.tar.gz
BuildRequires:
  - autoconf
  - automake
  - libtool
  - pkgconfig
  - alsa-lib-devel
  - glib2-devel
Requires:
  - speech-dispatcher = %{version}-%{release}

%description
Development files for speech-dispatcher.

%prep
%setup -q

%build
./configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
/usr/include/speechd/
/usr/lib/libspeechd.so
/usr/lib/pkgconfig/speechd.pc

%changelog
* %{__date} Dan Carpenter <DanC403@gmail.com> - %{version}-1
- Initial RPM build of speech-dispatcher-devel.
