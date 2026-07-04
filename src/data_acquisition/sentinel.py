import ee

PROJECT_ID = "krishimitra-ai-501314"


def initialize():
    """
    Initialize Google Earth Engine.
    """
    ee.Initialize(project=PROJECT_ID)


def get_sentinel_image(longitude, latitude, start_date, end_date):
    """
    Fetch the least cloudy Sentinel-2 image.
    """

    point = ee.Geometry.Point([longitude, latitude])

    collection = (
        ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
        .filterBounds(point)
        .filterDate(start_date, end_date)
        .sort("CLOUDY_PIXEL_PERCENTAGE")
    )

    return collection.first()


def get_image_metadata(image):
    """
    Extract useful metadata from a Sentinel-2 image.
    """

    info = image.getInfo()

    return {
        "image_id": info["id"],
        "cloud_cover": info["properties"]["CLOUDY_PIXEL_PERCENTAGE"],
        "acquisition_date": info["properties"]["DATATAKE_IDENTIFIER"],
    }