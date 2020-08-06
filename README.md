# Azimuth-and-elevation-of-astronomical-objects
This code provides a python script to request for the azimuth and elevation of objects inside the solar systems using JPL_HORIZONS web interface.

The location coordinates must be plugged manually. The eleavation is obtained using jawg maps api. This request requires an API key. So feel free to use tour choice of API server to get the elevation, and even the location coordinates. 
The main file is requesting.py. The data for the API call is provided in the data.py file (You must fill in the required data). The elevation is obtained using the elevation.py file.
The data must be filled is commented out. If got any doubts about the type of data to be plugged, please visit https://astroquery.readthedocs.io/en/latest/jplhorizons/jplhorizons.html
