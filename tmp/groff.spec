spec_content: %global debug_package %{nil}

Name:           groff
Version:        1.22.4
Release:        1%{?dist}
Summary:        GNU troff text formatting system - GPL

License:        GPLv3+
URL:            https://www.gnu.org/software/groff/

Source0:        %{name}-%{version}.tar.gz

BuildRequires:  zlib-devel
BuildRequires:  fontconfig-devel

Requires:       fontconfig
Requires:       ghostscript

%description
The GNU roff text formatting system.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# Remove precompiled nroff man pages, these are generated
# from the troff sources by make install.
rm -f %{buildroot}%{_mandir}/man1/nroff.1
rm -f %{buildroot}%{_mandir}/man7/groff.7

#Remove files not needed for the package.
rm -rf %{buildroot}%{_infodir}

%files
%{_bindir}/eqn
%{_bindir}/gdiffmk
%{_bindir}/grops
%{_bindir}/grotty
%{_bindir}/gtroff
%{_bindir}/pic
%{_bindir}/tbl
%{_bindir}/addftinfo
%{_bindir}/afmtodit
%{_bindir}/grodvi
%{_bindir}/groff
%{_bindir}/hpftodit
%{_bindir}/indxbib
%{_bindir}/lkbib
%{_bindir}/lookbib
%{_bindir}/mmroff
%{_bindir}/neqn
%{_bindir}/nroff
%{_bindir}/pic2graph
%{_bindir}/roffbib
%{_bindir}/sortbib
%{_bindir}/tfmtodit
%{_mandir}/man1/eqn.1*
%{_mandir}/man1/gdiffmk.1*
%{_mandir}/man1/grops.1*
%{_mandir}/man1/grotty.1*
%{_mandir}/man1/gtroff.1*
%{_mandir}/man1/pic.1*
%{_mandir}/man1/tbl.1*
%{_mandir}/man1/addftinfo.1*
%{_mandir}/man1/afmtodit.1*
%{_mandir}/man1/grodvi.1*
%{_mandir}/man1/groff.1*
%{_mandir}/man1/hpftodit.1*
%{_mandir}/man1/indxbib.1*
%{_mandir}/man1/lkbib.1*
%{_mandir}/man1/lookbib.1*
%{_mandir}/man1/mmroff.1*
%{_mandir}/man1/neqn.1*
%{_mandir}/man1/pic2graph.1*
%{_mandir}/man1/roffbib.1*
%{_mandir}/man1/sortbib.1*
%{_mandir}/man1/tfmtodit.1*
%{_mandir}/man5/groff_font.5*
%{_mandir}/man5/groff.5*
%{_mandir}/man7/groff.7*
%{_mandir}/man7/groff_tmac.7*
%{_datadir}/groff
%{_datadir}/misc/term.tcap
%{_libdir}/groff
%doc AUTHORS NEWS README THANKS
%license COPYING

%changelog
* %{date} Dan Carpenter DanC403@gmail.com - 1.22.4-1
- Initial package build.

package_name: groff
