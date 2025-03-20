using Gtk;
using GLib;
using Gio;

public class ApplicationWindow : Gtk.Window {

    private ListStore desktop_file_list;
    private TreeView desktop_file_treeview;
    private IconView desktop_file_iconview;
    private Button launch_button;
    private Button cancel_button;
    private string selected_desktop_file_path;
    private Notebook notebook;

    public ApplicationWindow() {
        // Window Setup
        title = "Application Launcher";
        window_position = WindowPosition.CENTER;
        border_width = 10;
        default_width = 400;
        default_height = 300;

        // Accessibility: Window Description
        accessible.role = AccessibleRole.DIALOG;
        accessible.description = "Select an application to launch from the list.";

        // Create the main vertical box
        var main_vbox = new Box(Orientation.VERTICAL, 6); // Spacing of 6 pixels
        add(main_vbox);

        // Label
        var label = new Label("Select an application:");
        label.xalign = 0; // Align left
        main_vbox.pack_start(label, false, false, 0);

        // Create the ListStore to hold desktop file information
        // Columns: Icon (Gdk.Pixbuf), Display Name (string), File Path (string)
        desktop_file_list = new ListStore(3, typeof(Gdk.Pixbuf), typeof(string), typeof(string));

        // Create the Notebook for TreeView and IconView
        notebook = new Notebook();
        main_vbox.pack_start(notebook, true, true, 0);

        // --- TreeView ---
        desktop_file_treeview = new TreeView(desktop_file_list);
        desktop_file_treeview.headers_visible = false;  // Hide column headers
        desktop_file_treeview.search_column = 1; // Enable searching on display name

        // Accessibility: Treeview Description
        desktop_file_treeview.accessible.role = AccessibleRole.LIST;
        desktop_file_treeview.accessible.description = "List of available applications. Use arrow keys to navigate and enter to select.";

        // Create a column for the application icons
        var icon_column = new TreeViewColumn();
        var icon_cell = new CellRendererPixbuf();
        icon_column.pack_start(icon_cell, false);
        icon_column.add_attribute(icon_cell, "pixbuf", 0); // Map column 0 of the ListStore to the "pixbuf" property
        desktop_file_treeview.append_column(icon_column);

        // Create a column for the application names
        var name_column = new TreeViewColumn();
        var name_cell = new CellRendererText();
        name_column.pack_start(name_cell, true);
        name_column.add_attribute(name_cell, "text", 1); // Map column 1 of the ListStore to the "text" property
        desktop_file_treeview.append_column(name_column);

        // Scrollable Window for TreeView
        var treeview_scrolled_window = new ScrolledWindow(null, null);
        treeview_scrolled_window.hscrollbar_policy = PolicyType.NEVER;
        treeview_scrolled_window.vscrollbar_policy = PolicyType.AUTOMATIC;
        treeview_scrolled_window.add(desktop_file_treeview);
        notebook.append_page(treeview_scrolled_window, new Label("Tree View"));

        // --- IconView ---
        desktop_file_iconview = new IconView(desktop_file_list);
        desktop_file_iconview.set_pixbuf_column(0);
        desktop_file_iconview.set_text_column(1);
        desktop_file_iconview.selection_mode = SelectionMode.SINGLE;

        // Accessibility: Iconview Description
        desktop_file_iconview.accessible.role = AccessibleRole.LIST;
        desktop_file_iconview.accessible.description = "List of available applications displayed as icons. Use arrow keys to navigate and enter to select.";

        // Scrollable Window for IconView
        var iconview_scrolled_window = new ScrolledWindow(null, null);
        iconview_scrolled_window.hscrollbar_policy = PolicyType.AUTOMATIC;
        iconview_scrolled_window.vscrollbar_policy = PolicyType.AUTOMATIC;
        iconview_scrolled_window.add(desktop_file_iconview);
        notebook.append_page(iconview_scrolled_window, new Label("Icon View"));


        // Create a Horizontal Box for the Buttons
        var button_hbox = new Box(Orientation.HORIZONTAL, 6); // Spacing of 6 pixels
        button_hbox.halign = Align.END; // Align buttons to the right
        main_vbox.pack_start(button_hbox, false, false, 0);

        // Create the Launch Button
        launch_button = new Button.with_label("Launch");
        launch_button.sensitive = false; // Initially disabled until an item is selected

        // Accessibility: Launch Button Description
        launch_button.accessible.role = AccessibleRole.PUSH_BUTTON;
        launch_button.accessible.description = "Launch the selected application.";

        launch_button.clicked.connect(() => {
            if (!string.is_empty(selected_desktop_file_path)) {
                launch_application(selected_desktop_file_path);
            }
        });
        button_hbox.pack_end(launch_button, false, false, 0);

        // Create the Cancel Button
        cancel_button = new Button.with_label("Cancel");

        // Accessibility: Cancel Button Description
        cancel_button.accessible.role = AccessibleRole.PUSH_BUTTON;
        cancel_button.accessible.description = "Close the application launcher.";

        cancel_button.clicked.connect(() => {
            destroy();
        });
        button_hbox.pack_end(cancel_button, false, false, 0);

        // Selection Changed signals for both TreeView and IconView
        desktop_file_treeview.selection.changed.connect(() => {
            update_selected_path_and_button_state(desktop_file_treeview);
        });

        desktop_file_iconview.selection_changed.connect(() => {
            update_selected_path_and_button_state(desktop_file_iconview);
        });

        // Load desktop files
        load_desktop_files();

        // Handle key presses for accessibility and keyboard navigation
        key_press_event.connect((widget, event) => {
            if (event.keyval == Keyval.Return || event.keyval == Keyval.KP_Enter) {
                if (launch_button.sensitive) {
                    launch_button.clicked(); // Simulate a button click
                    return true; // Consume the event
                }
            } else if (event.keyval == Keyval.Escape) {
                cancel_button.clicked(); // Simulate a button click
                return true; // Consume the event
            }
            return false; // Allow other handlers to process the event
        });

        // Focus the currently active view on startup for keyboard navigation
        realize.connect(() => {
            if (notebook.page == 0) {
                desktop_file_treeview.grab_focus();
            } else {
                desktop_file_iconview.grab_focus();
            }
        });

        notebook.switch_page.connect((notebook, page_num) => {
            if (page_num == 0) {
                desktop_file_treeview.grab_focus();
            } else {
                desktop_file_iconview.grab_focus();
            }
        });

        show_all();
    }

    private void update_selected_path_and_button_state(Widget widget) {
        TreeIter iter;
        TreeModel model;

        if (widget is TreeView) {
            if (((TreeView)widget).selection.get_selected(out model, out iter)) {
                selected_desktop_file_path = model.get_value(iter, 2) as string; // Get filepath from column 2
                launch_button.sensitive = !string.is_empty(selected_desktop_file_path);
            } else {
                selected_desktop_file_path = null;
                launch_button.sensitive = false;
            }
        } else if (widget is IconView) {
            TreePath[] selected_paths = ((IconView)widget).get_selected_items();
            if (selected_paths.length > 0) {
                TreeIter iconview_iter;
                desktop_file_list.get_iter(out iconview_iter, selected_paths[0]);
                selected_desktop_file_path = desktop_file_list.get_value(iconview_iter, 2) as string;
                launch_button.sensitive = !string.is_empty(selected_desktop_file_path);
            } else {
                selected_desktop_file_path = null;
                launch_button.sensitive = false;
            }

            foreach (TreePath path in selected_paths) {
                path.free();
            }
        } else {
            selected_desktop_file_path = null;
            launch_button.sensitive = false;
        }
    }


    private string[] get_desktop_files() {
        string[] desktop_files = {};

        // User-specific desktop files (priority)
        string user_dir = Path.build_filename(Environment.get_home_dir(), ".local", "share", "applications");
        try {
            var files = Dir.list_dir(user_dir, 0);
            foreach (string file in files) {
                if (file.has_suffix(".desktop")) {
                    desktop_files += Path.build_filename(user_dir, file);
                }
            }
        } catch (Error e) {
            stderr.printf("Error reading directory %s: %s\n", user_dir, e.message);
        }

        // System-wide desktop files
        string[] system_paths = {
            "/usr/share/applications",
            "/usr/local/share/applications"
        };

        foreach (string path in system_paths) {
            try {
                var files = Dir.list_dir(path, 0);
                foreach (string file in files) {
                    if (file.has_suffix(".desktop")) {
                        desktop_files += Path.build_filename(path, file);
                    }
                }
            } catch (Error e) {
                stderr.printf("Error reading directory %s: %s\n", path, e.message);
            }
        }

        // Return the list of desktop files (deduplicated)
        return desktop_files.to_set().to_array();
    }

    private void load_desktop_files() {
        string[] desktop_files = get_desktop_files();

        foreach (string path in desktop_files) {
            try {
                var desktop_entry = new DesktopAppInfo(path);
                if (desktop_entry.is_nodisplay() || desktop_entry.is_hidden()) {
                    continue; // Skip NoDisplay and Hidden entries
                }
                string? name = desktop_entry.get_name();
                if (name == null) {
                    continue; // Filter out any entries with no Name
                }

                Gdk.Pixbuf icon = get_icon_for_desktop_entry(desktop_entry);

                desktop_file_list.append([icon, name, path]);
            } catch (Error e) {
                stderr.printf("Error loading desktop file %s: %s\n", path, e.message);
            }
        }
    }

    private Gdk.Pixbuf get_icon_for_desktop_entry(DesktopAppInfo desktop_entry) {
        string? icon_name = desktop_entry.get_icon_name();

        if (icon_name == null || icon_name == "") {
            return get_default_icon();
        }
        
        Gdk.Pixbuf? icon = null;

        // Try to load icon from user's home directory first
        string user_icon_path = Path.build_filename(Environment.get_home_dir(), ".icons", icon_name + ".png");
        if (File.test(user_icon_path, FileTest.EXISTS)) {
            try {
                icon = new Gdk.Pixbuf.from_file_at_size(user_icon_path, 24, 24);
                return icon;
            } catch (Error e) {
                stderr.printf("Error loading user icon %s: %s\n", user_icon_path, e.message);
            }
        }

        user_icon_path = Path.build_filename(Environment.get_home_dir(), ".icons", icon_name + ".svg");
        if (File.test(user_icon_path, FileTest.EXISTS)) {
            try {
                icon = new Gdk.Pixbuf.from_file_at_size(user_icon_path, 24, 24);
                return icon;
            } catch (Error e) {
                stderr.printf("Error loading user icon %s: %s\n", user_icon_path, e.message);
            }
        }


        // Fallback to system icon theme
        try {
            icon = IconTheme.get_default().load_icon(icon_name, 24, IconLookupFlags.FORCE_SIZE);
            if (icon != null) {
                return icon;
            }
        } catch (Error e) {
            stderr.printf("Error loading icon %s from theme: %s\n", icon_name, e.message);
        }
        
        //If all else fails, return a default icon
        return get_default_icon();
    }


    private Gdk.Pixbuf get_default_icon() {
          try {
            // Attempt to load the "application-x-executable" icon from the system theme.
            Gdk.Pixbuf? icon = IconTheme.get_default().load_icon("application-x-executable", 24, IconLookupFlags.FORCE_SIZE);
            if (icon != null) {
                return icon;
            }
          } catch (Error e) {
             stderr.printf("Error loading default icon from theme: %s\n", e.message);
             // Fallback to a hardcoded path only as a last resort, as this may not exist on all systems
             try {
               return new Gdk.Pixbuf.from_file("/usr/share/icons/gnome/24x24/apps/application-default-icon.png");  //fallback to standard icon, might not work on all systems.
            } catch (Error e2) {
                 stderr.printf("Error loading fallback icon: %s\n", e2.message);
                 // Return a tiny transparent pixbuf as a last resort to avoid crashing
                  return new Gdk.Pixbuf(Colorspace.RGB, true, 8, 1, 1).fill(0x00000000);
             }


          }

         // If the icon isn't found and no exception occurred, create a tiny transparent pixbuf
        return new Gdk.Pixbuf(Colorspace.RGB, true, 8, 1, 1).fill(0x00000000);

     }



    private void launch_application(string desktop_file_path) {
        try {
            var app_info = Gio.DesktopAppInfo.new_from_filename(desktop_file_path);
            if (app_info != null) {
                app_info.launch(new List<Gio.File>(), null);
                destroy(); // Close the application launcher after launching
            } else {
                throw new IOError.FAILED("Failed to create Gio.DesktopAppInfo from file.");
            }
        } catch (Error e) {
            stderr.printf("Error launching application: %s\n", e.message);

            // Show an error dialog
            var dialog = new MessageDialog(this, DialogFlags.MODAL, MessageType.ERROR, ButtonsType.OK, "Error launching application: %s", e.message);
            dialog.run();
            dialog.destroy();
        }
    }
}

public class DesktopAppInfo : GLib.Object, Gio.AppInfo {
    private string desktop_file_path;
    private Gio.DesktopAppInfo app_info;

    public DesktopAppInfo(string path) {
        desktop_file_path = path;
        try {
            app_info = Gio.DesktopAppInfo.new_from_filename(path);
            if (app_info == null) {
                throw new IOError.FAILED("Failed to create Gio.DesktopAppInfo from file.");
            }
        } catch (Error e) {
            stderr.printf("Error parsing desktop file %s: %s\n", path, e.message);
            throw e;
        }
    }

    public string? get_name() {
        return app_info.get_display_name();
    }

    public bool is_nodisplay() {
        return app_info.get_nodisplay();
    }

    public bool is_hidden() {
        return app_info.get_hidden();
    }

    public string[] get_categories() {
        return app_info.get_categories();
    }

    public string? get_icon_name() {
        return app_info.get_icon();
    }

    // Implement the Gio.AppInfo interface methods.
    public string get_id() { return app_info.get_id(); }
    public string get_executable() { return app_info.get_executable(); }
    public bool launch(File[] files, GLib.LaunchContext? context) { return app_info.launch(files, context); }
    public bool launch_uris(string[] uris, GLib.LaunchContext? context) { return app_info.launch_uris(uris, context); }
    public Icon get_icon() { return app_info.get_icon(); }
    public bool supports_uris() { return app_info.supports_uris(); }
    public bool supports_files() { return app_info.supports_files(); }
    public string get_description() { return app_info.get_description(); }
    public string get_display_name() { return app_info.get_display_name(); }
    public string get_commandline() { return app_info.get_commandline(); }
    public bool set_as_default_for_type(string content_type) { return app_info.set_as_default_for_type(content_type); }
    public bool set_as_default_for_uri_scheme(string uri_scheme) { return app_info.set_as_default_for_uri_scheme(uri_scheme); }
    public void add_supports_type(string content_type) { app_info.add_supports_type(content_type); }
    public void remove_supports_type(string content_type) { app_info.remove_supports_type(content_type); }
    public bool will_handle_uri(string uri) { return app_info.will_handle_uri(uri); }
    public bool can_delete() { return app_info.can_delete(); }
    public void delete() { app_info.delete(); }
    public bool set_attribute(string key, GLib.Variant value) { return app_info.set_attribute(key, value); }
    public GLib.Variant get_attribute(string key) { return app_info.get_attribute(key); }
    public bool equal(Gio.AppInfo other) { return app_info.equal(other); }
}

public static int main(string[] args) {
    Gtk.init(ref args);

    var app = new ApplicationWindow();
    app.destroy.connect(Gtk.main_quit); // Quit main loop on window close

    Gtk.main();
    return 0;
}
