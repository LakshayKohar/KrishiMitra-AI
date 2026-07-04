import json


def save_analysis_report(
    location,
    latitude,
    longitude,
    cloud_cover,
    ndvi_stats,
    crop_health,
    recommendation,
):
    """
    Save the analysis report as a JSON file.
    """

    report = {
        "location": location,
        "latitude": latitude,
        "longitude": longitude,
        "cloud_cover": cloud_cover,
        "ndvi": {
            "minimum": ndvi_stats["NDVI_min"],
            "maximum": ndvi_stats["NDVI_max"],
            "average": ndvi_stats["NDVI_mean"],
        },
        "crop_health": crop_health,
        "recommendation": recommendation,
    }

    with open("outputs/analysis_report.json", "w") as file:
        json.dump(report, file, indent=4)

    print("\n✅ Analysis report saved successfully.")