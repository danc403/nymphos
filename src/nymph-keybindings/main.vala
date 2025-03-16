```vala
# -------------------- main.vala -------------------- #

using Gtk;
using GLib;
using Gee;

namespace KeybindingEditor {
    public class MainWindow : Window {
        private Grid grid;
        private ComboBoxText config_combobox;
        private Button user_button;
        private Button system_button;
        private Button orca_user_button;
        private Button orca_system_button;
		private Button nvda_user_button;
        private Button nvda_system_button;
        private Button macos_button;
        private TreeView treeview;
        private Button restore_button;
        private Button save_button;
        private Button add_button;
        private Button remove_button;
        private Label status_label;

        private string rcfile_path = null;
        private Hash<string, bool> used_keys = new Hash<string, bool>();
        private ListStore liststore;
        private string current_config = null;

        public MainWindow() {
            // Set up internationalization
            Intl.setlocale(LocaleCategory.ALL, "");
            Intl.bindtextdomain(Config.GETTEXT_PACKAGE, Config.LOCALEDIR);
            Intl.textdomain(Config.GETTEXT_PACKAGE);

            this.title = _("nymph Keybinding Editor");
            this.destroy.connect(Gtk.main_quit);

            this.grid = new Grid();
            this.add(this.grid);

            // Config ComboBox
            this.config_combobox = new ComboBoxText();
            this.config_combobox.changed.connect(on_config_changed);
            this.grid.attach(this.config_combobox, 0, 0, 2, 1);
            populate_config_combobox();

            this.user_button = new Button.with_label(_("Openbox User Keybindings"));
            this.user_button.accessible.name = _("Openbox User keybindings");
            this.system_button = new Button.with_label(_("Openbox System Keybindings"));
            this.system_button.accessible.name = _("Openbox System keybindings");
            this.orca_user_button = new Button.with_label(_("Orca User Keybindings"));
            this.orca_user_button.accessible.name = _("Orca User keybindings");
            this.orca_system_button = new Button.with_label(_("Orca System Keybindings"));
            this.orca_system_button.accessible.name = _("Orca System keybindings");
			this.nvda_user_button = new Button.with_label(_("NVDA User Keybindings"));
            this.nvda_user_button.accessible.name = _("NVDA User keybindings");
            this.nvda_system_button = new Button.with_label(_("NVDA System Keybindings"));
            this.nvda_system_button.accessible.name = _("NVDA System keybindings");
            this.macos_button = new Button.with_label(_("macOS VoiceOver Keybindings"));
            this.macos_button.accessible.name = _("macOS VoiceOver keybindings");
            this.grid.attach(this.user_button, 0, 1, 1, 1);
            this.grid.attach(this.system_button, 1, 1, 1, 1);
            this.grid.attach(this.orca_user_button, 0, 2, 1, 1);
            this.grid.attach(this.orca_system_button, 1, 2, 1, 1);
			this.grid.attach(this.nvda_user_button, 0, 3, 1, 1);
            this.grid.attach(this.nvda_system_button, 1, 3, 1, 1);
            this.grid.attach(this.macos_button, 0, 4, 2, 1);

            this.treeview = new TreeView();
            this.grid.attach(this.treeview, 0, 5, 2, 1);

            this.restore_button = new Button.with_label(_("Restore User Keybindings from System Defaults"));
            this.restore_button.accessible.name = _("Restore user keybindings from system defaults");
            this.grid.attach(this.restore_button, 0, 6, 2, 1);

            this.save_button = new Button.with_label(_("Save"));
            this.save_button.accessible.name = _("Save keybindings");
            this.grid.attach(this.save_button, 0, 7, 2, 1);

            this.add_button = new Button.with_label(_("Add Keybinding"));
            this.add_button.accessible.name = _("Add keybinding");
            this.remove_button = new Button.with_label(_("Remove Keybinding"));
            this.remove_button.accessible.name = _("Remove keybinding");
            this.grid.attach(this.add_button, 0, 8, 1, 1);
            this.grid.attach(this.remove_button, 1, 8, 1, 1);

            this.status_label = new Label();
            this.grid.attach(this.status_label, 0, 9, 2, 1);

            this.user_button.clicked.connect(on_user_clicked);
            this.system_button.clicked.connect(on_system_clicked);
            this.orca_user_button.clicked.connect(on_orca_user_clicked);
            this.orca_system_button.clicked.connect(on_orca_system_clicked);
			this.nvda_user_button.clicked.connect(on_nvda_user_clicked);
            this.nvda_system_button.clicked.connect(on_nvda_system_clicked);
            this.macos_button.clicked.connect(on_macos_clicked);
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

        private void populate_config_combobox() {
            string[] configs = {_("Openbox"), _("nymph-TTS"), _("Orca"), _("NVDA"), _("macOS VoiceOver")};
            bool[] exists = {
                NymphOS.check_exists(),
                NymphTTS.check_exists(),
                Orca.check_exists(),
                NVDA.check_exists(),
                MacOS.check_exists()
            };

            for (int i = 0; i < configs.length; i++) {
                if (exists[i]) {
                    this.config_combobox.append_text(configs[i]);
                }
            }

			// Select first config if available
			if (this.config_combobox.get_model().get_n_items() > 0){
				this.config_combobox.set_active(0);
			}
        }

        private void on_config_changed(ComboBoxText widget) {
            this.current_config = widget.get_active_text();
            if (this.current_config != null) {
                switch (this.current_config) {
                    case _("Openbox"):
                        on_user_clicked(null); // Load nymph-OS user keybindings by default
                        break;
                    case _("nymph-TTS"):
                        load_nymph_tts_keybindings(false);
                        break;
                    case _("Orca"):
                        on_orca_user_clicked(null); // Load Orca user keybindings by default
                        break;
					case _("NVDA"):
                        on_nvda_user_clicked(null); // Load NVDA user keybindings by default
                        break;
					case _("macOS VoiceOver"):
						on_macos_clicked(null);
						break;
                }
            }
        }

		private void on_user_clicked(Button widget) {
            this.rcfile_path = NymphOS.user_config_path;
            load_keybindings();
        }

        private void on_system_clicked(Button widget) {
            if (Posix.geteuid() == 0) {
                this.rcfile_path = NymphOS.system_config_path;
                load_keybindings();
            } else {
                this.show_error_dialog(_("Root permissions required."));
            }
        }

		 private void on_restore_clicked(Button widget) {
            show_restore_dialog();
        }

        private void on_save_clicked(Button widget) {
            save_keybindings();
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
            string user_rcfile_path = NymphOS.user_config_path;
            string system_default_rcfile_path = NymphOS.system_default_config_path;

            if (!File.test(system_default_rcfile_path, FileTest.EXISTS)) {
                this.show_error_dialog(_("Default keybindings file not found."));
                return;
            }

            try {
                FileUtils.copy_file(system_default_rcfile_path, user_rcfile_path);
                this.show_status_message(_("User keybindings restored from system defaults."));
                load_keybindings();
            } catch (Error e) {
                this.show_error_dialog(_("Error restoring keybindings: ") + e.message);
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
                restore_keybindings();
            }
        }

		private void show_malformed_dialog(string message, string error_type) {
            var dialog = new MessageDialog(this, DialogFlags.MODAL, MessageType.WARNING, ButtonsType.NONE, message);
            dialog.add_buttons(Stock.EDIT, ResponseType.EDIT, Stock.RESTORE, ResponseType.RESTORE);
            dialog.accessible.name = _("Malformed config file");
            var response = dialog.run();
            dialog.destroy();

            if (response == ResponseType.EDIT) {
                try{
                    new Subprocess.with_argv({"xdg-open", this.rcfile_path}, SubprocessFlags.NONE);
                } catch (Error e){
                    this.show_error_dialog(_("Could not open file, xdg-open not found."));
                }

            } else if (response == ResponseType.RESTORE) {
                restore_keybindings();
            }
        }
/*
        private void on_orca_save_clicked(Button widget) {
            save_keybindings();
        }

		private void on_orca_add_clicked(Button widget) {
            this.liststore.append({"", "", ""});
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
                this.update_used_keys();
            }
        }

		private void on_orca_cell_edited(CellRendererText renderer, string path, string new_text, int col_num) {
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

		private bool is_orca_running(){
			try {
                new Subprocess.with_argv({"pidof", "orca"}, SubprocessFlags.NONE);
				return true;
            } catch (Error e){
                return false;
            }
		}
*/
    }
}
```
