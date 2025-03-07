#!/usr/bin/env python3

import os

def set_gtk_font(font_name, font_size, output_path_gtk3, output_path_gtk4):
    """
    Sets the default font for GTK 3 and GTK 4.

    Args:
        font_name (str): The name of the font.
        font_size (int): The size of the font.
        output_path_gtk3 (str): The path to the GTK 3 settings.ini file.
        output_path_gtk4 (str): The path to the GTK 4 settings.ini file.
    """

    font_setting = f"{font_name} {font_size}"

    gtk3_content = f"""
[Settings]
gtk-font-name={font_setting}
"""

    gtk4_content = f"""
[Settings]
gtk-font-name={font_setting}
"""

    # Create the GTK 3 directory if it doesn't exist.
    os.makedirs(os.path.dirname(output_path_gtk3), exist_ok=True)

    # Create the GTK 4 directory if it doesn't exist.
    os.makedirs(os.path.dirname(output_path_gtk4), exist_ok=True)

    try:
        with open(output_path_gtk3, 'w') as f:
            f.write(gtk3_content)
        print(f"GTK 3 settings.ini file created at {output_path_gtk3}")
    except Exception as e:
        print(f"Error creating GTK 3 settings.ini: {e}")

    try:
        with open(output_path_gtk4, 'w') as f:
            f.write(gtk4_content)
        print(f"GTK 4 settings.ini file created at {output_path_gtk4}")
    except Exception as e:
        print(f"Error creating GTK 4 settings.ini: {e}")

if __name__ == "__main__":
    font_name = "Luciole"
    font_size = 14
    output_path_gtk3 = "/etc/skel/.config/gtk-3.0/settings.ini"
    output_path_gtk4 = "/etc/skel/.config/gtk-4.0/settings.ini"
    set_gtk_font(font_name, font_size, output_path_gtk3, output_path_gtk4)
