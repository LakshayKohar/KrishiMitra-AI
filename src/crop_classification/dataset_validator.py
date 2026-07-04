REQUIRED_COLUMNS = [
    "ndvi",
    "ndwi",
    "msi",
    "temperature",
    "rainfall",
    "humidity",
    "wind_speed",
    "crop_label",
]


def validate_crop_dataset(df):
    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]

    if missing:
        raise ValueError(
            f"Dataset is missing required columns: {missing}. "
            "Add real crop_label values before training."
        )

    if df["crop_label"].isnull().any():
        raise ValueError("crop_label column contains empty values.")

    return True