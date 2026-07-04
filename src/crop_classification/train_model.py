import os
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

from src.crop_classification.dataset_validator import validate_crop_dataset


FEATURE_COLUMNS = [
    "ndvi",
    "ndwi",
    "msi",
    "temperature",
    "rainfall",
    "humidity",
    "wind_speed",
]


def train_crop_classifier(dataset_path):
    df = pd.read_csv(dataset_path)

    validate_crop_dataset(df)

    X = df[FEATURE_COLUMNS]
    y = df["crop_label"]

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
    )

    model.fit(X, y)

    predictions = model.predict(X)

    accuracy = accuracy_score(y, predictions)

    print(f"Training Accuracy: {accuracy:.3f}")
    print(classification_report(y, predictions))

    os.makedirs("models", exist_ok=True)

    model_path = "models/crop_classifier.pkl"

    joblib.dump(model, model_path)

    print(f"Model saved to {model_path}")

    return model_path