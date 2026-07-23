"""
Centralised ML model loader using joblib.

Usage:
    from utils.model_loader import load_model
    crop_model = load_model("models/crop_model.pkl")
    prediction = crop_model.predict([[90, 42, 43, 20.8, 82.0, 6.5, 202.9]])
"""

import os
import joblib


_MODEL_CACHE: dict = {}


def load_model(path: str):
    """
    Load a joblib-serialised model from disk.

    Models are cached in memory after the first load so repeated requests
    do not incur disk I/O.

    Args:
        path: Path to the .pkl / .joblib file, relative to the project root.

    Returns:
        The loaded scikit-learn (or compatible) estimator.

    Raises:
        FileNotFoundError: If the model file does not exist at the given path.
    """
    if path in _MODEL_CACHE:
        return _MODEL_CACHE[path]

    abs_path = os.path.abspath(path)
    if not os.path.exists(abs_path):
        raise FileNotFoundError(
            f"Model file not found at '{abs_path}'. "
            "Train and export your model first, then place it at that path."
        )

    model = joblib.load(abs_path)
    _MODEL_CACHE[path] = model
    return model


def clear_cache():
    """Clear the in-memory model cache (useful for testing)."""
    _MODEL_CACHE.clear()
