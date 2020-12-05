#! /usr/bin/python3
# fetchWeaterData.py - pulls json data from openweathermap.org and
# prints data.

import requests
import json
from pprint import pprint
from sys import argv, exit
def weatherForecast():
	print('')
	if len(argv) < 2:
		print('Usage: fetchWeatherData.py location')
		exit()
	siteData = requests.get('http://api.openweathermap.org/data/2.5/forecast?q=%s&appid=0a54021e232c7a9915131ce68cf08812' % ' '.join(argv[1:]))
	if siteData.status_code != 200:
		print('Failed! Status Code: %s' % siteData.status_code)
	else:
		siteJson = json.loads(siteData.text)
		for i in range(0, 7):
			print(siteJson['list'][i]['dt_txt'])
			print(siteJson['list'][i]['main']['temp'])
			print(siteJson['list'][i]['weather'][0]['description'])
			print('')

weatherForecast()
