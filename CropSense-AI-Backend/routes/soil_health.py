from fastapi import APIRouter
from models.soil_models import SoilHealthInput, SoilHealthResponse

router = APIRouter()


@router.post("/analyze", response_model=SoilHealthResponse, summary="Analyze soil health from sensor data")
def analyze_soil(data: SoilHealthInput):
    """
    Analyze soil health based on NPK values, pH, moisture, and temperature.

    Returns a health score, condition category, and actionable recommendations.
    """
    # TODO: Implement ML/rule-based soil health analysis.
    # Derive a composite health score and surface recommendations.

    return SoilHealthResponse(
        health_score=72.5,
        condition="Moderate",
        recommendations=[
            "Increase organic matter by adding compost.",
            "Adjust pH with lime; current value is slightly acidic.",
            "Potassium levels are adequate – no immediate action needed.",
        ],
        message="Placeholder response – analysis model not yet loaded.",
    )


@router.get("/guidelines", summary="Get soil health guidelines")
def get_guidelines():
    """Return general soil health guidelines and ideal value ranges."""
    return {
        "ph": {"ideal_min": 6.0, "ideal_max": 7.5, "unit": "pH"},
        "nitrogen": {"ideal_min": 30, "ideal_max": 60, "unit": "kg/ha"},
        "phosphorus": {"ideal_min": 25, "ideal_max": 50, "unit": "kg/ha"},
        "potassium": {"ideal_min": 20, "ideal_max": 45, "unit": "kg/ha"},
        "moisture": {"ideal_min": 30, "ideal_max": 60, "unit": "%"},
    }
