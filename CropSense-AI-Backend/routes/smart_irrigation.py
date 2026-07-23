from fastapi import APIRouter
from models.irrigation_models import IrrigationInput, IrrigationResponse

router = APIRouter()


@router.post("/recommend", response_model=IrrigationResponse, summary="Get smart irrigation recommendations")
def recommend_irrigation(data: IrrigationInput):
    """
    Generate an irrigation schedule based on crop type, soil moisture,
    weather forecast, and growth stage.

    Returns whether irrigation is needed and the recommended water amount.
    """
    # TODO: Implement irrigation scheduling logic or ML model.
    # Consider ETc (crop evapotranspiration), soil water-holding capacity,
    # recent rainfall, and current soil moisture readings.

    return IrrigationResponse(
        irrigation_needed=True,
        water_amount_mm=25.0,
        schedule="Irrigate tomorrow morning (06:00–08:00).",
        reason="Soil moisture is below threshold; no rainfall expected in the next 48 hours.",
        message="Placeholder response – irrigation model not yet loaded.",
    )


@router.get("/crops", summary="List crops with irrigation profiles")
def list_irrigated_crops():
    """Return crops and their typical water requirement ranges."""
    return {
        "crops": [
            {"name": "Wheat", "water_requirement_mm_per_season": "450-650"},
            {"name": "Rice", "water_requirement_mm_per_season": "1000-2000"},
            {"name": "Maize", "water_requirement_mm_per_season": "500-800"},
            {"name": "Cotton", "water_requirement_mm_per_season": "700-1300"},
            {"name": "Sugarcane", "water_requirement_mm_per_season": "1500-2500"},
        ]
    }
