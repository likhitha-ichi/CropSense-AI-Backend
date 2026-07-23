# CropSense-AI-Backend

AI-powered agriculture platform backend built with Python and FastAPI.

## Project Structure

```
CropSense-AI-Backend/
├── main.py                     # App entry point, CORS config, router registration
├── requirements.txt            # Python dependencies
├── routes/                     # One file per API domain
│   ├── crop_prediction.py      # POST /api/crop/predict
│   ├── weather.py              # GET  /api/weather/current & /forecast
│   ├── soil_health.py          # POST /api/soil/analyze
│   ├── smart_irrigation.py     # POST /api/irrigation/recommend
│   ├── pest_detection.py       # POST /api/pest/detect  (image upload)
│   └── voice_assistant.py      # POST /api/voice/query & /transcribe
├── models/                     # Pydantic request / response schemas
│   ├── crop_models.py
│   ├── weather_models.py
│   ├── soil_models.py
│   ├── irrigation_models.py
│   ├── pest_models.py
│   └── voice_models.py
└── utils/                      # Shared helpers
    ├── helpers.py              # Scoring, normalization, error builders
    └── model_loader.py         # Cached joblib model loader
```

## API Endpoints

| Module            | Method | Path                          | Description                          |
|-------------------|--------|-------------------------------|--------------------------------------|
| Health            | GET    | `/`                           | Root health check                    |
| Health            | GET    | `/api/health`                 | Health check                         |
| Crop Prediction   | POST   | `/api/crop/predict`           | Predict best crop from soil/env data |
| Crop Prediction   | GET    | `/api/crop/list`              | List supported crops                 |
| Weather           | GET    | `/api/weather/current`        | Current weather by coordinates       |
| Weather           | GET    | `/api/weather/forecast`       | 7-day forecast by coordinates        |
| Soil Health       | POST   | `/api/soil/analyze`           | Analyze soil health from NPK/pH data |
| Soil Health       | GET    | `/api/soil/guidelines`        | Ideal soil value ranges              |
| Smart Irrigation  | POST   | `/api/irrigation/recommend`   | Irrigation schedule recommendation   |
| Smart Irrigation  | GET    | `/api/irrigation/crops`       | Crop water requirement profiles      |
| Pest Detection    | POST   | `/api/pest/detect`            | Detect pest from uploaded image      |
| Pest Detection    | GET    | `/api/pest/pests`             | List detectable pests                |
| Voice Assistant   | POST   | `/api/voice/query`            | Answer a text agriculture query      |
| Voice Assistant   | POST   | `/api/voice/transcribe`       | Transcribe audio to text             |
| Voice Assistant   | GET    | `/api/voice/languages`        | List supported languages             |

## Getting Started

### 1. Install dependencies

```bash
cd CropSense-AI-Backend
pip install -r requirements.txt
```

### 2. Run the development server

```bash
uvicorn main:app --reload --port 8000
```

### 3. Open interactive API docs

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc:       [http://localhost:8000/redoc](http://localhost:8000/redoc)

## CORS

The server allows requests from the following React dev-server origins:

- `http://localhost:3000` (Create React App)
- `http://localhost:5173` (Vite)

To add your production frontend URL, edit the `origins` list in `main.py`.

## Adding ML Models

Place trained `.pkl` / `.joblib` files anywhere in the project and load them with the cached loader:

```python
from utils.model_loader import load_model

crop_model = load_model("models/crop_model.pkl")
prediction = crop_model.predict([[90, 42, 43, 20.8, 82.0, 6.5, 202.9]])
```

Each route file contains a `# TODO` comment showing exactly where to plug in the model call.
