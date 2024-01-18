# main.py

from api_handler import get_weather

latitude = 52.52
longitude = 13.41

weather_data = get_weather(latitude, longitude)

if weather_data:
    # Process and display the weather data as needed
    print("Current Weather:")
    print(f"Time: {weather_data['current']['time']}")
    print(f"Temperature at 2m: {weather_data['current']['temperature_2m']}°C")
    print(f"Wind Speed at 10m: {weather_data['current']['wind_speed_10m']} m/s")

    print("\nHourly Weather:")
    times = weather_data['hourly']['time']
    temperatures = weather_data['hourly']['temperature_2m']
    relative_humidity = weather_data['hourly']['relative_humidity_2m']
    wind_speeds = weather_data['hourly']['wind_speed_10m']

    for i in range(len(times)):
        print(f"Time: {times[i]}")
        print(f"Temperature at 2m: {temperatures[i]}°C")
        print(f"Relative Humidity at 2m: {relative_humidity[i]}%")
        print(f"Wind Speed at 10m: {wind_speeds[i]} m/s")
        print("\n---")
else:
    print("Unable to fetch weather data.")
