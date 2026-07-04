import ee


def calculate_ndvi_statistics(ndvi_image, geometry):
    """
    Calculate minimum, maximum and mean NDVI.
    """

    stats = ndvi_image.reduceRegion(
        reducer=ee.Reducer.minMax().combine(
            reducer2=ee.Reducer.mean(),
            sharedInputs=True
        ),
        geometry=geometry,
        scale=10,
        maxPixels=1e9
    )

    return stats.getInfo()