project('media-control', 'vala',
  version : '0.1',
  default_options : ['warning_level=1'])

vala_version = '>=0.46'
gtk_version = '>=3.0'
pulse_version = '>=14.0'

vala_dep = dependency('vala', version : vala_version)
gtk_dep = dependency('gtk+-3.0', version : gtk_version)
pulse_dep = dependency('libpulse', version : pulse_version)

executable('media-control',
  'media_control.vala',
  dependencies : [vala_dep, gtk_dep, pulse_dep],
  install : true)
