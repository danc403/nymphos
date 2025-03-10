Name: nymphDesktop
Version: 1.0
Release: 1%{?dist}
Summary: Nymph Desktop Environment Meta-Package
License: GPLv3
BuildArch: noarch

# Dependencies
Requires: nymph-plank
Requires: nymph-menu
Requires: whitesur-theme
#Requires: caja
Requires: thunar
Requires: openbox
Requires: lightdm
# Add any other required packages here

%description
This meta-package installs the Nymph Desktop Environment, including Plank, custom pipe menus,
the WhiteSur theme, Caja, Thunar, Openbox and LightDM.

%install
# Example: Copy default Plank settings
# Replace /path/to/your/plank/settings with the actual path to your customized Plank settings file.
mkdir -p %{buildroot}%{_userconfigdir}/plank/dock1/
cp /path/to/your/plank/settings %{buildroot}%{_userconfigdir}/plank/dock1/settings

# Example: Copy default Openbox menu configuration
# Replace /path/to/your/openbox/menu.xml with the actual path to your custom Openbox menu file.
mkdir -p %{buildroot}%{_userconfigdir}/openbox/
cp /path/to/your/openbox/menu.xml %{buildroot}%{_userconfigdir}/openbox/menu.xml

# Example: Copy default tint2 configuration
# Replace /path/to/your/tint2/tint2rc with the actual path to your custom tint2 configuration file.
mkdir -p %{buildroot}%{_userconfigdir}/tint2/
cp /path/to/your/tint2/tint2rc %{buildroot}%{_userconfigdir}/tint2/tint2rc

# Example: Copy desktop files for launchers
# Replace /path/to/your/desktop/files with the actual path to your desktop files.
mkdir -p %{buildroot}%{_datadir}/applications/
cp /path/to/your/desktop/files/*.desktop %{buildroot}%{_datadir}/applications/

# Example: Set default LightDM theme
# Replace 'your-lightdm-theme' with the actual name of your LightDM theme.
# This assumes your LightDM theme is packaged and installed correctly.
# LightDM config files can vary, so consult your distro's LightDM documentation.
# echo "[Seat:*]" > %{buildroot}%{_sysconfdir}/lightdm/lightdm.conf.d/99-nymph.conf
# echo "greeter-session=lightdm-gtk-greeter" >> %{buildroot}%{_sysconfdir}/lightdm/lightdm.conf.d/99-nymph.conf
# echo "user-session=openbox" >> %{buildroot}%{_sysconfdir}/lightdm/lightdm.conf.d/99-nymph.conf
# echo "theme-name=your-lightdm-theme" >> %{buildroot}%{_sysconfdir}/lightdm/lightdm.conf.d/99-nymph.conf

# Add any other installation logic here.

%files
# List any files that are part of this meta-package itself.
# For example, if you include custom configuration files.
%{_userconfigdir}/plank/dock1/settings
%{_userconfigdir}/openbox/menu.xml
%{_userconfigdir}/tint2/tint2rc
%{_datadir}/applications/*.desktop
# If you are placing lightdm configuration files, list them here.
# %{_sysconfdir}/lightdm/lightdm.conf.d/99-nymph.conf

%changelog
* Mon Jan 01 2024 Your Name <your.email@example.com> - 1.0-1
- Initial release.
