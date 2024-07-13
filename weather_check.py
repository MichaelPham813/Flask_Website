import urllib
import json


def get_weather(lat,lon):
    API_KEY = '38cc08e46aa1fd12229524e91e84c96e'
    WEATHER_URL = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'
    
    request = urllib.request.urlopen(WEATHER_URL,timeout = 15)
    response = json.loads(request.read())
    
    return response