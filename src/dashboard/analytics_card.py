import streamlit as st


def render_time_series_analytics(analytics):
    st.header("📊 Dataset Analytics")

    if not analytics:
        st.info("No analytics available.")
        return

    c1, c2, c3 = st.columns(3)

    c1.metric("Images Used", analytics["images_used"])
    c2.metric("Average NDVI", f"{analytics['average_ndvi']:.3f}")
    c3.metric("Avg Cloud Cover", f"{analytics['average_cloud_cover']:.2f}%")

    c4, c5 = st.columns(2)

    c4.metric(
        "Highest NDVI",
        f"{analytics['highest_ndvi']:.3f}",
        help=f"Date: {analytics['highest_ndvi_date']}"
    )

    c5.metric(
        "Lowest NDVI",
        f"{analytics['lowest_ndvi']:.3f}",
        help=f"Date: {analytics['lowest_ndvi_date']}"
    )

    st.divider()