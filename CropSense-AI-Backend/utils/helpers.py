"""
General utility helpers for CropSense AI Backend.
"""

import numpy as np


def normalize(value: float, min_val: float, max_val: float) -> float:
    """Normalize a value to the [0, 1] range."""
    if max_val == min_val:
        return 0.0
    return (value - min_val) / (max_val - min_val)


def compute_soil_health_score(N: float, P: float, K: float, ph: float, moisture: float) -> float:
    """
    Compute a simple composite soil health score (0–100).

    Weights can be tuned once the agronomic model is validated.
    """
    ideal = {"N": 45, "P": 37, "K": 32, "ph": 6.5, "moisture": 45}
    ranges = {"N": (0, 140), "P": (0, 145), "K": (0, 205), "ph": (0, 14), "moisture": (0, 100)}

    def score_param(val, ideal_val, lo, hi):
        deviation = abs(val - ideal_val) / (hi - lo)
        return max(0.0, 1.0 - deviation * 2)

    weights = {"N": 0.25, "P": 0.20, "K": 0.20, "ph": 0.20, "moisture": 0.15}
    params = {"N": N, "P": P, "K": K, "ph": ph, "moisture": moisture}

    total = sum(
        weights[k] * score_param(params[k], ideal[k], *ranges[k])
        for k in weights
    )
    return round(total * 100, 2)


def classify_health_score(score: float) -> str:
    """Map a numeric health score to a human-readable condition label."""
    if score >= 80:
        return "Excellent"
    elif score >= 65:
        return "Good"
    elif score >= 45:
        return "Moderate"
    elif score >= 25:
        return "Poor"
    else:
        return "Critical"


def build_error_response(detail: str, code: int = 400) -> dict:
    """Standardised error response payload."""
    return {"error": True, "code": code, "detail": detail}
