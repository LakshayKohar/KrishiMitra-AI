from src.dashboard.weather_card import render_weather_card
from src.dashboard.irrigation_card import render_irrigation_card
from src.dashboard.moisture_card import render_moisture_card
import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]
sys.path.append(str(project_root))

import json
import streamlit as st

from src.analysis_pipeline import analyze_location
from src.dashboard.header import render_header
from src.dashboard.sidebar import render_sidebar
from src.dashboard.metrics import render_ndvi_metrics
from src.dashboard.health_card import render_health_card
from src.dashboard.download import render_download_button
from src.dashboard.footer import render_footer
from src.dashboard.map_view import render_map


st.set_page_config(
    page_title="KrishiMitra AI",
    page_icon="🌾",
    layout="wide",
)

location, start_date, end_date, analyze = render_sidebar()

render_header()

if "report" not in st.session_state:
    st.session_state.report = None

if "ndvi_image" not in st.session_state:
    st.session_state.ndvi_image = None

if "satellite_image" not in st.session_state:
    st.session_state.satellite_image = None


if analyze:
    with st.spinner("Analyzing satellite data..."):
        report, ndvi_image, satellite_image = analyze_location(
            location,
            str(start_date),
            str(end_date),
        )

        st.session_state.report = report
        st.session_state.ndvi_image = ndvi_image
        st.session_state.satellite_image = satellite_image

    st.success("✅ Analysis Completed!")

elif st.session_state.report is None:
    try:
        with open("outputs/analysis_report.json", "r") as file:
            st.session_state.report = json.load(file)

        st.success("✅ Previous Analysis Loaded!")

    except Exception:
        st.info("Enter location and click Analyze to generate a report.")


report = st.session_state.report
ndvi_image = st.session_state.ndvi_image
satellite_image = st.session_state.satellite_image


if report:
    col1, col2 = st.columns(2)

    with col1:
        st.header("📍 Location")
        st.write(f"**Location:** {report['location']}")
        st.write(f"**Latitude:** {report['latitude']:.6f}")
        st.write(f"**Longitude:** {report['longitude']:.6f}")

    with col2:
        st.header("🛰 Satellite")
        st.write(f"**Cloud Cover:** {report['cloud_cover']:.2f}%")
        st.write(f"**Acquisition:** {report.get('acquisition_date', 'N/A')}")

    st.divider()

    render_ndvi_metrics(report)

    render_health_card(report)
    render_weather_card(report)
    render_irrigation_card(report)
    render_moisture_card(report)

    if ndvi_image is not None and satellite_image is not None:
        render_map(
            ndvi_image,
            satellite_image,
            report,
        )
    else:
        st.info("Run a fresh analysis to view Sentinel-2 and NDVI map layers.")

    render_download_button(report)

render_footer()