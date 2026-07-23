from typing import List
from pydantic import BaseModel, Field


class PestDetectionResponse(BaseModel):
    detected_pest: str
    confidence: float = Field(..., ge=0, le=1, description="Detection confidence (0–1)")
    severity: str = Field(..., description="One of: Low, Moderate, High, Critical")
    treatment: List[str]
    file_name: str
    file_size_kb: float
    message: str = ""
