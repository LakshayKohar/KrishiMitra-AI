def classify_crop(mean_ndvi, mean_ndwi, mean_msi, month):
    """
    Rule-based crop classification MVP.
    This is the first version and will later be replaced/improved with ML.
    """

    if month in [11, 12, 1, 2, 3]:
        if mean_ndvi >= 0.45 and mean_ndwi >= -0.10:
            return {
                "crop": "Wheat / Rabi Crop",
                "confidence": "Medium",
                "reason": "High winter NDVI pattern suggests active Rabi-season vegetation."
            }

        if mean_ndvi >= 0.30:
            return {
                "crop": "Mustard / Rabi Crop",
                "confidence": "Low-Medium",
                "reason": "Moderate winter vegetation pattern may indicate mustard or other Rabi crops."
            }

    if month in [6, 7, 8, 9, 10]:
        if mean_ndvi >= 0.50 and mean_ndwi >= 0.00:
            return {
                "crop": "Rice / Kharif Crop",
                "confidence": "Medium",
                "reason": "High NDVI with relatively higher water index suggests Kharif crop conditions."
            }

        if mean_ndvi >= 0.35 and mean_msi <= 1.00:
            return {
                "crop": "Cotton / Maize / Kharif Crop",
                "confidence": "Low-Medium",
                "reason": "Moderate vegetation and moisture pattern suggests possible Kharif crop."
            }

    return {
        "crop": "Unknown / Mixed Land Cover",
        "confidence": "Low",
        "reason": "Current spectral and seasonal indicators are insufficient for confident crop classification."
    }