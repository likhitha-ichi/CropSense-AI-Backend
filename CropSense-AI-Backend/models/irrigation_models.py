from pydantic import BaseModel, Field


class IrrigationInput(BaseModel):
    crop: str = Field(..., description="Crop type (e.g. wheat, rice)")
    moisture: float = Field(..., ge=0, le=100, description="Current soil moisture (%)")
    temperature: float = Field(..., description="Current air temperature (°C)")
    humidity: float = Field(..., ge=0, le=100, description="Relative humidity (%)")
    rainfall : float = Field(0.0, ge=0, description="Rainfall   (mm)")
     

    model_config = {
        "json_schema_extra": {
            "example": {
                "crop": "wheat",
                "moisture": 28.0,
                "temperature": 26.5,
                "humidity": 55.0,
                 "rainfall": 5.0
            }
        }
    }


class IrrigationResponse(BaseModel):
    irrigation_needed: bool
    water_amount_mm: float  
    schedule: str
    reason: str
    message: str = ""
