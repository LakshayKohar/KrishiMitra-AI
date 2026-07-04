import os
import joblib
import pandas as pd


FEATURE_COLUMNS = [
    "ndvi",
    "ndwi",
    "msi",
    "temperature",
    "rainfall",
    "humidity",
    "wind_speed",
]


def predict_crop_from_features(features, model_path="models/crop_classifier.pkl"):
    if not os.path.exists(model_path):
        return {
            "crop": "ML model not trained",
            "confidence": "N/A",
            "reason": "Train a crop classification model using real labeled crop data."
        }

    model = joblib.load(model_path)

    df = pd.DataFrame([features], columns=FEATURE_COLUMNS)

    prediction = model.predict(df)[0]

    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(df)[0]
        confidence = max(probabilities)
    else:
        confidence = None

    return {
        "crop": prediction,
        "confidence": f"{confidence:.2f}" if confidence is not None else "N/A",
        "reason": "Prediction generated using trained Random Forest crop classifier."
    }