# nymph-keybindings

`nymph-keybindings` is a tool for managing keybindings in the Openbox window manager. It allows users to easily add, edit, and remove keybindings directly from a graphical interface.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
  - [Setting Up the Development Environment](#setting-up-the-development-environment)
  - [Adding or Modifying Keybindings](#adding-or-modifying-keybindings)
  - [Localizations](#localizations)
    - [Adding a New Language](#adding-a-new-language)
    - [Updating Existing Translations](#updating-existing-translations)
- [License](#license)

## Installation

### From Source

1. **Clone the repository:**
   ```sh
   git clone https://github.com/danc403/nymph-keybindings.git
   cd nymph-keybindings
2. 
Install dependencies:
Ensure you have the necessary dependencies installed. On a Debian-based system, you can install them using:
sudo apt-get update
sudo apt-get install valac libgtk-3-dev libgee-dev libxml2-dev desktop-file-utils xdg-utils gettext
3. 
Compile and install:
./autogen.sh
./configure
make
sudo make install
From RPM Package
1. 
Build the RPM package:
rpmbuild -ba nymph-keybindings.spec
2. 
Install the RPM package:
sudo rpm -i ~/rpmbuild/RPMS/x86_64/nymph-keybindings-1.0-1.x86_64.rpm
Usage
1. 
Launch the application:
• You can launch `nymph-keybindings` from your application menu or by running the following command in the terminal:
nymph-keybindings
2. 
User Keybindings:
• Click on the "User Keybindings" button to manage user-specific keybindings.
• The application will load the keybindings from `~/.config/openbox/rc.xml`.
3. 
System Keybindings:
• Click on the "System Keybindings" button to manage system-wide keybindings.
• The application will load the keybindings from `/etc/xdg/openbox/rc.xml`.
• Note: Root permissions are required to edit system keybindings.
4. 
Restore Default Keybindings:
• Click on the "Restore User Keybindings from System Defaults" button to reset user keybindings to the system defaults.
5. 
Add Keybinding:
• Click on the "Add Keybinding" button to add a new keybinding.
• Enter the key combination, action, and name for the new keybinding.
6. 
Remove Keybinding:
• Select a keybinding in the list and click on the "Remove Keybinding" button to remove it.
7. 
Save:
• Click on the "Save" button to save the changes to the keybindings file.
Contributing
Setting Up the Development Environment
1. 
Clone the repository:
git clone https://github.com/danc403/nymph-keybindings.git
cd nymph-keybindings
2. 
Install dependencies:
Ensure you have the necessary dependencies installed. On a Debian-based system, you can install them using:
sudo apt-get update
sudo apt-get install valac libgtk-3-dev libgee-dev libxml2-dev desktop-file-utils xdg-utils gettext
3. 
Compile the application:
./autogen.sh
./configure
make
4. 
Run the application:
./nymph-keybindings
Adding or Modifying Keybindings
• 
Adding Keybindings:
• Open `nymph-keybindings.vala` and modify the code to add new keybindings or modify existing ones.
• Ensure that the keybinding logic is correctly implemented.
• 
Modifying Keybindings:
• Locate the section in `nymph-keybindings.vala` where keybindings are loaded and saved.
• Update the logic to reflect any changes you want to make.
Localizations
Adding a New Language
1. 
Generate a new `.po` file:
• Use `msginit` to create a new `.po` file for the desired language. For example, to add Spanish (`es`):
msginit -i po/nymph-keybindings.pot -o po/es.po -l es
2. 
Translate the `.po` file:
• Open the newly created `.po` file in a text editor or a translation tool like `Poedit`.
• Translate the strings provided in the file.
3. 
Compile the `.po` file:
• Compile the `.po` file to a `.mo` file:
cd po
make all
4. 
Commit and push the changes:
• Add the new `.po` file to the repository and commit your changes:
git add po/es.po
git commit -m "Add Spanish localization"
git push
Updating Existing Translations
1. 
Update the `.pot` file:
• Ensure that the `.pot` file is up-to-date with the latest strings from the source code:
xgettext -k_ -kN_ -kC_ -kNC_ -kQ_ -kP_ -kQ_ -kCP_ -kCQ_ -kQT_ -kD_ -kDP_ -kN_ -kNC_ -kNQ_ -kNP_ -kNCP_ -kNQT_ -kDP_ -kD_ -kP_ -kQ_ -kCP_ -kCQ_ -kQT_ -kN_ -kNC_ -kNQ_ -kNP_ -kNCP_ -kNQT_ -kDP_ -kD_ -kP_ -kQ_ -kCP_ -kCQ_ -kQT_ -kN_ -kNC_ -kNQ_ -kNP_ -kNCP_ -kNQT_ -kDP_ -kD_ -kP_ -kQ_ -kCP_ -kCQ_ -kQT_ -kN_ -kNC_ -kNQ_ -kNP_ -kNCP_ -kNQT_ -kDP_ -kD_ -kP_ -kQ_ -kCP_ -kCQ_ -kQT_ -kN_ -kNC_ -kNQ_ -kNP_ -kNCP_ -kNQT_ -kDP_ -kD_ -kP_ -kQ_ -kCP_ -kCQ_ -kQT_ -kN_ -kNC_ -kNQ_ -kNP_ -kNCP_ -kNQT_ -kDP_ -kD_ -kP_ -kQ_ -kCP_ -kCQ_ -kQT_ -kN_ -kNC_ -kNQ_ -kNP_ -kNCP_ -kNQT_ -kDP_ -kD_ -kP_ -kQ_ -kCP_ -kCQ_ -kQT_ -kN_ -kNC_ -kNQ_ -kNP_ -kNCP_ -kNQT_ -kDP_ -kD_
2. 
Update the `.po` files:
• Use `msgmerge` to update the existing `.po` files with the new strings from the `.pot` file:
cd po
for po in *.po; do
    msgmerge -U $po nymph-keybindings.pot
done
3. 
Compile the `.po` files:
• Compile the updated `.po` files to `.mo` files:
make all
4. 
Commit and push the changes:
• Add the updated `.po` files to the repository and commit your changes:
git add po/*.po
git commit -m "Update existing translations"
git push
License
`nymph-keybindings` is licensed under the GPLv3+ license. See the LICENSE file for more details.

### Directory Structure

Ensure your source tarball `nymph-keybindings-1.0.tar.gz` contains the following structure:
nymph-keybindings-1.0/
├── README.md
├── LICENSE
├── src/
│ └── nymph-keybindings.vala
├── nymph-keybindings.desktop
├── po/
│ ├── de.po
│ ├── es.po
│ ├── fr.po
│ ├── ja.po
│ ├── zh_CN.po
│ └── nymph-keybindings.pot
├── configure.ac
├── Makefile.am
└── autogen.sh

### Additional Configuration:

**configure.ac:**
```m4
AC_INIT([nymph-keybindings], [1.0], [danc403@gmail.com])
AM_INIT_AUTOMAKE([-Wall -Werror foreign])
AC_PROG_CC
AM_PROG_VALAC([0.40])
IT_PROG_INTLTOOL([0.50.1])
AC_CONFIG_FILES([Makefile])
AC_OUTPUT
Makefile.am:
bin_PROGRAMS = nymph-keybindings
nymph_keybindings_SOURCES = src/nymph-keybindings.vala

appdatadir = $(datadir)/applications
appdata_DATA = nymph-keybindings.desktop

po_makefile_in = po/Makefile.in.in
autogen.sh:
#!/bin/sh
set -e
aclocal --install
autoreconf --force --install
Make sure to give `autogen.sh` execute permissions:
chmod +x autogen.sh
