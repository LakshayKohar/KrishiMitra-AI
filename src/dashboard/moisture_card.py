import streamlit as st


def render_moisture_card(report):
    st.header("💧 Moisture Stress Intelligence")

    if "ndwi" not in report or "msi" not in report:
        st.info("Run a fresh analysis to calculate moisture stress.")
        return

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Average NDWI", f"{report['ndwi']['average']:.3f}")

    with col2:
        st.metric("Average MSI", f"{report['msi']['average']:.3f}")

    moisture = report["moisture_status"]
    severity = moisture["severity"]

    if severity == "Low":
        st.success(f"🟢 {moisture['status']}")

    elif severity == "Moderate":
        st.warning(f"🟡 {moisture['status']}")

    elif severity == "High":
        st.error(f"🟠 {moisture['status']}")

    elif severity == "Critical":
        st.error(f"🔴 {moisture['status']}")

    else:
        st.info(moisture["status"])

    st.markdown("### Recommendation")
    st.info(report["water_stress_advice"])

    st.divider()