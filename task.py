# import the required libraries
import pandas as pd
import numpy as np
import seaborn as sns

import requests
import os
import dotenv

def get_weather_data(latitude, longitude) -> dict:
    api_key = "d0f963a8c4a7942ce3029ec4fb0ff65f"
    if api_key:
        print("API KEY Found!!!", api_key)
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"
        response =  requests.get(url)
        print(response.status_code)
        if response.status_code == 200:
            
            result = response.json()

            return result
    

def extract_current(weather_data):
    current_weather = ...
    
    return current_weather


def save_to_csv(filename):
    if filename in os.listdir(): # if file already exists
        # populate the csv file
        pass
    else:
        ## save to the empty file
        pass

def get_coord(city):
    # Use this function to get the latitude and longitude
    url = f"https://geocode.maps.co/search?q={city}&api_key=65c4b7ee942df610164192nzce4ad7e"
    result = requests.get(url).json()
    res = result[0]
    latitude, longitude = float(res['lat']), float(res['lon'])
    return latitude, longitude

def main():
    # run the code
    pass
    lat, lon = ...