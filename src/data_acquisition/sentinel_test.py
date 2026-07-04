from src.preprocessing.cloud_mask import mask_clouds
from src.data_acquisition.sentinel import (
    initialize,
    get_sentinel_image,
    get_image_metadata,
)


def main():
    # Initialize Earth Engine
    initialize()

    # Retrieve Sentinel-2 image
    image = get_sentinel_image(
        longitude=76.8222,
        latitude=29.9695,
        start_date="2024-01-01",
        end_date="2024-01-31",
    )

    # Apply cloud mask
    masked_image = mask_clouds(image)

    # Get metadata
    metadata = get_image_metadata(image)

    print("=" * 50)
    print("Sentinel-2 Image Retrieved Successfully")
    print("=" * 50)
    print(f"Image ID: {metadata['image_id']}")
    print(f"Acquisition Date: {metadata['acquisition_date']}")
    print(f"Cloud Cover: {metadata['cloud_cover']} %")

    # Verify cloud masking
    if masked_image:
        print("\n✅ Cloud masking applied successfully.")


if __name__ == "__main__":
    main()