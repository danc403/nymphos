content: Name:           tar
Version:        1.34
Release:        1%{?dist}
Summary:        GNU tar (tape archiver) - archiving utility [GPLv3+]

License:        GPLv3+
URL:            https://www.gnu.org/software/tar/

Source0:        %{name}-%{version}.tar.xz

BuildRequires:  xz

#No longer needed on modern systems
#Requires:       gzip
#Requires:       bzip2
#Requires:       xz


%description
The GNU tar program saves many files together into a single archive,
and can restore individual files from the archive.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# Move the info files to the correct location.
mkdir -p %{buildroot}%{_infodir}
install -m 644 doc/tar.info %{buildroot}%{_infodir}/

%files
%{_bindir}/tar
%{_mandir}/man1/tar.1*
%{_infodir}/tar.info*
%{_libexecdir}/tar
%license COPYING

%changelog
* %{ Fri Nov 3 2023 } Dan Carpenter DanC403@gmail.com - 1.34-1
- Initial package build.

