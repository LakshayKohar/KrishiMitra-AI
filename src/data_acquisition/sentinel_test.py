from src.preprocessing.cloud_mask import mask_clouds
from src.feature_engineering.vegetation_indices import calculate_ndvi
from src.feature_engineering.ndvi_statistics import calculate_ndvi_statistics
from src.utils.geocoder import get_coordinates
from src.irrigation_engine.crop_health import interpret_ndvi
from src.utils.report_generator import save_analysis_report
from src.data_acquisition.sentinel import (
    initialize,
    get_sentinel_image,
    get_image_metadata,
    get_image_geometry,
)


def main():
    # Initialize Earth Engine
    initialize()

    # Get coordinates from place name
    latitude, longitude = get_coordinates("NIT Kurukshetra, Haryana")

    # Retrieve Sentinel-2 image
    image = get_sentinel_image(
        longitude=longitude,
        latitude=latitude,
        start_date="2024-01-01",
        end_date="2024-01-31",
    )

    # Apply cloud mask
    masked_image = mask_clouds(image)

    # Calculate NDVI
    ndvi_image = calculate_ndvi(masked_image)

    # Get image geometry
    geometry = get_image_geometry(masked_image)

    # Calculate NDVI statistics
    stats = calculate_ndvi_statistics(
        ndvi_image,
        geometry
    )

    # Get metadata
    metadata = get_image_metadata(image)

    # Print metadata
    print("=" * 50)
    print("Sentinel-2 Image Retrieved Successfully")
    print("=" * 50)
    print(f"Location: NIT Kurukshetra, Haryana")
    print(f"Latitude: {latitude:.6f}")
    print(f"Longitude: {longitude:.6f}")
    print(f"Image ID: {metadata['image_id']}")
    print(f"Acquisition Date: {metadata['acquisition_date']}")
    print(f"Cloud Cover: {metadata['cloud_cover']} %")

    # Status messages
    print("\n✅ Cloud masking applied successfully.")
    print("✅ NDVI calculated successfully.")

    # NDVI Statistics
    print("\nNDVI Statistics")
    print("-" * 30)
    print(f"Minimum NDVI : {stats['NDVI_min']:.3f}")
    print(f"Maximum NDVI : {stats['NDVI_max']:.3f}")
    print(f"Average NDVI : {stats['NDVI_mean']:.3f}")

    # Crop Health Report
    report = interpret_ndvi(stats["NDVI_mean"])

    print("\nCrop Health Report")
    print("-" * 30)
    print(f"Health Status : {report['status']}")
    print(f"Recommendation: {report['recommendation']}")

    # Save analysis report
    save_analysis_report(
        location="NIT Kurukshetra, Haryana",
        latitude=latitude,
        longitude=longitude,
        cloud_cover=metadata["cloud_cover"],
        ndvi_stats=stats,
        crop_health=report["status"],
        recommendation=report["recommendation"],
    )


if __name__ == "__main__":
    main()