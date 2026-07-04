import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]
sys.path.append(str(project_root))

import json
import streamlit as st
from src.utils.pdf_report import generate_pdf_report
from src.analysis_pipeline import analyze_location
from src.dashboard.header import render_header
from src.dashboard.sidebar import render_sidebar
from src.dashboard.metrics import render_ndvi_metrics
from src.dashboard.health_card import render_health_card
from src.dashboard.download import render_download_button
from src.dashboard.footer import render_footer
from src.dashboard.map_view import render_map
from src.dashboard.weather_card import render_weather_card
from src.dashboard.irrigation_card import render_irrigation_card
from src.dashboard.moisture_card import render_moisture_card
from src.dashboard.crop_card import render_crop_card
from src.dashboard.growth_stage_card import render_growth_stage_card
from src.dashboard.final_advisory_card import render_final_advisory_card

from src.time_series.dataset_builder import build_time_series_dataset
from src.time_series.temporal_analysis import analyze_time_series
from src.dashboard.trend_chart import render_trend_charts
from src.dashboard.analytics_card import render_time_series_analytics


st.set_page_config(
    page_title="KrishiMitra AI",
    page_icon="🌾",
    layout="wide",
)

location, start_date, end_date, analyze, build_dataset = render_sidebar()

render_header()

if "report" not in st.session_state:
    st.session_state.report = None

if "ndvi_image" not in st.session_state:
    st.session_state.ndvi_image = None

if "satellite_image" not in st.session_state:
    st.session_state.satellite_image = None

if "time_series_df" not in st.session_state:
    st.session_state.time_series_df = None

if "time_series_csv" not in st.session_state:
    st.session_state.time_series_csv = None

if "time_series_analytics" not in st.session_state:
    st.session_state.time_series_analytics = None


if analyze:
    try:
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

    except Exception as error:
        st.error("❌ Analysis failed. Try another location or date range.")
        st.exception(error)


if build_dataset:
    try:
        with st.spinner("Building time-series dataset..."):
            df, csv_path = build_time_series_dataset(
                location=location,
                start_date=str(start_date),
                end_date=str(end_date),
                max_cloud=40,
            )

            analytics = analyze_time_series(df)

            st.session_state.time_series_df = df
            st.session_state.time_series_csv = csv_path
            st.session_state.time_series_analytics = analytics

        st.success("✅ Time-Series Dataset Built Successfully!")

    except Exception as error:
        st.error("❌ Time-series dataset generation failed.")
        st.exception(error)


if st.session_state.report is None:
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
    render_crop_card(report)
    render_growth_stage_card(report)
    render_final_advisory_card(report)
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

    if st.session_state.time_series_df is not None:
        render_time_series_analytics(
            st.session_state.time_series_analytics
        )

        render_trend_charts(
            st.session_state.time_series_df
        )

        csv_data = st.session_state.time_series_df.to_csv(index=False)

        st.download_button(
            label="⬇ Download Time-Series CSV",
            data=csv_data,
            file_name="krishimitra_time_series_dataset.csv",
            mime="text/csv",
        )

    render_download_button(report)

    if report:
     pdf_path = generate_pdf_report(report)

    with open(pdf_path, "rb") as pdf_file:
        st.download_button(
            label="⬇ Download PDF Report",
            data=pdf_file,
            file_name="krishimitra_report.pdf",
            mime="application/pdf",
        )

render_footer()