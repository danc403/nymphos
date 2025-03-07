#!/bin/bash

# Set high-contrast theme for GTK3
mkdir -p /etc/skel/.config/gtk-3.0/
cat <<EOF > /etc/skel/.config/gtk-3.0/settings.ini
[Settings]
gtk-theme-name=HighContrast
EOF

# Set high-contrast theme for GTK4
mkdir -p /etc/skel/.config/gtk-4.0/
cat <<EOF > /etc/skel/.config/gtk-4.0/settings.ini
[Settings]
gtk-theme-name=HighContrast
EOF
