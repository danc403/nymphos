#!/usr/bin/env python3

import os

INDEX = "assets/gtk/common-assets/assets.txt"
SINDEX = "assets/gtk/common-assets/sidebar-assets.txt"
WINDEX = "assets/gtk/windows-assets/assets.txt"
OUTPUT_FILE = "gtk.gresource.xml"

def generate_gresource_xml():
    """Generates gtk.gresource.xml."""

    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)

    with open(OUTPUT_FILE, "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write("<gresources>\n")
        f.write('  <gresource prefix="/org/gnome/theme">\n')

        def add_assets(index_file, asset_path):
            """Adds assets from an index file."""
            try:
                with open(index_file, "r") as index:
                    for asset in index:
                        asset = asset.strip()
                        if asset:
                            f.write(f"    <file>{asset_path}/{asset}.png</file>\n")
                            f.write(f"    <file>{asset_path}/{asset}@2.png</file>\n")
                            if asset_path == "windows-assets":
                                f.write(f"    <file>{asset_path}/{asset}-dark.png</file>\n")
                                f.write(f"    <file>{asset_path}/{asset}-dark@2.png</file>\n")
            except FileNotFoundError:
                print(f"Index file '{index_file}' not found.")

        add_assets(INDEX, "assets/gtk/common-assets")
        add_assets(SINDEX, "assets/gtk/common-assets")
        add_assets(WINDEX, "assets/gtk/windows-assets")

        svg_files = [
            "assets/scalable/checkbox-checked-symbolic.svg",
            "assets/scalable/checkbox-checked-big-symbolic.svg",
            "assets/scalable/checkbox-mixed-symbolic.svg",
            "assets/scalable/radio-checked-symbolic.svg",
            "assets/scalable/combobox-arrow-symbolic.svg",
            "assets/scalable/checkbox-checked-symbolic@2.svg",
            "assets/scalable/checkbox-mixed-symbolic@2.svg",
            "assets/scalable/radio-checked-symbolic@2.svg",
            "assets/scalable/combobox-arrow-symbolic@2.svg",
        ]

        for svg in svg_files:
            f.write(f"    <file>{svg}</file>\n")

        f.write('    <file alias="assets/scalable/radio-mixed-symbolic.svg">assets/scalable/checkbox-mixed-symbolic.svg</file>\n')
        f.write('    <file alias="assets/scalable/radio-mixed-symbolic@2.svg">assets/scalable/checkbox-mixed-symbolic@2.svg</file>\n')

        f.write("    <file>gtk.css</file>\n")
        f.write("    <file>gtk-dark.css</file>\n")

        f.write("  </gresource>\n")
        f.write("</gresources>\n")

if __name__ == "__main__":
    generate_gresource_xml()
    print(f"Generated {OUTPUT_FILE}")
