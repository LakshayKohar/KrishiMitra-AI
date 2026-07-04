def analyze_time_series(df):
    if df.empty:
        return {}

    highest_ndvi_row = df.loc[df["ndvi"].idxmax()]
    lowest_ndvi_row = df.loc[df["ndvi"].idxmin()]

    return {
        "images_used": len(df),
        "average_ndvi": df["ndvi"].mean(),
        "highest_ndvi": highest_ndvi_row["ndvi"],
        "highest_ndvi_date": highest_ndvi_row["date"],
        "lowest_ndvi": lowest_ndvi_row["ndvi"],
        "lowest_ndvi_date": lowest_ndvi_row["date"],
        "average_cloud_cover": df["cloud_cover"].mean(),
        "average_rainfall": df["rainfall"].mean(),
        "average_temperature": df["temperature"].mean(),
    }