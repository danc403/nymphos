Name:           nymph-boot-config
Version:        1.0  # Update with your actual version
Release:        1%{?dist}
Summary:        Nymph Boot Configuration Tool

License:        GPLv3+  # Or the actual license
URL:            https://example.com/nymph-bootconfig # Replace with the actual URL if available.  If not available, remove this line.

Source0:        %{name}-%{version}.tar.zz # Assume you're creating a tarball of the source code.  If not, change this.
Source1:        %{name}.desktop

BuildRequires:  gtk-sharp2
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk-sharp-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(efibootmgr)  # Assuming efibootmgr is a pkgconfig package. If not, find the correct Provides.
Requires:       gtk-sharp2
Requires:       efibootmgr  # Assuming efibootmgr is in base or similar

%description
Nymph Boot Configuration is a tool to manage and configure your boot entries,
supporting legacy, EFI, Windows, macOS, and Linux boot options.

%prep
%autosetup -p1 # Adjust p value if needed (number of directory levels to strip)

%build
mcs -target:exe -out:%{name} \
    -reference:/usr/lib/mono/gtk-sharp2/gtk-sharp.dll \
    -reference:/usr/lib/mono/gdk-sharp2/gdk-sharp.dll \
    -reference:/usr/lib/mono/glib-sharp2/glib-sharp.dll \
    -reference:/usr/lib/mono/pango-sharp2/pango-sharp.dll \
    -reference:/usr/lib/mono/atk-sharp2/atk-sharp.dll \
    MainWindow.cs BootData.cs DetailsPanel.cs # List all .cs files in your project

%install
install -Dm 755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dm 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

# Assuming icon goes in the hicolor theme
install -Dm 644 %{SOURCE1:r}.png %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.png # Add this line if you have an icon. Adjust path/size as needed.  Use a scalable SVG icon when possible.

# Create directory for revert script
mkdir -p %{buildroot}/usr/local/bin

# Create dummy revert script (this needs to be populated correctly if you have a working version)
echo '#!/bin/sh' > %{buildroot}/usr/local/bin/revert_boot.sh
chmod 755 %{buildroot}/usr/local/bin/revert_boot.sh


%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.png # Only include this if you have an icon
/usr/local/bin/revert_boot.sh  # Include revert script

%changelog
* Tue Oct 24 2023 Your Name <your.email@example.com> - 0.1.0-1
- Initial package.
