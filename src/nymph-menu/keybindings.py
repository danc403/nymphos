#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import os
import subprocess
import xml.etree.ElementTree as ET

class KeybindingEditor:
    def __init__(self):
        self.window = Gtk.Window()
        self.window.set_title("Openbox Keybinding Editor")
        self.window.connect("destroy", Gtk.main_quit)

        self.grid = Gtk.Grid()
        self.window.add(self.grid)

        self.user_button = Gtk.Button(label="User Keybindings")
        self.user_button.set_accessible_name("User keybindings")
        self.system_button = Gtk.Button(label="System Keybindings")
        self.system_button.set_accessible_name("System keybindings")
        self.grid.attach(self.user_button, 0, 0, 1, 1)
        self.grid.attach(self.system_button, 1, 0, 1, 1)

        self.treeview = Gtk.TreeView()
        self.grid.attach(self.treeview, 0, 1, 2, 1)

        self.restore_button = Gtk.Button(label="Restore User Keybindings from System Defaults")
        self.restore_button.set_accessible_name("Restore user keybindings from system defaults")
        self.grid.attach(self.restore_button, 0, 2, 2, 1)

        self.save_button = Gtk.Button(label="Save")
        self.save_button.set_accessible_name("Save keybindings")
        self.grid.attach(self.save_button, 0, 3, 2, 1)

        self.add_button = Gtk.Button(label="Add Keybinding")
        self.add_button.set_accessible_name("Add keybinding")
        self.remove_button = Gtk.Button(label="Remove Keybinding")
        self.remove_button.set_accessible_name("Remove keybinding")
        self.grid.attach(self.add_button, 0, 4, 1, 1)
        self.grid.attach(self.remove_button, 1, 4, 1, 1)

        self.status_label = Gtk.Label()
        self.grid.attach(self.status_label, 0, 5, 2, 1)

        self.user_button.connect("clicked", self.on_user_clicked)
        self.system_button.connect("clicked", self.on_system_clicked)
        self.restore_button.connect("clicked", self.on_restore_clicked)
        self.save_button.connect("clicked", self.on_save_clicked)
        self.add_button.connect("clicked", self.on_add_clicked)
        self.remove_button.connect("clicked", self.on_remove_clicked)

        self.window.show_all()
        self.rcfile_path = None
        self.used_keys = {} #Dictionary to hold used keys.
        self.liststore = Gtk.ListStore(str, str, str)  # Key, Action, Name
        self.treeview.set_model(self.liststore)
        self.setup_treeview_columns()

    def setup_treeview_columns(self):
        for column in self.treeview.get_columns():
            self.treeview.remove_column(column)
        for i, column_title in enumerate(["Key Combination", "Action", "Name"]):
            renderer = Gtk.CellRendererText()
            renderer.set_property("editable", True)
            renderer.connect("edited", self.on_cell_edited, i)
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            self.treeview.append_column(column)

    def on_user_clicked(self, widget):
        self.rcfile_path = os.path.expanduser("~/.config/openbox/rc.xml")
        self.load_keybindings()

    def on_system_clicked(self, widget):
        if os.geteuid() == 0:
            self.rcfile_path = "/etc/xdg/openbox/rc.xml"
            self.load_keybindings()
        else:
            self.show_error_dialog("Root permissions required.")

    def on_restore_clicked(self, widget):
        self.show_restore_dialog()

    def on_save_clicked(self, widget):
        self.save_keybindings()

    def load_keybindings(self):
        self.used_keys = {} #clear old used keys.
        self.liststore.clear()
        if not self.rcfile_path or not os.path.exists(self.rcfile_path):
            self.show_error_dialog("Keybindings file not found.")
            return

        try:
            tree = ET.parse(self.rcfile_path)
            root = tree.getroot()
            keyboard = root.find("keyboard")
            if keyboard is None:
                self.show_malformed_dialog("Keyboard section not found or malformed.", "keyboard")
                return

            keybindings = keyboard.findall(".//keybind")

            for keybind in keybindings:
                key_element = keybind.find("key")
                action_element = keybind.find("action")
                name_element = keybind.find("name")

                key = key_element.text if key_element is not None else ""
                action = action_element.find("*").tag if action_element is not None and action_element.find("*") is not None else ""
                name = name_element.text if name_element is not None else ""

                if key:
                    if key in self.used_keys:
                        self.show_status_message(f"Warning: Duplicate key found in config: {key}")
                    self.used_keys[key] = True

                self.liststore.append([key, action, name])

        except ET.ParseError as e:
            self.show_malformed_dialog(f"Error parsing XML: {e}", "parse")
        except FileNotFoundError as e:
            self.show_malformed_dialog(f"File not found: {e}", "file")
        except Exception as e:
            self.show_malformed_dialog(f"Unexpected error: {e}", "general")

    def save_keybindings(self):
        if not self.rcfile_path or not os.path.exists(self.rcfile_path):
            self.show_error_dialog("Keybindings file not found.")
            return

        try:
            tree = ET.parse(self.rcfile_path)
            root = tree.getroot()
            keyboard = root.find("keyboard")
            if keyboard is None:
                self.show_malformed_dialog("Keyboard section not found or malformed.", "keyboard")
                return

            keybindings = keyboard.findall(".//keybind")
            for keybind in keybindings[:]:
                keyboard.remove(keybind)

            for row in self.liststore:
                key_combination = row[0]
                action = row[1]
                name = row[2]

                if key_combination: #Only add if key combination is not empty.
                    keybind = ET.Element("keybind")
                    key_element = ET.Element("key")
                    key_element.text = key_combination
                    action_element = ET.Element("action")
                    action_sub_element = ET.Element(action)
                    name_element = ET.Element("name")
                    name_element.text = name

                    action_element.append(action_sub_element)
                    keybind.append(key_element)
                    keybind.append(action_element)
                    keybind.append(name_element)
                    keyboard.append(keybind)

            tree.write(self.rcfile_path)
            self.show_status_message("Keybindings saved successfully.")

        except ET.ParseError as e:
            self.show_malformed_dialog(f"Error parsing XML: {e}", "parse")
        except FileNotFoundError as e:
            self.show_malformed_dialog(f"File not found: {e}", "file")
        except Exception as e:
            self.show_malformed_dialog(f"Unexpected error: {e}", "general")

def restore_keybindings(self):
        user_rcfile_path = os.path.expanduser("~/.config/openbox/rc.xml")
        system_default_rcfile_path = "/etc/xdg/openbox/rc.xml.default"  # Or your system's default path

        if not os.path.exists(system_default_rcfile_path):
            self.show_error_dialog("Default keybindings file not found.")
            return

        try:
            subprocess.run(["cp", system_default_rcfile_path, user_rcfile_path], check=True)
            self.show_status_message("User keybindings restored from system defaults.")
            self.load_keybindings()  # Reload keybindings to reflect changes
        except subprocess.CalledProcessError as e:
            self.show_error_dialog(f"Error restoring keybindings: {e}")
        except Exception as e:
            self.show_error_dialog(f"Unexpected error: {e}")

    def get_password(self):
        dialog = Gtk.Dialog("Enter Password", self.window, Gtk.DialogFlags.MODAL,
                            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                             Gtk.STOCK_OK, Gtk.ResponseType.OK))
        dialog.set_default_size(150, 100)
        dialog.set_accessible_name("Enter password")

        label = Gtk.Label("Password:")
        password_entry = Gtk.PasswordEntry()
        password_entry.set_visibility(False)
        password_entry.set_accessible_name("Password Entry")

        vbox = dialog.get_content_area()
        vbox.pack_start(label, True, True, 0)
        vbox.pack_start(password_entry, True, True, 0)
        dialog.show_all()

        response = dialog.run()
        password = password_entry.get_text()
        dialog.destroy()

        if response == Gtk.ResponseType.OK:
            return password
        else:
            return None

    def run_sudo_command(self, command):
        password = self.get_password()
        if password is None:
            self.show_error_dialog("Password entry cancelled.")
            return
        try:
            process = subprocess.Popen(["sudo", "-S"] + command, stdin=subprocess.PIPE,
                                       stderr=subprocess.PIPE, stdout=subprocess.PIPE,
                                       universal_newlines=True)
            stdout, stderr = process.communicate(input=password + '\n')
            if process.returncode != 0:
                self.show_error_dialog(f"Error running command: {stderr}")
            elif stderr:
                print(stderr)
        except FileNotFoundError:
            self.show_error_dialog("sudo command not found.")
        except Exception as e:
            self.show_error_dialog(f"Unexpected error: {e}")

    def on_add_clicked(self, widget):
        self.liststore.append(["", "", ""])  # Add an empty row

    def on_remove_clicked(self, widget):
        selection = self.treeview.get_selection()
        model, paths = selection.get_selected_rows()
        if paths:
            for path in reversed(paths):  # Remove from bottom to top
                self.liststore.remove(model.get_iter(path))
            self.update_used_keys()

    def show_malformed_dialog(self, message, error_type):
        dialog = Gtk.MessageDialog(
            parent=self.window,
            flags=0,
            message_type=Gtk.MessageType.WARNING,
            buttons=Gtk.ButtonsType.NONE,
            text=message
        )
        dialog.add_buttons(Gtk.STOCK_EDIT, Gtk.ResponseType.EDIT,
                           Gtk.STOCK_RESTORE, Gtk.ResponseType.RESTORE)
        dialog.set_accessible_name("Malformed config file")
        response = dialog.run()
        dialog.destroy()

        if response == Gtk.ResponseType.EDIT:
            subprocess.run(["xdg-open", self.rcfile_path])
        elif response == Gtk.ResponseType.RESTORE:
            self.restore_keybindings()

    def on_cell_edited(self, renderer, path, new_text, col_num):
        old_key = self.liststore[path][0]
        self.liststore[path][col_num] = new_text
        if col_num == 0:
            self.update_used_keys()
            if self.check_conflict(new_text) and new_text != old_key and new_text != "":
              self.show_status_message(f"Warning: Key combination '{new_text}' is already in use.")
              self.liststore[path][0] = old_key
              self.update_used_keys()
              return

    def check_conflict(self, key_combination):
        if key_combination in self.used_keys and key_combination != "":
            return True
        return False

    def update_used_keys(self):
        self.used_keys = {}
        for row in self.liststore:
            key = row[0]
            if key:
                if key in self.used_keys:
                    self.show_status_message(f"Warning: Duplicate key found in list: {key}")
                self.used_keys[key] = True

    def show_status_message(self, message):
        self.status_label.set_text(message)

    def show_error_dialog(self, message):
        dialog = Gtk.MessageDialog(
            parent=self.window,
            flags=0,
            message_type=Gtk.MessageType.ERROR,
            buttons=Gtk.ButtonsType.OK,
            text=message,
        )
        dialog.run()
        dialog.destroy()

    def show_restore_dialog(self):
        dialog = Gtk.MessageDialog(
            parent=self.window,
            flags=0,
            message_type=Gtk.MessageType.QUESTION,
            buttons=Gtk.ButtonsType.YES_NO,
            text="Are you sure you want to restore user keybindings from system defaults?"
        )
        response = dialog.run()
        dialog.destroy()
        if response == Gtk.ResponseType.YES:
            self.restore_keybindings()

if __name__ == "__main__":
    editor = KeybindingEditor()
    Gtk.main()
