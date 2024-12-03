"""
This module provides functions to retrieve weather data from the AccuWeather API.
"""

import requests
from api_key import API_KEY


def get_location_key(lat, lon):
    """
    Retrieves the location key from AccuWeather API using latitude and longitude.

    Args:
        lat: The latitude of the location.
        lon: The longitude of the location.

    Returns:
        The location key.

    Raises:
        requests.exceptions.HTTPError: If the API request fails.
    """

    url = f"http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey={API_KEY}&q={lat},{lon}"
    response = requests.get(url)
    response.raise_for_status() 
    data = response.json()

    return data['Key']


def get_weather_data(location_key):
    """
    Retrieves current weather data from AccuWeather API using a location key.

    Args:
        location_key: The location key obtained from get_location_key().

    Returns:
        A dictionary containing the weather data.

    Raises:
        requests.exceptions.HTTPError: If the API request fails.
    """
    
    url = f"http://dataservice.accuweather.com/currentconditions/v1/{location_key}?apikey={API_KEY}&details=true"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    return data
