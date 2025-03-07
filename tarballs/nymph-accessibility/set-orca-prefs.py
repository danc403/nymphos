#!/usr/bin/env python3

import os
import locale

def is_laptop():
    """
    Determines if the system is a laptop based on the presence of battery information.

    Returns:
        bool: True if it's a laptop, False otherwise.
    """
    return os.path.exists("/sys/class/power_supply/BAT0") or os.path.exists("/sys/class/power_supply/battery")

def create_orca_prefs(output_path):
    """
    Creates an orca.prefs file with default settings for a new user,
    including locale-based voice selection, modifier key based on system type, and punctuation level.

    Args:
        output_path (str): The path where the orca.prefs file should be created.
    """

    # Get the user's locale.
    user_locale, encoding = locale.getdefaultlocale()

    # Determine the voice based on the locale.
    voice = "en"  # Default to English if locale detection fails or no matching voice.
    if user_locale:
        lang_code = user_locale.split("_")[0]  # Get the language code (e.g., "en", "fr", "es").
        # Add logic here to map language codes to available Orca voices.
        # Example:
        if lang_code == "fr":
            voice = "fr"
        elif lang_code == "es":
            voice = "es"
        # Add more language mappings as needed.

    # Determine the modifier key based on system type.
    modifier_key = "Insert"  # Default to Insert for desktops.
    if is_laptop():
        modifier_key = "Caps_Lock"  # Use Caps Lock for laptops.

    # Set the punctuation level.
    punctuation_level = 2  # Level 2: Some punctuation.

    prefs_content = f"""
[general]
speech_enabled=true  # Enables speech output.
braille_enabled=false # Disables braille output (can be enabled later).
enable_sounds=true    # Enables sound feedback.

[speech]
voice={voice}             # Sets the default voice based on locale.
rate=180             # Sets the speech rate to 180 words per minute.
volume=50            # Sets the speech volume to 50%.
punctuation_level={punctuation_level} # Sets the punctuation level (0: None, 1: Some, 2: Most, 3: All).

[keyboard]
modifier_key={modifier_key} # Sets the modifier key for Orca commands.

[verbosity]
process_events=2    # Sets the verbosity level for process events.
"""

    # Create the directory if it doesn't exist.
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    try:
        with open(output_path, 'w') as f:
            f.write(prefs_content)
        print(f"orca.prefs file created at {output_path}")
    except Exception as e:
        print(f"Error creating orca.prefs: {e}")

if __name__ == "__main__":
    output_path = "/etc/skel/.config/orca/orca.prefs"
    create_orca_prefs(output_path)
