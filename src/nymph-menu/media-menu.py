#!/usr/bin/env python3

import dbus
import dbus.mainloop.glib
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf
import pulsectl
import subprocess
import time

def get_running_players():
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    bus = dbus.SessionBus()
    players = []
    for service in bus.list_names():
        if service.startswith('org.mpris.MediaPlayer2.'):
            players.append(service)
    return players

def get_player_metadata(player_service):
    try:
        player = bus.get_object(player_service, '/org/mpris/MediaPlayer2')
        properties = dbus.Interface(player, 'org.freedesktop.DBus.Properties')
        metadata = properties.Get('org.mpris.MediaPlayer2.Player', 'Metadata')
        return metadata
    except dbus.exceptions.DBusException:
        return None

def get_player_playback_status(player_service):
    try:
        player = bus.get_object(player_service, '/org/mpris/MediaPlayer2')
        properties = dbus.Interface(player, 'org.freedesktop.DBus.Properties')
        status = properties.Get('org.mpris.MediaPlayer2.Player', 'PlaybackStatus')
        return status
    except dbus.exceptions.DBusException:
        return None

def get_player_icon(player_service):
    # Logic to get player icon, possibly from metadata or a predefined list
    metadata = get_player_metadata(player_service)
    if metadata and 'xesam:artist' in metadata and metadata['xesam:artist']:
        artist = metadata['xesam:artist'][0]
        return f"{artist.lower().replace(' ', '_')}_icon.png"  # Placeholder
    return "default-media-icon.png"

def generate_player_menu(player_service):
    metadata = get_player_metadata(player_service)
    if metadata:
        title = metadata.get('xesam:title', 'Unknown Title')
        artist = metadata.get('xesam:artist', ['Unknown Artist'])[0]
        print(f'<separator label="{player_service}"/>')
        print(f'<item label="{title} by {artist}"/>')
    else:
        print(f'<separator label="{player_service}"/>')
        print(f'<item label="No metadata available"/>')

    print('<item label="Play"><action name="Execute"><execute>dbus-send --session --type=method --dest="{}" /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Play</execute></action></item>'.format(player_service))
    print('<item label="Pause"><action name="Execute"><execute>dbus-send --session --type=method --dest="{}" /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Pause</execute></action></item>'.format(player_service))
    print('<item label="Stop"><action name="Execute"><execute>dbus-send --session --type=method --dest="{}" /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Stop</execute></action></item>'.format(player_service))
    print('<item label="Next"><action name="Execute"><execute>dbus-send --session --type=method --dest="{}" /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next</execute></action></item>'.format(player_service))
    print('<item label="Previous"><action name="Execute"><execute>dbus-send --session --type=method --dest="{}" /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous</execute></action></item>'.format(player_service))

def generate_volume_menu():
    pulse = pulsectl.Pulse('volume-control')
    sinks = pulse.sink_list()
    for sink in sinks:
        volume = sink.volume.value_flat * 100
        print('<separator label="Volume Control"/>')
        print(f'<item label="Sink: {sink.name}"/>')
        print(f'<item label="Volume: {volume:.0f}%"/>')
        print('<item label="Volume Up"><action name="Execute"><execute>pactl set-sink-volume "{}" +5%</execute></action></item>'.format(sink.name))
        print('<item label="Volume Down"><action name="Execute"><execute>pactl set-sink-volume "{}" -5%</execute></action></item>'.format(sink.name))
        print('<item label="Mute"><action name="Execute"><execute>pactl set-sink-mute "{}" toggle</execute></action></item>'.format(sink.name))

def launch_vlc():
    print('<separator label="No active media player"/>')
    print('<item label="Launch VLC"><action name="Execute"><execute>vlc</execute></action></item>')

def wait_for_vlc():
    # Wait for VLC to register with D-Bus
    for _ in range(10):
        time.sleep(1)
        running_players = get_running_players()
        if 'org.mpris.MediaPlayer2.vlc' in running_players:
            return 'org.mpris.MediaPlayer2.vlc'
    return None

if __name__ == "__main__":
    print('<openbox_pipe_menu>')
    running_players = get_running_players()
    active_player = None

    for player_service in running_players:
        status = get_player_playback_status(player_service)
        if status in ['Playing', 'Paused']:
            active_player = player_service
            break

    if active_player:
        player_icon = get_player_icon(active_player)
        generate_player_menu(active_player)
    else:
        launch_vlc()
        active_player = wait_for_vlc()
        if active_player:
            player_icon = get_player_icon(active_player)
            generate_player_menu(active_player)

    generate_volume_menu()
    print('</openbox_pipe_menu>')
	