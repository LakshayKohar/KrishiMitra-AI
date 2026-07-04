def generate_water_stress_advice(moisture_status, rainfall, temperature):
    """
    Generate consistent water stress advisory using moisture status and weather.
    """

    severity = moisture_status["severity"]

    if rainfall > 2:
        return "Rainfall has been detected. Irrigation can be delayed temporarily, but continue monitoring field conditions."

    if severity == "Low":
        return "Moisture condition appears stable. No immediate irrigation action is required."

    if severity == "Moderate":
        if temperature >= 30:
            return "Mild moisture stress is detected with high temperature. Monitor the field closely and consider irrigation if stress persists."
        return "Mild moisture stress is detected. Continue monitoring soil moisture and crop appearance."

    if severity == "High":
        if temperature >= 30:
            return "Moderate moisture stress is detected under high temperature. Irrigation should be considered soon."
        return "Moderate moisture stress is detected. Field inspection and irrigation planning are recommended."

    if severity == "Critical":
        return "Severe moisture stress is detected. Immediate field inspection and irrigation are strongly recommended."

    return "Moisture condition could not be clearly classified. Field inspection is recommended."