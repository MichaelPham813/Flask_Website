import urllib.request
import json
import socket
def get_location():
        
    #URL
    ISS_URL = "http://api.open-notify.org/iss-now.json"
    ISS_ALTERNATIVE_URL = "https://api.wheretheiss.at/v1/satellites/25544"

    #If open notify is broken or wonky use the alternative url to run

    #Getting JSON API
    # request = urllib.request.urlopen(ISS_URL)
    request = urllib.request.urlopen(ISS_ALTERNATIVE_URL)
    response = json.loads(request.read())

    #Get pos of coordinate
    # lat = response['iss_position']['latitude']
    # lon = response['iss_position']['longitude']
    lat = response['latitude']
    lon = response['longitude']   
    return lat,lon

print(get_location())
