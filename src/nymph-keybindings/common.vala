using Gtk;
using GLib;
using Gee;

namespace KeybindingEditor {

    public enum ConfigType {
        NYMPH_OS,
        NYMPH_TTS,
        ORCA,
        NVDA,
        MACOS
    }

    public static class Config {
        public const string GETTEXT_PACKAGE = "keybinding-editor";
        public const string LOCALEDIR = "/usr/share/locale";
    }

    public class FilePath {
        public static string build_filename(string basedir, string filename) {
            return Path.build_filename(basedir, filename);
        }
    }

    // Helper function to show error dialogs
    public delegate void ShowErrorDialog(string message);

    // Helper function to show status messages
    public delegate void ShowStatusMessage(string message);
}
