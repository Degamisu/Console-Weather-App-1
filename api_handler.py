# api_handler.py

import requests
import json.decoder  # Import the JSONDecodeError class

def get_weather(city):
    base_url = "https://api.open-meteo.com/v1/forecast"
    params = {"forecast": "now", "daily": "weathercode", "timezone": "auto", "city": city}
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        print(f"Response Status Code: {response.status_code}")
        print(f"Response Content: {response.text}")

        data = response.json()
        return data
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.RequestException as err:
        print(f"Request Error: {err}")
    except json.decoder.JSONDecodeError as err:
        print(f"JSON Decode Error: {err}")
    except Exception as err:
        print(f"Error: {err}")

    return None
