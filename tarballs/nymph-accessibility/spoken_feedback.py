#!/usr/bin/env python3

import subprocess
import time
import os
import dbus
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib

def get_current_desktop():
    """Gets the current desktop number."""
    try:
        result = subprocess.run(["wmctrl", "-d"], capture_output=True, text=True, check=True)
        lines = result.stdout.splitlines()
        for line in lines:
            if "*" in line:
                return line.split()[0]
    except subprocess.CalledProcessError:
        return None

def announce_desktop():
    """Announces the current desktop number."""
    desktop = get_current_desktop()
    if desktop:
        subprocess.run(["spd-say", f"Desktop {desktop}"], check=True)

def announce_window_focus(window_id):
    """Announces the window title when a window gains focus."""
    try:
        result = subprocess.run(["xprop", "-id", window_id, "WM_NAME"], capture_output=True, text=True, check=True)
        title = result.stdout.split('"')[1]
        subprocess.run(["spd-say", f"Window {title} focused"], check=True)
    except (subprocess.CalledProcessError, IndexError):
        pass

def announce_notification(summary, body):
    """Announces the notification content."""
    subprocess.run(["spd-say", f"Notification: {summary}. {body}"], check=True)

def announce_error(message):
    """Announces an error message."""
    subprocess.run(["spd-say", f"Error: {message}"], check=True)

def announce_system_status():
    """Announces system status (battery level, network connection)."""
    # Add logic to get battery level and network connection status.
    # Example (battery level):
    if os.path.exists("/sys/class/power_supply/BAT0/capacity"):
        with open("/sys/class/power_supply/BAT0/capacity", "r") as f:
            battery_level = f.read().strip()
            subprocess.run(["spd-say", f"Battery level: {battery_level} percent"], check=True)

def announce_application_launch(app_name):
    """Announces the application launch."""
    subprocess.run(["spd-say", f"Application launched: {app_name}"], check=True)

def handle_active_window_changed(window_id):
    """Handles active window changes."""
    announce_window_focus(window_id)

def handle_notification(summary, body):
    """Handles notifications."""
    announce_notification(summary, body)

def handle_desktop_switch():
    """Handles desktop switches."""
    announce_desktop()

def run_feedback_loop():
    """Runs the feedback loop."""
    DBusGMainLoop(set_as_default=True)
    bus = dbus.SessionBus()

    # Window focus monitoring.
    try:
        bus.add_signal_receiver(
            handle_active_window_changed,
            signal_name="ActiveWindowChanged",
            dbus_interface="org.freedesktop.WindowManager",
            bus_name="org.freedesktop.WindowManager",
        )
    except dbus.exceptions.DBusException:
        print("Warning: Window focus monitoring not available.")

    # Notification monitoring.
    try:
        bus.add_signal_receiver(
            handle_notification,
            signal_name="Notify",
            dbus_interface="org.freedesktop.Notifications",
            bus_name="org.freedesktop.Notifications",
        )
    except dbus.exceptions.DBusException:
        print("Warning: Notification monitoring not available.")

    # Desktop switch monitoring.
    GLib.timeout_add_seconds(1, handle_desktop_switch) #simple polling method.

    loop = GLib.MainLoop()
    loop.run()

if __name__ == "__main__":
    run_feedback_loop()
