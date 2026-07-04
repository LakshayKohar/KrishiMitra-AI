def detect_growth_stage(crop_name, mean_ndvi, month):
    """
    Detect approximate crop growth stage using crop type, NDVI, and month.
    This is an MVP rule-based detector. Later it can be replaced by ML/time-series logic.
    """

    crop_name = crop_name.lower()

    if mean_ndvi < 0.20:
        return {
            "stage": "Germination / Early Growth",
            "confidence": "Medium",
            "message": "Low NDVI suggests early crop development or sparse vegetation."
        }

    if 0.20 <= mean_ndvi < 0.45:
        return {
            "stage": "Vegetative Growth",
            "confidence": "Medium",
            "message": "Moderate NDVI suggests active vegetative development."
        }

    if 0.45 <= mean_ndvi < 0.65:
        if "wheat" in crop_name or "rabi" in crop_name:
            return {
                "stage": "Tillering / Stem Elongation",
                "confidence": "Medium",
                "message": "NDVI and season suggest wheat may be in tillering or stem elongation stage."
            }

        if "rice" in crop_name or "kharif" in crop_name:
            return {
                "stage": "Vegetative / Panicle Initiation",
                "confidence": "Medium",
                "message": "NDVI suggests active vegetative growth or early reproductive development."
            }

        return {
            "stage": "Active Vegetative Stage",
            "confidence": "Medium",
            "message": "NDVI indicates strong crop canopy development."
        }

    if 0.65 <= mean_ndvi < 0.80:
        return {
            "stage": "Flowering / Reproductive Stage",
            "confidence": "Medium-High",
            "message": "High NDVI suggests dense canopy and possible reproductive stage."
        }

    return {
        "stage": "Peak Growth / Maturity",
        "confidence": "Medium",
        "message": "Very high NDVI suggests peak vegetation or late growth stage."
    }