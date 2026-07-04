def generate_final_advisory(report):
    """
    Generate a final farmer-friendly advisory by combining:
    - crop health
    - moisture stress
    - weather
    - irrigation advice
    - growth stage
    - crop prediction
    """

    ndvi = report["ndvi"]["average"]
    crop_health = report["crop_health"]
    moisture_status = report["moisture_status"]
    weather = report["weather"]
    growth_stage = report.get("growth_stage", {})
    crop_prediction = report.get("ml_crop_prediction", {})

    priority = "Low"
    actions = []

    if moisture_status["severity"] in ["High", "Critical"]:
        priority = "High"
        actions.append("Inspect field moisture condition.")
        actions.append("Plan irrigation soon.")

    if moisture_status["severity"] == "Critical":
        priority = "Critical"
        actions.append("Immediate irrigation is recommended.")

    if ndvi < 0.30:
        priority = "High"
        actions.append("Check for poor crop growth or bare patches.")

    if weather["rainfall"] > 2:
        actions.append("Rainfall detected. Delay irrigation temporarily.")

    if weather["temperature"] >= 32:
        actions.append("High temperature detected. Monitor crop stress closely.")

    if not actions:
        actions.append("Continue regular monitoring.")

    summary = (
        f"The field shows {crop_health.lower()} with "
        f"{moisture_status['status'].lower()}. "
    )

    if crop_prediction:
        summary += f"Predicted crop type is {crop_prediction.get('crop', 'unknown')}. "

    if growth_stage:
        summary += f"The crop appears to be in {growth_stage.get('stage', 'unknown stage')}. "

    summary += "Recommendations are based on satellite indices, weather, and rule-based intelligence."

    return {
        "priority": priority,
        "summary": summary,
        "actions": actions,
    }