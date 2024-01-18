# api_handler.py

import requests
import json.decoder  # Import the JSONDecodeError class

def get_weather(latitude, longitude):
    base_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m",
        "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m",
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        print(f"Response Status Code: {response.status_code}")
        print(f"Number of bytes received: {len(response.content)}")
        print(f"Raw Response Content: {response.content}")

        if not response.content:
            print("Empty response content. Unable to fetch weather data.")
            return None

        # Attempt to decode JSON
        try:
            data = response.json()
            return data
        except json.decoder.JSONDecodeError as err:
            print(f"JSON Decode Error: {err}")
            return None

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.RequestException as err:
        print(f"Request Error: {err}")
    except Exception as err:
        print(f"Error: {err}")

    return None
