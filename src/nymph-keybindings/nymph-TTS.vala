using Gtk;
using GLib;
using Gee;
using Xml;

namespace KeybindingEditor {
    public class NymphTTS {
        // Placeholder paths for Nymph-TTS configuration files
        private static string user_config_path = FilePath.build_filename(Environment.get_home_dir(), ".config/nymph-TTS/keybindings.xml");
        private static string system_config_path = "/etc/nymph-TTS/keybindings.xml";

        public static bool is_config_file_present(bool is_system) {
            string config_path = is_system ? system_config_path : user_config_path;
            return File.test(config_path, FileTest.EXISTS);
        }

        public static string get_config_path(bool is_system) {
            return is_system ? system_config_path : user_config_path;
        }

        public static void load_keybindings(ListStore liststore, string config_path, Action<string> show_error_dialog, Action<string> show_status_message) {
            try {
                var tree = Xml.parse_file(config_path);
                var root = tree.get_root();
                if (root == null) {
                    show_error_dialog(_("Invalid XML structure: Root element not found."));
                    return;
                }

                var keybinds = root.get_elements("keybind");

                foreach (var keybind in keybinds) {
                    var key_element = keybind.get_element("key");
                    var action_element = keybind.get_element("action");
                    var name_element = keybind.get_element("name");

                    string key = key_element != null ? key_element.get_content() : "";
                    string action = action_element != null ? action_element.get_content() : "";
                    string name = name_element != null ? name_element.get_content() : "";

                    liststore.append({key, action, name});
                }
                show_status_message(_("Nymph-TTS keybindings loaded successfully."));

            } catch (Error e) {
                show_error_dialog(_("Error parsing Nymph-TTS XML configuration file: ") + e.message);
            }
        }

        public static void save_keybindings(ListStore liststore, string config_path, Action<string> show_error_dialog, Action<string> show_status_message) {
            try {
                var root = new XmlElement("keybindings");
                var tree = new Xml.Document(root);

                for (int i = 0; i < liststore.n_items(); i++) {
                    string key = liststore.get_value(i, 0) as string;
                    string action = liststore.get_value(i, 1) as string;
                    string name = liststore.get_value(i, 2) as string;

                    var keybind = new XmlElement("keybind");

                    var key_element = new XmlElement("key");
                    key_element.set_content(key);
                    keybind.add_element(key_element);

                    var action_element = new XmlElement("action");
                    action_element.set_content(action);
                    keybind.add_element(action_element);

                    var name_element = new XmlElement("name");
                    name_element.set_content(name);
                    keybind.add_element(name_element);

                    root.add_element(keybind);
                }

                tree.to_file(config_path);
                show_status_message(_("Nymph-TTS keybindings saved successfully."));

            } catch (Error e) {
                show_error_dialog(_("Error saving Nymph-TTS XML configuration file: ") + e.message);
            }
        }
    }
}
