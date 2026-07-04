def classify_moisture_status(ndwi_mean, msi_mean):
    """
    Classify crop moisture condition using NDWI and MSI.
    """

    if ndwi_mean >= 0.30 and msi_mean <= 0.60:
        return {
            "status": "Good Moisture Condition",
            "severity": "Low",
            "message": "Crop water condition appears stable."
        }

    elif ndwi_mean >= 0.10 and msi_mean <= 0.90:
        return {
            "status": "Mild Moisture Stress",
            "severity": "Moderate",
            "message": "Slight reduction in water content detected. Monitor field conditions."
        }

    elif ndwi_mean >= 0.00 and msi_mean <= 1.20:
        return {
            "status": "Moderate Moisture Stress",
            "severity": "High",
            "message": "Moisture stress is likely. Irrigation may be required soon."
        }

    else:
        return {
            "status": "Severe Moisture Stress",
            "severity": "Critical",
            "message": "Strong water stress indicators detected. Immediate field inspection is recommended."
        }