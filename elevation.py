#function to calculate the altitude 
import requests



def altitude_func(cord):
        param ={'locations' : cord,
                'access-token' : 'Your access token here'
        }

        elevations =  requests.get('https://api.jawg.io/elevations',params=param)
        out = elevations.json()
        return out