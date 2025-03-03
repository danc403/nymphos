import os
import re
from datetime import datetime

def update_changelog(spec_file, new_date, new_name, new_email):
    """Replaces all changelog entries in a .spec file and adds the version."""

    try:
        with open(spec_file, 'r') as f:
            lines = f.readlines()

        updated_lines = []
        changelog_started = False
        version = None

        for line in lines:
            if line.startswith('Version:'):
                version = line.split(':')[1].strip()
            if line.startswith('%changelog'):
                changelog_started = True
                updated_lines.append(line)
                continue

            if changelog_started and line.strip().startswith('*'):
                updated_line = f"* {new_date} {new_name} <{new_email}> - {version}-1\n"
                updated_lines.append(updated_line)
            else:
                updated_lines.append(line)

        with open(spec_file, 'w') as f:
            f.writelines(updated_lines)

        print(f"Updated changelog in {spec_file}")

    except FileNotFoundError:
        print(f"File not found: {spec_file}")
    except Exception as e:
        print(f"Error processing {spec_file}: {e}")

def main():
    spec_dir = "./specs"  # Change to your spec file directory
    new_date = datetime.now().strftime("%a %b %d %Y")
    new_name = "Dan Carpenter"
    new_email = "danc403@gmail.com"

    for filename in os.listdir(spec_dir):
        if filename.endswith(".spec"):
            spec_file = os.path.join(spec_dir, filename)
            update_changelog(spec_file, new_date, new_name, new_email)

if __name__ == "__main__":
    main()
