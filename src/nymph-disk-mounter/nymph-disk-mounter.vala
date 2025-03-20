/*
 * nymph-disk-mounter.vala - A GTK3 application to mount and manage disks.
 *
 * Copyright (C) 2024
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

using Gtk;
using GLib;
using Gee;
using System;
using System.Text.RegularExpressions;

namespace NymphDiskMounter {

    const string DISPLAY_OPTIONS_FILE = "/tmp/nymph-disk-mounter_display_options";
    const string APP_ID = "com.example.nymph-disk-mounter";

    //Localization domain
    const string GETTEXT_PACKAGE = "nymph-disk-mounter";

    // Define Gettext domain to use
    [CCode (cprefix = "", lower_case_cprefix = "")]
    extern string gettext (string msgid);
    [CCode (cprefix = "", lower_case_cprefix = "")]
    extern string dgettext (string domainname, string msgid);
    [CCode (cprefix = "", lower_case_cprefix = "")]
    extern string dcgettext (string domainname, string msgid, int category);
    [CCode (cprefix = "", lower_case_cprefix = "")]
    extern string ngettext (string msgid, string msgid_plural, ulong n);
    [CCode (cprefix = "", lower_case_cprefix = "")]
    extern string dngettext (string domainname, string msgid, string msgid_plural, ulong n);
    [CCode (cprefix = "", lower_case_cprefix = "")]
    extern string dcngettext (string domainname, string msgid, string msgid_plural, ulong n, int category);
    [CCode (cprefix = "", lower_case_cprefix = "")]
    extern string bindtextdomain (string domainname, string dirname);
    [CCode (cprefix = "", lower_case_cprefix = "")]
    extern string textdomain (string domainname);
    [CCode (cprefix = "", lower_case_cprefix = "")]
    extern string bind_textdomain_codeset (string domainname, string codeset);


    public class Application : Gtk.Application {

        private string? removable_regex;
        private string? optical_regex;
        private bool show_internal;
        private string[] blacklist;
        private string? filemanager;
        private string removable_display;
        private string optical_display;
        private Window? main_window;

        public Application() {
            Object(application_id: APP_ID,
                   flags: ApplicationFlags.FLAGS_NONE);
            bindtextdomain(GETTEXT_PACKAGE, "/usr/share/locale");
            textdomain(GETTEXT_PACKAGE);
            removable_regex = get_removable_regex();
            optical_regex = get_optical_regex();
            show_internal = get_show_internal();
            blacklist = get_blacklist();
            filemanager = get_filemanager();
            string[] display_options = get_display_options();
            removable_display = display_options[0];
            optical_display = display_options[1];
        }

        protected override void activate() {
            if (main_window == null) {
                create_window();
            }
            main_window.present();
        }

        private void create_window() {
            main_window = new Window(WindowType.TOPLEVEL);
            main_window.title = dgettext (GETTEXT_PACKAGE, "Disk Mounter");
            main_window.window_position = WindowPosition.CENTER;
            main_window.destroy.connect(() => {
                main_window = null;
            });
            main_window.set_default_size(300, 400);

            var vbox = new Box(Orientation.VERTICAL, 5);
            main_window.add(vbox);

            // Display Options Menu
            var display_options_menu = new Menu();
            var show_removable_filename = new MenuItem.with_label(dgettext (GETTEXT_PACKAGE, "Show Removable Filename"));
            show_removable_filename.set_use_underline(true); // For accessibility
            show_removable_filename.activate.connect(() => {
                removable_display = (removable_display == "label") ? "filename" : "label";
                set_display_options(removable_display, optical_display);
                create_window(); // Recreate window to refresh the list
                main_window.show_all();
            });
            display_options_menu.append(show_removable_filename);

            var show_optical_filename = new MenuItem.with_label(dgettext (GETTEXT_PACKAGE, "Show Optical Filename"));
            show_optical_filename.set_use_underline(true); // For accessibility
            show_optical_filename.activate.connect(() => {
                optical_display = (optical_display == "label") ? "filename" : "label";
                set_display_options(removable_display, optical_display);
                create_window(); // Recreate window to refresh the list
                main_window.show_all();
            });
            display_options_menu.append(show_optical_filename);

            var display_options_button = new MenuButton {
                label = dgettext (GETTEXT_PACKAGE, "Display Options"),
                popup = display_options_menu,
                use_underline = true
            };
            vbox.pack_start(display_options_button, false, false, 0);

            // Removable Devices
            var removable_label = new Label(dgettext (GETTEXT_PACKAGE, "Removable Media"));
            removable_label.set_xalign(0);
            vbox.pack_start(removable_label, false, false, 0);

            var removable_devices = get_devices(removable_regex);
            removable_devices = fancy_sort(removable_devices);

            var mounted_removable = new List<string>();
            int total_removable = 0;

            foreach (var device in removable_devices) {
                total_removable++;
                string devmajor = Regex.replace(device, @"[0-9]+$", "");
                string? internal_str = get_device_info(devmajor, "system internal");
                bool internal = (internal_str != null && internal_str == "1");
                if (internal && !show_internal) {
                    continue;
                }

                bool skip = false;
                string info = run_command(new string[] {"udisks", "--show-info", device});
                if(info != null) {
                    foreach (string bl in blacklist) {
                        if (info.contains(bl)) {
                            skip = true;
                            break;
                        }
                    }
                }

                if (skip) {
                    continue;
                }

                string? label = get_device_info(device, "label");
                if (label == null) label = get_device_info(devmajor, "model");
                if (label == null) label = get_device_info(devmajor, "vendor");
                if (label == null) label = dgettext (GETTEXT_PACKAGE, "No label");
                if (get_device_info(device, "label") == null && label != dgettext (GETTEXT_PACKAGE, "No label")) {
                    label = string.printf (dgettext (GETTEXT_PACKAGE, "No label (%s)"), label);
                }

                string? is_mounted_str = get_device_info(device, "is mounted");
                bool mounted = (is_mounted_str != null && is_mounted_str == "1");
                string mounted_text = mounted ? dgettext (GETTEXT_PACKAGE, " (Mounted)") : dgettext (GETTEXT_PACKAGE, " (Unmounted)");

                string display_label = (removable_display == "filename") ?
                    string.printf("%s: %s%s", device.replace("/dev/", ""), label, mounted_text) :
                    string.printf("%s%s", label, mounted_text);

                var button = new Button {
                    label = display_label,
                    use_underline = true
                };
                button.clicked.connect(() => {
                    show_mount_menu("removable", device);
                });
                button.set_tooltip_text(string.printf (dgettext (GETTEXT_PACKAGE, "Manage %s"), device));
                vbox.pack_start(button, false, false, 0);

                if (mounted) {
                    mounted_removable.add(device);
                }
            }

            if (total_removable == 0) {
                var none_label = new Label(dgettext (GETTEXT_PACKAGE, "None"));
                none_label.set_xalign(0);
                vbox.pack_start(none_label, false, false, 0);
            } else if (mounted_removable.size > 0) {
                var unmount_all_button = new Button {
                    label = dgettext (GETTEXT_PACKAGE, "Unmount all"),
                    use_underline = true
                };
                unmount_all_button.clicked.connect(() => {
                    if (show_confirmation_dialog(dgettext (GETTEXT_PACKAGE, "Unmount all removable devices?"))) {
                        foreach (var device in mounted_removable) {
                            run_command(new string[] {"udisks", "--unmount", device});
                        }
                        create_window(); // Refresh
                        main_window.show_all();
                    }
                });
                unmount_all_button.set_tooltip_text(dgettext (GETTEXT_PACKAGE, "Unmount all mounted removable devices"));
                vbox.pack_start(unmount_all_button, false, false, 0);
            }

            // Optical Devices
            var optical_label = new Label(dgettext (GETTEXT_PACKAGE, "Optical Media"));
            optical_label.set_xalign(0);
            vbox.pack_start(optical_label, false, false, 0);

            var optical_devices = get_devices(optical_regex);
            var mounted_optical = new List<string>();

            foreach (var device in optical_devices) {
                string? has_media_str = get_device_info(device, "has media");
                bool has_media = (has_media_str != null && has_media_str == "1");

                bool skip = false;
                string info = run_command(new string[] {"udisks", "--show-info", device});
                if(info != null) {
                    foreach (string bl in blacklist) {
                        if (info.contains(bl)) {
                            skip = true;
                            break;
                        }
                    }
                }
                if (skip) {
                    continue;
                }

                if (!has_media) {
                    var none_label = new Label(string.printf("%s: %s", device.replace("/dev/", ""), dgettext (GETTEXT_PACKAGE, "None")));
                    none_label.set_xalign(0);
                    vbox.pack_start(none_label, false, false, 0);
                    continue;
                }

                string? blank_str = get_device_info(device, "blank");
                bool blank = (blank_str != null && blank_str == "1");
                string label = blank ? dgettext (GETTEXT_PACKAGE, "Blank media") : get_device_info(device, "label");
                if (label == null) label = get_device_info(re.sub(@"[0-9]+$", "", device), "model");
                if (label == null) label = get_device_info(re.sub(@"[0-9]+$", "", device), "vendor");
                if (label == null) label = dgettext (GETTEXT_PACKAGE, "No label");

                string? is_mounted_str = get_device_info(device, "is mounted");
                bool mounted = (is_mounted_str != null && is_mounted_str == "1");
                string mounted_text = mounted ? dgettext (GETTEXT_PACKAGE, " (Mounted)") : dgettext (GETTEXT_PACKAGE, " (Unmounted)");

                string display_label = (optical_display == "filename") ?
                    string.printf("%s: %s%s", device.replace("/dev/", ""), label, mounted_text) :
                    string.printf("%s%s", label, mounted_text);

                var button = new Button {
                    label = display_label,
                    use_underline = true
                };
                button.clicked.connect(() => {
                    show_mount_menu("optical", device);
                });
                button.set_tooltip_text(string.printf (dgettext (GETTEXT_PACKAGE, "Manage %s"), device));
                vbox.pack_start(button, false, false, 0);

                if (mounted) {
                    mounted_optical.add(device);
                }
            }

            if (mounted_optical.size > 0) {
                var unmount_all_button = new Button {
                    label = dgettext (GETTEXT_PACKAGE, "Unmount all"),
                    use_underline = true
                };
                unmount_all_button.clicked.connect(() => {
                    if (show_confirmation_dialog(dgettext (GETTEXT_PACKAGE, "Unmount all optical devices?"))) {
                        foreach (var device in mounted_optical) {
                            run_command(new string[] {"udisks", "--unmount", device});
                        }
                        create_window(); // Refresh
                        main_window.show_all();
                    }
                });
                unmount_all_button.set_tooltip_text(dgettext (GETTEXT_PACKAGE, "Unmount all mounted optical devices"));
                vbox.pack_start(unmount_all_button, false, false, 0);
            }

            main_window.show_all();
        }

        private void show_mount_menu(string media_type, string device) {
            var dialog = new Dialog {
                title = string.printf (dgettext (GETTEXT_PACKAGE, "Options for %s"), device),
                transient_for = main_window,
                modal = true,
                use_header_bar = true
            };
            dialog.add_button(Stock.CANCEL, ResponseType.CANCEL);

            var content_area = dialog.get_content_area();
            var vbox = new Box(Orientation.VERTICAL, 5);
            content_area.add(vbox);

            string? label = get_device_info(device, "label");
            if (label == null) label = get_device_info(re.sub(@"[0-9]+$", "", device), "model");
            if (label == null) label = get_device_info(re.sub(@"[0-9]+$", "", device), "vendor");
            if (label == null) label = dgettext (GETTEXT_PACKAGE, "No label");

            var device_label = new Label(string.printf("%s: %s", device, label));
            device_label.set_xalign(0);
            vbox.pack_start(device_label, false, false, 0);

            string? is_mounted_str = get_device_info(device, "is mounted");
            bool mounted = (is_mounted_str != null && is_mounted_str == "1");
            string? is_ejectable_str = get_device_info(device, "ejectable");
            bool ejectable = (is_ejectable_str != null && is_ejectable_str == "1");

            if (!mounted) {
                var open_button = new Button {
                    label = dgettext (GETTEXT_PACKAGE, "Open"),
                    use_underline = true
                };
                open_button.clicked.connect(() => {
                    if (mount_and_open(device)) {
                        dialog.close();
                        create_window(); // Refresh
                        main_window.show_all();
                    }
                });
                open_button.set_tooltip_text(dgettext (GETTEXT_PACKAGE, "Mount and open in file manager"));
                vbox.pack_start(open_button, false, false, 0);

                var mount_button = new Button {
                    label = dgettext (GETTEXT_PACKAGE, "Mount"),
                    use_underline = true
                };
                mount_button.clicked.connect(() => {
                    if (mount_device(device)) {
                        dialog.close();
                        create_window(); // Refresh
                        main_window.show_all();
                    }
                });
                mount_button.set_tooltip_text(dgettext (GETTEXT_PACKAGE, "Mount the device"));
                vbox.pack_start(mount_button, false, false, 0);
            } else {
                string? mount_path_str = get_device_info(device, "mount paths");
                if(mount_path_str != null){
                    string mount_path = mount_path_str.split()[0];
                    var open_button = new Button {
                        label = dgettext (GETTEXT_PACKAGE, "Open"),
                        use_underline = true
                    };
                    open_button.clicked.connect(() => {
                        run_command(new string[] {filemanager, mount_path});
                        dialog.close();
                    });
                    open_button.set_tooltip_text(dgettext (GETTEXT_PACKAGE, "Open the device in file manager"));
                    vbox.pack_start(open_button, false, false, 0);
                }

                var unmount_button = new Button {
                    label = dgettext (GETTEXT_PACKAGE, "Unmount"),
                    use_underline = true
                };
                unmount_button.clicked.connect(() => {
                    run_command(new string[] {"udisks", "--unmount", device});
                    dialog.close();
                    create_window(); // Refresh
                    main_window.show_all();
                });
                unmount_button.set_tooltip_text(dgettext (GETTEXT_PACKAGE, "Unmount the device"));
                vbox.pack_start(unmount_button, false, false, 0);
            }

            if (ejectable) {
                var eject_button = new Button {
                    label = dgettext (GETTEXT_PACKAGE, "Eject"),
                    use_underline = true
                };
                eject_button.clicked.connect(() => {
                    run_command(new string[] {"udisks", "--eject", device});
                    dialog.close();
                    create_window(); // Refresh
                    main_window.show_all();
                });
                eject_button.set_tooltip_text(dgettext (GETTEXT_PACKAGE, "Eject the device"));
                vbox.pack_start(eject_button, false, false, 0);
            }

            var info_button = new Button {
                label = dgettext (GETTEXT_PACKAGE, "Info"),
                use_underline = true
            };
            info_button.clicked.connect(() => {
                show_info_menu(device);
                dialog.close();
            });
            info_button.set_tooltip_text(dgettext (GETTEXT_PACKAGE, "Show device information"));
            vbox.pack_start(info_button, false, false, 0);

            vbox.show_all();
            dialog.show_all();
            dialog.run();
            dialog.destroy();
        }

        private void show_info_menu(string device) {
            string? output = run_command(new string[] {"udisks", "--show-info", device});
            if (output != null) {
                var dialog = new Dialog {
                    title = string.printf (dgettext (GETTEXT_PACKAGE, "Info: %s"), device),
                    transient_for = main_window,
                    modal = true,
                    use_header_bar = true
                };
                dialog.add_button(Stock.OK, ResponseType.OK);

                var content_area = dialog.get_content_area();
                var scrolled_window = new ScrolledWindow {
                    hscrollbar_policy = PolicyType.NEVER,
                    vscrollbar_policy = PolicyType.AUTOMATIC
                };
                content_area.add(scrolled_window);

                var text_view = new TextView {
                    editable = false,
                    cursor_visible = false
                };
                var buffer = text_view.get_buffer();
                buffer.text = output;
                scrolled_window.add(text_view);

                scrolled_window.show_all();
                dialog.show_all();
                dialog.run();
                dialog.destroy();
            }
        }

        private bool mount_and_open(string device) {
            if (mount_device(device)) {
                string? mount_path_str = get_device_info(device, "mount paths");
                if(mount_path_str != null) {
                    string mount_path = mount_path_str.split()[0];
                    run_command(new string[] {filemanager, mount_path});
                    return true;
                } else {
                    return false;
                }
            } else {
                return false;
            }
        }

        private bool mount_device(string device) {
            try {
                run_command(new string[] {"udisks", "--mount", device});
                return true; // Mount success
            } catch (Error e) {
                try {
                    run_command(new string[] {"pkexec", "udisks", "--mount", device});
                    return true; // Mount success
                } catch (Error e2) {
                    print("Failed to mount device (insufficient privileges or incorrect password).\n");
                    return false; // Mount failed
                }
            }
        }

        private bool show_confirmation_dialog(string message) {
            var dialog = new MessageDialog(main_window,
                                              DialogFlags.MODAL,
                                              MessageType.QUESTION,
                                              ButtonsType.YES_NO,
                                              message);
            dialog.title = dgettext (GETTEXT_PACKAGE, "Confirmation");
            var result = dialog.run();
            dialog.destroy();
            return result == ResponseType.YES;
        }


        // Environment variable retrieval and defaults
        private string get_removable_regex() {
            string? regex = Environment.get_variable("OBDEVICEMENU_REMOVABLE_REGEX");
            if (regex != null) {
                try {
                    new Regex(regex);
                    return regex;
                } catch (RegexException e) {
                    return @"/dev/sd[a-z][0-9]*";
                }
            } else {
                return @"/dev/sd[a-z][0-9]*";
            }
        }

        private string get_optical_regex() {
            string? regex = Environment.get_variable("OBDEVICEMENU_OPTICAL_REGEX");
            if (regex != null) {
                try {
                    new Regex(regex);
                    return regex;
                } catch (RegexException e) {
                    return @"/dev/sr[0-9]*";
                }
            } else {
                return @"/dev/sr[0-9]*";
            }
        }

        private bool get_show_internal() {
            string? show_internal_str = Environment.get_variable("OBDEVICEMENU_SHOW_INTERNAL");
            return (show_internal_str != null && show_internal_str == "1");
        }

        private string[] get_blacklist() {
            string? blacklist_str = Environment.get_variable("OBDEVICEMENU_BLACKLIST");
            if (blacklist_str != null) {
                return blacklist_str.split();
            } else {
                return new string[0];
            }
        }

        private string get_filemanager() {
            string? filemanager = Environment.get_variable("FILEMANAGER");
            if (filemanager != null) {
                return filemanager;
            }

            string? desktop_session = Environment.get_variable("DESKTOP_SESSION");
            string? xdg_desktop = Environment.get_variable("XDG_CURRENT_DESKTOP");

            if (desktop_session == "xfce" || xdg_desktop == "XFCE") {
                if (FileUtils.test("thunar", FileTest.EXISTS)) {
                    return "thunar";
                }
            } else if (desktop_session == "gnome" || xdg_desktop == "GNOME") {
                if (FileUtils.test("nautilus", FileTest.EXISTS)) {
                    return "nautilus";
                }
            } else if (desktop_session == "kde" || xdg_desktop == "KDE") {
                if (FileUtils.test("dolphin", FileTest.EXISTS)) {
                    return "dolphin";
                }
            }

            if (FileUtils.test("thunar", FileTest.EXISTS)) {
                return "thunar";
            } else if (FileUtils.test("caja", FileTest.EXISTS)) {
                return "caja";
            }

            return "thunar"; // Default to thunar if none found.
        }

        // Command execution
        private string run_command(string[] command) {
            try {
                Process proc = new Process {
                    argv = command,
                    redirect_stdout = true,
                    redirect_stderr = true
                };

                if (!proc.spawn()) {
                    print("Failed to execute command: %s\n", string.joinv(" ", command));
                    return null;
                }

                string stdout, stderr;
                proc.communicate(out stdout, out stderr);

                int exit_code = proc.wait();
                if (exit_code != 0) {
                    print("Command '%s' failed with exit code %d. Stderr: %s\n",
                          string.joinv(" ", command), exit_code, stderr);
                    throw new Error.literal("Command execution failed");
                }

                return stdout.strip();
            } catch (Error e) {
                print("Error running command: %s\n", e.message);
                return null;
            }
        }

        // Device retrieval
        private string[] get_devices(string regex) {
            string? output = run_command(new string[] {"udisks", "--enumerate-device-files"});
            if (output != null) {
                Regex r = new Regex(regex, RegexOptions.MULTILINE);
                MatchCollection matches = r.matches(output);
                string[] devices = new string[matches.count];
                for (int i = 0; i < matches.count; i++) {
                    devices[i] = matches[i].value;
                }
                Array.sort(devices);
                return devices;
            }
            return new string[0];
        }

        // Device information retrieval
        private string get_device_info(string device, string key) {
            string? output = run_command(new string[] {"udisks", "--show-info", device});
            if (output != null) {
                string pattern = string.printf(@"^\s*%s:\s*(.+)", key);
                Regex r = new Regex(pattern, RegexOptions.MULTILINE);
                Match match = r.match(output);
                if (match.success) {
                    return match.groups[1].value.strip();
                }
            }
            return null;
        }

        // Fancy sort
        private string[] fancy_sort(string[] devices) {
            var temp_devices = new List<string>();
            foreach (string device in devices) {
                string devmajor = Regex.replace(device, @"[0-9]+$", "");
                if (device == devmajor) {
                    temp_devices.add(device);
                } else {
                    string? partition_number_str = Regex.match(device, @"[0-9]+$").groups[0].value;
                    if (partition_number_str != null) {
                        int partition_number = int.parse(partition_number_str);
                        temp_devices.add(string.printf("%s%02d", devmajor, partition_number));
                    } else {
                        temp_devices.add(device); // If parsing fails, add original device
                    }
                }
            }
            temp_devices.sort();
            string[] sorted_devices = new string[temp_devices.size];
            for (int i = 0; i < temp_devices.size; i++) {
                string device = temp_devices[i];
                string devmajor = Regex.replace(device, @"[0-9]+$", "");
                if (device == devmajor) {
                    sorted_devices[i] = device;
                } else {
                    string? partition_number_str = Regex.match(device, @"[0-9]+$").groups[0].value;
                    if(partition_number_str != null) {
                        int partition_number = int.parse(partition_number_str);
                        sorted_devices[i] = string.printf("%s%d", devmajor, partition_number);
                    } else {
                        sorted_devices[i] = device;
                    }

                }
            }
            return sorted_devices;
        }

        // Display options tracking (using a simple file)
        private string[] get_display_options() {
            try {
                string content = FileUtils.get_contents(DISPLAY_OPTIONS_FILE);
                return content.split(",");
            } catch (Error e) {
                return new string[] {"label", "label"};  // Default: label for both removable and optical
            }
        }

        private void set_display_options(string removable, string optical) {
            try {
                FileUtils.save_contents(DISPLAY_OPTIONS_FILE, string.printf("%s,%s", removable, optical));
            } catch (Error e) {
                print("Error saving display options: %s\n", e.message);
            }
        }
    }

    public static int main(string[] args) {
        // Set locale
        Intl.setlocale(LocaleCategory.ALL, "");
        Intl.bindtextdomain(GETTEXT_PACKAGE, "/usr/share/locale");
        Intl.textdomain(GETTEXT_PACKAGE);

        var app = new Application();
        return app.run(args);
    }
}

