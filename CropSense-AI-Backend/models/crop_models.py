from pydantic import BaseModel, Field


class CropPredictionInput(BaseModel):
    N: float = Field(..., ge=0, description="Nitrogen content in soil (kg/ha)")
    P: float = Field(..., ge=0, description="Phosphorus content in soil (kg/ha)")
    K: float = Field(..., ge=0, description="Potassium content in soil (kg/ha)")
    temperature: float = Field(..., description="Temperature in Celsius")
    humidity: float = Field(..., ge=0, le=100, description="Relative humidity (%)")
    ph: float = Field(..., ge=0, le=14, description="Soil pH value")
    rainfall: float = Field(..., ge=0, description="Annual rainfall (mm)")

    model_config = {
        "json_schema_extra": {
            "example": {
                "N": 90,
                "P": 42,
                "K": 43,
                "temperature": 20.8,
                "humidity": 82.0,
                "ph": 6.5,
                "rainfall": 202.9,
            }
        }
    }


class CropPredictionResponse(BaseModel):
    recommended_crop: str
    confidence: float = Field(..., ge=0, le=1, description="Model confidence (0–1)")
    message: str = ""
