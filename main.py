# main.py

from api_handler import get_weather
from display_handler import display_weather
import time

def main():
    city = input("Enter city name: ")

    while True:
        weather_data = get_weather(city)
        display_weather(weather_data)

        # Update every 5 minutes
        time.sleep(300)

if __name__ == "__main__":
    main()
