# Makefile for nymph-run

# Compiler and linker flags
CC = valac
CFLAGS = --pkg gtk+-3.0
LDLIBS = -pthread

# Executable name
TARGET = nymph-run

# Source files
SOURCES = nymph-run.vala

# Object files
OBJECTS = $(SOURCES:.vala=.o)

# Installation directories
PREFIX ?= /usr/local
BINDIR = $(PREFIX)/bin
DATADIR = $(PREFIX)/share/applications

# Desktop file name
DESKTOP_FILE = nymph-run.desktop

all: $(TARGET)

$(TARGET): $(OBJECTS)
	$(CC) $(CFLAGS) -o $@ $^ $(LDLIBS)

%.o: %.vala
	$(CC) $(CFLAGS) -c $< -o $@

install: all
	install -D $(TARGET) $(BINDIR)/$(TARGET)
	install -D $(DESKTOP_FILE) $(DATADIR)/$(DESKTOP_FILE)

uninstall:
	rm -f $(BINDIR)/$(TARGET)
	rm -f $(DATADIR)/$(DESKTOP_FILE)

clean:
	rm -f $(OBJECTS) $(TARGET)

.PHONY: all install uninstall clean
