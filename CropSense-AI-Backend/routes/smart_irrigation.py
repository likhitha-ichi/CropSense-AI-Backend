from fastapi import APIRouter
from models.irrigation_models import IrrigationInput, IrrigationResponse

router = APIRouter()


@router.post("/recommend", response_model=IrrigationResponse, summary="Get smart irrigation recommendations")
def recommend_irrigation(data: IrrigationInput):

    irrigation_needed = False
    water_amount = 0
    reasons = []

    # Soil moisture
    if data.moisture < 30:
        irrigation_needed = True
        water_amount += 20
        reasons.append("Soil moisture is low.")

    # Temperature
    if data.temperature > 35:
        irrigation_needed = True
        water_amount += 10
        reasons.append("High temperature increases water loss.")

    # Humidity
    if data.humidity < 40:
        irrigation_needed = True
        water_amount += 5
        reasons.append("Low humidity dries the soil faster.")

    # Rainfall
    if data.rainfall > 20:
        irrigation_needed = False
        water_amount = 0
        reasons = ["Rainfall is sufficient. Irrigation is not required."]

    schedule = (
        "Irrigate early morning (6:00–8:00 AM)."
        if irrigation_needed
        else "No irrigation needed today."
    )

    if not reasons:
        reasons.append("Current soil conditions are healthy.")

    return IrrigationResponse(
        irrigation_needed=irrigation_needed,
        water_amount_mm=water_amount,
        schedule=schedule,
        reason=" ".join(reasons),
        message="Irrigation analysis completed successfully."
    )


@router.get("/crops", summary="List crops with irrigation profiles")
def list_irrigated_crops():
    return {
        "crops": [
            {"name": "Wheat", "water_requirement_mm_per_season": "450-650"},
            {"name": "Rice", "water_requirement_mm_per_season": "1000-2000"},
            {"name": "Maize", "water_requirement_mm_per_season": "500-800"},
            {"name": "Cotton", "water_requirement_mm_per_season": "700-1300"},
            {"name": "Sugarcane", "water_requirement_mm_per_season": "1500-2500"},
        ]
    }