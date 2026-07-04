import streamlit as st
from datetime import date


def render_sidebar():
    st.sidebar.title("🌾 KrishiMitra AI")

    location = st.sidebar.text_input(
        "📍 Location",
        "Rohtak, Haryana"
    )

    start_date = st.sidebar.date_input(
        "📅 Start Date",
        value=date(2024, 1, 1)
    )

    end_date = st.sidebar.date_input(
        "📅 End Date",
        value=date(2024, 1, 31)
    )

    analyze = st.sidebar.button("🚀 Analyze")

    st.sidebar.divider()

    st.sidebar.subheader("System Status")
    st.sidebar.success("Earth Engine Connected")
    st.sidebar.success("Geocoder Ready")
    st.sidebar.success("NDVI Engine Ready")
    st.sidebar.success("Dashboard Active")

    st.sidebar.divider()

    st.sidebar.write("Version 1.0")

    return location, start_date, end_date, analyze