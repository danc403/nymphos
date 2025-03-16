using Gtk;
using GLib;
using Gee;

namespace KeybindingEditor {
    public static class MacOS {

        public static string get_name() {
            return _("macOS VoiceOver");
        }

        public static string get_user_config_path() {
            // macOS stores VoiceOver keybindings in the user's preferences.
            // Verify the exact path. It might be slightly different depending on the macOS version.
            return FilePath.build_filename(Environment.get_home_dir(), "Library/Preferences/com.apple.VoiceOver.plist");
        }

        public static string get_system_config_path() {
            //macOS really doesnt have a system wide config for this so we will just store it in the default location.
             return FilePath.build_filename(Environment.get_home_dir(), "Library/Preferences/com.apple.VoiceOver.plist");
        }

        public static bool config_file_exists(bool is_system) {
            string config_path = is_system ? get_system_config_path() : get_user_config_path();
            return File.test(config_path, FileTest.EXISTS);
        }

        public static Hash<string, string> load_keybindings(string config_path) {
            var keybindings = new Hash<string, string>();

            if (!File.test(config_path, FileTest.EXISTS)) {
                // Handle the case where the file doesn't exist in the calling function
                return keybindings;
            }

            // Implement the logic to load VoiceOver keybindings from the preferences file.
            // This will likely involve parsing the plist file.  You'll need to find a Vala library
            // that can handle plist files.  One possibility is to use a GLib.Variant and associated functions
            // to read and parse the plist (which is often a binary plist).  However, handling binary plists
            // directly can be complex.  It might be easier to call out to a command-line tool like
            // `defaults read com.apple.VoiceOver` to get the settings as a string, and then parse that string.
            //
            // Example (using a theoretical plist parsing library):
            // try {
            //     var plist = Plist.parse_file(get_voiceover_preferences_path());
            //     var keybindings = plist.get("keybindings"); // Adjust key name if needed
            //
            //     // Assuming keybindings is a dictionary/hash of key:action
            //     if (keybindings is Hash<string, string>) {
            //         foreach (var key in keybindings.get_keys()) {
            //             string action = keybindings.get(key);
            //             // Update the liststore with keybindings
            //             this.liststore.append({key, action, "VoiceOver"});
            //         }
            //     } else {
            //         this.show_error_dialog(_("Unexpected format for VoiceOver keybindings."));
            //     }
            // } catch (Error e) {
            //     this.show_error_dialog(_("Error reading VoiceOver preferences: ") + e.message);
            // }
            //
            // **Important:** You'll need to adapt this code to use the correct plist parsing method
            // and to handle the specific structure of the VoiceOver preferences file.  The above
            // is just a placeholder.  You also need to add the correct imports if you use a plist library.
            //
            // For now, just display a message:
            print(_("Loading VoiceOver keybindings (implementation pending).\n"));
            return keybindings;
        }

        public static void save_keybindings(string config_path, Hash<string, string> keybindings) {

            if (!File.test(config_path, FileTest.EXISTS)) {
                // Handle the case where the file doesn't exist in the calling function
                return;
            }
            // Implement the logic to save VoiceOver keybindings to the preferences file.
            // This will involve creating or modifying the plist file.  You'll need to use the same
            // plist parsing library as used in load_voiceover_keybindings.
            //
            // Example (using a theoretical plist parsing library):
            // try {
            //     var plist = Plist.new();
            //     var keybindings = new Hash<string, string>();
            //
            //     // Populate keybindings from the liststore
            //     for (int i = 0; i < this.liststore.n_items(); i++) {
            //         string key = this.liststore.get_value(i, 0) as string;
            //         string action = this.liststore.get_value(i, 1) as string;
            //         keybindings.set(key, action);
            //     }
            //
            //     plist.set("keybindings", keybindings); // Adjust key name if needed
            //     plist.write_to_file(get_voiceover_preferences_path());
            //     this.show_status_message(_("VoiceOver keybindings saved successfully."));
            // } catch (Error e) {
            //     this.show_error_dialog(_("Error writing VoiceOver preferences: ") + e.message);
            // }
            //
            // **Important:** You'll need to adapt this code to use the correct plist parsing method
            // and to handle the specific structure of the VoiceOver preferences file. The above
            // is just a placeholder. You also need to add the correct imports if you use a plist library.
            //
            // For now, just display a message:
            print(_("Saving VoiceOver keybindings (implementation pending).\n"));
        }
    }
}
