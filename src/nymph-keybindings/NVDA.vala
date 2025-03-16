/* NVDA.vala */
using GLib;
using Gee;

namespace KeybindingEditor {
    public static class NVDA {
        public static string get_name() {
            return _("NVDA");
        }

        public static string get_user_config_path() {
            // NVDA stores configuration in the user's AppData\Roaming folder on Windows.
            // Getting this reliably from Vala/GLib is tricky and platform-dependent.
            // A more robust solution would involve platform-specific code or environment variables.
            // For now, let's return a placeholder path, and note that it will likely need adjustment.

            // Use Linux equivalent for user configuration: ~/.nvda/nvda.ini
            // Use macOS equivalent for user configuration: ~/Library/Application Support/NVDA/nvda.ini

            #if WIN32
            string configDir = Path.build_filename(Environment.get_home_dir(), "AppData/Roaming/nvda");
            #elif MACOS
             string configDir = Path.build_filename(Environment.get_home_dir(), "Library/Application Support/NVDA");
            #else
            string configDir = Path.build_filename(Environment.get_home_dir(), ".nvda");
            #endif
            if (!File.test(configDir, FileTest.EXISTS)) {
                DirUtils.create_with_parents(configDir, 0777);
            }
            return FilePath.build_filename(configDir, "nvda.ini");
        }

        public static string get_system_config_path() {
            // NVDA typically doesn't have a system-wide configuration in the same way Openbox does.
            // If a system-wide default configuration is desired, it might be stored in the NVDA installation directory.
            // Again, this is highly platform-dependent. Return a placeholder.

            // Use Linux equivalent for system configuration: /etc/nvda/nvda_system_defaults.ini
            // Use macOS equivalent for system configuration: /Applications/NVDA.app/Contents/Resources/nvda_system_defaults.ini

            #if WIN32
            return "/Program Files/NVDA/nvda_system_defaults.ini";
            #elif MACOS
            return "/Applications/NVDA.app/Contents/Resources/nvda_system_defaults.ini";
            #else
            return "/etc/nvda/nvda_system_defaults.ini";
            #endif
        }

        public static bool config_file_exists(bool is_system) {
            string config_path = is_system ? get_system_config_path() : get_user_config_path();
            return File.test(config_path, FileTest.EXISTS);
        }

        public static Hash<string, string> load_keybindings(string config_path, Action<string> show_error_dialog, Action<string> show_status_message) {
            var keybindings = new Hash<string, string>();

            if (!File.test(config_path, FileTest.EXISTS)) {
                // Handle the case where the file doesn't exist
                show_error_dialog(_("NVDA configuration file not found: %s").printf(config_path));
                return keybindings;
            }

            try {
                var file = File.new_for_path(config_path);
                var file_input = file.read(null);
                var data = file_input.read_bytes(file_input.get_size()).get_data();
                var contents = (string) data;
                var lines = contents.split("\n");

                foreach (var line in lines) {
                    if (line.has_prefix("commands.")) {
                        // Split the line into parts
                        string[] parts = line.split("=", 2);

                        // Ensure there are two parts to the line
                        if (parts.length == 2) {
                            // Get the first part, removing commands.
                            string commandPart = parts[0].strip().substring(9);

                            // Get the second part
                            string keybinding = parts[1].strip();

                            // Replace any brackets
                            keybinding = keybinding.replace("[", "");
                            keybinding = keybinding.replace("]", "");

                            // Add to the hash table
                            keybindings.set(keybinding, commandPart);
                        }
                    }
                }
                show_status_message(_("NVDA keybindings loaded successfully."));

            } catch (Error e) {
                show_error_dialog(_("Error loading NVDA keybindings: ") + e.message);
            }

            return keybindings;
        }

        public static void save_keybindings(string config_path, Hash<string, string> keybindings, Action<string> show_error_dialog, Action<string> show_status_message) {
             try {
                var file = File.new_for_path(config_path);

                // Prepare the new contents
                string new_contents = "";

                // Add a header to the file, if it is empty it will make it a complete config file.
                new_contents += "[global]\n";
                new_contents += "focusReported=true\n";
                new_contents += "lastUpdateCheck=1697759762.466359\n";
                new_contents += "keyboardLayout=en_US\n";
                new_contents += "speechMode=0\n";
                new_contents += "port=auto\n";
                new_contents += "autoRunAddons=\n";
                new_contents += "\n";

                // Add the keybinding data
                foreach (var key in keybindings.get_keys()) {
                    new_contents += "commands." + keybindings.get(key) + " = [" + key + "]\n";
                }

                // Write the new contents back to the file
                var file_output = file.replace(null, false, FileCreateFlags.NONE, null);
                file_output.write(new_contents.data, new_contents.length, null);
                file_output.close(null);
                show_status_message(_("NVDA keybindings saved successfully."));

            } catch (Error e) {
                show_error_dialog(_("Error saving NVDA keybindings: ") + e.message);
            }
        }

        public static bool restore_default_config(string config_path, Action<string> show_error_dialog, Action<string> show_status_message){
            string system_default_config_path = get_system_config_path();
             if (!File.test(system_default_config_path, FileTest.EXISTS)) {
                show_error_dialog(_("Default NVDA configuration file not found."));
                return false;
            }
             try {
                FileUtils.copy_file(system_default_config_path, config_path);
                show_status_message(_("User NVDA keybindings restored from system defaults."));
                return true;
            } catch (Error e) {
                show_error_dialog(_("Error restoring NVDA keybindings: ") + e.message);
                return false;
            }
        }
    }
}
