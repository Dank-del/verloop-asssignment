import os

import requests
from dotenv import load_dotenv

from app.models.response_models import WeatherResponse

load_dotenv()

url = "https://weatherapi-com.p.rapidapi.com/current.json"

headers = {
    "x-rapidapi-key": os.getenv(
        "WEATHER_API_KEY"
    ),
    "x-rapidapi-host": "weatherapi-com.p.rapidapi.com",
}


def get_weather_by_city(city: str):
    response = requests.get(url, headers=headers, params={"q": city}, timeout=10)

    if response.status_code != 200:
        return None

    return WeatherResponse(**response.json())
