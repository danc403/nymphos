using Gtk;
using System;
using System.IO;
using System.Collections.Generic;
using Gettext;
using System.Diagnostics;

namespace NymphWallpaperSwitcher {

    public class MainWindow : Window {

        private ComboBoxText wallpaper_combo;
        private Button apply_button;
        private string user_config_dir;
        private string user_config_file;
        private string system_config_dir;
        private string system_config_file;
        private string user_autostart_file;
        private string system_autostart_file;
        private string openbox_autostart_file;
        private string current_wallpaper;
        private List<string> wallpaper_paths;
        private Image preview_image;
        private CheckButton system_wide_checkbox;

        public MainWindow() {
            Title = _("Nymph Wallpaper Switcher");
            BorderWidth = 10;
            SetDefaultSize(600, 300);
            WindowPosition = WindowPosition.Center;

            var vbox = new Box(Orientation.VERTICAL, 5);
            Add(vbox);

            var hbox = new Box(Orientation.HORIZONTAL, 5);
            vbox.PackStart(hbox, false, false, 0);

            var vbox_left = new Box(Orientation.VERTICAL, 5);
            hbox.PackStart(vbox_left, false, false, 0);

            wallpaper_combo = new ComboBoxText();
            vbox_left.PackStart(wallpaper_combo, false, false, 0);

            apply_button = new Button.WithLabel(_("Apply Wallpaper"));
            vbox_left.PackStart(apply_button, false, false, 0);

            system_wide_checkbox = new CheckButton(_("Set for all users"));
            vbox_left.PackStart(system_wide_checkbox, false, false, 0);

            preview_image = new Image();
            hbox.PackStart(preview_image, true, true, 0);

            apply_button.Clicked += OnApplyClicked;
            wallpaper_combo.Changed += OnWallpaperChanged;
            system_wide_checkbox.Toggled += OnSystemWideToggled;

            user_config_dir = Path.Combine(Environment.GetEnvironmentVariable("XDG_CONFIG_HOME") ?? Path.Combine(Environment.GetEnvironmentVariable("HOME"), ".config"), "nymph-wallpaper-switcher");
            user_config_file = Path.Combine(user_config_dir, "config");
            user_autostart_file = Path.Combine(user_config_dir, "autostart.sh");

            system_config_dir = "/etc/nymph-wallpaper-switcher";
            system_config_file = Path.Combine(system_config_dir, "config");
            system_autostart_file = Path.Combine(system_config_dir, "autostart.sh");

            openbox_autostart_file = Path.Combine(Environment.GetEnvironmentVariable("XDG_CONFIG_HOME") ?? Path.Combine(Environment.GetEnvironmentVariable("HOME"), ".config"), "openbox", "autostart.sh");

            ensure_config_files_exist();
            ensure_autostart_files_exist();

            load_wallpapers();
            load_current_wallpaper();
            update_preview();
        }

        private void ensure_config_files_exist() {
            if (!Directory.Exists(user_config_dir)) {
                Directory.CreateDirectory(user_config_dir);
            }
            if (!File.Exists(user_config_file)) {
                try {
                    using (var writer = new StreamWriter(user_config_file)) {
                        writer.WriteLine("[wallpaper]");
                        writer.WriteLine("path=");
                    }
                } catch (Exception ex) {
                    Console.Error.WriteLine($"Error creating user config file: {ex.Message}");
                }
            }

            if (system_wide_checkbox.Active) {
                if (!Directory.Exists(system_config_dir)) {
                    try {
                        Directory.CreateDirectory(system_config_dir);
                    } catch (Exception ex) {
                        Console.Error.WriteLine($"Error creating system config directory: {ex.Message}");
                    }
                }
                if (!File.Exists(system_config_file)) {
                    try {
                        using (var writer = new StreamWriter(system_config_file)) {
                            writer.WriteLine("[wallpaper]");
                            writer.WriteLine("path=");
                        }
                    } catch (Exception ex) {
                        Console.Error.WriteLine($"Error creating system config file: {ex.Message}");
                    }
                }
            }
        }

        private void ensure_autostart_files_exist() {
            if (!File.Exists(user_autostart_file)) {
                try {
                    using (var writer = new StreamWriter(user_autostart_file)) {
                        writer.WriteLine("#!/bin/bash");
                        writer.WriteLine($"feh --bg-scale $(grep -Po '(?<=path=).*' {user_config_file}) &");
                    }
                    File.SetAttributes(user_autostart_file, File.GetAttributes(user_autostart_file) | FileAttributes.Hidden);
                    File.SetAttributes(user_autostart_file, File.GetAttributes(user_autostart_file) | FileAttributes.ReadOnly);
                } catch (Exception ex) {
                    Console.Error.WriteLine($"Error creating user autostart file: {ex.Message}");
                }
            }

            if (system_wide_checkbox.Active) {
                if (!File.Exists(system_autostart_file)) {
                    try {
                        using (var writer = new StreamWriter(system_autostart_file)) {
                            writer.WriteLine("#!/bin/bash");
                            writer.WriteLine($"feh --bg-scale $(grep -Po '(?<=path=).*' {system_config_file}) &");
                        }
                        File.SetAttributes(system_autostart_file, File.GetAttributes(system_autostart_file) | FileAttributes.Hidden);
                        File.SetAttributes(system_autostart_file, File.GetAttributes(system_autostart_file) | FileAttributes.ReadOnly);
                    } catch (Exception ex) {
                        Console.Error.WriteLine($"Error creating system autostart file: {ex.Message}");
                    }
                }
            }

            // Ensure the autostart file is linked to Openbox's autostart
            if (!File.Exists(openbox_autostart_file) || !File.ReadAllText(openbox_autostart_file).Contains(user_autostart_file)) {
                try {
                    using (var writer = new StreamWriter(openbox_autostart_file, true)) {
                        writer.WriteLine($"sh {user_autostart_file}");
                    }
                } catch (Exception ex) {
                    Console.Error.WriteLine($"Error updating Openbox autostart file: {ex.Message}");
                }
            }

            if (system_wide_checkbox.Active) {
                if (!File.Exists(openbox_autostart_file) || !File.ReadAllText(openbox_autostart_file).Contains(system_autostart_file)) {
                    try {
                        using (var writer = new StreamWriter(openbox_autostart_file, true)) {
                            writer.WriteLine($"sudo sh {system_autostart_file}");
                        }
                    } catch (Exception ex) {
                        Console.Error.WriteLine($"Error updating Openbox autostart file for system-wide: {ex.Message}");
                    }
                }
            }
        }

        private void load_wallpapers() {
            wallpaper_paths = new List<string>();
            var data_dirs = Environment.GetEnvironmentVariable("XDG_DATA_DIRS").Split(':');
            foreach (var data_dir in data_dirs) {
                var wallpapers_dir = Path.Combine(data_dir, "wallpapers");
                if (Directory.Exists(wallpapers_dir)) {
                    foreach (var file in Directory.GetFiles(wallpapers_dir)) {
                        if (is_image_file(file)) {
                            wallpaper_paths.Add(file);
                            wallpaper_combo.AppendText(Path.GetFileName(file));
                        }
                    }
                }
            }
        }

        private bool is_image_file(string file_path) {
            var ext = Path.GetExtension(file_path).ToLower();
            return ext == ".png" || ext == ".jpg" || ext == ".jpeg" || ext == ".gif";
        }

        private void load_current_wallpaper() {
            if (system_wide_checkbox.Active && File.Exists(system_config_file)) {
                try {
                    using (var reader = new StreamReader(system_config_file)) {
                        var line = reader.ReadLine();
                        if (line != null && line.StartsWith("path=")) {
                            current_wallpaper = line.Substring(5);
                            var index = wallpaper_paths.IndexOf(current_wallpaper);
                            if (index >= 0) {
                                wallpaper_combo.Active = index;
                            }
                        }
                    }
                } catch (Exception ex) {
                    Console.Error.WriteLine($"Error reading system-wide current wallpaper: {ex.Message}");
                }
            } else if (File.Exists(user_config_file)) {
                try {
                    using (var reader = new StreamReader(user_config_file)) {
                        var line = reader.ReadLine();
                        if (line != null && line.StartsWith("path=")) {
                            current_wallpaper = line.Substring(5);
                            var index = wallpaper_paths.IndexOf(current_wallpaper);
                            if (index >= 0) {
                                wallpaper_combo.Active = index;
                            }
                        }
                    }
                } catch (Exception ex) {
                    Console.Error.WriteLine($"Error reading user current wallpaper: {ex.Message}");
                }
            }
        }

        private void OnApplyClicked(object sender, EventArgs e) {
            var index = wallpaper_combo.Active;
            if (index >= 0) {
                var wallpaper_path = wallpaper_paths[index];
                try {
                    set_wallpaper(wallpaper_path);
                    update_config(wallpaper_path);
                    current_wallpaper = wallpaper_path;
                } catch (Exception ex) {
                    var dialog = new MessageDialog(this, DialogFlags.Modal, MessageType.Error, ButtonsType.Ok, _("Error setting wallpaper: {0}").Replace("{0}", ex.Message));
                    dialog.Run();
                    dialog.Destroy();
                }
            }
        }

        private void OnWallpaperChanged(object sender, EventArgs e) {
            update_preview();
        }

        private void OnSystemWideToggled(object sender, EventArgs e) {
            ensure_config_files_exist();
            ensure_autostart_files_exist();
        }

        private void update_preview() {
            var index = wallpaper_combo.Active;
            if (index >= 0) {
                var wallpaper_path = wallpaper_paths[index];
                try {
                    preview_image.Pixbuf = new Gdk.Pixbuf(wallpaper_path);
                } catch (Exception ex) {
                    Console.Error.WriteLine($"Error loading preview: {ex.Message}");
                    preview_image.Clear();
                }
            } else {
                preview_image.Clear();
            }
        }

        private void set_wallpaper(string file_path) {
            // Use feh for Openbox
            string command = $"feh --bg-scale \"{file_path}\"";
            try {
                using (var process = new Process()) {
                    process.StartInfo.FileName = "bash";
                    process.StartInfo.Arguments = $"-c \"{command}\"";
                    process.Start();
                }
            } catch (Exception ex) {
                throw new Exception($"Error setting wallpaper: {ex.Message}");
            }
        }

        private void update_config(string wallpaper_path) {
            if (system_wide_checkbox.Active) {
                try {
                    using (var writer = new StreamWriter(system_config_file, false)) {
                        writer.WriteLine($"[wallpaper]");
                        writer.WriteLine($"path={wallpaper_path}");
                    }
                } catch (Exception ex) {
                    Console.Error.WriteLine($"Error updating system-wide configuration: {ex.Message}");
                }
            }

            try {
                using (var writer = new StreamWriter(user_config_file, false)) {
                    writer.WriteLine($"[wallpaper]");
                    writer.WriteLine($"path={wallpaper_path}");
                }
            } catch (Exception ex) {
                Console.Error.WriteLine($"Error updating user configuration: {ex.Message}");
            }
        }
    }

    public static class Program {
        public static int Main(string[] args) {
            Locale.Bindtextdomain("nymph-wallpaper-switcher", Environment.GetEnvironmentVariable("LOCALEDIR") ?? "/usr/share/locale");
            Locale.Textdomain("nymph-wallpaper-switcher");

            Gtk.Application.Init();
            var window = new MainWindow();
            window.Destroyed += Gtk.Application.Quit;
            window.ShowAll();
            Gtk.Application.Run();
            return 0;
        }
    }
}
