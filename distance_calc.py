import geopy.distance

def dist(ISS_lat, ISS_lon,lat,lon):
    coords_1 = (ISS_lat,ISS_lon)
    coords_2 = (lat,lon)
    distance = round((geopy.distance.distance(coords_1,coords_2).km),2)
    return distance