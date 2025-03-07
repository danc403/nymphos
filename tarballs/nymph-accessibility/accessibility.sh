#!/bin/bash

# Enable general accessibility according to https://www.freedesktop.org/wiki/Accessibility/AT-SPI2/
export GTK_MODULES=gail:atk-bridge
export GNOME_ACCESSIBILITY=1
export QT_ACCESSIBILITY=1
export QT_LINUX_ACCESSIBILITY_ALWAYS_ON=1
