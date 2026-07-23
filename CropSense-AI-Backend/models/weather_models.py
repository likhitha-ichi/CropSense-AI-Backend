from typing import List
from pydantic import BaseModel


class WeatherResponse(BaseModel):
    location: str
    temperature: float
    humidity: float
    wind_speed: float
    description: str
    message: str = ""


class DailyForecast(BaseModel):
    date: str
    temperature_min: float
    temperature_max: float
    humidity: float
    description: str
    rainfall_mm: float = 0.0


class ForecastResponse(BaseModel):
    location: str
    forecast: List[DailyForecast]
    message: str = ""
