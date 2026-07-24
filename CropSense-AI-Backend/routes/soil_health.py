from fastapi import APIRouter
from models.soil_models import SoilHealthInput, SoilHealthResponse

router = APIRouter()


@router.post("/analyze", response_model=SoilHealthResponse, summary="Analyze soil health from sensor data")
def analyze_soil(data: SoilHealthInput):

    score = 100
    recommendations = []

    # Nitrogen
    if data.N < 30:
        score -= 10
        recommendations.append("Nitrogen is low. Apply nitrogen-rich fertilizer.")
    elif data.N > 80:
        score -= 5
        recommendations.append("Nitrogen is high. Avoid adding more nitrogen fertilizer.")

    # Phosphorus
    if data.P < 25:
        score -= 10
        recommendations.append("Phosphorus is low. Add phosphate fertilizer.")
    elif data.P > 60:
        score -= 5
        recommendations.append("Phosphorus is high. Reduce phosphorus fertilizer.")

    # Potassium
    if data.K < 20:
        score -= 10
        recommendations.append("Potassium is low. Apply potash fertilizer.")
    elif data.K > 60:
        score -= 5
        recommendations.append("Potassium is high. Reduce potassium fertilizer.")

    # Soil pH
    if data.ph < 6.0:
        score -= 15
        recommendations.append("Soil is acidic. Apply agricultural lime.")
    elif data.ph > 7.5:
        score -= 15
        recommendations.append("Soil is alkaline. Add organic compost or gypsum.")

    # Moisture
    if data.moisture < 30:
        score -= 15
        recommendations.append("Soil moisture is low. Increase irrigation.")
    elif data.moisture > 60:
        score -= 15
        recommendations.append("Soil moisture is high. Improve drainage.")

    # Temperature
    if data.temperature < 20:
        score -= 10
        recommendations.append("Soil temperature is low. Use mulch to retain warmth.")
    elif data.temperature > 35:
        score -= 10
        recommendations.append("Soil temperature is high. Mulching is recommended.")

    score = max(0, min(score, 100))

    if score >= 90:
        condition = "Excellent"
    elif score >= 75:
        condition = "Good"
    elif score >= 50:
        condition = "Moderate"
    elif score >= 25:
        condition = "Poor"
    else:
        condition = "Critical"

    if not recommendations:
        recommendations.append("Your soil is in excellent condition. Keep following the current farming practices.")

    return SoilHealthResponse(
        health_score=score,
        condition=condition,
        recommendations=recommendations,
        message="Soil analysis completed successfully."
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
