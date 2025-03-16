
GETTEXT_PACKAGE = nymph-keybindings
LOCALEDIR = ./locale

.PHONY: all install clean update-po fr.mo es.mo pt.mo de.mo

all: fr.mo es.mo pt.mo de.mo


fr.po: nymph-keybindings.pot
	@echo "Updating fr.po..."
	msgmerge --update fr.po nymph-keybindings.pot --no-wrap

fr.mo: fr.po
	@echo "Building fr.mo..."
	msgfmt fr.po -o fr.mo


es.po: nymph-keybindings.pot
	@echo "Updating es.po..."
	msgmerge --update es.po nymph-keybindings.pot --no-wrap

es.mo: es.po
	@echo "Building es.mo..."
	msgfmt es.po -o es.mo


pt.po: nymph-keybindings.pot
	@echo "Updating pt.po..."
	msgmerge --update pt.po nymph-keybindings.pot --no-wrap

pt.mo: pt.po
	@echo "Building pt.mo..."
	msgfmt pt.po -o pt.mo


de.po: nymph-keybindings.pot
	@echo "Updating de.po..."
	msgmerge --update de.po nymph-keybindings.pot --no-wrap

de.mo: de.po
	@echo "Building de.mo..."
	msgfmt de.po -o de.mo


install:
	install -d "$(LOCALEDIR)"

	install -d "$(LOCALEDIR)/fr/LC_MESSAGES"
	install -m 644 fr.mo "$(LOCALEDIR)/fr/LC_MESSAGES/$(GETTEXT_PACKAGE).mo"

	install -d "$(LOCALEDIR)/es/LC_MESSAGES"
	install -m 644 es.mo "$(LOCALEDIR)/es/LC_MESSAGES/$(GETTEXT_PACKAGE).mo"

	install -d "$(LOCALEDIR)/pt/LC_MESSAGES"
	install -m 644 pt.mo "$(LOCALEDIR)/pt/LC_MESSAGES/$(GETTEXT_PACKAGE).mo"

	install -d "$(LOCALEDIR)/de/LC_MESSAGES"
	install -m 644 de.mo "$(LOCALEDIR)/de/LC_MESSAGES/$(GETTEXT_PACKAGE).mo"

update-po:

	make fr.po

	make es.po

	make pt.po

	make de.po

clean:
	rm -f *.mo

	rm -f "$(LOCALEDIR)/fr/LC_MESSAGES/$(GETTEXT_PACKAGE).mo"

	rm -f "$(LOCALEDIR)/es/LC_MESSAGES/$(GETTEXT_PACKAGE).mo"

	rm -f "$(LOCALEDIR)/pt/LC_MESSAGES/$(GETTEXT_PACKAGE).mo"

	rm -f "$(LOCALEDIR)/de/LC_MESSAGES/$(GETTEXT_PACKAGE).mo"
