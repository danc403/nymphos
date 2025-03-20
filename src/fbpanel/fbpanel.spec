Name:           fbpanel
Version:        6.1
Release:        2%{?dist}  # Increment release because we're adding functionality
Summary:        A lightweight GTK+ panel for X11 environments.

License:        GPLv2+
URL:            http://fbpanel.sourceforge.net/  # Or the actual sourceforge URL
Source0:        fbpanel-6.1.tbz2
Source1:        fbpanel.openrc  # Our OpenRC init script (see below)

BuildRequires:  gtk2-devel
BuildRequires:  libwnck-devel  # For window manager support (often used)
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
#Add any other build requirments here based on compile failures.

#Requires:      #Dependencies will be auto-populated by rpmbuild

#Provides:       #Optional: If fbpanel provides a certain capability, declare it here

%description
fbpanel is a lightweight GTK+ panel. It's commonly used with window managers
like Openbox, Fluxbox, etc.  It can display launchers, tasklists,
systray icons, and other widgets.  This build is optimized for use within an
Openbox/OpenRC environment and is targeted towards blind and low vision users.

%package        devel
Summary:        Development files for fbpanel.
Requires:       %{name} = %{version}-%{release}

%description    devel
This package contains the header files and other resources needed to
develop applications that use fbpanel.

%prep
%setup -q #No extraction required since .tbz2 is a tarballe.
#%autosetup -n fbpanel-6.1 -q #If you needed to rename or work in a new directory.

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# Remove unneeded files (e.g., docs if not needed)
#rm -rf %{buildroot}/usr/share/doc/%{name}

# Install the OpenRC init script
install -D -m 0755 %{SOURCE1} %{buildroot}/etc/init.d/fbpanel

# Create the devel directory structure
mkdir -p %{buildroot}%{_includedir}
cp fbpanel.h %{buildroot}%{_includedir}

%files
%license COPYING  #Or LICENCE or whatever the licencing file is named.
%{_bindir}/fbpanel
%{_datadir}/applications/fbpanel.desktop
%{_datadir}/pixmaps/fbpanel.png
%{_datadir}/fbpanel/
%{_mandir}/man1/fbpanel.1*
/etc/init.d/fbpanel   # Add the init script to the list of files to include

%files devel
%{_includedir}/fbpanel.h

%changelog
* Mon Oct 23 2023 Your Name <your.email@example.com> - 6.1-2
- Added OpenRC init script for system startup.

* Mon Oct 23 2023 Your Name <your.email@example.com> - 6.1-1
- Initial package build for Openbox/OpenRC and blind/low vision focus.

#    rpmbuild -ba fbpanel.spec
#    This will create both the RPM and SRPM in the `RPMS` and `SRPMS` subdirectories of your `rpmbuild` directory (usually `$HOME/rpmbuild`).
