# import the required libraries
import pandas as pd
import numpy as np
import seaborn as sns

import requests
import os
import dotenv
import time

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
        else:
            print("error:", response.status_code)
            return None

    else:
        print("API key not found")
        return None

def extract_current(weather_data):
    current_weather = {
'description' : weather_data['weather'][0]['description'],
'Temperature' : weather_data['main']['temp'],
'Humidity' : weather_data['main']['humidity'],
'Pressure' : weather_data['main']['pressure']
                      }
    
    return current_weather


def save_to_csv(filename, weather_data):
    if filename in os.listdir(): # if file already exists
        # populate the csv file
        df = pd.read_csv(filename)
        new_data = pd.DataFrame(weather_data, index=[0])
        df = pd.concat([df, new_data], ignore_index=True)
        df.to_csv(filename, index=False)
    else:
        ## save to the empty file
        df = pd.DataFrame(weather_data, index=[0])
        df.to_csv(filename, index=False)


def get_coord(city):
    # Use this function to get the latitude and longitude
    url = f"https://geocode.maps.co/search?q={city}&api_key=65c4b7ee942df610164192nzce4ad7e"
    result = requests.get(url).json()
    res = result[0]
    latitude, longitude = float(res['lat']), float(res['lon'])
    return latitude, longitude

def main():
    # run the code
    city_name= input("Enter city name: ")

    latitude, longitude = get_coord(city_name)

    end_time = time.time() + 18000

    while time.time() < end_time:

        weather_data = get_weather_data(latitude, longitude)

        if weather_data:
            current_weather = extract_current(weather_data)
            
            data_to_save = {'City': [city_name], 'Latitude': [latitude], 'Longitude': [longitude], 'Current Weather': [current_weather]}
            save_to_csv("weather_data.csv", data_to_save)
            print("Data is saved to weather_data.csv")
        else:
            print("Failed to fetch weather data.")
        time.sleep(600)
main()
