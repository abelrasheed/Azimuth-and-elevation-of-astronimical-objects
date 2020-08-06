#importing required modules

from astroquery.jplhorizons import Horizons
import requests
import data 
import polyline
from elevation import altitude_func

#creating a temporary dictionary to store location parameter to be sent to horizons
location = {}

# encoding the location coordinates into polyline
cord = polyline.encode([("lattitide","longitude")], 5)

#calling the altitude function
elev_obj = altitude_func(cord)

#adding the locations parameter to the object to be sent through the api request
location_temp = elev_obj[0]['location']
location['lat'] = location_temp['lat']
location['lon'] = location_temp['lng']
location['elevation'] = elev_obj[0]['elevation']
po = data.input_dat
po['location'] = location


#making the request
obj = Horizons(**po)
data_eph = obj.ephemerides(quantities =  4)


azimuth = data_eph['AZ']
elevation = data_eph['EL']
print(data_eph)


