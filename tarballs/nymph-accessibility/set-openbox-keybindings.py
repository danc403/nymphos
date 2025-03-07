#!/usr/bin/env python3

import os
import xml.etree.ElementTree as ET

# Define the keybindings in a dictionary for easy editing and understanding.
keybindings = {
    "A-F4": "<action name=\"Close\"/>",  # Alt + F4: Close the current window.
    "S-A-F1": "<action name=\"SendToDesktop\"><to>1</to></action>",  # Shift + Alt + F1: Move window to desktop 1.
    "S-A-F2": "<action name=\"SendToDesktop\"><to>2</to></action>",  # Shift + Alt + F2: Move window to desktop 2.
    "S-A-F3": "<action name=\"SendToDesktop\"><to>3</to></action>",  # Shift + Alt + F3: Move window to desktop 3.
    "S-A-F4": "<action name=\"SendToDesktop\"><to>4</to></action>",  # Shift + Alt + F4: Move window to desktop 4.
    "C-S-A-Down": "<action name=\"SendToDesktop\"><to>down</to></action>",  # Ctrl + Shift + Alt + Down: Move window to the desktop below.
    "C-S-A-Up": "<action name=\"SendToDesktop\"><to>up</to></action>",  # Ctrl + Shift + Alt + Up: Move window to the desktop above.
    "C-A-Down": "<action name=\"Desktop\"><to>down</to></action>",  # Ctrl + Alt + Down: Switch to the desktop below.
    "C-A-Up": "<action name=\"Desktop\"><to>up</to></action>",  # Ctrl + Alt + Up: Switch to the desktop above.
    "W-d": "<action name=\"ShowDesktop\"/>",  # Super + d: Show the desktop.
    "A-Tab": "<action name=\"NextWindow\"/>",  # Alt + Tab: Switch to the next window.
    "W-Tab": "<action name=\"NextWindow\"><group>yes</group></action>",  # Super + Tab: Switch to the next window in the same application group.
    "A-Above_Tab": "<action name=\"PreviousWindow\"><group>yes</group></action>",  # Alt + Above Tab: Switch to the previous window in the same application group.
    "W-Left": "<action name=\"SendToDesktop\"><to>left</to></action>", # Super + Left: move window to left workspace.
    "W-Right": "<action name=\"SendToDesktop\"><to>right</to></action>", # Super + Right: move window to right workspace.
    "C-A-Left": "<action name=\"Desktop\"><to>left</to></action>", # Ctrl + Alt + Left: move to left workspace.
    "C-A-Right": "<action name=\"Desktop\"><to>right</to></action>", # Ctrl + Alt + Right: move to right workspace.
    "W-Home": "<action name=\"Execute\"><command>caja .</command></action>", # Super + Home: open caja in home directory
    "A-W-f": "<action name=\"Execute\"><command>firefox</command></action>", # Alt + Super + f: launch firefox
    "C-A-t": "<action name=\"Execute\"><command>mate-terminal</command></action>", # Ctrl + Alt + t: launch terminal
    "A-W-Up": "<action name=\"Execute\"><command>wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%+ && play /usr/share/sounds/freedesktop/stereo/audio-volume-change.oga</command></action>", # Alt + Super + Up: volume up.
    "A-W-Down": "<action name=\"Execute\"><command>wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%- && play /usr/share/sounds/freedesktop/stereo/audio-volume-change.oga</command></action>", # Alt + Super + Down: volume down.
    "A-W-Left": "<action name=\"Execute\"><command>wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle && play /usr/share/sounds/freedesktop/stereo/audio-volume-change.oga</command></action>", # Alt + Super + Left: toggle mute.
    "A-W-o": "<action name=\"Execute\"><command>orca -r</command></action>", # Alt + Super + o: restart orca.
    "A-W-s": "<action name=\"Execute\"><command>orca</command></action>", # Alt + Super + s: start orca.
}

rc_xml_path = "/etc/skel/.config/openbox/rc.xml"

# Check if rc.xml exists
if os.path.exists(rc_xml_path):
    try:
        tree = ET.parse(rc_xml_path)
        root = tree.getroot()
        keyboard = root.find("keyboard")

        # Add keybindings
        for key, action in keybindings.items():
            keybind = ET.SubElement(keyboard, "keybind")
            keybind.set("key", key)
            ET.fromstring(action).tail = "\n"  # Add newline for readability
            keybind.append(ET.fromstring(action))

        tree.write(rc_xml_path)

    except ET.ParseError:
        print(f"Error parsing {rc_xml_path}. Creating a new file.")
        # Create a new rc.xml if parsing fails.
        create_new_rc_xml()

else:
    # Create a new rc.xml if it doesn't exist.
    create_new_rc_xml()

def create_new_rc_xml():
    """Creates a new rc.xml file with the keybindings."""
    os.makedirs(os.path.dirname(rc_xml_path), exist_ok=True)
    root = ET.Element("openbox_config")
    root.set("xmlns", "http://openbox.org/")
    root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
    root.set("xsi:schemaLocation", "http://openbox.org/ file:///usr/share/openbox/openbox-3.4.xsd")
    keyboard = ET.SubElement(root, "keyboard")

    for key, action in keybindings.items():
        keybind = ET.SubElement(keyboard, "keybind")
        keybind.set("key", key)
        ET.fromstring(action).tail = "\n"  # Add newline for readability
        keybind.append(ET.fromstring(action))

    tree = ET.ElementTree(root)
    tree.write(rc_xml_path)
