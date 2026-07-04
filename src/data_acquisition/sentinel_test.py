import ee

PROJECT_ID = "krishimitra-ai-501314"

# Initialize Earth Engine
ee.Initialize(project=PROJECT_ID)

# Sample location: NIT Kurukshetra
point = ee.Geometry.Point([76.8222, 29.9695])

# Get Sentinel-2 images
collection = (
    ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
    .filterBounds(point)
    .filterDate("2024-01-01", "2024-01-31")
    .sort("CLOUDY_PIXEL_PERCENTAGE")
)

image = collection.first()

if image is None:
    print("No image found.")
else:
    info = image.getInfo()

    print("=" * 50)
    print("Sentinel-2 Image Retrieved Successfully")
    print("=" * 50)

    print(f"Image ID: {info['id']}")
    print(f"Acquisition Date: {info['properties']['DATATAKE_IDENTIFIER']}")
    print(f"Cloud Cover: {info['properties']['CLOUDY_PIXEL_PERCENTAGE']} %")