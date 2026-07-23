from pydantic import BaseModel, Field


class IrrigationInput(BaseModel):
    crop: str = Field(..., description="Crop type (e.g. wheat, rice)")
    growth_stage: str = Field(..., description="Growth stage (e.g. seedling, vegetative, flowering, maturity)")
    soil_moisture: float = Field(..., ge=0, le=100, description="Current soil moisture (%)")
    temperature: float = Field(..., description="Current air temperature (°C)")
    humidity: float = Field(..., ge=0, le=100, description="Relative humidity (%)")
    rainfall_last_7_days_mm: float = Field(0.0, ge=0, description="Rainfall in the past 7 days (mm)")
    rainfall_forecast_48h_mm: float = Field(0.0, ge=0, description="Forecasted rainfall in next 48 hours (mm)")

    model_config = {
        "json_schema_extra": {
            "example": {
                "crop": "wheat",
                "growth_stage": "vegetative",
                "soil_moisture": 28.0,
                "temperature": 26.5,
                "humidity": 55.0,
                "rainfall_last_7_days_mm": 5.0,
                "rainfall_forecast_48h_mm": 0.0,
            }
        }
    }


class IrrigationResponse(BaseModel):
    irrigation_needed: bool
    water_amount_mm: float = Field(..., ge=0, description="Recommended water to apply (mm)")
    schedule: str
    reason: str
    message: str = ""
