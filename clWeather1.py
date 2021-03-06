# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 14:55:42 2019

@author: jrbrad
"""

import requests

def k2f(temp):
    return '{:4.1f}'.format((temp - 273.15) * 9./5. + 32.)

locZip = '23185'

""" Geolocation API using Google Geocoding API"""
""" A Google Developer account is required, with which one can 
    obtain an API key """
apiKeyGeocode = ''
urlGeoTemplate = 'https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'
urlGeo = urlGeoTemplate % (locZip,apiKeyGeocode)
response = requests.get(urlGeo)
response = response.json()
lat = response['results'][0]['geometry']['location']['lat']
lat = '{:5.2f}'.format(lat)
lon = response['results'][0]['geometry']['location']['lng']
lon = '{:5.2f}'.format(lon)

""" Weather web site comments:
      - temperature is in degrees Kelvin 
"""

""" A key is required from http://api.openweathermap.org/data/2.5/forecast """
template = 'https://api.openweathermap.org/data/2.5/forecast?zip=%s,us&appid=%s'
apiKeyWeather = ''
url = template % (locZip,apiKeyWeather)

response = requests.get(url)

response = response.json()

summary = {'tempMax':{'ind':0, 'value':0}, 'tempMin': {'ind':0, 'value':999}}

""" Find the highest and lowest temperature """
for i in range(len(response['list'])):
    #print('\n\n',response['list'][i]['dt_txt'], k2f(response['list'][i]['main']['temp_min']),k2f(response['list'][i]['main']['temp_max']))
    if response['list'][i]['main']['temp_min'] < summary['tempMin']['value']:
        summary['tempMin']['value'] = response['list'][i]['main']['temp_min']
        summary['tempMin']['ind']  = i
    if response['list'][i]['main']['temp_max'] > summary['tempMax']['value']:
        summary['tempMax']['value'] = response['list'][i]['main']['temp_max']
        summary['tempMax']['ind']  = i
        
print('\n\nSummary of four day forecast at zip code ' + str(locZip) + ', latitude '+ lat + ' longitude '+ lon +':')
print('High temperature: ', response['list'][summary['tempMax']['ind']]['dt_txt'], k2f(response['list'][summary['tempMax']['ind']]['main']['temp_max']))
print('Low temperature: ', response['list'][summary['tempMin']['ind']]['dt_txt'], k2f(response['list'][summary['tempMin']['ind']]['main']['temp_min']))