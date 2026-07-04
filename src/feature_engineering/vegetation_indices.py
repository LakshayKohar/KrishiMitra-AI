import ee


def calculate_ndvi(image):
    """
    Calculate NDVI from a Sentinel-2 image.

    NDVI = (B8 - B4) / (B8 + B4)
    """

    return image.normalizedDifference(["B8", "B4"]).rename("NDVI")