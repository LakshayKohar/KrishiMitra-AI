import requests


def get_weather_history(latitude, longitude, start_date, end_date):
    url = (
        "https://archive-api.open-meteo.com/v1/archive"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        f"&start_date={start_date}"
        f"&end_date={end_date}"
        "&daily=temperature_2m_mean,precipitation_sum,relative_humidity_2m_mean,wind_speed_10m_mean"
        "&timezone=auto"
    )

    response = requests.get(url, timeout=20)
    response.raise_for_status()

    data = response.json()
    daily = data["daily"]

    weather_by_date = {}

    for i, date in enumerate(daily["time"]):
        weather_by_date[date] = {
            "temperature": daily["temperature_2m_mean"][i],
            "rainfall": daily["precipitation_sum"][i],
            "humidity": daily["relative_humidity_2m_mean"][i],
            "wind_speed": daily["wind_speed_10m_mean"][i],
        }

    return weather_by_date