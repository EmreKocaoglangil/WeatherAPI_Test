import requests
import json

from pprint import pprint

from config import API_KEY


city = (input('Please enter the city that you want to check the weather.'))

base_url = 'http://api.weatherapi.com/v1/current.json?key='+API_KEY+'&q='+city+'&aqi=no'

data_weather = requests.get(base_url).json()




print(city,' is', data_weather['current']['temp_c'],
      ' Celcius RN and feels like', data_weather['current']['feelslike_c'],'Celcius also the Wind is',data_weather['current']['wind_kph'] ,'Km/H')