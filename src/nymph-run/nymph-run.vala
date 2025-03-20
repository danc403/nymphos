using Gtk;
using GLib;

public class RunDialog : Dialog {

    private Entry command_entry;
    private Button run_button;
    private Button cancel_button;

    public RunDialog(Window? parent) {
        Object(title: "Run...", transient_for: parent, modal: true,
               default_response: ResponseType.CANCEL);

        // Content Area
        var content_area = this.get_content_area();
        content_area.set_spacing(10);
        content_area.set_margin_start(10);
        content_area.set_margin_end(10);
        content_area.set_margin_top(10);
        content_area.set_margin_bottom(10);

        // Command Entry
        command_entry = new Entry();
        command_entry.set_hexpand(true);
        content_area.append(command_entry);

        // Buttons
        var button_box = new Box(Orientation.HORIZONTAL, 10);
        button_box.set_halign(Align.END);

        run_button = new Button.with_label("Run");
        run_button.set_response_sensitive(ResponseType.OK, true); // Ensure ResponseType.OK is linked to the button.
        run_button.clicked.connect(() => {
            this.response(ResponseType.OK);
        });
        button_box.append(run_button);

        cancel_button = new Button.with_label("Cancel");
        cancel_button.set_response_sensitive(ResponseType.CANCEL, true); // Ensure ResponseType.CANCEL is linked to the button.
        cancel_button.clicked.connect(() => {
            this.response(ResponseType.CANCEL);
        });
        button_box.append(cancel_button);

        content_area.append(button_box);
        content_area.show_all();


        // Actions
        this.response.connect((response_id) => {
            switch (response_id) {
                case ResponseType.OK:
                    string command = command_entry.get_text();
                    run_command(command);
                    this.close(); // Close after running, crucial for single command and exit.
                    break;
                case ResponseType.CANCEL:
                    this.close();
                    break;
                default:
                    this.close();
                    break;
            }
        });

        // Set initial focus and position
        this.realize.connect(() => {
            this.present(); // Present before setting focus, otherwise focus is lost.
            command_entry.grab_focus();

        });

        this.set_default_size(400, 100);
        this.set_position(WindowPosition.CENTER);
    }

    private void run_command(string command) {
        try {
            // Execute the command using GLib.spawn_command_line_async
            string[] argv = { "/bin/sh", "-c", command };
            bool success = GLib.spawn_async(null, argv, null, SpawnFlags.SEARCH_PATH | SpawnFlags.DO_NOT_REAP_CHILD, null, out int pid);  //Crucial Change: DO_NOT_REAP_CHILD

            if (!success) {
                print("Failed to execute command: %s\n", command);
                // Consider showing an error dialog to the user
                var dialog = new MessageDialog(this, DialogFlags.MODAL, MessageType.ERROR, ButtonsType.OK, "Failed to execute command: %s", command);
                dialog.run();
                dialog.destroy();
            } else {
                print("Command executed with PID: %d\n", pid);
            }

        } catch (Error err) {
            print("Error executing command: %s\n", err.message);
             var dialog = new MessageDialog(this, DialogFlags.MODAL, MessageType.ERROR, ButtonsType.OK, "Error executing command: %s", err.message);
                dialog.run();
                dialog.destroy();
        }
    }
}


public class Application : Gtk.Application {

    private Window main_window;

    public Application() {
        Object(application_id: "org.example.rundialog");
        this.register_for_all();
        this.activate.connect(() => {
            // Open Run Dialog directly on activation.  No main window needed.
            var dialog = new RunDialog(null);
            dialog.show();
            dialog.run(); // This will block until the dialog is closed (response is received).
            dialog.destroy();
            quit(); // Quit the application after the dialog is closed.

        });
    }
}

public static int main(string[] args) {
    var app = new Application();
    return app.run(args);
}
