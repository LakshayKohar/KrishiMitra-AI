import ee
from src.preprocessing.cloud_mask import mask_clouds
from src.feature_engineering.vegetation_indices import (
    calculate_ndvi,
    calculate_ndwi,
    calculate_msi,
)
from src.feature_engineering.index_statistics import calculate_index_statistics


def extract_features_from_image(image, longitude, latitude, buffer_meters=1000):
    masked_image = mask_clouds(image)

    ndvi = calculate_ndvi(masked_image)
    ndwi = calculate_ndwi(masked_image)
    msi = calculate_msi(masked_image)

    ndvi_stats = calculate_index_statistics(
        ndvi, "NDVI", longitude, latitude, buffer_meters
    )

    ndwi_stats = calculate_index_statistics(
        ndwi, "NDWI", longitude, latitude, buffer_meters
    )

    msi_stats = calculate_index_statistics(
        msi, "MSI", longitude, latitude, buffer_meters
    )

    date = ee.Date(image.get("system:time_start")).format("YYYY-MM-dd").getInfo()

    cloud_cover = image.get("CLOUDY_PIXEL_PERCENTAGE").getInfo()

    return {
        "date": date,
        "ndvi": ndvi_stats["NDVI_mean"],
        "ndwi": ndwi_stats["NDWI_mean"],
        "msi": msi_stats["MSI_mean"],
        "cloud_cover": cloud_cover,
    }