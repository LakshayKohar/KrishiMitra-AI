import ee


def calculate_index_statistics(index_image, index_name, longitude, latitude, buffer_meters=1000):
    """
    Calculate min, max and mean statistics for any Earth Engine index image.
    """

    point = ee.Geometry.Point([longitude, latitude])
    region = point.buffer(buffer_meters)

    stats = index_image.reduceRegion(
        reducer=ee.Reducer.minMax().combine(
            reducer2=ee.Reducer.mean(),
            sharedInputs=True
        ),
        geometry=region,
        scale=10,
        maxPixels=1e9,
        bestEffort=True,
    )

    result = stats.getInfo()

    mean_key = f"{index_name}_mean"

    if result.get(mean_key) is None:
        raise ValueError(
            f"{index_name} statistics could not be calculated. Try another location or date range."
        )

    return result