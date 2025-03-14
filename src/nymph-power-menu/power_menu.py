#!/usr/bin/env python3

import subprocess
import os

def show_menu():
    print("""
<openbox_pipe_menu>
  <item label="Log Out">
    <action name="Execute">
      <command>openbox --exit</command>
    </action>
  </item>
  <item label="Shut Down">
    <action name="Execute">
      <command>sudo shutdown -P now</command>
    </action>
  </item>
  <item label="Reboot">
    <action name="Execute">
      <command>sudo reboot</command>
    </action>
  </item>
</openbox_pipe_menu>
""")

if __name__ == "__main__":
    show_menu()
