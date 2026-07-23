from fastapi import APIRouter
from models.crop_models import CropPredictionInput, CropPredictionResponse
import joblib

router = APIRouter()
model = joblib.load("ml_models/crop_model.pkl")


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

    features = [[
        data.N,
        data.P,
        data.K,
        data.temperature,
        data.humidity,
        data.ph,
        data.rainfall
    ]]

    prediction = model.predict(features)[0]
    probabilities = model.predict_proba(features)[0]
    confidence = float(max(probabilities))

    return CropPredictionResponse(
        recommended_crop=prediction,
        confidence=confidence,
        message="Prediction successful."
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
