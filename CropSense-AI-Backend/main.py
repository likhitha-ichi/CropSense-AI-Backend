from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import (
    crop_prediction,
    weather,
    soil_health,
    smart_irrigation,
    pest_detection,
    voice_assistant,
)

app = FastAPI(
    title="CropSense AI Backend",
    description="AI-powered agriculture platform API for crop prediction, weather, soil health, irrigation, pest detection, and voice assistant.",
    version="1.0.0",
)

# ---------------------------------------------------------------------------
# CORS – allow any local React dev server and any deployed origin you add here
# ---------------------------------------------------------------------------
origins = [
    "http://localhost:3000",
    "http://localhost:5173",
    "http://localhost:5174",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5173",

    # Replit frontend
    "https://e853cbe2-84cf-48b9-8768-f92309e13eec-00-2g8ehzxt2ycdm.sisko.replit.dev",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------------------------------
# Routers
# ---------------------------------------------------------------------------
app.include_router(crop_prediction.router, prefix="/api/crop", tags=["Crop Prediction"])
app.include_router(weather.router, prefix="/api/weather", tags=["Weather"])
app.include_router(soil_health.router, prefix="/api/soil", tags=["Soil Health"])
app.include_router(smart_irrigation.router, prefix="/api/irrigation", tags=["Smart Irrigation"])
app.include_router(pest_detection.router, prefix="/api/pest", tags=["Pest Detection"])
app.include_router(voice_assistant.router, prefix="/api/voice", tags=["Voice Assistant"])


# ---------------------------------------------------------------------------
# Root health-check
# ---------------------------------------------------------------------------
@app.get("/", tags=["Health"])
def root():
    return {"status": "ok", "message": "CropSense AI Backend is running."}


@app.get("/api/health", tags=["Health"])
def health():
    return {"status": "healthy"}
