from fastapi import APIRouter, Query
from models.weather_models import WeatherResponse, ForecastResponse

router = APIRouter()


@router.get("/current", response_model=WeatherResponse, summary="Get current weather for a location")
def get_current_weather(
    lat: float = Query(..., description="Latitude of the location"),
    lon: float = Query(..., description="Longitude of the location"),
):
    """
    Fetch current weather data for the given coordinates.

    Integrates with an external weather API (e.g. OpenWeatherMap).
    Set your API key in the environment variable `WEATHER_API_KEY`.
    """
    # TODO: Replace with real API call.
    # import os, requests
    # api_key = os.getenv("WEATHER_API_KEY")
    # url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    # resp = requests.get(url).json()

    return WeatherResponse(
        location=f"{lat},{lon}",
        temperature=24.5,
        humidity=62.0,
        wind_speed=3.2,
        description="Partly cloudy",
        message="Placeholder response – weather API not yet configured.",
    )


@router.get("/forecast", response_model=ForecastResponse, summary="Get 7-day weather forecast")
def get_forecast(
    lat: float = Query(..., description="Latitude of the location"),
    lon: float = Query(..., description="Longitude of the location"),
):
    """
    Fetch a 7-day weather forecast for agricultural planning.
    """
    # TODO: Implement forecast API call.
    return ForecastResponse(
        location=f"{lat},{lon}",
        forecast=[],
        message="Placeholder response – forecast API not yet configured.",
    )
