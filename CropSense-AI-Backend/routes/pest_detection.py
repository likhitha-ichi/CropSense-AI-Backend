from fastapi import APIRouter, UploadFile, File, HTTPException
from models.pest_models import PestDetectionResponse

router = APIRouter()


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

    # TODO: Run image through a trained CNN / transfer-learning model.
    # Example with a joblib-saved sklearn pipeline or a TensorFlow/PyTorch model:
    #   from utils.image_utils import preprocess_image
    #   img_array = preprocess_image(contents)
    #   prediction = pest_model.predict(img_array)

    return PestDetectionResponse(
        detected_pest="Aphids",
        confidence=0.87,
        severity="Moderate",
        treatment=[
            "Apply neem oil spray (5 ml per litre of water).",
            "Introduce natural predators such as ladybugs.",
            "Remove heavily infested leaves and dispose of them away from the field.",
        ],
        file_name=file.filename,
        file_size_kb=round(file_size_kb, 2),
        message="Placeholder response – pest detection model not yet loaded.",
    )


@router.get("/pests", summary="List detectable pests and diseases")
def list_pests():
    """Return all pests and diseases the model can currently detect."""
    return {
        "pests": [
            "Aphids", "Armyworm", "Bacterial Blight", "Brown Spot",
            "Colorado Potato Beetle", "Early Blight", "Gray Leaf Spot",
            "Late Blight", "Leaf Miner", "Powdery Mildew",
            "Rice Blast", "Stem Borer", "Whitefly", "Yellow Mosaic Virus",
        ]
    }
