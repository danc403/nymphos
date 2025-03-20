using System;
using System.Collections.Generic;
using GLib;
using Gtk;
using System.IO;
using System.Text.RegularExpressions;
using Posix;
using GObject;

namespace NymphBootConfig {

    public class BootData {
        public List<BootEntry> legacy { get; set; }
        public List<BootEntry> efi { get; set; }
        public List<BootEntry> windows { get; set; }
        public List<BootEntry> macos { get; set; }
        public List<BootEntry> linux { get; set; }

        public BootData() {
            legacy = new List<BootEntry>();
            efi = new List<BootEntry>();
            windows = new List<BootEntry>();
            macos = new List<BootEntry>();
            linux = new List<BootEntry>();
        }
    }

    public class BootEntry : GObject.Object {
        private string _boot_type;
        public string boot_type {
            get { return _boot_type; }
            set {
                if (_boot_type != value) {
                    _boot_type = value;
                    notify("boot-type");
                }
            }
        }

        private string _label;
        public string label {
            get { return _label; }
            set {
                if (_label != value) {
                    _label = value;
                    notify("label");
                }
            }
        }

        private string _kernel;
        public string kernel {
            get { return _kernel; }
            set {
                if (_kernel != value) {
                    _kernel = value;
                    notify("kernel");
                }
            }
        }

        private string _append;
        public string append {
            get { return _append; }
            set {
                if (_append != value) {
                    _append = value;
                    notify("append");
                }
            }
        }

        private bool _chainload;
        public bool chainload {
            get { return _chainload; }
            set {
                if (_chainload != value) {
                    _chainload = value;
                    notify("chainload");
                }
            }
        }

        private string _chainload_path;
        public string chainload_path {
            get { return _chainload_path; }
            set {
                if (_chainload_path != value) {
                    _chainload_path = value;
                    notify("chainload-path");
                }
            }
        }

        private string _chainload_type;
        public string chainload_type {
            get { return _chainload_type; }
            set {
                if (_chainload_type != value) {
                    _chainload_type = value;
                    notify("chainload-type");
                }
            }
        }

        private string _partition;
        public string partition {
            get { return _partition; }
            set {
                if (_partition != value) {
                    _partition = value;
                    notify("partition");
                }
            }
        }

        private string _uuid;
        public string uuid {
            get { return _uuid; }
            set {
                if (_uuid != value) {
                    _uuid = value;
                    notify("uuid");
                }
            }
        }

        private string _fstype;
        public string fstype {
            get { return _fstype; }
            set {
                if (_fstype != value) {
                    _fstype = value;
                    notify("fstype");
                }
            }
        }

        public BootEntry() {
            _boot_type = "";
            _label = "";
            _kernel = "";
            _append = "";
            _chainload = false;
            _chainload_path = "";
            _chainload_type = "";
            _partition = "";
            _uuid = "";
            _fstype = "";
        }
    }

    public class DetailsPanel : Gtk.VBox {
        private Gtk.Label label_label;
        private Gtk.Entry label_entry;
        private Gtk.Label kernel_label;
        private Gtk.Entry kernel_entry;
        private Gtk.Label append_label;
        private Gtk.Entry append_entry;
        private BootEntry _current_entry;
        private Gtk.Button update_button;

        public BootEntry current_entry {
            get { return _current_entry; }
            set {
                 if (_current_entry != null) {
                    _current_entry.notify.disconnect(on_entry_changed);
                }

                _current_entry = value;

                if (_current_entry != null) {
                     _current_entry.notify.connect(on_entry_changed);
                     label_entry.text = _current_entry.label;
                     kernel_entry.text = _current_entry.kernel;
                     append_entry.text = _current_entry.append;
                }
                else
                {
                     label_entry.text = "";
                     kernel_entry.text = "";
                     append_entry.text = "";
                }
            }
        }

        public DetailsPanel() {
            spacing = 5;
            border_width = 5;

            // Label
            label_label = new Gtk.Label("Label:");
            label_entry = new Gtk.Entry();
            HBox label_box = new HBox(false, 5);
            label_box.pack_start(label_label, false, false, 0);
            label_box.pack_start(label_entry, true, true, 0);
            pack_start(label_box, false, false, 0);

            // Kernel
            kernel_label = new Gtk.Label("Kernel:");
            kernel_entry = new Gtk.Entry();
            HBox kernel_box = new HBox(false, 5);
            kernel_box.pack_start(kernel_label, false, false, 0);
            kernel_box.pack_start(kernel_entry, true, true, 0);
            pack_start(kernel_box, false, false, 0);

            // Append
            append_label = new Gtk.Label("Append:");
            append_entry = new Gtk.Entry();
            HBox append_box = new HBox(false, 5);
            append_box.pack_start(append_label, false, false, 0);
            append_box.pack_start(append_entry, true, true, 0);
            pack_start(append_box, false, false, 0);

            //Update Button
            update_button = new Gtk.Button("Update");
            pack_start(update_button, false, false, 0);
            update_button.clicked.connect(() => {
                  if (_current_entry != null)
                   {
                        _current_entry.label = label_entry.text;
                        _current_entry.kernel = kernel_entry.text;
                        _current_entry.append = append_entry.text;
                         update_entry(_current_entry);
                   }

            });

             label_entry.changed.connect(() => {
                if (_current_entry != null) {
                    _current_entry.label = label_entry.text;
                }
            });

            kernel_entry.changed.connect(() => {
                if (_current_entry != null) {
                    _current_entry.kernel = kernel_entry.text;
                }
            });

            append_entry.changed.connect(() => {
                if (_current_entry != null) {
                    _current_entry.append = append_entry.text;
                }
            });

            this.show_all();
        }

          private void on_entry_changed(string property_name) {
            // Update the UI elements when the properties of the BootEntry change

            if (_current_entry != null)
            {
                  label_entry.text = _current_entry.label;
                  kernel_entry.text = _current_entry.kernel;
                  append_entry.text = _current_entry.append;
             }


         }

    }

    public class MainWindow : Gtk.Window {

        private Gtk.TreeView boot_entries_treeview;
        private Gtk.TreeStore boot_entries_store;
        private Gtk.ScrolledWindow details_scrolled;
        private DetailsPanel details_panel;
        private BootData boot_data;

        private const string extlinux_config_path = "/boot/extlinux/extlinux.conf";
        private const string efi_mount_point = "/boot/efi";
        private const string revert_script_path = "/usr/local/bin/revert_boot.sh";
        private const string default_efi_kernel_label = "NymphOS";
        private const string default_efi_kernel_path = "/EFI/BOOT/BOOTX64.EFI"; //Hardcoded, should be adjustable via the UI or config file.
        private const string default_extlinux_config = "/boot/extlinux/extlinux.conf";

        private bool persistent_boot_var = false;

        public MainWindow() : base(Gtk.WindowType.TOPLEVEL) {
            this.title = "Nymph Boot Configuration";
            this.window_position = Gtk.WindowPosition.CENTER;
            this.border_width = 10;
            this.set_default_size(800, 600);
            this.destroy.connect(Gtk.main_quit);

            // Load settings
            Settings settings = new Settings("org.nymph.bootconfig");
            persistent_boot_var = settings.get_boolean("persistent-boot");

            VBox main_vbox = new VBox(false, 5);

            // Treeview
            boot_entries_store = new TreeStore(typeof(string), typeof(string), typeof(string));
            boot_entries_treeview = new TreeView(boot_entries_store);

            TreeViewColumn type_column = new TreeViewColumn();
            type_column.title = "Type";
            CellRendererText type_cell = new CellRendererText();
            type_column.pack_start(type_cell, true);
            type_column.add_attribute(type_cell, "text", 0);
            boot_entries_treeview.append_column(type_column);

            TreeViewColumn label_column = new TreeViewColumn();
            label_column.title = "Label";
            CellRendererText label_cell = new CellRendererText();
            label_column.pack_start(label_cell, true);
            label_column.add_attribute(label_cell, "text", 1);
            boot_entries_treeview.append_column(label_column);

            TreeViewColumn kernel_column = new TreeViewColumn();
            kernel_column.title = "Kernel";
            CellRendererText kernel_cell = new CellRendererText();
            kernel_column.pack_start(kernel_cell, true);
            kernel_column.add_attribute(kernel_cell, "text", 2);
            boot_entries_treeview.append_column(kernel_column);

            ScrolledWindow tree_scrolled = new ScrolledWindow();
            tree_scrolled.add(boot_entries_treeview);
            main_vbox.pack_start(tree_scrolled, true, true, 0);

            // Details Panel
            details_scrolled = new ScrolledWindow();
            details_panel = new DetailsPanel();
            details_scrolled.add(details_panel);
            main_vbox.pack_start(details_scrolled, true, true, 0);

            // Persistent Boot Toggle
            ToggleButton persistent_boot_toggle = new ToggleButton("Persistent Boot");
            persistent_boot_toggle.active = persistent_boot_var;
            main_vbox.pack_start(persistent_boot_toggle, false, false, 0);

            persistent_boot_toggle.toggled.connect(() => {
                persistent_boot_var = persistent_boot_toggle.active;
                settings.set_boolean("persistent-boot", persistent_boot_var);
            });

            // Load Boot Data
            boot_data = build_boot_data();
            add_entries_to_treeview("legacy", boot_data.legacy);
            add_entries_to_treeview("efi", boot_data.efi);
            add_entries_to_treeview("windows", boot_data.windows);
            add_entries_to_treeview("macos", boot_data.macos);
            add_entries_to_treeview("linux", boot_data.linux);

            // Selection Changed Handler
            boot_entries_treeview.selection.changed.connect(() => {
                TreeIter iter;
                if (boot_entries_treeview.selection.get_selected(out iter)) {
                    string type = (string) boot_entries_store.get_value(iter, 0);
                    string label = (string) boot_entries_store.get_value(iter, 1);

                    BootEntry selected_entry = null;

                    // Find the BootEntry in the appropriate list based on type and label
                    switch (type) {
                        case "legacy":
                            selected_entry = boot_data.legacy.find((BootEntry e) => e.label == label);
                            break;
                        case "efi":
                            selected_entry = boot_data.efi.find((BootEntry e) => e.label == label);
                            break;
                        case "windows":
                            selected_entry = boot_data.windows.find((BootEntry e) => e.label == label);
                            break;
                        case "macos":
                            selected_entry = boot_data.macos.find((BootEntry e) => e.label == label);
                            break;
                        case "linux":
                            selected_entry = boot_data.linux.find((BootEntry e) => e.label == label);
                            break;
                    }

                    if (selected_entry != null) {
                        show_details(selected_entry);
                    }
                } else {
                   details_panel.current_entry = null;
                }
            });

            this.add(main_vbox);
            this.show_all();
        }

        private void add_entries_to_treeview(string type, List<BootEntry> entries) {
            foreach (var entry in entries) {
                TreeIter iter;
                boot_entries_store.append(out iter);
                boot_entries_store.set(iter, {
                    type,
                    entry.label,
                    entry.kernel
                });
            }
        }

        private BootData build_boot_data() {
            BootData data = new BootData();
            data.legacy = parse_extlinux_config(extlinux_config_path);
            data.efi = parse_efi_config();
            //data.windows = parse_windows_config();  //Placeholder
            //data.macos = parse_macos_config();  //Placeholder
            //data.linux = parse_linux_config(); //Placeholder
            return data;
        }

        private List<BootEntry> parse_extlinux_config(string config_path) {
            List<BootEntry> entries = new List<BootEntry>();
            BootEntry current_entry = null;

            try {
                using (StreamReader reader = new StreamReader(config_path)) {
                    string line;
                    while ((line = reader.ReadLine()) != null) {
                        line = line.Trim();

                        if (line.StartsWith("label")) {
                            if (current_entry != null) {
                                entries.Add(current_entry);
                            }
                            current_entry = new BootEntry();
                            current_entry.boot_type = "legacy";
                            current_entry.label = line.Substring(6).Trim();
                        } else if (line.StartsWith("kernel")) {
                            if (current_entry != null) {
                                current_entry.kernel = line.Substring(7).Trim();
                            }
                        } else if (line.StartsWith("append")) {
                            if (current_entry != null) {
                                current_entry.append = line.Substring(7).Trim();
                            }
                        }
                    }
                    if (current_entry != null) {
                        entries.Add(current_entry);
                    }
                }
            } catch (Exception e) {
                print("Error parsing extlinux.conf: " + e.Message + "\n");
            }
            return entries;
        }

       private List<BootEntry> parse_efi_config() {
            List<BootEntry> entries = new List<BootEntry>();

            try {
                string efibootmgr_output = execute_command("efibootmgr", "-v");
                Regex boot_entry = new Regex(@"Boot(\d+)\* (.*)", RegexOptions.Compiled);
                Regex device_path = new Regex(@"HD\((\d+),", RegexOptions.Compiled);

                using (StringReader reader = new StringReader(efibootmgr_output)) {
                    string line;
                    while ((line = reader.ReadLine()) != null) {
                        line = line.Trim();
                        Match match = boot_entry.Match(line);
                        if (match.Success) {
                            string boot_number = match.Groups[1].Value;
                            string description = match.Groups[2].Value;

                            BootEntry entry = new BootEntry();
                            entry.boot_type = "efi";
                            entry.label = "Boot" + boot_number + "* " + description;

                            // Extract device path
                            Match device_match = device_path.Match(line);
                            if (device_match.Success) {
                                string partition_number = device_match.Groups[1].Value;
                                entry.partition = partition_number;
                            }

                            // Extract kernel path
                            Regex kernel_path = new Regex(@"\\(.*)", RegexOptions.Compiled);
                            Match kernel_match = kernel_path.Match(line);
                            if (kernel_match.Success) {
                                entry.kernel = kernel_match.Groups[1].Value;
                            }

                            entries.Add(entry);
                        }
                    }
                }
            } catch (Exception e) {
                print("Error parsing EFI boot variables: " + e.Message + "\n");
            }

            return entries;
        }

        private void show_details(BootEntry entry) {
            details_panel.current_entry = entry;
        }

            private void update_entry(BootEntry entry) {
             if (entry.boot_type == "efi") {
                update_efi_boot_vars(entry);
            } else if (entry.boot_type == "legacy") {
                update_extlinux_conf(boot_data.legacy);  // extlinux needs all entries to rewrite the file.
            }else
            {
                print("Unsupported boot type for update: " + entry.boot_type + "\n");
            }
        }

        private void update_efi_boot_vars(BootEntry efi_entry) {
            string backup_file = "/tmp/efi_boot_vars.bak";

            try {
                // 1. Create Backup
                string efibootmgr_output = execute_command("efibootmgr", "-v");
                File.write(backup_file, efibootmgr_output);

                // 2. Determine boot number from label
                Regex boot_number = new Regex(@"Boot(\d+)", RegexOptions.Compiled);
                Match boot_num_match = boot_number.Match(efi_entry.label);
                 string boot_num = "";
                if (boot_num_match.Success) {
                     boot_num = boot_num_match.Groups[1].Value;
                } else {
                    print("Could not determine boot number from label.\n");
                    return;
                }

                // 3. Delete Existing Entry
                execute_command("efibootmgr", "-b " + boot_num + " -B");

                // 4. Create New Entry
                string create_cmd = "-c -l \"" + efi_entry.kernel + "\" -L \"" + efi_entry.label + "\"";
                execute_command("efibootmgr", create_cmd);

                // 5. Update Boot Order (Optional)
                 string boot_order_output = execute_command("efibootmgr", "-v");
                Regex boot_order_regex = new Regex(@"BootOrder: ([\d,]+)", RegexOptions.Compiled);
                Match boot_order_match = boot_order_regex.Match(boot_order_output);
                 if (boot_order_match.Success)
                 {
                    string boot_order = boot_order_match.Groups[1].Value;
                    string new_boot_order = boot_order.Replace(boot_num, boot_num); // Ensure boot number is in the order
                    execute_command("efibootmgr", "-o " + new_boot_order);
                 }
                 else
                 {
                   print("Could not determine boot order.\n");
                 }


                 print("EFI boot entry " + boot_num + " updated successfully (backup created: " + backup_file + ").\n");

            } catch (Exception e) {
                print("Error updating EFI boot variables: " + e.Message + "\n");
                // Restore the backup if an error occurs
                if (File.exists(backup_file)) {
                    try {
                      execute_command("efibootmgr", "-v"); //print current variables.
                        print("Original EFI boot variables restored from backup.\n");
                    } catch (Exception restore_error) {
                        print("Error printing original efi variables.\n");
                    }
                }

            }
             finally
            {
               //Create a revert script if this is not a persistent boot.
               if(!persistent_boot_var)
               {
                  //capture efi variables as it was before this operation, since we are about to delete it.
                  string original_efi_boot_vars = execute_command("efibootmgr", "-v");
                  create_revert_script(original_efi_boot_vars, backup_file, null, "efi");
               }
                 if (File.exists(backup_file))
                 {
                    File.delete(backup_file);
                 }
            }
        }

        private void update_extlinux_conf(List<BootEntry> legacy_entries, string config_file = "/boot/extlinux/extlinux.conf") {
             string backup_file = config_file + ".bak";

            try {
                // 1. Create Backup
                File.copy(config_file, backup_file);

                // 2. Read and Rewrite the Configuration
                List<string> new_lines = new List<string>();

                 using (StreamReader reader = new StreamReader(config_file)) {
                        string line;
                        while ((line = reader.ReadLine()) != null) {
                            line = line.Trim();
                           new_lines.Add(line);
                        }
                 }

                //Overwrite the config lines.
                File.delete(config_file);
                using (StreamWriter writer = new StreamWriter(config_file)) {
                    foreach(var entry in legacy_entries){
                         List<string> entry_lines = generate_extlinux_entry_lines(entry);
                         foreach (string entryLine in entry_lines)
                         {
                            writer.WriteLine(entryLine);
                         }
                    }

                  writer.Flush();
                }

               print("extlinux.conf updated successfully (backup created: " + backup_file + ").\n");

            } catch (Exception e) {
                print("Error updating extlinux.conf: " + e.Message + "\n");
                // Restore the backup if an error occurs
                if (File.exists(backup_file)) {
                    File.move(backup_file, config_file);
                    print("Original extlinux.conf restored from backup.\n");
                }

            }
            finally
            {
               //Create a revert script if this is not a persistent boot.
               if(!persistent_boot_var)
               {
                  create_revert_script(null, backup_file, config_file, "extlinux");
               }
                 if (File.exists(backup_file))
                 {
                    File.delete(backup_file);
                 }
            }
        }

        private List<string> generate_extlinux_entry_lines(BootEntry entry) {
             List<string> lines = new List<string>();
             lines.Add("label " + entry.label);
             lines.Add("kernel " + entry.kernel);
             if (!string.IsNullOrEmpty(entry.append)) {
                lines.Add("append " + entry.append);
             }
            return lines;
        }

         private string execute_command(string filename, string arguments) {
             Process process = new Process();
             process.StartInfo.FileName = filename;
             process.StartInfo.Arguments = arguments;
             process.StartInfo.RedirectStandardOutput = true;
             process.StartInfo.UseShellExecute = false;
             process.StartInfo.CreateNoWindow = true;
             process.Start();

             string output = process.StandardOutput.ReadToEnd();
             process.WaitForExit();

             if (process.ExitCode != 0) {
                string error_message = "Command '" + filename + " " + arguments + "' failed with exit code: " + process.ExitCode.ToString();

                string error_output = "";
                  if (process.StandardError != null) {
                        error_output = process.StandardError.ReadToEnd();
                  }
                   error_message += " Error Output: " + error_output;

                  throw new Exception(error_message);

             }
                return output;
        }


           private void create_revert_script(string efi_boot_vars = null, string backup_path = null, string config_path = null, string boot_type = null) {
           // Skip revert script creation if PERSISTENT_BOOT_VAR is true
            if (persistent_boot_var) {
                print("Persistent boot is enabled. Skipping revert script creation.\n");
                return;
            }

            try {
                 using (StreamWriter f = new StreamWriter(revert_script_path)) {
                     f.WriteLine("#!/bin/sh");
                     f.WriteLine("# Revert Boot Script - Auto-generated");
                     f.WriteLine("");

                    // Export necessary environment variables before anything else.
                     f.WriteLine("export DEFAULT_EXTLINUX_CONFIG=\"" + default_extlinux_config + "\"");
                     f.WriteLine("export DEFAULT_EFI_KERNEL_LABEL=\"" + default_efi_kernel_label + "\"");
                     f.WriteLine("export DEFAULT_EFI_KERNEL_PATH=\"" + default_efi_kernel_path + "\"");
                     f.WriteLine("export REVERT_SCRIPT_PATH=\"" + revert_script_path + "\"");

                     f.WriteLine("set -e");  // Exit immediately if a command exits with a non-zero status.

                     if (boot_type == "extlinux") {
                         f.WriteLine("backup_path=\"" + backup_path + "\"");
                         f.WriteLine("config_path=\"" + config_path + "\"");
                         f.WriteLine("if [ -f \"$backup_path\" ]; then");
                         f.WriteLine("  mv \"$backup_path\" \"$config_path\"");
                         f.WriteLine("  echo \"Reverted extlinux.conf to backup.\"");
                         f.WriteLine("else");
                         f.WriteLine("  echo \"Backup file not found: $backup_path\"");
                         f.WriteLine("fi");

                     } else if (boot_type == "efi") {

                            //disk, partition = find_efi_partition() #This function needs to be created

                             string disk ="";
                             string partition = ""; //find_efi_partition()
                            if (string.IsNullOrEmpty(disk) || string.IsNullOrEmpty(partition)) {
                                f.WriteLine("  echo \"Error: Could not determine EFI partition.  Manual intervention required.\"");
                                f.WriteLine("  exit 1");
                                //return  # Exit the function if no EFI partition is found
                                return;
                            }

                            f.WriteLine("efi_boot_vars=\"\"\"");
                            f.WriteLine(efi_boot_vars);
                            f.WriteLine("\"\"\"");
                            f.WriteLine("if [ -n \"$efi_boot_vars\" ]; then");
                            f.WriteLine("  current_bootnum=$(efibootmgr | grep \"^BootCurrent\" | cut -d '*' -f1 | cut -d 't' -f2)");
                            f.WriteLine("  if [ -n \"$current_bootnum\" ]; then");
                            f.WriteLine("    efibootmgr --delete-bootnum \"$current_bootnum\"");
                            f.WriteLine("    echo \"Deleted current boot entry.\"");
                            f.WriteLine("  else");
                            f.WriteLine("    echo \"Warning: Could not determine current boot entry.\"");
                            f.WriteLine("  fi");
                            // Create a new boot entry based on our environment variables.
                            f.WriteLine("  efibootmgr --create --disk " + disk + " --part " + partition + " --loader '" + default_efi_kernel_path + "' --label '" + default_efi_kernel_label + "'");
                            f.WriteLine("  echo \"Created default boot entry.\"");

                            // Restore the EFI boot variables based on the backup.
                            f.WriteLine("  echo \"Restoring EFI boot variables...\"");

                            //Iterate through the backed up variables and recreate each boot entry.
                            f.WriteLine("  echo \"$efi_boot_vars\" | while read line; do");
                            f.WriteLine("    if [[ \"$line\" =~ ^Boot([0-9A-Fa-f]{4})\\* ]]; then");
                            f.WriteLine("      bootnum=${BASH_REMATCH[1]}");
                            f.WriteLine("      loader=$(echo \"$line\" | awk '{print $4}')");
                            f.WriteLine("      label=$(echo \"$line\" | awk '{print $2}')");
                            f.WriteLine("      efibootmgr --create --disk " + disk + " --part " + partition + " --loader \"$loader\" --label \"$label\"");
                            f.WriteLine("    fi");
                            f.WriteLine("  done");
                            f.WriteLine("  echo \"EFI boot variables restored.\"");

                     } else {
                            f.WriteLine("echo \"Error: Unsupported boot type. Manual intervention required.\"");
                            f.WriteLine("exit 1");
                            //return
                            return;
                     }

                    //Clean up and remove the revert script.
                     f.WriteLine("  rc-update del revert-boot default");
                     f.WriteLine("  rm \"" + revert_script_path + "\"");
                     f.WriteLine("  echo \"Revert script removed.\"");
                     f.WriteLine("fi");  // closes the if statement.


                 }

                 Posix.chmod(revert_script_path, 0o755);
                execute_command("rc-update", "add revert-boot default");
               print("Revert script created at " + revert_script_path + " and added to OpenRC.\n");

            } catch (Exception e) {
                 print("Error creating revert script: " + e.Message + "\n");
             }

        }

         private Tuple<string, string> find_efi_partition()
            {
                 string disk = null;
                 string partition = null;

                try {
                    string result = execute_command("findmnt", efi_mount_point + " -n -o SOURCE");
                    string device = result.Trim();
                    if (string.IsNullOrEmpty(device)) {
                        throw new Exception("No device found mounted at " + efi_mount_point);
                    }

                    // Extract disk and partition number
                     Regex device_regex = new Regex(@"(/dev/[a-z]+)(\d+)?", RegexOptions.Compiled);
                     Match device_match = device_regex.Match(device);
                      if (device_match.Success)
                      {
                         disk = device_match.Groups[1].Value;
                         partition = (device_match.Groups[2].Success) ? device_match.Groups[2].Value : "1"; // Default to partition 1 if not specified

                         print("EFI partition found: disk=" + disk + ", partition=" + partition + "\n");
                      }
                      else
                      {
                         throw new Exception("Unexpected device format: " + device);
                      }



                } catch (Exception e) {
                    print("Error finding EFI partition: " + e.Message + "\n");
                   return new Tuple<string, string>(null, null);
                }

                return new Tuple<string, string>(disk, partition);
            }
    }

}
