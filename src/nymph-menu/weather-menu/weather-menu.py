#!/usr/bin/python -o
# -*- coding: utf-8 -*-

from urllib import urlopen, quote
from xml.etree.cElementTree import parse
from datetime import datetime, timedelta
import os
from os.path import join
from sys import argv
try:
    import cPickle as pickle
except ImportError:
    import pickle


TRANSLATED_TEXT = {
    'en': {
        'current': 'Current conditions',
        'weather': 'Weather',
        'temp': 'Temperature',
        'humidity': 'Humidity',
        'wind': 'Wind',
        'forecast': 'Forecast',
        'mintemp': 'Minimun Temperature',
        'maxtemp': 'Maximun Temperature'
    },
    'es': {
        'current': u'Actualmente',
        'weather': u'Tiempo',
        'temp': u'Temperatura',
        'humidity': u'Humedad',
        'wind': u'Viento',
        'forecast': u'Previsión',
        'mintemp': u'Temperatura Mínima',
        'maxtemp': u'Temperatura Máxima'
    },
    'fr': {
        'current': u'Actuel',
        'weather': u'Météo',
        'temp': u'Température',
        'humidity': u'Humidité',
        'wind': u'Vent',
        'forecast': u'Prévision',
        'mintemp': u'Température minimale',
        'maxtemp': u'Température maximale'
    },
    'de': {
        'current': u'Aktuell',
        'weather': u'Wetter',
        'temp': u'Temperatur',
        'humidity': u'Luftfeuchtigkeit',
        'wind': u'Wind',
        'forecast': u'Prognostizieren',
        'mintemp': u'Minimale Temperatur',
        'maxtemp': u'Höchste Temperatur'
    }
}


if len(argv) != 3:
    raise Exception('Usage: gweather.py city language.')
else:
    city = argv[1]
    lang = argv[2]



CACHE_HOURS = 1

WEATHER_URL = 'http://www.google.com/ig/api?weather=%s&hl=%s&oe=UTF-8'


def get_weather(city, lang):
    url = WEATHER_URL % (quote(city), quote(lang))
    data = parse(urlopen(url))
    
    forecasts = []
    for forecast in data.findall('weather/forecast_conditions'):
        forecasts.append(
    dict([(element.tag, element.get("data")) for element in forecast.getchildren()]))
    
    return {
        'forecast_information': dict([(element.tag, element.get("data")) for element in data.find('weather/forecast_information').getchildren()]),
        'current_conditions': dict([(element.tag, element.get("data")) for element in data.find('weather/current_conditions').getchildren()]),
        'forecasts': forecasts
    }

def get_openbox_pipe_menu(lang, forecast_information, current_conditions, forecasts):
    if lang == 'en-US':
        lang = 'en'
    
    tt = TRANSLATED_TEXT[lang]
    
    temp_var, temp_unit = ("temp_c", u"\u00b0C") if forecast_information['unit_system'] == "SI" else ("temp_f", "F")
    
    output = '<openbox_pipe_menu>'
    output += '\n<separator label="%s (%s)" />' % (weather['forecast_information']['city'],forecast_information['forecast_date'])
    output += '\n<separator label="%s" />' % tt['current']
    output += '<item label="%s: %s" />' % (tt['weather'], current_conditions['condition'])
    output += '<item label="%s: %s %s" />' % (tt['temp'], current_conditions[temp_var], temp_unit)
    output += '<item label="%s: %s" />' % (tt['humidity'], current_conditions['humidity'])
    output += '<item label="%s: %s" />' % (tt['wind'], current_conditions['wind_condition'])
    for forecast in forecasts:
        output += '\n<separator label="%s: %s" />' % (tt['forecast'], forecast['day_of_week'])
        output += '<item label="%s: %s" />' % (tt['weather'], forecast['condition'])
        output += '<item label="%s: %s %s" />' % ( tt['mintemp'], forecast['low'], temp_unit )
        output += '<item label="%s: %s %s" />' % ( tt['maxtemp'], forecast['high'], temp_unit )
    output += '\n</openbox_pipe_menu>'
    
    return output.encode('utf-8')

cache_file = join(os.getenv("HOME"), '.gweather.cache')

try:
    f = open(cache_file,'rb')
    cache = pickle.load(f)
    f.close()
except IOError:
    cache = None

if cache == None or (city, lang) not in cache or (
        cache[(city, lang)]['date'] + timedelta(hours=CACHE_HOURS) < datetime.utcnow()):
    # The cache is outdated
    weather = get_weather(city, lang)
    ob_pipe_menu = get_openbox_pipe_menu(lang, **weather)
    print ob_pipe_menu
    if cache == None:
        cache = dict()
    cache[(city, lang)] = {'date': datetime.utcnow(), 'ob_pipe_menu': ob_pipe_menu}
    
    #Save the data in the cache
    try:
        f = open(cache_file, 'wb')
        cache = pickle.dump(cache, f, -1)
        f.close()
    except IOError:
        raise
else:
    print cache[(city, lang)]['ob_pipe_menu']

"""Examples:
$ python .config/openbox/scripts/gweather3.py "New York" en
<openbox_pipe_menu>
<separator label="New York, NY (2009-07-17)" />
<separator label="Current conditions" /><item label="Weather: Clear" /><item label="Temperature: 79 F" /><item label="Humidity: Humidity: 66%" /><item label="Wind: Wind: N at 5 mph" />
<separator label="Forecast: Fri" /><item label="Weather: Chance of Storm" /><item label="Minimun Temperature: 70 F" /><item label="Maximun Temperature: 90 F" />
<separator label="Forecast: Sat" /><item label="Weather: Chance of Storm" /><item label="Minimun Temperature: 65 F" /><item label="Maximun Temperature: 85 F" />
<separator label="Forecast: Sun" /><item label="Weather: Mostly Sunny" /><item label="Minimun Temperature: 63 F" /><item label="Maximun Temperature: 83 F" />
<separator label="Forecast: Mon" /><item label="Weather: Chance of Showers" /><item label="Minimun Temperature: 65 F" /><item label="Maximun Temperature: 81 F" />
</openbox_pipe_menu>

$ python .config/openbox/scripts/gweather3.py "New York" es
<openbox_pipe_menu>
<separator label="New York, NY (2009-07-17)" />
<separator label="Actualmente" /><item label="Tiempo: Despejado" /><item label="Temperatura: 26 °C" /><item label="Humedad: Humedad: 66%" /><item label="Viento: Viento: N a 8 km/h" />
<separator label="Previsión: vie" /><item label="Tiempo: Posibilidad de tormenta" /><item label="Temperatura Mínima: 21 °C" /><item label="Temperatura Máxima: 32 °C" />
<separator label="Previsión: sáb" /><item label="Tiempo: Posibilidad de tormenta" /><item label="Temperatura Mínima: 18 °C" /><item label="Temperatura Máxima: 29 °C" />
<separator label="Previsión: dom" /><item label="Tiempo: Mayormente soleado" /><item label="Temperatura Mínima: 17 °C" /><item label="Temperatura Máxima: 28 °C" />
<separator label="Previsión: lun" /><item label="Tiempo: Posibilidad de chubascos" /><item label="Temperatura Mínima: 18 °C" /><item label="Temperatura Máxima: 27 °C" />
</openbox_pipe_menu>

$ python .config/openbox/scripts/gweather3.py "New York" fr
<openbox_pipe_menu>
<separator label="New York, NY (2009-07-17)" />
<separator label="Actuel" /><item label="Météo: Temps clair" /><item label="Température: 26 °C" /><item label="Humidité: Humidité : 66 %" /><item label="Vent: Vent : N à 8 km/h" />
<separator label="Prévision: ven." /><item label="Météo: Risques de tempête" /><item label="Température minimale: 21 °C" /><item label="Température maximale: 32 °C" />
<separator label="Prévision: sam." /><item label="Météo: Risques de tempête" /><item label="Température minimale: 18 °C" /><item label="Température maximale: 29 °C" />
<separator label="Prévision: dim." /><item label="Météo: Ensoleillé dans l'ensemble" /><item label="Température minimale: 17 °C" /><item label="Température maximale: 28 °C" />
<separator label="Prévision: lun." /><item label="Météo: Risques d'averses" /><item label="Température minimale: 18 °C" /><item label="Température maximale: 27 °C" />
</openbox_pipe_menu>

$ python .config/openbox/scripts/gweather3.py "New York" de
<openbox_pipe_menu>
<separator label="New York, NY (2009-07-17)" />
<separator label="Aktuell" /><item label="Wetter: Klar" /><item label="Temperatur: 26 °C" /><item label="Luftfeuchtigkeit: Feuchtigkeit: 66 %" /><item label="Wind: Wind: N mit 8 km/h" />
<separator label="Prognostizieren: Fr." /><item label="Wetter: Vereinzelt stürmisch" /><item label="Minimale Temperatur: 21 °C" /><item label="Höchste Temperatur: 32 °C" />
<separator label="Prognostizieren: Sa." /><item label="Wetter: Vereinzelt stürmisch" /><item label="Minimale Temperatur: 18 °C" /><item label="Höchste Temperatur: 29 °C" />
<separator label="Prognostizieren: So." /><item label="Wetter: Meist sonnig" /><item label="Minimale Temperatur: 17 °C" /><item label="Höchste Temperatur: 28 °C" />
<separator label="Prognostizieren: Mo." /><item label="Wetter: Vereinzelte Schauer" /><item label="Minimale Temperatur: 18 °C" /><item label="Höchste Temperatur: 27 °C" />
</openbox_pipe_menu>

$ python .config/openbox/scripts/gweather3.py "Göttingen" de
<openbox_pipe_menu>
<separator label="Göttingen, NDS (2009-07-17)" />
<separator label="Aktuell" /><item label="Wetter: Meistens bewölkt" /><item label="Temperatur: 21 °C" /><item label="Luftfeuchtigkeit: Feuchtigkeit: 49 %" /><item label="Wind: Wind: SW mit 13 km/h" />
<separator label="Prognostizieren: Fr." /><item label="Wetter: Meist sonnig" /><item label="Minimale Temperatur: 13 °C" /><item label="Höchste Temperatur: 23 °C" />
<separator label="Prognostizieren: Sa." /><item label="Wetter: Vereinzelt Regen" /><item label="Minimale Temperatur: 11 °C" /><item label="Höchste Temperatur: 16 °C" />
<separator label="Prognostizieren: So." /><item label="Wetter: Vereinzelt stürmisch" /><item label="Minimale Temperatur: 12 °C" /><item label="Höchste Temperatur: 17 °C" />
<separator label="Prognostizieren: Mo." /><item label="Wetter: Vereinzelt Regen" /><item label="Minimale Temperatur: 10 °C" /><item label="Höchste Temperatur: 20 °C" />
</openbox_pipe_menu>
"""
#
