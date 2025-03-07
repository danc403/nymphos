Name:           nymph-accessibility
Version:        1.0
Release:        1%{?dist}
Summary:        Accessibility settings for Nymph OS

License:        GPL-2.0-or-later
Source0:        accessibility.sh
Source1:        orca-login-wrapper
Source2:        orca.desktop
Source3:        bashrc
Source4:        bash_profile
Source5:        profile
Source6:        set-high-contrast-theme.sh
Source7:        set-openbox-keybindings.py
Source8:        set-orca-prefs.py
Source9:        set-font.py
Source10:       sound_events.dconf
Source11:       set-sound-events.py
Source12:       spoken_feedback.py
Source13:       spoken-feedback
Source14:       lightdm-greeter-feedback.py

Requires:       speech-dispatcher
Requires:       orca
Requires:       gtk-high-contrast-theme
Requires:       python3
Requires:       dconf
Requires:       wmctrl
Requires:       python3-dbus
Requires:       python3-gobject
Requires:       x11-utils
Requires:       xkb-utils
Requires:       xscreensaver
Requires:       xdotool

%description
This package provides essential accessibility settings for the Nymph OS,
including environment variables, Speech Dispatcher configuration,
Orca integration, default bash configuration, high-contrast theme settings,
Openbox keybindings, Orca preferences, font settings, sound events, spoken feedback,
and LightDM greeter feedback.

%install
install -Dm644 %{SOURCE0} %{buildroot}/etc/profile.d/accessibility.sh
install -Dm755 %{SOURCE1} %{buildroot}/usr/local/bin/orca-login-wrapper
install -Dm644 %{SOURCE2} %{buildroot}/etc/skel/.config/autostart/orca.desktop
install -Dm644 %{SOURCE3} %{buildroot}/etc/skel/.bashrc
install -Dm644 %{SOURCE4} %{buildroot}/etc/skel/.bash_profile
install -Dm644 %{SOURCE5} %{buildroot}/etc/skel/.profile
install -Dm755 %{SOURCE6} %{buildroot}/usr/local/bin/set-high-contrast-theme.sh
install -Dm755 %{SOURCE7} %{buildroot}/usr/local/bin/set-openbox-keybindings.py
install -Dm755 %{SOURCE8} %{buildroot}/usr/local/bin/set-orca-prefs.py
install -Dm755 %{SOURCE9} %{buildroot}/usr/local/bin/set-font.py
install -Dm644 %{SOURCE10} %{buildroot}/etc/nymph/sound_events.dconf
install -Dm755 %{SOURCE11} %{buildroot}/usr/local/bin/set-sound-events.py
install -Dm755 %{SOURCE12} %{buildroot}/usr/local/bin/spoken_feedback.py
install -Dm755 %{SOURCE13} %{buildroot}/etc/init.d/spoken-feedback
install -Dm755 %{SOURCE14} %{buildroot}/usr/local/bin/lightdm-greeter-feedback.py

%files
/etc/profile.d/accessibility.sh
/usr/local/bin/orca-login-wrapper
/etc/skel/.config/autostart/orca.desktop
/etc/speech-dispatcher/speechd.conf
/etc/skel/.bashrc
/etc/skel/.bash_profile
/etc/skel/.profile
/usr/local/bin/set-high-contrast-theme.sh
/usr/local/bin/set-openbox-keybindings.py
/usr/local/bin/set-orca-prefs.py
/usr/local/bin/set-font.py
/etc/nymph/sound_events.dconf
/usr/local/bin/set-sound-events.py
/usr/local/bin/spoken_feedback.py
/etc/init.d/spoken-feedback
/usr/local/bin/lightdm-greeter-feedback.py

%post
# Configure speech dispatcher using sed
sed -i '/^#AddModule "espeak-ng" "espeak-ng.conf"/s/^#//' /etc/speech-dispatcher/speechd.conf
# Set high-contrast theme
/usr/local/bin/set-high-contrast-theme.sh
# Set Openbox keybindings
/usr/local/bin/set-openbox-keybindings.py
# Set Orca preferences
/usr/local/bin/set-orca-prefs.py
# Set GTK Font
/usr/local/bin/set-font.py
# set sound events.
/usr/local/bin/set-sound-events.py
# Enable spoken feedback service
rc-update add spoken-feedback default
# Enable lightdm greeter feedback
if ! grep -q "greeter-setup-script=/usr/local/bin/lightdm-greeter-feedback.py" /etc/lightdm/lightdm.conf; then
  echo "[SeatDefaults]" >> /etc/lightdm/lightdm.conf
  echo "greeter-setup-script=/usr/local/bin/lightdm-greeter-feedback.py" >> /etc/lightdm/lightdm.conf
fi

%changelog
* %{date} Dan Carpenter <danc403@gmail.com> - 1.0-1
- Initial release of nymph-accessibility package.
- Configured speechd.conf with sed in %post.
- Added bash configuration files.
- Added high contrast theme settings.
- Added Openbox keybindings setup via Python script.
- Added Orca preferences setup via Python script.
- Added GTK Font settings setup via Python script.
- Added sound event setup.
- Added spoken feedback.
- Added OpenRC init script for spoken feedback.
- Added LightDM greeter feedback.
- Added xdotool to dependencies.
- Improved lightdm config update.
