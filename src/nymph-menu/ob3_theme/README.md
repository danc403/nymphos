
ob3_theme.c-v0.07.2:
  ob3_theme is an openbox3 pipe-menu program that generates an xml menu
  based on available themes. The menu entry can be clicked to change to
  the selected theme.
 *
Requirements:
  openbox 3.0    - http://www.openbox.org/
  gtk+ 2.x       - http://www.gtk.org/
 *
Compiling:
  gcc -Wall -O2 `pkg-config --cflags gtk+-2.0 obparser-3.0` ob3_theme.c -o \
      ob3_theme `pkg-config --libs gtk+-2.0 obparser-3.0`
 *
Usage:
  ~/.config/openbox/rc.xml:
    <theme>
      <name>~/.config/ob3_theme/theme</name>
    </theme>
 *
  ~/.config/openbox/menu.xml:
    <menu id="ob3_theme" label="Themes" execute="ob3_theme" />
 *
Created Files/Directories:
  ~/.config/ob3_theme
  ~/.config/ob3_theme/theme   (current theme, symlink)
 *
Notes:
  ob3_theme does NOT modify your config. Instead, when rc.xml is configured
  as above, openbox uses a symlink. This symlink is managed by ob3_theme.
 *
  The theme currently in use will be denoted with an arrow.
 *
(c) 2003 Mike Hokenson <logan at dct dot com>
All rights reserved.
 *
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the distribution.
3. The name of the author may not be used to endorse or promote products
   derived from this software without specific prior written permission.
 *
THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.



--- Changelog --------------------------------------------------------------
 *
 0.01 - 2003/09/23:
   initial release.
 *
 0.02 - 2003/10/17:
   x[ht]ml-ize the name to allow for themes containing <>&'" or other
     characters the xml parser may not like.
   use g_warning() instead of g_warning().
 *
 0.03 - 2003/10/21:
   relocated configuration to ~/.config/ob3_theme.
   include openbox/parse.h for XDG related functions.
   remove glib.h include (already included with openbox/parser.h).
 *
 0.04 - 2003/10/22:
   use full path to theme directory instead of the name. this allows for
     multiple themes with the same name, but only one is denoted.
   add recursive mkdir for ~/.config (or $XDG_CONFIG_HOME).
   fix improper g_return_[val]if_fail() usage.
   other cleanups.
 *
 0.05 - 2003/11/07:
   require openbox 3.0. remove ob3_mkdir* and use parse_mkdir*, dupe check.
   make ob3_readlink() return an allocated buffer.
   move parse_paths_shutdown() to ob3_exit().
   updated ob3_string_to_xml_safe() to only encode <>&'" and non-printable
     characters.
   use g_shell_quote() on paths.
   use g_warning() instead of ob3_error().
   use g_path_get_basename() instead of deprecated g_basename().
   when creating ~/.config/ob3_theme/theme symlink, first try the openbox
     config file, then fallback to 'TheBear'.
   reworked gdk_property_get() call to get _OPENBOX_PID.
   other cleanups.
 *
 0.06 - 2003/11/15:
   add in pipe-menu helpers, use xml functions to print the created menu.
     removed ob3_string_to_xml_safe().
   use g_critical() in appropriate situations.
 *
 0.07 - 2004/11/08:
   minor cleanups.
 *
 0.07.1 - 2006/08/27:
   fix libxml signedness warnings
 *
--- Changelog --------------------------------------------------------------

