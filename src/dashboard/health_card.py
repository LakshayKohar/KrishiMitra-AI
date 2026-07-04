import streamlit as st


def render_health_card(report):
    st.header("🌾 Crop Health")

    health = report["crop_health"]

    if health == "Excellent Vegetation":
        st.success(f"🟢 {health}")

    elif health == "Healthy Vegetation":
        st.success(f"🟢 {health}")

    elif health == "Moderate Vegetation":
        st.warning(f"🟡 {health}")

    elif health == "Poor Vegetation":
        st.error(f"🟠 {health}")

    else:
        st.error(f"🔴 {health}")

    st.info(report["recommendation"])

    st.divider()