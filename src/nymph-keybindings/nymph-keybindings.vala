using Gtk;
using GLib;
using Gee;

namespace KeybindingEditor {
    public class MainWindow : Window {
        private Grid grid;
        private Button user_button;
        private Button system_button;
        private Button orca_user_button;
        private Button orca_system_button;
        private TreeView treeview;
        private Button restore_button;
        private Button save_button;
        private Button add_button;
        private Button remove_button;
        private Label status_label;

        private string rcfile_path = null;
        private Hash<string, bool> used_keys = new Hash<string, bool>();
        private ListStore liststore;

        public MainWindow() {
            // Set up internationalization
            Intl.setlocale(LocaleCategory.ALL, "");
            Intl.bindtextdomain(Config.GETTEXT_PACKAGE, Config.LOCALEDIR);
            Intl.textdomain(Config.GETTEXT_PACKAGE);

            this.title = _("nymph Keybinding Editor");
            this.destroy.connect(Gtk.main_quit);

            this.grid = new Grid();
            this.add(this.grid);

            this.user_button = new Button.with_label(_("User Keybindings"));
            this.user_button.accessible.name = "User keybindings";
            this.system_button = new Button.with_label(_("System Keybindings"));
            this.system_button.accessible.name = "System keybindings";
            this.orca_user_button = new Button.with_label(_("User Orca Keybindings"));
            this.orca_user_button.accessible.name = "User Orca keybindings";
            this.orca_system_button = new Button.with_label(_("System Orca Keybindings"));
            this.orca_system_button.accessible.name = "System Orca keybindings";
            this.grid.attach(this.user_button, 0, 0, 1, 1);
            this.grid.attach(this.system_button, 1, 0, 1, 1);
            this.grid.attach(this.orca_user_button, 0, 1, 1, 1);
            this.grid.attach(this.orca_system_button, 1, 1, 1, 1);

            this.treeview = new TreeView();
            this.grid.attach(this.treeview, 0, 2, 2, 1);

            this.restore_button = new Button.with_label(_("Restore User Keybindings from System Defaults"));
            this.restore_button.accessible.name = "Restore user keybindings from system defaults";
            this.grid.attach(this.restore_button, 0, 3, 2, 1);

            this.save_button = new Button.with_label(_("Save"));
            this.save_button.accessible.name = "Save keybindings";
            this.grid.attach(this.save_button, 0, 4, 2, 1);

            this.add_button = new Button.with_label(_("Add Keybinding"));
            this.add_button.accessible.name = "Add keybinding";
            this.remove_button = new Button.with_label(_("Remove Keybinding"));
            this.remove_button.accessible.name = "Remove keybinding";
            this.grid.attach(this.add_button, 0, 5, 1, 1);
            this.grid.attach(this.remove_button, 1, 5, 1, 1);

            this.status_label = new Label();
            this.grid.attach(this.status_label, 0, 6, 2, 1);

            this.user_button.clicked.connect(on_user_clicked);
            this.system_button.clicked.connect(on_system_clicked);
            this.orca_user_button.clicked.connect(on_orca_user_clicked);
            this.orca_system_button.clicked.connect(on_orca_system_clicked);
            this.restore_button.clicked.connect(on_restore_clicked);
            this.save_button.clicked.connect(on_save_clicked);
            this.add_button.clicked.connect(on_add_clicked);
            this.remove_button.clicked.connect(on_remove_clicked);

            this.liststore = new ListStore(typeof(string), typeof(string), typeof(string));
            this.treeview.model = this.liststore;
            this.setup_treeview_columns();

            this.show_all();
        }

        private void setup_treeview_columns() {
            foreach (var column in this.treeview.get_columns()) {
                this.treeview.remove_column(column);
            }
            string[] column_titles = {_("Key Combination"), _("Action"), _("Name")};
            for (int i = 0; i < column_titles.length; i++) {
                var renderer = new CellRendererText();
                renderer.editable = true;
                renderer.edited.connect((renderer, path, new_text) => on_cell_edited(renderer, path, new_text, i));
                var column = new TreeViewColumn.with_attributes(column_titles[i], renderer, "text", i);
                this.treeview.append_column(column);
            }
        }

        private void on_user_clicked(Button widget) {
            this.rcfile_path = FilePath.build_filename(Environment.get_home_dir(), ".config/openbox/rc.xml");
            this.load_keybindings();
        }

        private void on_system_clicked(Button widget) {
            if (Posix.geteuid() == 0) {
                this.rcfile_path = "/etc/xdg/openbox/rc.xml";
                this.load_keybindings();
            } else {
                this.show_error_dialog(_("Root permissions required."));
            }
        }

        private void on_restore_clicked(Button widget) {
            this.show_restore_dialog();
        }

        private void on_save_clicked(Button widget) {
            this.save_keybindings();
        }

        private void load_keybindings() {
            this.used_keys.clear();
            this.liststore.clear();
            if (this.rcfile_path == null || !File.test(this.rcfile_path, FileTest.EXISTS)) {
                this.show_error_dialog(_("Keybindings file not found."));
                return;
            }

            try {
                var tree = Xml.parse_file(this.rcfile_path);
                var root = tree.get_root();
                var keyboard = root.get_element("keyboard");
                if (keyboard == null) {
                    this.show_malformed_dialog(_("Keyboard section not found or malformed."), "keyboard");
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

                    if (key != "") {
                        if (this.used_keys.has_key(key)) {
                            this.show_status_message(_("Warning: Duplicate key found in config: ") + key);
                        }
                        this.used_keys.set(key, true);
                    }
                    this.liststore.append({key, action, name});
                }
            } catch (Error e) {
                this.show_malformed_dialog(_("Error parsing XML: ") + e.message, "parse");
            }
        }

        private void save_keybindings() {
            if (this.rcfile_path == null || !File.test(this.rcfile_path, FileTest.EXISTS)) {
                this.show_error_dialog(_("Keybindings file not found."));
                return;
            }

            try {
                var tree = Xml.parse_file(this.rcfile_path);
                var root = tree.get_root();
                var keyboard = root.get_element("keyboard");
                if (keyboard == null) {
                    this.show_malformed_dialog(_("Keyboard section not found or malformed."), "keyboard");
                    return;
                }

                keyboard.remove_all_elements("keybind");

                for (int i = 0; i < this.liststore.n_items(); i++) {
                    string key_combination = this.liststore.get_value(i, 0) as string;
                    string action = this.liststore.get_value(i, 1) as string;
                    string name = this.liststore.get_value(i, 2) as string;

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
                tree.to_file(this.rcfile_path);
                this.show_status_message(_("Keybindings saved successfully."));

            } catch (Error e) {
                this.show_malformed_dialog(_("Error parsing XML: ") + e.message, "parse");
            }
        }

        private void restore_keybindings() {
            string user_rcfile_path = FilePath.build_filename(Environment.get_home_dir(), ".config/openbox/rc.xml");
            string system_default_rcfile_path = "/etc/xdg/openbox/rc.xml.default";

            if (!File.test(system_default_rcfile_path, FileTest.EXISTS)) {
                this.show_error_dialog(_("Default keybindings file not found."));
                return;
            }

            try {
                FileUtils.copy_file(system_default_rcfile_path, user_rcfile_path);
                this.show_status_message(_("User keybindings restored from system defaults."));
                this.load_keybindings();
            } catch (Error e) {
                this.show_error_dialog(_("Error restoring keybindings: ") + e.message);
            }
        }

        private string get_password() {
            var dialog = new Dialog(_("Enter Password"), this, DialogFlags.MODAL, Stock.CANCEL, ResponseType.CANCEL, Stock.OK, ResponseType.OK);
            dialog.default_size = new Size(150, 100);
            dialog.accessible.name = "Enter password";

            var label = new Label(_("Password:"));
            var password_entry = new PasswordEntry();
            password_entry.visibility = false;
            password_entry.accessible.name = "Password Entry";

            var vbox = dialog.content_area;
            vbox.pack_start(label, true, true, 0);
            vbox.pack_start(password_entry, true, true, 0);
            dialog.show_all();

            var response = dialog.run();
            string password = password_entry.text;
            dialog.destroy();

            if (response == ResponseType.OK) {
                return password;
            } else {
                return null;
            }
        }

        private void run_sudo_command(string[] command) {
            string password = this.get_password();
            if (password == null) {
                this.show_error_dialog(_("Password entry cancelled."));
                return;
            }

            try {
                var process = new Subprocess.with_argv({"sudo", "-S", ...command}, SubprocessFlags.STDERR_MERGE);
                process.communicate(password + "\n");
                if (process.get_exit_status() != 0) {
                    this.show_error_dialog(_("Error running command: ") + process.get_stdout_data());
                } else if (process.get_stdout_data().length > 0) {
                    print(process.get_stdout_data());
                }
            } catch (Error e) {
                this.show_error_dialog(_("Unexpected error: ") + e.message);
            }
        }

        private void on_add_clicked(Button widget) {
            this.liststore.append({"", "", ""});
        }

        private void on_remove_clicked(Button widget) {
            var selection = this.treeview.selection;
            TreeModel model;
            TreePath[] paths;
            selection.get_selected_rows(out model, out paths);
            if (paths.length > 0) {
                for (int i = paths.length - 1; i >= 0; i--) {
                    TreeIter iter;
                    if (model.get_iter(out iter, paths[i])) {
                        this.liststore.remove(iter);
                    }
                }
                this.update_used_keys();
            }
        }

        private void show_malformed_dialog(string message, string error_type) {
            var dialog = new MessageDialog(this, DialogFlags.MODAL, MessageType.WARNING, ButtonsType.NONE, message);
            dialog.add_buttons(Stock.EDIT, ResponseType.EDIT, Stock.RESTORE, ResponseType.RESTORE);
            dialog.accessible.name = "Malformed config file";
            var response = dialog.run();
            dialog.destroy();

            if (response == ResponseType.EDIT) {
                try{
                    new Subprocess.with_argv({"xdg-open", this.rcfile_path}, SubprocessFlags.NONE);
                } catch (Error e){
                    this.show_error_dialog(_("Could not open file, xdg-open not found."));
                }

            } else if (response == ResponseType.RESTORE) {
                this.restore_keybindings();
            }
        }

        private void on_cell_edited(CellRendererText renderer, string path, string new_text, int col_num) {
            TreeIter iter;
            if (this.liststore.get_iter(out iter, new TreePath.from_string(path))) {
                string old_key = this.liststore.get_value(iter, 0) as string;
                this.liststore.set_value(iter, col_num, new_text);

                if (col_num == 0) {
                    this.update_used_keys();
                    if (this.check_conflict(new_text) && new_text != old_key && new_text != "") {
                        this.show_status_message(_("Warning: Key combination '%s' is already in use.").printf(new_text));
                        this.liststore.set_value(iter, 0, old_key);
                        this.update_used_keys();
                    }
                }
            }
        }

        private bool check_conflict(string key_combination) {
            if (this.used_keys.has_key(key_combination) && key_combination != "") {
                return true;
            }
            return false;
        }

        private void update_used_keys() {
            this.used_keys.clear();
            TreeIter iter;
            if (this.liststore.get_iter_first(out iter)) {
                do {
                    string key = this.liststore.get_value(iter, 0) as string;
                    if (key != "") {
                        if (this.used_keys.has_key(key)) {
                            this.show_status_message(_("Warning: Duplicate key found in list: ") + key);
                        }
                        this.used_keys.set(key, true);
                    }
                } while (this.liststore.iter_next(iter));
            }
        }

        private void show_status_message(string message) {
            this.status_label.text = message;
        }

        private void show_error_dialog(string message) {
            var dialog = new MessageDialog(this, DialogFlags.MODAL, MessageType.ERROR, ButtonsType.OK, message);
            dialog.run();
            dialog.destroy();
        }

        private void show_restore_dialog() {
            var dialog = new MessageDialog(this, DialogFlags.MODAL, MessageType.QUESTION, ButtonsType.YES_NO, _("Are you sure you want to restore user keybindings from system defaults?"));
            var response = dialog.run();
            dialog.destroy();
            if (response == ResponseType.YES) {
                this.restore_keybindings();
            }
        }

        // Orca Keybindings Functions

        private string get_orca_config_path(bool is_system) {
            if (is_system) {
                return "/etc/xdg/orca/orca_prefs.py";
            } else {
                return FilePath.build_filename(Environment.get_home_dir(), ".config/orca/orca_prefs.py");
            }
        }

        private void load_orca_keybindings(bool is_system) {
            string config_path = get_orca_config_path(is_system);
            if (!File.test(config_path, FileTest.EXISTS)) {
                this.show_error_dialog(_("Orca configuration file not found."));
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
                foreach (var line in lines) {
                    if (line.strip().has_prefix("keybindings = {")) {
                        var start_index = line.find("{") + 1;
                        var end_index = line.rfind("}");
                        if (start_index != -1 && end_index != -1) {
                            var bindings_str = line.substring(start_index, end_index - start_index);
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
                    }
                }

                // Update the liststore with keybindings
                this.liststore.clear();
                foreach (var key in keybindings.get_keys()) {
                    this.liststore.append({key, keybindings.get(key)});
                }
            } catch (Error e) {
                this.show_error_dialog(_("Error reading Orca configuration file: ") + e.message);
            }
        }

        private void save_orca_keybindings(bool is_system) {
            string config_path = get_orca_config_path(is_system);
            if (!File.test(config_path, FileTest.EXISTS)) {
                this.show_error_dialog(_("Orca configuration file not found."));
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
                foreach (var line in lines) {
                    if (line.strip().has_prefix("keybindings = {")) {
                        in_keybindings = true;
                        new_contents += line + "\n";
                        new_contents += "    ";
                        for (int i = 0; i < this.liststore.n_items(); i++) {
                            string key = this.liststore.get_value(i, 0) as string;
                            string action = this.liststore.get_value(i, 1) as string;
                            if (i > 0) {
                                new_contents += ", ";
                            }
                            new_contents += "\"" + key + "\": \"" + action + "\"";
                        }
                        new_contents += "\n}";
                    } else if (in_keybindings) {
                        in_keybindings = false;
                    } else {
                        new_contents += line + "\n";
                    }
                }

                // Write the new contents back to the file
                var file_output = file.replace(null, false, FileCreateFlags.NONE, null);
                file_output.write(new_contents.data, new_contents.length, null);
                file_output.close(null);

                this.show_status_message(_("Orca keybindings saved successfully."));
            } catch (Error e) {
                this.show_error_dialog(_("Error writing Orca configuration file: ") + e.message);
            }
        }

        private void restore_orca_keybindings(bool is_system) {
            string user_config_path = FilePath.build_filename(Environment.get_home_dir(), ".config/orca/orca_prefs.py");
            string system_default_config_path = "/etc/xdg/orca/orca_prefs.py.default";

            if (!File.test(system_default_config_path, FileTest.EXISTS)) {
                this.show_error_dialog(_("Default Orca configuration file not found."));
                return;
            }

            try {
                FileUtils.copy_file(system_default_config_path, user_config_path);
                this.show_status_message(_("User Orca keybindings restored from system defaults."));
                this.load_orca_keybindings(false);
            } catch (Error e) {
                this.show_error_dialog(_("Error restoring Orca keybindings: ") + e.message);
            }
        }

        private void on_orca_user_clicked(Button widget) {
            load_orca_keybindings(false);
        }

        private void on_orca_system_clicked(Button widget) {
            if (Posix.geteuid() == 0) {
                load_orca_keybindings(true);
            } else {
                this.show_error_dialog(_("Root permissions required."));
            }
        }

        private void on_orca_save_clicked(Button widget) {
            if (Posix.geteuid() == 0) {
                save_orca_keybindings(true);
            } else {
                save_orca_keybindings(false);
            }
        }

        private void on_orca_add_clicked(Button widget) {
            this.liststore.append({"", ""});
        }

        private void on_orca_remove_clicked(Button widget) {
            var selection = this.treeview.selection;
            TreeModel model;
            TreePath[] paths;
            selection.get_selected_rows(out model, out paths);
            if (paths.length > 0) {
                for (int i = paths.length - 1; i >= 0; i--) {
                    TreeIter iter;
                    if (model.get_iter(out iter, paths[i])) {
                        this.liststore.remove(iter);
                    }
                }
            }
        }

        private void on_orca_cell_edited(CellRendererText renderer, string path, string new_text, int col_num) {
            TreeIter iter;
            if (this.liststore.get_iter(out iter, new TreePath.from_string(path))) {
                this.liststore.set_value(iter, col_num, new_text);
            }
        }

        private bool is_orca_running() {
            try {
                var process = new Subprocess.with_argv({"pgrep", "orca"}, SubprocessFlags.STDOUT_PIPE);
                process.wait();
                return process.get_exit_status() == 0;
            } catch (Error e) {
                return false;
            }
        }
    }

    public static int main(string[] args) {
        Gtk.init(ref args);
        var window = new MainWindow();
        Gtk.main();
        return 0;
    }
}

