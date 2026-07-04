import ee

PROJECT_ID = "krishimitra-ai-501314"


def initialize():
    ee.Initialize(project=PROJECT_ID)


def get_sentinel_collection(longitude, latitude, start_date, end_date, max_cloud=40):
    point = ee.Geometry.Point([longitude, latitude])

    collection = (
        ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
        .filterBounds(point)
        .filterDate(start_date, end_date)
        .filter(ee.Filter.lte("CLOUDY_PIXEL_PERCENTAGE", max_cloud))
        .sort("system:time_start")
    )

    return collection