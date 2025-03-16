import os

def generate_makefile_auto_pot(locale_dir="./locale"):
    """
    Generates a Makefile in the current directory to build translations
    from existing .po files, automatically detecting the .pot file.

    Args:
        locale_dir (str): The directory where the locales will be installed.
    """
    po_files = [f for f in os.listdir() if f.endswith(".po")]
    pot_files = [f for f in os.listdir() if f.endswith(".pot")]

    if not pot_files:
        print("Error: No .pot file found in the current directory. Makefile not generated.")
        return

    if len(pot_files) > 1:
        print("Warning: Multiple .pot files found. Using the first one found:", pot_files[0])
        pot_filename = pot_files[0]
    else:
        pot_filename = pot_files[0]

    if not po_files:
        print("No .po files found in the current directory. Makefile not generated.")
        return

    gettext_package = pot_filename.replace(".pot", "")

    makefile_content = f"""
GETTEXT_PACKAGE = {gettext_package}
LOCALEDIR = {locale_dir}

.PHONY: all install clean update-po {' '.join([f.replace('.po', '.mo') for f in po_files])}

all: {' '.join([f.replace('.po', '.mo') for f in po_files])}

"""

    for po_file in po_files:
        lang_code = po_file.replace(".po", "")
        mo_file = lang_code + ".mo"
        makefile_content += f"""
{po_file}: {pot_filename}
\t@echo "Updating {po_file}..."
\tmsgmerge --update {po_file} {pot_filename} --no-wrap

{mo_file}: {po_file}
\t@echo "Building {mo_file}..."
\tmsgfmt {po_file} -o {mo_file}

"""

    makefile_content += """
install:
\tinstall -d "$(LOCALEDIR)"
"""
    for po_file in po_files:
        lang_code = po_file.replace(".po", "")
        mo_file = lang_code + ".mo"
        makefile_content += f"""
\tinstall -d "$(LOCALEDIR)/{lang_code}/LC_MESSAGES"
\tinstall -m 644 {mo_file} "$(LOCALEDIR)/{lang_code}/LC_MESSAGES/$(GETTEXT_PACKAGE).mo"
"""

    makefile_content += """
update-po:
"""
    for po_file in po_files:
        makefile_content += f"""
\tmake {po_file}
"""

    makefile_content += """
clean:
\trm -f *.mo
"""
    for po_file in po_files:
        lang_code = po_file.replace(".po", "")
        makefile_content += f"""
\trm -f "$(LOCALEDIR)/{lang_code}/LC_MESSAGES/$(GETTEXT_PACKAGE).mo"
"""

    with open("Makefile", "w") as f:
        f.write(makefile_content)

    print("Makefile generated successfully.")

if __name__ == "__main__":
    generate_makefile_auto_pot()
