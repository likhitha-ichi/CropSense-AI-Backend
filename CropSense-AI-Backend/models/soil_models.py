from typing import List
from pydantic import BaseModel, Field


class SoilHealthInput(BaseModel):
    N: float = Field(..., ge=0, description="Nitrogen (kg/ha)")
    P: float = Field(..., ge=0, description="Phosphorus (kg/ha)")
    K: float = Field(..., ge=0, description="Potassium (kg/ha)")
    ph: float = Field(..., ge=0, le=14, description="Soil pH")
    moisture: float = Field(..., ge=0, le=100, description="Soil moisture (%)")
    temperature: float = Field(..., description="Soil temperature (°C)")

    model_config = {
        "json_schema_extra": {
            "example": {
                "N": 40,
                "P": 30,
                "K": 25,
                "ph": 6.2,
                "moisture": 45.0,
                "temperature": 22.5,
            }
        }
    }


class SoilHealthResponse(BaseModel):
    health_score: float = Field(..., ge=0, le=100, description="Composite health score (0–100)")
    condition: str = Field(..., description="One of: Excellent, Good, Moderate, Poor, Critical")
    recommendations: List[str]
    message: str = ""
