using Gtk;
using System;
using Gettext;

namespace NymphPowerMenu {

    public class MainWindow : Window {

        public MainWindow() {
            Title = _("Nymph Power Menu");
            BorderWidth = 10;
            WindowPosition = WindowPosition.CENTER;
            Destroy.connect(Gtk.main_quit);

            var hbox = new Box(Orientation.HORIZONTAL, 10);
            add(hbox);

            var logoutButton = new Button.with_label(_("Log Out"));
            logoutButton.clicked.connect(onLogoutClicked);
            hbox.pack_start(logoutButton, false, false, 0);

            var shutdownButton = new Button.with_label(_("Shut Down"));
            shutdownButton.clicked.connect(onShutdownClicked);
            hbox.pack_start(shutdownButton, false, false, 0);

            var rebootButton = new Button.with_label(_("Reboot"));
            rebootButton.clicked.connect(onRebootClicked);
            hbox.pack_start(rebootButton, false, false, 0);
        }

        private void onLogoutClicked(Button button) {
            try {
                var process = new Subprocess.with_argv({"openbox", "--exit"}, SubprocessFlags.LEAVE_STDERR_OPEN);
                process.wait();
            } catch (Error e) {
                stderr.printf("Error: %s\n", e.message);
            }
            Gtk.main_quit();
        }

        private void onShutdownClicked(Button button) {
            try {
                var process = new Subprocess.with_argv({"sudo", "shutdown", "-P", "now"}, SubprocessFlags.LEAVE_STDERR_OPEN);
                process.wait();
            } catch (Error e) {
                stderr.printf("Error: %s\n", e.message);
            }
            Gtk.main_quit();
        }

        private void onRebootClicked(Button button) {
            try {
                var process = new Subprocess.with_argv({"sudo", "reboot"}, SubprocessFlags.LEAVE_STDERR_OPEN);
                process.wait();
            } catch (Error e) {
                stderr.printf("Error: %s\n", e.message);
            }
            Gtk.main_quit();
        }
    }

    public static int main(string[] args) {
        Locale.bindtextdomain("nymph-power-menu", Environment.get_locale_dir());
        Locale.bind_textdomain_codeset("nymph-power-menu", "UTF-8");
        Locale.textdomain("nymph-power-menu");

        Gtk.init(ref args);
        var window = new MainWindow();
        window.show_all();
        Gtk.main();
        return 0;
    }
}
