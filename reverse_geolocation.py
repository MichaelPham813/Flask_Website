import urllib.request
import json


def get_country(lat,lon):
    API_KEY = 'bdc_9b826110ec8744559b072514c71c01aa'
    URL = f'https://api-bdc.net/data/reverse-geocode?latitude={lat}&longitude={lon}&localityLanguage=en&key={API_KEY}'
    
    request = urllib.request.urlopen(URL,timeout = 15)
    response = json.loads(request.read())
    
    return response
