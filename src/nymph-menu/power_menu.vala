/* power_menu.vala */

using Gtk;

int main (string[] args) {
    Gtk.init (ref args);

    var window = new Window (WindowType.TOPLEVEL);
    window.title = "Power Menu";
    window.border_width = 10;
    window.window_position = WindowPosition.CENTER;
    window.destroy.connect (Gtk.main_quit);

    var hbox = new HBox (false, 10); // Spacing of 10 pixels
    window.add (hbox);

    var logout_button = new Button.with_label ("Log Out");
    logout_button.clicked.connect (() => {
        try {
            var process = new Subprocess.with_argv ({"openbox", "--exit"}, SubprocessFlags.LEAVE_STDERR_OPEN);
            process.wait ();
        } catch (Error e) {
            stderr.printf ("Error: %s\n", e.message);
        }
        Gtk.main_quit ();
    });
    hbox.pack_start (logout_button, false, false, 0);

    var shutdown_button = new Button.with_label ("Shut Down");
    shutdown_button.clicked.connect (() => {
        try {
            var process = new Subprocess.with_argv ({"sudo", "shutdown", "-P", "now"}, SubprocessFlags.LEAVE_STDERR_OPEN);
            process.wait ();
        } catch (Error e) {
            stderr.printf ("Error: %s\n", e.message);
        }
        Gtk.main_quit ();
    });
    hbox.pack_start (shutdown_button, false, false, 0);

    var reboot_button = new Button.with_label ("Reboot");
    reboot_button.clicked.connect (() => {
        try {
            var process = new Subprocess.with_argv ({"sudo", "reboot"}, SubprocessFlags.LEAVE_STDERR_OPEN);
            process.wait ();
        } catch (Error e) {
            stderr.printf ("Error: %s\n", e.message);
        }
        Gtk.main_quit ();
    });
    hbox.pack_start (reboot_button, false, false, 0);

    window.show_all ();

    Gtk.main ();

    return 0;
}
