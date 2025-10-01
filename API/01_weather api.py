import urllib.request

city = "Belagavi"
url = f"https://wttr.in/{city}?format=2"

with urllib.request.urlopen(url) as response:
    weather = response.read().decode("utf-8")
    print(weather)


import urllib.request
import json

city = "Bangalore"
url = f"https://wttr.in/{city}?format=j1"   # j1 = JSON format

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode("utf-8"))

# Extract weather info
current = data["current_condition"][0]
temp = current["temp_C"]
feels_like = current["FeelsLikeC"]
humidity = current["humidity"]
wind_speed = current["windspeedKmph"]
description = current["weatherDesc"][0]["value"]

print(f"Weather in {city}: {description}")
print(f"🌡 Temperature: {temp}°C (Feels like {feels_like}°C)")
print(f"💧 Humidity: {humidity}%")
print(f"🌬 Wind Speed: {wind_speed} km/h")
