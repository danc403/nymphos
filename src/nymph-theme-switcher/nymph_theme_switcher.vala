using Gtk;
using GLib;
using Gee;

public class ThemeSwitcher : Window {

    public static string APP_NAME = "nymph-theme-switcher";
    public static string LOCALE_DIR = "/usr/share/locale";

    private ListStore theme_list;
    private ComboBox theme_combo;
    private Button apply_button;
    private CheckButton system_theme_check;

    public ThemeSwitcher() {
        Title = _("Nymph Theme Switcher");
        BorderWidth = 10;
        WindowPosition = WindowPosition.CENTER;
        Destroy.connect(Gtk.main_quit);

        var vbox = new VBox(false, 5);
        add(vbox);

        theme_list = new ListStore(1, typeof(string));
        theme_combo = new ComboBox.with_model(theme_list);
        var renderer = new CellRendererText();
        theme_combo.pack_start(renderer, true);
        theme_combo.add_attribute(renderer, "text", 0);
        vbox.pack_start(theme_combo, false, false, 0);

        system_theme_check = new CheckButton.with_label(_("System Theme (Admin)"));
        vbox.pack_start(system_theme_check, false, false, 0);

        apply_button = new Button.with_label(_("Apply Theme"));
        apply_button.clicked.connect(apply_theme);
        vbox.pack_start(apply_button, false, false, 0);

        scan_themes();
        set_current_theme();

        show_all();
    }

    private void scan_themes() {
        var data_dirs = parse_xdg_data_dirs();
        foreach (var dir in data_dirs) {
            var theme_dir = Path.build_filename(dir, "themes");
            if (Dir.exists(theme_dir)) {
                var dir_iter = new DirIterator(theme_dir, DirIteratorFlags.NONE);
                string? filename;
                while ((filename = dir_iter.next_file()) != null) {
                    var theme_path = Path.build_filename(theme_dir, filename);
                    if (is_theme_dir(theme_path)) {
                        theme_list.append([filename]);
                    }
                }
            }
        }
    }

    private bool is_theme_dir(string path) {
        var rc_file = Path.build_filename(path, "openbox-3", "themerc");
        return File.test(rc_file, FileTest.EXISTS);
    }

    private void apply_theme() {
        TreeIter iter;
        if (theme_combo.get_active_iter(out iter)) {
            string theme_name = (string) theme_list.get_value(iter, 0);
            var data_dirs = parse_xdg_data_dirs();
            foreach (var dir in data_dirs) {
                var theme_path = Path.build_filename(Path.build_filename(dir, "themes"), theme_name);
                if (is_theme_dir(theme_path)) {
                    set_theme(theme_path);
                    break;
                }
            }
        }
    }

    private void set_theme(string theme_path){
      string command;
      if(system_theme_check.active){
        command = "sudo openbox --reconfigure --theme " + theme_path;
      } else {
        command = "openbox --reconfigure --theme " + theme_path;
      }
      try{
        var process = new Subprocess.with_argv(command.shell_parse_argv(),SubprocessFlags.LEAVE_STDERR_OPEN);
        process.wait();
      } catch (Error e){
        stderr.printf(_("Error: %s\n"), e.message);
      }
    }

    private void set_current_theme(){
      string theme = get_current_theme();
      if(theme != null){
        for(int i = 0; i < theme_list.get_n_items(); i++){
          TreeIter iter;
          if(theme_list.get_iter(out iter, i)){
            if(theme == (string)theme_list.get_value(iter, 0)){
              theme_combo.set_active_iter(iter);
              break;
            }
          }
        }
      }
    }

    private string get_current_theme(){
      string? current_theme = null;
      try{
        var process = new Subprocess.with_argv({"openbox", "--show-current-theme"}, SubprocessFlags.LEAVE_STDERR_OPEN);
        process.wait();
        var output = process.get_stdout_data();
        current_theme = String.strip(output);
      } catch (Error e){
        stderr.printf(_("Error: %s\n"), e.message);
      }
      return current_theme;
    }

    public static int main(string[] args) {
        Gtk.init(ref args);

        // Set up gettext
        Intl.set_application_domain(APP_NAME);
        Intl.bindtextdomain(APP_NAME, LOCALE_DIR);
        Intl.textdomain(APP_NAME);

        new ThemeSwitcher();
        Gtk.main();
        return 0;
    }
}
