#!/usr/bin/env python3

import os
import shutil

INDEX = "assets/gtk/common-assets/assets.txt"
#notepad "assets/gtk/common-assets/assets.txt"

SINDEX = "assets/gtk/common-assets/sidebar-assets.txt"
WINDEX = "assets/gtk/windows-assets/assets.txt"
OUTPUT_FILE = "gtk.gresource.xml"


PROJECT_DIR = "my_theme"  # Replace with your project directory
LIGHT_DIR = os.path.join(PROJECT_DIR, "light")
DARK_DIR = os.path.join(PROJECT_DIR, "dark")
LIGHT_ICONS_DIR = os.path.join(LIGHT_DIR, "icons")
DARK_ICONS_DIR = os.path.join(DARK_DIR, "icons")

def copy_and_generate_themerc(index_file, dest_icons_dir, state="active"):
    """Copies PNG assets and generates themerc entries."""
    os.makedirs(dest_icons_dir, exist_ok=True)
    themerc_lines = []
    try:
        # Determine the base directory for PNG files
        base_dir = os.path.dirname(index_file)
        with open(index_file, "r") as index:
            for asset in index:
                asset = asset.strip()
                if asset:
                    png_path = os.path.join(base_dir, asset + ".png")
                    if os.path.exists(png_path):
                        dest_path = os.path.join(dest_icons_dir, asset + ".png")
                        shutil.copy(png_path, dest_path)

                        # Generate themerc entries
                        if "close" in asset:
                            themerc_lines.append(f"button.close.image.{state}: {os.path.relpath(dest_path, PROJECT_DIR)}")
                        if "maximize" in asset:
                            themerc_lines.append(f"button.maximize.image.{state}: {os.path.relpath(dest_path, PROJECT_DIR)}")
                        if "minimize" in asset:
                            themerc_lines.append(f"button.minimize.image.{state}: {os.path.relpath(dest_path, PROJECT_DIR)}")

    except FileNotFoundError:
        print(f"Index file '{index_file}' not found.")
    return themerc_lines

def copy_css(src_css, dest_dir):
    """Copies CSS files."""
    os.makedirs(dest_dir, exist_ok=True)
    dest_path = os.path.join(dest_dir, os.path.basename(src_css))
    shutil.copy(src_css, dest_path)

if __name__ == "__main__":
    light_themerc_lines = []
    dark_themerc_lines = []

    # Process light theme assets
    light_themerc_lines.extend(copy_and_generate_themerc(INDEX, LIGHT_ICONS_DIR))
    light_themerc_lines.extend(copy_and_generate_themerc(SINDEX, LIGHT_ICONS_DIR))
    light_themerc_lines.extend(copy_and_generate_themerc(WINDEX, LIGHT_ICONS_DIR))

    # Process dark theme assets
    dark_themerc_lines.extend(copy_and_generate_themerc(WINDEX.replace(".txt", "-dark.txt"), DARK_ICONS_DIR, "inactive"))

    # Copy CSS files
    copy_css("gtk.css", LIGHT_DIR)
    copy_css("gtk-dark.css", DARK_DIR)

    # Write themerc files
    with open(os.path.join(LIGHT_DIR, "themerc"), "w") as f:
        f.write("\n".join(light_themerc_lines))
    with open(os.path.join(DARK_DIR, "themerc"), "w") as f:
        f.write("\n".join(dark_themerc_lines))

    print(f"Theme files generated in {PROJECT_DIR}")
