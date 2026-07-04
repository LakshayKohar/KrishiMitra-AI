from src.preprocessing.cloud_mask import mask_clouds
from src.feature_engineering.vegetation_indices import calculate_ndvi
from src.feature_engineering.ndvi_statistics import calculate_ndvi_statistics
from src.irrigation_engine.crop_health import interpret_ndvi
from src.irrigation_engine.irrigation_advisor import generate_irrigation_advice
from src.weather.weather_service import get_weather
from src.utils.geocoder import get_coordinates
from src.utils.report_generator import save_analysis_report
from src.data_acquisition.sentinel import (
    initialize,
    get_sentinel_image,
    get_image_metadata,
)


def analyze_location(location, start_date, end_date):
    initialize()

    latitude, longitude = get_coordinates(location)

    image = get_sentinel_image(
        longitude=longitude,
        latitude=latitude,
        start_date=start_date,
        end_date=end_date,
    )

    masked_image = mask_clouds(image)
    ndvi_image = calculate_ndvi(masked_image)

    stats = calculate_ndvi_statistics(
        ndvi_image=ndvi_image,
        longitude=longitude,
        latitude=latitude,
        buffer_meters=1000,
    )

    metadata = get_image_metadata(image)

    crop_report = interpret_ndvi(stats["NDVI_mean"])

    weather = get_weather(latitude, longitude)

    irrigation_advice = generate_irrigation_advice(
        mean_ndvi=stats["NDVI_mean"],
        rainfall=weather["rainfall"],
        temperature=weather["temperature"],
    )

    report = {
        "location": location,
        "latitude": latitude,
        "longitude": longitude,
        "cloud_cover": metadata["cloud_cover"],
        "image_id": metadata["image_id"],
        "acquisition_date": metadata["acquisition_date"],
        "ndvi": {
            "minimum": stats["NDVI_min"],
            "maximum": stats["NDVI_max"],
            "average": stats["NDVI_mean"],
        },
        "weather": weather,
        "crop_health": crop_report["status"],
        "recommendation": crop_report["recommendation"],
        "irrigation_advice": irrigation_advice,
    }

    save_analysis_report(
        location=location,
        latitude=latitude,
        longitude=longitude,
        cloud_cover=metadata["cloud_cover"],
        ndvi_stats=stats,
        crop_health=crop_report["status"],
        recommendation=crop_report["recommendation"],
    )

    return report, ndvi_image, masked_image