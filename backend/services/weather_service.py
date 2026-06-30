import requests
from utils.config import OPENWEATHER_API_KEY


def get_weather(city: str):

    # Step 1: Get latitude & longitude
    geo_url = (
        f"https://geocoding-api.open-meteo.com/v1/search"
        f"?name={city}&count=1"
    )

    geo_response = requests.get(geo_url).json()

    if "results" not in geo_response:
        return {
            "error": "City not found."
        }

    location = geo_response["results"][0]

    latitude = location["latitude"]
    longitude = location["longitude"]

    # Step 2: Fetch weather
    weather_url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        f"&current=temperature_2m,relative_humidity_2m,"
        f"wind_speed_10m,rain"
    )

    weather = requests.get(weather_url).json()

    current = weather["current"]

    return {
        "city": location["name"],
        "temperature": current["temperature_2m"],
        "humidity": current["relative_humidity_2m"],
        "wind_speed": current["wind_speed_10m"],
        "rainfall": current["rain"]
    }