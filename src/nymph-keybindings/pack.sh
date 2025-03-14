#!/bin/bash

# Define the archive name and version
ARCHIVE_NAME="nymph-keybindings-1.0.tar.xz"
VERSION="1.0"

# Check if the archive already exists and prompt to overwrite
if [ -f "$ARCHIVE_NAME" ]; then
    read -p "Warning: Archive '$ARCHIVE_NAME' already exists. Overwrite? (y/n): " choice
    case "$choice" in
        [yY]*) echo "Overwriting..."; rm "$ARCHIVE_NAME"; ;;
        [nN]*) echo "Exiting."; exit 1 ;;
        *) echo "Invalid input. Exiting."; exit 1 ;;
    esac
fi

# Create the tar.xz archive
tar -cJvf "$ARCHIVE_NAME" \
    nymph-keybindings.vala \
    nymph-keybindings.desktop \
    nymph-keybindings.spec \
    README.md \
    po/

# Check if the archive was created successfully
if [ $? -eq 0 ]; then
    echo "Archive '$ARCHIVE_NAME' created successfully."
else
    echo "Error: Failed to create archive '$ARCHIVE_NAME'."
    exit 1
fi
