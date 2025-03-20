using Gtk;
using GLib;
using PulseAudio;

namespace MediaControl {
    public class VolumeController {
        private Pulse.Context? context; // Use Pulse.Context?
        private Pulse.Mainloop? mainloop;
        private string default_sink_name;

        public VolumeController() {
            init_pulseaudio();
        }

        ~VolumeController() {
            if (context != null) {
                Pulse.context_disconnect(context);
                Pulse.context_unref(context);
                context = null;
            }
            if(mainloop != null) {
                Pulse.mainloop_free(mainloop);
                mainloop = null;
            }
        }

        private void init_pulseaudio() {
            mainloop = Pulse.mainloop_new();
            assert(mainloop != null);

            string app_name = "Vala Media Control";
            context = Pulse.context_new(mainloop.get_api(), app_name);
            assert(context != null);

            Pulse.context_set_state_callback(context, context_state_cb);
            Pulse.context_connect(context, null, Pulse.ContextFlags.NOAUTOSPAWN, null);
            Pulse.mainloop_run(mainloop);


            // Initial run to set default sink name
            get_default_sink();
        }

        private void context_state_cb(Pulse.Context context) {
            unowned var state = Pulse.context_get_state(context);

            switch (state) {
                case Pulse.ContextState.READY:
                    stdout.printf("PulseAudio context is ready.\n");
                    get_default_sink();
                    break;
                case Pulse.ContextState.FAILED:
                case Pulse.ContextState.TERMINATED:
                    stderr.printf("PulseAudio context failed or terminated.\n");
                    break;
                case Pulse.ContextState.CONNECTING:
                case Pulse.ContextState.AUTHORIZING:
                case Pulse.ContextState.SETTING_CLIENT_NAME:
                    stdout.printf("PulseAudio context connecting...\n");
                    break;
                default:
                    stdout.printf("PulseAudio context state: %s\n", state.to_string());
                    break;
            }
        }

        private void get_default_sink() {
            Pulse.operation_get_server_info(context, (info) => {
                unowned var server_info = Pulse.server_info_get(info);
                if (server_info != null) {
                    default_sink_name = server_info.default_sink_name;
                    stdout.printf("Default sink name: %s\n", default_sink_name);
                    Pulse.operation_unref(info); //Unref the operation
                } else {
                    stderr.printf("Failed to get server info.\n");
                }
            });
        }

        public void increase_volume() {
           if (default_sink_name != null) {
                get_sink_info(default_sink_name, (sink_info) => {
                    if (sink_info != null) {
                       float current_volume = sink_info.volume.value_flat;
                       float new_volume = Math.min(current_volume + 0.02, 1.0);  // Increase by 2%, limit to 100%
                       set_sink_volume(default_sink_name, new_volume);
                    }
                });
            }
        }

        public void decrease_volume() {
            if (default_sink_name != null) {
                get_sink_info(default_sink_name, (sink_info) => {
                    if (sink_info != null) {
                       float current_volume = sink_info.volume.value_flat;
                       float new_volume = Math.max(current_volume - 0.02, 0.0);  // Decrease by 2%, limit to 0%
                       set_sink_volume(default_sink_name, new_volume);
                    }
                });
            }
        }

        public void toggle_mute() {
            if (default_sink_name != null) {
                get_sink_info(default_sink_name, (sink_info) => {
                    if (sink_info != null) {
                        set_sink_mute(default_sink_name, !sink_info.mute);  // Toggle mute state
                    }
                });
            }
        }

        private void get_sink_info(string sink_name, Pulse.sink_info_cb callback) {
              Pulse.operation_get_sink_info_by_name(context, sink_name, callback);
        }

        private void set_sink_volume(string sink_name, float volume) {
            var vol = new Pulse.Volume();
            vol.values[0] = volume;  //Monophonic volume
            Pulse.operation_set_sink_volume_by_name(context, sink_name, vol);
        }

        private void set_sink_mute(string sink_name, bool mute) {
            Pulse.operation_set_sink_mute_by_name(context, sink_name, mute);
        }
    }


    public class MainWindow : Gtk.Window {
        private VolumeController volume_controller;
        private Gtk.Button volume_up_button;
        private Gtk.Button volume_down_button;
        private Gtk.Button mute_button;

        public MainWindow() {
            this.title = "Media Control";
            this.window_position = WindowPosition.CENTER;
            this.border_width = 10;

            volume_controller = new VolumeController();

            var vbox = new Gtk.Box(Orientation.VERTICAL, 5);
            add(vbox);

            volume_up_button = new Gtk.Button.with_label("Volume Up");
            volume_up_button.clicked.connect(on_volume_up_clicked);
            vbox.pack_start(volume_up_button, false, false, 0);

            volume_down_button = new Gtk.Button.with_label("Volume Down");
            volume_down_button.clicked.connect(on_volume_down_clicked);
            vbox.pack_start(volume_down_button, false, false, 0);

            mute_button = new Gtk.Button.with_label("Mute");
            mute_button.clicked.connect(on_mute_clicked);
            vbox.pack_start(mute_button, false, false, 0);

            this.delete_event.connect(Gtk.main_quit); //Proper quit
        }


        private void on_volume_up_clicked() {
            volume_controller.increase_volume();
        }

        private void on_volume_down_clicked() {
            volume_controller.decrease_volume();
        }

        private void on_mute_clicked() {
            volume_controller.toggle_mute();
        }
    }

    public static int main(string[] args) {
        Gtk.init(ref args);

        var win = new MainWindow();
        win.show_all();

        Gtk.main();
        return 0;
    }
}
