// orca.vala
using Gtk;
using GLib;
using Gee;

namespace KeybindingEditor {
    public static class Orca {

        private static string user_config_path {
            get {
                return FilePath.build_filename(Environment.get_home_dir(), ".config/orca/orca_prefs.py");
            }
        }

        private static string system_config_path {
            get {
                return "/etc/xdg/orca/orca_prefs.py";
            }
        }

        private static string system_default_config_path {
            get {
                return "/etc/xdg/orca/orca_prefs.py.default";
            }
        }

        public static bool check_exists() {
            return File.test(user_config_path, FileTest.EXISTS) || (Posix.geteuid() == 0 && File.test(system_config_path, FileTest.EXISTS));
        }

        public static string get_config_path(bool is_system) {
            return is_system ? system_config_path : user_config_path;
        }

        public static void load_keybindings(ListStore liststore, string config_path, Action<string> show_error_dialog, Action<string> show_status_message) {
            if (!File.test(config_path, FileTest.EXISTS)) {
                show_error_dialog(_("Orca configuration file not found."));
                return;
            }

            try {
                var file = File.new_for_path(config_path);
                var file_input = file.read(null);
                var data = file_input.read_bytes(file_input.get_size()).get_data();
                var contents = (string) data;

                // Parse the contents to extract keybindings
                // Example: keybindings = {"Ctrl+Alt+Shift+T": "toggle_speech", ...}
                var keybindings = new Hash<string, string>();
                var lines = contents.split("\n");
                bool in_keybindings = false;
                string bindings_str = "";

                foreach (var line in lines) {
                    if (line.strip().has_prefix("keybindings = {")) {
                        in_keybindings = true;
                        bindings_str += line.strip().substring(line.strip().find("{") + 1).strip();
                    } else if (in_keybindings) {
                        if (line.strip().has_suffix("}")) {
                            bindings_str += line.strip().substring(0, line.strip().find("}")).strip();
                            in_keybindings = false;
                        } else {
                            bindings_str += line.strip();
                        }
                    }
                }

                if (bindings_str != "") {
                    var pairs = bindings_str.split(",");
                    foreach (var pair in pairs) {
                        var parts = pair.split(":", 2);
                        if (parts.length == 2) {
                            string key = parts[0].strip().replace("\"", "");
                            string action = parts[1].strip().replace("\"", "").replace("'", "");
                            keybindings.set(key, action);
                        }
                    }
                }

                // Update the liststore with keybindings
                liststore.clear();
                foreach (var key in keybindings.get_keys()) {
                    liststore.append({key, keybindings.get(key), "Orca"});
                }
                show_status_message(_("Orca keybindings loaded successfully."));

            } catch (Error e) {
                show_error_dialog(_("Error reading Orca configuration file: ") + e.message);
            }
        }

        public static void save_keybindings(ListStore liststore, string config_path, Action<string> show_error_dialog, Action<string> show_status_message) {
            if (!File.test(config_path, FileTest.EXISTS)) {
                show_error_dialog(_("Orca configuration file not found."));
                return;
            }

            try {
                var file = File.new_for_path(config_path);
                var file_input = file.read(null);
                var data = file_input.read_bytes(file_input.get_size()).get_data();
                var contents = (string) data;

                // Find the keybindings section
                var lines = contents.split("\n");
                string new_contents = "";
                bool in_keybindings = false;
                string keybindings_section = "keybindings = {\n";

                foreach (var line in lines) {
                    if (line.strip().has_prefix("keybindings = {")) {
                        in_keybindings = true;
                    } else if (in_keybindings) {
                        if (line.strip().has_suffix("}")) {
                            in_keybindings = false;
                        }
                    } else {
                        new_contents += line + "\n";
                    }
                }

                for (int i = 0; i < liststore.n_items(); i++) {
                    string key = liststore.get_value(i, 0) as string;
                    string action = liststore.get_value(i, 1) as string;
                    if (i > 0) {
                        keybindings_section += ", ";
                    }
                    keybindings_section += f"    \"{key}\": \"{action}\"";
                }
                keybindings_section += "\n}\n";

                new_contents += keybindings_section;

                // Write the new contents back to the file
                var file_output = file.replace(null, false, FileCreateFlags.NONE, null);
                file_output.write(new_contents.data, new_contents.length, null);
                file_output.close(null);

                show_status_message(_("Orca keybindings saved successfully."));
            } catch (Error e) {
                show_error_dialog(_("Error writing Orca configuration file: ") + e.message);
            }
        }

        public static void restore_keybindings(Action<string> show_error_dialog, Action<string> show_status_message) {
            string user_config_path = FilePath.build_filename(Environment.get_home_dir(), ".config/orca/orca_prefs.py");
            string system_default_config_path = "/etc/xdg/orca/orca_prefs.py.default";

            if (!File.test(system_default_config_path, FileTest.EXISTS)) {
                show_error_dialog(_("Default Orca configuration file not found."));
                return;
            }

            try {
                FileUtils.copy_file(system_default_config_path, user_config_path);
                show_status_message(_("User Orca keybindings restored from system defaults."));
            } catch (Error e) {
                show_error_dialog(_("Error restoring Orca keybindings: ") + e.message);
            }
        }

        public static bool is_running() {
            try {
                var process = new Subprocess.with_argv({"pgrep", "orca"}, SubprocessFlags.STDOUT_PIPE);
                process.wait();
                return process.get_exit_status() == 0;
            } catch (Error e) {
                return false;
            }
        }
    }
}
