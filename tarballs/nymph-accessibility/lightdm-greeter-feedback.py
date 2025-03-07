#!/usr/bin/env python3

import subprocess
import os
import threading
import time

def announce_login_prompt():
    """Announces the login prompt."""
    subprocess.run(["spd-say", "Nymph OS Login. Please enter your username and password."], check=True)

def announce_character(character):
    """Announces a character."""
    subprocess.run(["spd-say", character], check=True)

def monitor_key_presses():
    """Monitors key presses using xev and announces characters."""
    try:
        xev_process = subprocess.Popen(["xev", "-event", "keyboard"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        while True:
            line = xev_process.stdout.readline()
            if "state" in line and "keycode" in line:
                keycode_line = line.strip()
                keycode = keycode_line.split("keycode ")[1].split(",")[0]
                try:
                    xkb_result = subprocess.run(["xkbcat", "-keycode", keycode], capture_output=True, text=True, check=True)
                    key_symbol = xkb_result.stdout.strip()
                    if key_symbol:
                        # Character echo (printed character).
                        if is_input_focused():
                            try:
                                result = subprocess.run(["xdotool", "getwindowfocus", "getwindowname"], capture_output=True, text=True, check=True)
                                window_id = result.stdout.strip()
                                result = subprocess.run(["xdotool", "getwindowfocus", "getwindowpid"], capture_output=True, text=True, check=True)

                                result = subprocess.run(["xdotool", "getwindowfocus", "getwindowname"], capture_output=True, text=True, check=True)
                                window_name = result.stdout.strip()

                                result = subprocess.run(["xdotool", "getwindowfocus", "getwindowtype"], capture_output=True, text=True, check=True)
                                window_type = result.stdout.strip()

                                result = subprocess.run(["xdotool", "getwindowfocus", "getwindowgeometry"], capture_output=True, text=True, check=True)
                                window_geometry = result.stdout.strip()
                                # attempt to get the printed character.
                                result = subprocess.run(["xdotool", "getwindowfocus", "getwindowpid", "type", key_symbol, "getactivewindow"], capture_output=True, text=True, check=True)
                                printed_character = result.stdout.strip()
                                announce_character(printed_character)
                            except (subprocess.CalledProcessError, IndexError):
                                pass
                        if is_screen_locked():
                            announce_screen_locked()

                except (subprocess.CalledProcessError, IndexError):
                    pass
    except FileNotFoundError:
        print("Error: xev or xkbcat not found. Key press monitoring disabled.")

def get_focused_window_title():
    """Gets the title of the focused window."""
    try:
        result = subprocess.run(["xprop", "-root", "_NET_ACTIVE_WINDOW"], capture_output=True, text=True, check=True)
        window_id = result.stdout.split("window id # ")[1].strip()
        result = subprocess.run(["xprop", "-id", window_id, "WM_NAME"], capture_output=True, text=True, check=True)
        title = result.stdout.split('"')[1]
        return title
    except (subprocess.CalledProcessError, IndexError):
        return None

def announce_focused_element():
    """Announces the focused element."""
    title = get_focused_window_title()
    if title:
        if is_input_focused():
            content = get_input_content()
            subprocess.run(["spd-say", f"{title} input {content}"], check=True)
        else:
            subprocess.run(["spd-say", f"Focused element: {title}"], check=True)

def is_input_focused():
    """Checks if an input element is focused."""
    try:
        result = subprocess.run(["xdotool", "getwindowfocus", "getwindowname"], capture_output=True, text=True, check=True)
        return "input" in result.stdout.lower() or "password" in result.stdout.lower()
    except (subprocess.CalledProcessError, IndexError):
        return False

def get_input_content():
    """Gets the content of the focused input element."""
    try:
        result = subprocess.run(["xdotool", "getwindowfocus", "getwindowname", "getwindowpid", "getwindowgeometry", "getwindowname", "getwindowtype", "getwindowgeometry", "getwindowname", "getwindowpid", "getwindowgeometry", "getwindowname", "getwindowpid", "getwindowgeometry", "getwindowname", "getwindowpid", "getwindowgeometry", "getwindowname", "getwindowpid", "getwindowgeometry", "getwindowname", "getwindowpid", "getwindowgeometry", "getwindowname", "getwindowpid", "getwindowgeometry", "getwindowname", "getwindowpid", "getwindowgeometry", "getwindowname", "getwindowpid", "getwindowgeometry", "getwindowname", "getwindowpid", "getwindowgeometry", "getwindowname", "getwindowpid", "getwindowgeometry", "getwindowname", "getwindowpid", "getwindowgeometry", "getwindowname", "getwindowpid", "getwindowgeometry", "getwindowname", "getwindowpid", "getwindowgeometry", "getwindowname", "getwindowpid", "getwindowgeometry", "getwindowname", "getwindowpid", "getwindowgeometry", "getwindowname", "getwindowpid", "getwindowgeometry", "getwindowname", "getwindowpid", "getwindowgeometry", "getwindowname", "getwindowpid", "getwindowgeometry", "getwindowname", "getwindowpid", "getwindowgeometry", "getwindowname", "getwindowpid", "getwindowgeometry", "getwindowname", "getwindowpid", "getwindowgeometry", "getwindowname", "getwindowpid", "getwindowgeometry"], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except (subprocess.CalledProcessError, IndexError):
        return ""

def is_screen_locked():
    """Checks if the screen is locked."""
    try:
        subprocess.run(["xscreensaver-command", "-time"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return False
    except subprocess.CalledProcessError:
        return True

def announce_screen_locked():
    """Announces that the screen is locked."""
    subprocess.run(["spd-say", "Screen locked."], check=True)

def run_greeter_feedback():
    """Runs the greeter feedback."""
    announce_login_prompt()

    # Key press monitoring thread.
    key_press_thread = threading.Thread(target=monitor_key_presses)
    key_press_thread.daemon = True
    key_press_thread.start()

    # Element focus monitoring loop.
    last_focused_title = None
    while True:
        current_focused_title = get_focused_window_title()
        if current_focused_title != last_focused_title:
            announce_focused_element()
            last_focused_title = current_focused_title
        if is_screen_locked():
            if last_locked == False:
                announce_screen_locked()
            last_locked = True;
        else:
            last_locked = False;
        time.sleep(1)

if __name__ == "__main__":
    last_locked = False;
    run_greeter_feedback()
