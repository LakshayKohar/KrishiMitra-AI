import ee


def calculate_ndvi_statistics(ndvi_image, longitude, latitude, buffer_meters=1000):
    """
    Calculate NDVI statistics around a selected location.
    """

    point = ee.Geometry.Point([longitude, latitude])
    region = point.buffer(buffer_meters)

    stats = ndvi_image.reduceRegion(
        reducer=ee.Reducer.minMax().combine(
            reducer2=ee.Reducer.mean(),
            sharedInputs=True
        ),
        geometry=region,
        scale=10,
        maxPixels=1e9,
        bestEffort=True
    )

    result = stats.getInfo()

    if result.get("NDVI_mean") is None:
        raise ValueError(
            "NDVI statistics could not be calculated. Try another date range or location."
        )

    return result