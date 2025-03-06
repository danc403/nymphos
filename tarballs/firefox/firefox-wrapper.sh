#!/bin/bash

# Detect the user's locale setting.
# This line retrieves the LANG variable from the system's locale settings.
# It uses 'locale', 'grep', and 'awk' to extract the language code.
locale=$(locale | grep LANG | awk -F '=' '{print $2}' | awk -F '.' '{print $1}')

# Use a 'case' statement to determine which Firefox executable to launch.
# The '$locale' variable is matched against the supported locale codes.
case "$locale" in
    # If the locale is English (US), launch the English (US) Firefox.
    en_US)
        /usr/lib/firefox-en_US/firefox "$@"
        ;;
    # If the locale is Spanish (Spain), launch the Spanish (Spain) Firefox.
    es_ES)
        /usr/lib/firefox-es_ES/firefox "$@"
        ;;
    # If the locale is French (France), launch the French (France) Firefox.
    fr_FR)
        /usr/lib/firefox-fr_FR/firefox "$@"
        ;;
    # If the locale is Italian (Italy), launch the Italian (Italy) Firefox.
    it_IT)
        /usr/lib/firefox-it_IT/firefox "$@"
        ;;
    # If the locale is Russian (Russia), launch the Russian (Russia) Firefox.
    ru_RU)
        /usr/lib/firefox-ru_RU/firefox "$@"
        ;;
    # If the locale is Hindi (India), launch the Hindi (India) Firefox.
    hi_IN)
        /usr/lib/firefox-hi_IN/firefox "$@"
        ;;
    # If the locale is Japanese (Japan), launch the Japanese (Japan) Firefox.
    ja_JP)
        /usr/lib/firefox-ja_JP/firefox "$@"
        ;;
    # If the locale is Simplified Chinese (China), launch the Simplified Chinese (China) Firefox.
    zh_CN)
        /usr/lib/firefox-zh_CN/firefox "$@"
        ;;
    # If the locale is not recognized, launch the default English (US) Firefox.
    *)
        /usr/lib/firefox-en_US/firefox "$@"
        ;;
esac

# Explanation:
# - "$@" passes all command-line arguments to the Firefox executable.
# - The 'case' statement allows for easy expansion to include more locales.
# - The default case ensures that Firefox can always be launched, even if the locale detection fails.

