#!/bin/bash

# Set variables
ARCHIVE_NAME="nymph-theme-switcher-1.0.tar.xz"

# Check if the archive already exists
if [ -f "$ARCHIVE_NAME" ]; then
    echo "Warning: Archive '$ARCHIVE_NAME' already exists. Overwriting."
fi

# Create the archive
tar -cJvf "$ARCHIVE_NAME" nymph_theme_switcher.vala nymph-theme-switcher.desktop po/ README.md

# Check if the archive was created successfully
if [ $? -eq 0 ]; then
    echo "Archive '$ARCHIVE_NAME' created successfully."
else
    echo "Error: Failed to create archive '$ARCHIVE_NAME'."
    exit 1
fi
