
# coding: utf-8


import json
import requests
import urllib

url = "http://api.openweathermap.org/data/2.5/weather?lat=35&lon=139&units=metric&appid=2de143494c0b295cca9337e1e96b00e0"
response = urllib.request.urlopen(url)
parsed_json = json.loads(response.read().decode(response.info().get_param('charset') or 'utf-8'))
print(parsed_json)
kolekcja = (parsed_json['main'])
print (kolekcja)
print ("temperatura = %s\u2103" % kolekcja['temp'])  # stopień \xb0, stopień celcjusza \u2103




