from fastapi import APIRouter, UploadFile, File, HTTPException
from models.pest_models import PestDetectionResponse
import tensorflow as tf
import numpy as np
import json
from PIL import Image
from io import BytesIO

router = APIRouter()

model = tf.keras.models.load_model("models/plant_disease_model.keras")

with open("models/class_names.json") as f:
    class_indices = json.load(f)

classes = list(class_indices.keys())


@router.post("/detect", response_model=PestDetectionResponse, summary="Detect pests from a crop image")
async def detect_pest(file: UploadFile = File(..., description="Crop leaf or plant image (JPEG/PNG)")):
    """
    Upload a crop image to detect pests or diseases.

    Accepted formats: JPEG, PNG.
    Returns the detected pest/disease name, confidence score, and treatment advice.
    """
    allowed_types = {"image/jpeg", "image/png", "image/jpg"}
    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type '{file.content_type}'. Please upload a JPEG or PNG image.",
        )

    contents = await file.read()

    file_size_kb = len(contents) / 1024

    try:
        image = Image.open(BytesIO(contents)).convert("RGB")
        image = image.resize((224, 224))
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Invalid image file."
        )

    img = np.array(image) / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img, verbose=0)

    index = np.argmax(prediction)

    confidence = float(prediction[0][index])

    disease = classes[index]

    # Determine severity
    if "healthy" in disease.lower():
        severity = "Low"
    else:
        if confidence > 0.90:
            severity = "High"
        else:
            severity = "Moderate"

    # Treatment suggestions
    if "healthy" in disease.lower():
        treatment = [
            "Plant appears healthy.",
            "Continue regular irrigation.",
            "Monitor the crop regularly."
        ]
    else:
        treatment = [
            "Remove infected leaves.",
            "Apply recommended fungicide or pesticide.",
            "Avoid spreading the infection.",
            "Consult your local agricultural officer."
        ]

    return PestDetectionResponse(
        detected_pest=disease,
        confidence=confidence,
        severity=severity,
        treatment=treatment,
        file_name=file.filename,
        file_size_kb=round(file_size_kb, 2),
        message="Prediction generated using trained AI model."
    )