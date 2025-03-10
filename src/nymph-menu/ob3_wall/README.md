
ob3_wall.c-v0.08.1:
  ob3_wall is an openbox3 pipe-menu program that generates an xml menu
  based on available wallpaper. The menu entry can be clicked to change to
  the current wallpaper.
 *
Requirements:
  openbox 3.0    - http://www.openbox.org/
 *
Compiling:
  gcc -Wall -O2 `pkg-config --cflags obparser-3.0` ob3_wall.c -o \
     ob3_wall `pkg-config --libs obparser-3.0`
 *
Usage:
  ~/.config/openbox/menu.xml:
    <menu id="ob3_wall" label="Wallpaper" execute="ob3_wall" />
 *
Created Files/Directories:
  ~/.config/ob3_wall
  ~/.config/ob3_wall/rc.xml   (configuration)
  ~/.config/ob3_wall/wall     (current wallpaper, symlink)
 *
Notes:
  ob3_wall creates a menu with all files found in the specified directories.
  There is no special check for known image types, it is assumed any files
  in these directories would be images only.
 *
  ob3_wall can be used in ~/.xinitrc to setup the wallpaper selected from
  a previous X session, just add in 'ob3_wall -' before openbox.
 *
  The wallpaper currently in use will be denoted with an arrow.
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
 0.01 - 2003/10/19:
   initial release.
 *
 0.02 - 2003/10/21:
   relocated configuration to ~/.config/ob3_wall.
   denote currently used wallpaper with an arrow.
   include openbox/parse.h for XDG related functions.
   use XDG data dirs as defaults, empty when user-defined dirs are found.
   remove glib.h include (already included with openbox/parser.h).
 *
 0.03 - 2003/10/22:
   added some generic checks for image types. ignore README, *.txt or 
     files with no extentions.
   if no 'command' is specified in the config file, $PATH will be scanned
     for: bsetbg, Esetroot, wmsetbg, xsetbg, xli, qiv, and xv. if nothing
     is found, an error will be displayed and ob3_wall will exit.
   add recursive mkdir for ~/.config (or $XDG_CONFIG_HOME).
   fix improper g_return_[val]if_fail() usage.
 *
 0.04 - 2003/11/04:
   require openbox 3.0. remove ob3_mkdir* and use parse_mkdir*, dupe check.
   make ob3_readlink() return an allocated buffer.
   move parse_paths_shutdown() to ob3_exit().
   use system paths if no custom dirs have been configured (in rc), check
     for dupes before adding wallpaper to the list.
   updated ob3_string_to_xml_safe() to only encode <>&'" and non-printable
     characters.
   use g_shell_quote() on paths.
   use g_warning() instead of ob3_error().
   use g_path_get_basename() instead of deprecated g_basename().
   use parse_expand_tidle() instead of ob3_expand_tilde().
   do tilde expansion on 'command' (config).
   other cleanups.
 *
 0.05 - 2003/11/06:
   convert config to xml, renamed to rc.xml.
 *
 0.06 - 2003/11/15:
   add in pipe-menu helpers, use xml functions to print the created menu.
     removed ob3_string_to_xml_safe().
   use g_critical() in appropriate situations.
 *
 0.07 - 2004/11/08:
   misc cleanups.
 *
 0.07.1 - 2006/08/27:
   fix libxml signedness warnings
 *
 0.08 - 2006/10/25:
   resolve relative paths when creating the symlink
 *
 0.08.1 - 2006/10/31:
   don't remove symlink on reuse last
 *
--- Changelog --------------------------------------------------------------

