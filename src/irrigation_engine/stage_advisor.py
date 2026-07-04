def generate_stage_advice(growth_stage, moisture_status):
    """
    Generate crop management advice based on growth stage and moisture stress.
    """

    stage = growth_stage["stage"]
    severity = moisture_status["severity"]

    if "Germination" in stage:
        if severity in ["High", "Critical"]:
            return "Early growth stage with moisture stress. Light and timely irrigation is important for crop establishment."
        return "Crop appears to be in early growth. Maintain adequate soil moisture."

    if "Vegetative" in stage or "Tillering" in stage:
        if severity in ["High", "Critical"]:
            return "Vegetative stage is sensitive to water stress. Irrigation should be considered to support canopy development."
        return "Vegetative growth appears active. Continue regular monitoring."

    if "Flowering" in stage or "Reproductive" in stage:
        if severity in ["High", "Critical"]:
            return "Flowering or reproductive stage with moisture stress can reduce yield. Irrigation is strongly recommended."
        return "Crop appears to be in reproductive stage. Maintain stable moisture to protect yield."

    if "Maturity" in stage:
        return "Crop appears near maturity. Avoid unnecessary irrigation unless field inspection confirms stress."

    return "Monitor crop condition and combine satellite results with field observations."