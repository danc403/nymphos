namespace KeybindingEditor {
    public static class NymphOS {
        public static string get_name() {
            return _("nymph-OS");
        }

        public static string user_config_path {
            get {
                return FilePath.build_filename(Environment.get_home_dir(), ".config/openbox/rc.xml");
            }
        }

        public static string system_config_path {
            get {
                return "/etc/xdg/openbox/rc.xml";
            }
        }

        public static bool check_exists() {
            return File.test(user_config_path, FileTest.EXISTS) || (Posix.geteuid() == 0 && File.test(system_config_path, FileTest.EXISTS));
        }

         public static void load_keybindings(ListStore liststore, Action<string> show_error_dialog, Action<string> show_status_message) {
            string config_path = user_config_path;
            if (!File.test(config_path, FileTest.EXISTS) && Posix.geteuid() == 0 && File.test(system_config_path, FileTest.EXISTS)) {
                config_path = system_config_path;
            }

            if (!File.test(config_path, FileTest.EXISTS)) {
                show_error_dialog(_("Keybindings file not found: %s").printf(config_path));
                return;
            }

            try {
                var tree = Xml.parse_file(config_path);
                var root = tree.get_root();
                if (root == null) {
                    show_error_dialog(_("Invalid XML structure: Root element not found."));
                    return;
                }

                var keyboard = root.get_element("keyboard");
                if (keyboard == null) {
                    show_error_dialog(_("Keyboard section not found or malformed."));
                    return;
                }

                var keybindings = keyboard.get_elements("keybind");

                foreach (var keybind in keybindings) {
                    var key_element = keybind.get_element("key");
                    var action_element = keybind.get_element("action");
                    var name_element = keybind.get_element("name");

                    string key = key_element != null ? key_element.get_content() : "";
                    string action = action_element != null && action_element.get_elements().length > 0 ? action_element.get_elements()[0].get_name() : "";
                    string name = name_element != null ? name_element.get_content() : "";

                    liststore.append({key, action, name});
                }
                show_status_message(_("nymph-OS keybindings loaded successfully."));

            } catch (Error e) {
                show_error_dialog(_("Error parsing nymph-OS XML configuration file: ") + e.message);
            }
        }

        public static void save_keybindings(ListStore liststore, string config_path, Action<string> show_error_dialog, Action<string> show_status_message) {
            try {
                var tree = Xml.parse_file(config_path);
                var root = tree.get_root();
                var keyboard = root.get_element("keyboard");
                if (keyboard == null) {
                    show_error_dialog(_("Keyboard section not found or malformed."));
                    return;
                }

                keyboard.remove_all_elements("keybind");

                for (int i = 0; i < liststore.n_items(); i++) {
                    string key_combination = liststore.get_value(i, 0) as string;
                    string action = liststore.get_value(i, 1) as string;
                    string name = liststore.get_value(i, 2) as string;

                    if (key_combination != "") {
                        var keybind = new XmlElement("keybind");
                        var key_element = new XmlElement("key");
                        key_element.set_content(key_combination);
                        var action_element = new XmlElement("action");
                        var action_sub_element = new XmlElement(action);
                        var name_element = new XmlElement("name");
                        name_element.set_content(name);

                        action_element.add_element(action_sub_element);
                        keybind.add_element(key_element);
                        keybind.add_element(action_element);
                        keybind.add_element(name_element);
                        keyboard.add_element(keybind);
                    }
                }
                tree.to_file(config_path);
                show_status_message(_("nymph-OS keybindings saved successfully."));

            } catch (Error e) {
                show_error_dialog(_("Error saving nymph-OS XML configuration file: ") + e.message);
            }
        }

    }
}
