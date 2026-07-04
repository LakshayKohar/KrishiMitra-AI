import streamlit as st


def render_ndvi_metrics(report):
    st.header("🌱 NDVI Statistics")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Minimum NDVI",
        f"{report['ndvi']['minimum']:.3f}"
    )

    col2.metric(
        "Average NDVI",
        f"{report['ndvi']['average']:.3f}"
    )

    col3.metric(
        "Maximum NDVI",
        f"{report['ndvi']['maximum']:.3f}"
    )

    avg_ndvi = report["ndvi"]["average"]

    st.write("### NDVI Health Meter")

    progress_value = max(0.0, min(1.0, avg_ndvi))

    st.progress(progress_value)

    st.caption("0 = Poor vegetation | 1 = Excellent vegetation")

    st.divider()