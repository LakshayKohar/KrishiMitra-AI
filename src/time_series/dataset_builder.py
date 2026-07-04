import os
import ee
import pandas as pd

from src.utils.geocoder import get_coordinates
from src.time_series.image_collection import initialize, get_sentinel_collection
from src.time_series.feature_extractor import extract_features_from_image
from src.time_series.weather_history import get_weather_history


def build_time_series_dataset(location, start_date, end_date, max_cloud=40):
    initialize()

    latitude, longitude = get_coordinates(location)

    collection = get_sentinel_collection(
        longitude=longitude,
        latitude=latitude,
        start_date=start_date,
        end_date=end_date,
        max_cloud=max_cloud,
    )

    count = collection.size().getInfo()

    if count == 0:
        raise ValueError("No Sentinel-2 images found for this date range/location.")

    weather_data = get_weather_history(
        latitude=latitude,
        longitude=longitude,
        start_date=start_date,
        end_date=end_date,
    )

    image_list = collection.toList(count)

    rows = []

    for i in range(count):
        image = ee.Image(image_list.get(i))

        try:
            features = extract_features_from_image(
                image=image,
                longitude=longitude,
                latitude=latitude,
                buffer_meters=1000,
            )

            weather = weather_data.get(features["date"], {})

            rows.append({
                "location": location,
                "latitude": latitude,
                "longitude": longitude,
                "date": features["date"],
                "ndvi": features["ndvi"],
                "ndwi": features["ndwi"],
                "msi": features["msi"],
                "cloud_cover": features["cloud_cover"],
                "temperature": weather.get("temperature"),
                "rainfall": weather.get("rainfall"),
                "humidity": weather.get("humidity"),
                "wind_speed": weather.get("wind_speed"),
            })

        except Exception as error:
            print(f"Skipping image {i + 1}/{count}: {error}")

    if not rows:
        raise ValueError(
            "No valid time-series rows could be generated. Try a wider date range or lower cloud filtering."
        )

    df = pd.DataFrame(rows)

    df = df.sort_values("date").drop_duplicates(subset=["date"])

    os.makedirs("data/datasets", exist_ok=True)

    safe_name = (
        location.replace(" ", "_")
        .replace(",", "")
        .replace("/", "_")
        .replace("\\", "_")
    )

    output_path = f"data/datasets/{safe_name}_time_series.csv"

    df.to_csv(output_path, index=False)

    return df, output_path