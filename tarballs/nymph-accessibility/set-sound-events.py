#!/usr/bin/env python3

import subprocess

def set_sound_events(dconf_file):
    """
    Sets sound events using dconf.

    Args:
        dconf_file (str): The path to the dconf file.
    """
    try:
        subprocess.run(["dconf", "load", "/", dconf_file], check=True)
        print(f"Sound events set from {dconf_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error setting sound events: {e}")

if __name__ == "__main__":
    dconf_file = "/etc/nymph/sound_events.dconf"
    set_sound_events(dconf_file)
