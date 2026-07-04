from src.preprocessing.cloud_mask import mask_clouds
from src.feature_engineering.vegetation_indices import (
    calculate_ndvi,
    calculate_ndwi,
    calculate_msi,
)
from src.feature_engineering.index_statistics import calculate_index_statistics
from src.irrigation_engine.crop_health import interpret_ndvi
from src.irrigation_engine.irrigation_advisor import generate_irrigation_advice
from src.irrigation_engine.water_stress_advisor import generate_water_stress_advice
from src.moisture_stress.moisture_analyzer import classify_moisture_status
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
    ndwi_image = calculate_ndwi(masked_image)
    msi_image = calculate_msi(masked_image)

    ndvi_stats = calculate_index_statistics(
        ndvi_image,
        "NDVI",
        longitude,
        latitude,
        buffer_meters=1000,
    )

    ndwi_stats = calculate_index_statistics(
        ndwi_image,
        "NDWI",
        longitude,
        latitude,
        buffer_meters=1000,
    )

    msi_stats = calculate_index_statistics(
        msi_image,
        "MSI",
        longitude,
        latitude,
        buffer_meters=1000,
    )

    metadata = get_image_metadata(image)

    crop_report = interpret_ndvi(ndvi_stats["NDVI_mean"])

    weather = get_weather(latitude, longitude)

    irrigation_advice = generate_irrigation_advice(
        mean_ndvi=ndvi_stats["NDVI_mean"],
        rainfall=weather["rainfall"],
        temperature=weather["temperature"],
    )

    moisture_status = classify_moisture_status(
        ndwi_mean=ndwi_stats["NDWI_mean"],
        msi_mean=msi_stats["MSI_mean"],
    )

    water_stress_advice = generate_water_stress_advice(
        moisture_status=moisture_status,
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
            "minimum": ndvi_stats["NDVI_min"],
            "maximum": ndvi_stats["NDVI_max"],
            "average": ndvi_stats["NDVI_mean"],
        },
        "ndwi": {
            "minimum": ndwi_stats["NDWI_min"],
            "maximum": ndwi_stats["NDWI_max"],
            "average": ndwi_stats["NDWI_mean"],
        },
        "msi": {
            "minimum": msi_stats["MSI_min"],
            "maximum": msi_stats["MSI_max"],
            "average": msi_stats["MSI_mean"],
        },
        "weather": weather,
        "crop_health": crop_report["status"],
        "recommendation": crop_report["recommendation"],
        "irrigation_advice": irrigation_advice,
        "moisture_status": moisture_status,
        "water_stress_advice": water_stress_advice,
    }

    save_analysis_report(
        location=location,
        latitude=latitude,
        longitude=longitude,
        cloud_cover=metadata["cloud_cover"],
        ndvi_stats=ndvi_stats,
        crop_health=crop_report["status"],
        recommendation=crop_report["recommendation"],
    )

    return report, ndvi_image, masked_image