import streamlit as st


def render_weather_card(report):
    if "weather" not in report:
        st.info("Run a fresh analysis to load weather data.")
        return

    weather = report["weather"]

    st.header("🌦 Weather Intelligence")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Temperature", f"{weather['temperature']} °C")
    col2.metric("Humidity", f"{weather['humidity']} %")
    col3.metric("Rainfall", f"{weather['rainfall']} mm")
    col4.metric("Wind Speed", f"{weather['wind_speed']} km/h")

    st.divider()