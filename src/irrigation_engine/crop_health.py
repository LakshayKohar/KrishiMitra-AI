def interpret_ndvi(mean_ndvi):
    """
    Interpret crop health based on average NDVI.
    Returns a dictionary containing the health status and recommendation.
    """

    if mean_ndvi >= 0.70:
        return {
            "status": "Excellent Vegetation",
            "recommendation": "Crop is healthy. Continue current irrigation and nutrient management."
        }

    elif mean_ndvi >= 0.50:
        return {
            "status": "Healthy Vegetation",
            "recommendation": "Crop is healthy. Monitor field conditions regularly."
        }

    elif mean_ndvi >= 0.30:
        return {
            "status": "Moderate Vegetation",
            "recommendation": "Monitor irrigation and nutrient levels. Early signs of stress may be present."
        }

    elif mean_ndvi >= 0.10:
        return {
            "status": "Poor Vegetation",
            "recommendation": "Inspect the field for water stress, pests, or nutrient deficiencies."
        }

    else:
        return {
            "status": "Very Sparse or No Vegetation",
            "recommendation": "No healthy crop detected. Verify crop stage or field condition."
        }