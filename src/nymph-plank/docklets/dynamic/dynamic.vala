// dynamic.vala

#include <signal.h>
#include <unistd.h>

public static void docklet_init (Plank.DockletManager manager) {
    manager.register_docklet (typeof (DynamicDocklet.DynamicDockletDocklet));
}

namespace DynamicDocklet {

    public class DynamicDockletDocklet : Object, Plank.Docklet {

        private const string ID = "dynamic";
        private const string ICON = "application-x-executable";

        public unowned string get_id () { return ID; }
        public unowned string get_name () { return "Dynamic Dock Item"; }
        public unowned string get_description () { return "Runs a specified .desktop launcher."; }
        public unowned string get_icon () { return ICON; }
        public bool is_supported () { return true; }

        public Plank.DockElement make_element (string launcher, GLib.File file) {
            return new DynamicDocklet.DynamicDocklet.with_dockitem_file (file);
        }
    }

    public class DynamicDocklet : Plank.DockElement {

        public DynamicDocklet.with_dockitem_file (GLib.File file) {
            Object (dockitem_file: file);
            signal(SIGUSR1, signal_handler);
            save_pid();
            load_desktop_file ();
        }

        private void save_pid(){
            string desktop_file_path = Plank.DockPreferences.get_string (
                "DynamicDocklet.desktop_file",
                ""
            );
            if (!desktop_file_path.empty()) {
                try {
                    var file = GLib.File.new_for_path(desktop_file_path);
                    string file_name = file.get_basename();
                    string pid_file_name = file_name.replace(".desktop","");
                    pid_file_name = pid_file_name.replace_regex("[^a-zA-Z0-9]", "-");
                    string pid_file_path = "/tmp/nymph-plank-docklet-" + pid_file_name + ".pid";
                    int pid = getpid();
                    string pid_string = pid.to_string();
                    try {
                        FileStream pid_file = FileStream.open(pid_file_path, "w");
                        pid_file.puts(pid_string);
                        pid_file.close();
                    } catch (Error e) {
                        print("Error saving pid: %s\n", e.message);
                    }
                } catch (GLib.Error e) {
                    print("Error getting file name: %s\n", e.message);
                }
            }
        }

        private void load_desktop_file () {
            string desktop_file_path = Plank.DockPreferences.get_string (
                "DynamicDocklet.desktop_file",
                "" // Empty string, no default
            );

            if (desktop_file_path.empty()) {
                return; // Do not create button if no path is set
            }

            try {
                var desktop_file = GLib.DesktopAppInfo.new_from_filename (desktop_file_path);
                if (desktop_file != null) {
                    string icon_name = desktop_file.get_icon ();
                    string app_name = desktop_file.get_name ();

                    var button = new Gtk.Button ();
                    button.clicked.connect (on_button_clicked);
                    button.set_label (app_name); // Always set label

                    if (icon_name != null && !icon_name.empty ()) {
                        var icon = Gtk.IconTheme.get_default ().load_icon (icon_name, 24, Gtk.IconLookupFlags.GENERIC_FALLBACK);
                        if (icon != null) {
                            var image = new Gtk.Image.from_gicon (icon, Gtk.IconSize.MENU);
                            button.set_image (image);
                        }
                    }

                    add (button);
                    set_data ("desktop_file", desktop_file);
                } else {
                    display_notification ("Error: Could not load .desktop file.");
                }
            } catch (GLib.Error e) {
                display_notification ("Error: %s".printf (e.message));
            }
        }

        private void on_button_clicked () {
            var desktop_file = get_data ("desktop_file") as GLib.DesktopAppInfo;
            if (desktop_file != null) {
                try {
                    desktop_file.launch_default_for_uri (null, null);
                } catch (GLib.Error e) {
                    display_notification ("Error launching application: %s".printf (e.message));
                }
            }
        }

        private void display_notification (string message) {
            var notification = new GLib.Notification ("Dynamic Dock Item");
            notification.set_body (message);
            notification.set_priority (GLib.NotificationPriority.NORMAL);

            try {
                var app = Gtk.Application.get_default ();
                if (app != null) {
                    app.send_notification ("dynamic-dock-item-error", notification);
                }
            } catch (GLib.Error e) {
                print("Error displaying notification: %s\n", e.message);
            }
        }

        void signal_handler(int signum) {
            if (signum == SIGUSR1) {
                refresh_menu();
            }
        }

        void refresh_menu() {
            string desktop_file_path = Plank.DockPreferences.get_string (
                "DynamicDocklet.desktop_file",
                ""
            );

            if (!desktop_file_path.empty()) {
                try {
                    var desktop_file = GLib.DesktopAppInfo.new_from_filename(desktop_file_path);
                    if (desktop_file != null) {
                        desktop_file.launch_default_for_uri (null, null);
                    }
                } catch (GLib.Error e) {
                    print("Error refreshing menu: %s\n", e.message);
                }
            }
        }
    }
}
