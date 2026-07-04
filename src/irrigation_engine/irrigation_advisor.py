def generate_irrigation_advice(mean_ndvi, rainfall, temperature):
    """
    Generate irrigation advice using NDVI and weather.
    """

    if rainfall > 2:
        return "Rainfall detected. Irrigation can be delayed for now."

    if mean_ndvi < 0.30 and temperature > 30:
        return "High irrigation priority. Low NDVI and high temperature indicate possible crop stress."

    if mean_ndvi < 0.50 and temperature > 28:
        return "Moderate irrigation priority. Monitor the field and consider irrigation soon."

    if mean_ndvi >= 0.50:
        return "Crop condition appears stable. Continue regular monitoring."

    return "Monitor field conditions. Irrigation decision should be based on crop stage and soil moisture."