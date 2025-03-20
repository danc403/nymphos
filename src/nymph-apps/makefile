CC = valac
CFLAGS = --pkg gtk3 -Wall -Werror  # Added warnings
EXEC = nymph-apps
PREFIX = /usr/local
BINDIR = $(PREFIX)/bin
DATADIR = $(PREFIX)/share/applications

all: $(EXEC)

$(EXEC): nymph-apps.vala
	$(CC) $(CFLAGS) -o $(EXEC) nymph-apps.vala

# Example rule for desktop file (adapt to your needs)
application-launcher.desktop: application-launcher.desktop.in icon.png
	sed "s|@EXEC@|$(EXEC)|g" application-launcher.desktop.in > application-launcher.desktop


install: $(EXEC) application-launcher.desktop
	sudo install -D $(EXEC) $(BINDIR)/$(EXEC) || (echo "Install failed" && exit 1)
    sudo install -D application-launcher.desktop $(DATADIR)/application-launcher.desktop || (echo "Desktop file install failed" && exit 1)

uninstall:
	sudo rm $(BINDIR)/$(EXEC) || (echo "Uninstall failed" && exit 1)
    sudo rm $(DATADIR)/application-launcher.desktop || (echo "Desktop file uninstall failed" && exit 1)

clean:
	rm -f $(EXEC) application-launcher.desktop

.PHONY: all install uninstall clean
