Name:           stallman
Version:        1.0
Release:        1%{?dist}
Summary:        A simple CLI tool to interact with the rss feed on Richard Stallmans website

License:        GPLv3+
URL:            https://example.com/stallman  # Replace with a real URL if available
Source0:        stallman-1.0.tar.xz

BuildArch:      noarch  # Since it's a Python script

Requires:       python3

%description
This is a simple command-line tool inspired by Richard Stallman.
A simple CLI tool to interact with the rss feed on Richard Stallmans website.
%prep
%autosetup -n stallman-1.0

%build
# No build process needed for a simple Python script.  Just need to make it executable.
chmod +x stallman.py

%install
# Install the Python script to /usr/local/bin and make it executable.
install -D -m 0755 stallman.py %{buildroot}/usr/local/bin/stallman

%files
/usr/local/bin/stallman

%changelog
* Mon Oct 23 2023 Your Name <your.email@example.com> - 1.0-1
- Initial package.
