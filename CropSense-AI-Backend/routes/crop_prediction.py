from fastapi import APIRouter
from models.crop_models import CropPredictionInput, CropPredictionResponse

router = APIRouter()


@router.post("/predict", response_model=CropPredictionResponse, summary="Predict the best crop for given conditions")
def predict_crop(data: CropPredictionInput):
    """
    Predict the most suitable crop based on soil and environmental parameters.

    - **N**: Nitrogen content in soil (kg/ha)
    - **P**: Phosphorus content in soil (kg/ha)
    - **K**: Potassium content in soil (kg/ha)
    - **temperature**: Temperature in Celsius
    - **humidity**: Relative humidity (%)
    - **ph**: Soil pH value
    - **rainfall**: Annual rainfall (mm)
    """
    # TODO: Load and run ML model (joblib) here.
    # Example:
    #   model = joblib.load("models/crop_model.pkl")
    #   features = [[data.N, data.P, data.K, data.temperature, data.humidity, data.ph, data.rainfall]]
    #   prediction = model.predict(features)[0]

    return CropPredictionResponse(
        recommended_crop="wheat",
        confidence=0.91,
        message="Placeholder response – model not yet loaded.",
    )


@router.get("/list", summary="List all supported crops")
def list_crops():
    """Return the list of crops supported by the prediction model."""
    crops = [
        "rice", "maize", "chickpea", "kidneybeans", "pigeonpeas",
        "mothbeans", "mungbean", "blackgram", "lentil", "pomegranate",
        "banana", "mango", "grapes", "watermelon", "muskmelon",
        "apple", "orange", "papaya", "coconut", "cotton",
        "jute", "coffee", "wheat",
    ]
    return {"crops": crops, "total": len(crops)}
