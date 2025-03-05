Name: bzip2
Version: 1.0.8
Release: 1%{?dist}
Summary: A file compression utility
License: BSD-like
URL: https://sourceware.org/bzip2/
Source0: %{name}-%{version}.tar.gz

%description
bzip2 compresses files using the Burrows-Wheeler block-sorting text
compression algorithm, and Huffman coding. Compression is generally
much better than that achieved by more conventional LZ77/LZ78-based
compressors, and close to the performance of PPM-based compressors.

%prep
%setup -q

%build
make -f Makefile-libbz2_so %{?_smp_mflags}
make %{?_smp_mflags}

%install
make install PREFIX=%{buildroot}/usr
install -m 755 bzip2 %{buildroot}/usr/bin/
install -m 755 bunzip2 %{buildroot}/usr/bin/
install -m 755 bzcat %{buildroot}/usr/bin/
install -m 755 bzmore %{buildroot}/usr/bin/
install -m 755 bzdiff %{buildroot}/usr/bin/
install -m 755 bzgrep %{buildroot}/usr/bin/
install -m 755 bzip2recover %{buildroot}/usr/bin/
install -m 644 bzip2.1 %{buildroot}/usr/share/man/man1/
install -m 644 bunzip2.1 %{buildroot}/usr/share/man/man1/
install -m 644 bzcat.1 %{buildroot}/usr/share/man/man1/
install -m 644 bzmore.1 %{buildroot}/usr/share/man/man1/
install -m 644 bzdiff.1 %{buildroot}/usr/share/man/man1/
install -m 644 bzgrep.1 %{buildroot}/usr/share/man/man1/
install -m 644 bzip2recover.1 %{buildroot}/usr/share/man/man1/

%files
%license LICENSE
%doc README
/usr/bin/bzip2
/usr/bin/bunzip2
/usr/bin/bzcat
/usr/bin/bzmore
/usr/bin/bzdiff
/usr/bin/bzgrep
/usr/bin/bzip2recover
/usr/lib/libbz2.so.*
/usr/share/man/man1/bzip2.1*
/usr/share/man/man1/bunzip2.1*
/usr/share/man/man1/bzcat.1*
/usr/share/man/man1/bzmore.1*
/usr/share/man/man1/bzdiff.1*
/usr/share/man/man1/bzgrep.1*
/usr/share/man/man1/bzip2recover.1*

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%changelog
* %{__date} Dan Carpenter <DanC403@gmail.com> - %{version}-1
- Initial RPM build of bzip2.
