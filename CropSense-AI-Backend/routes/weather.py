from fastapi import APIRouter, Query
from models.weather_models import WeatherResponse
import requests

router = APIRouter()


@router.get("/current", response_model=WeatherResponse)
def get_current_weather(
    lat: float = Query(...),
    lon: float = Query(...)
):
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        f"&current=temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return WeatherResponse(
            location=f"{lat},{lon}",
            temperature=0,
            humidity=0,
            wind_speed=0,
            description="Unable to fetch weather.",
            message="Weather API error."
        )

    data = response.json()["current"]

    weather_codes = {
        0: "Clear Sky",
        1: "Mainly Clear",
        2: "Partly Cloudy",
        3: "Cloudy",
        45: "Fog",
        48: "Fog",
        51: "Light Drizzle",
        61: "Rain",
        63: "Moderate Rain",
        65: "Heavy Rain",
        71: "Snow",
        80: "Rain Showers",
        95: "Thunderstorm",
    }

    return WeatherResponse(
        location=f"{lat},{lon}",
        temperature=data["temperature_2m"],
        humidity=data["relative_humidity_2m"],
        wind_speed=data["wind_speed_10m"],
        description=weather_codes.get(data["weather_code"], "Unknown"),
        message="Live weather fetched successfully."
    )