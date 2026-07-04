def calculate_ndvi(image):
    """
    NDVI = (NIR - Red) / (NIR + Red)
    Sentinel-2: B8 = NIR, B4 = Red
    """
    return image.normalizedDifference(["B8", "B4"]).rename("NDVI")


def calculate_ndwi(image):
    """
    NDWI = (Green - NIR) / (Green + NIR)
    Sentinel-2: B3 = Green, B8 = NIR
    Higher NDWI usually indicates more water content.
    """
    return image.normalizedDifference(["B3", "B8"]).rename("NDWI")


def calculate_msi(image):
    """
    MSI = SWIR / NIR
    Sentinel-2: B11 = SWIR, B8 = NIR
    Higher MSI usually indicates higher moisture stress.
    """
    return image.select("B11").divide(image.select("B8")).rename("MSI")