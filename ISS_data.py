from ISS_location import get_location
from reverse_geolocation import get_country
from country_locaion import get_country_data
from distance_calc import dist
from weather_check import get_weather
#ISS Location function and variables

def ISS_dataset():
    # #Get ISS coordinate
    coor = get_location()
    lat,lon = coor[0],coor[1]
    #Sudbury cords
    # lat 46.493919 lon -80.995415
    #Call in weather API and weather function
    weather = get_weather(lat,lon)
    celcius_temp = round(weather['main']['temp'] - 273.15,2)
    desc = weather['weather'][0]
    description = desc['description']

    # #Country information
    country = get_country(lat,lon)

    over_water = None
    country_name = country['countryName']
    country_data = get_country_data(country_name)
    flag = None
    if(country_name == ''):
        over_water = 'Over water'

    else:
        over_water = country_name
        if country_data['data'] == '':
            flag_data = ''
        else:
            flag_data = country_data['data']
            flag_link = flag_data['href']
            flag = flag_link['flag']

        
    #Get distance from ISS to my resident
    #Default location Sudbury near Cambrian College 
    distance_from_ISS = dist(lat,lon,46.493919,-80.995415)
    return celcius_temp,description,country_name,over_water,distance_from_ISS,flag



