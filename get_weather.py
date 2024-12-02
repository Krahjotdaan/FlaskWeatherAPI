import os
import json
import requests
from api_key import API_KEY


LOCATION_KEY = None
DATA_DIR = "weather_data"

def get_location_key(lat, lon):
    url = f"http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey={API_KEY}&q={lat},{lon}"
    response = requests.get(url)
    response.raise_for_status() 
    data = response.json()

    return data['Key']


def get_weather_data(location_key):
    url = f"http://dataservice.accuweather.com/currentconditions/v1/{location_key}?apikey={API_KEY}&details=true"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    return data


def write_weather_data_to_file(latitude, longitude, data):
    os.makedirs(DATA_DIR, exist_ok=True) 
    filename = os.path.join(DATA_DIR, f"{latitude}_{longitude}.json")
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
