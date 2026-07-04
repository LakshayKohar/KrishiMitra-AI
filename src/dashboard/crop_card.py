import streamlit as st


def render_crop_card(report):
    st.header("🌾 Crop Classification")

    if "crop_prediction" in report:
        rule_crop = report["crop_prediction"]

        st.subheader("Rule-Based Prediction")
        st.metric("Predicted Crop", rule_crop["crop"])
        st.write(f"**Confidence:** {rule_crop['confidence']}")
        st.info(rule_crop["reason"])

    if "ml_crop_prediction" in report:
        ml_crop = report["ml_crop_prediction"]

        st.subheader("ML Model Prediction")
        st.metric("ML Predicted Crop", ml_crop["crop"])
        st.write(f"**Confidence:** {ml_crop['confidence']}")
        st.info(ml_crop["reason"])

    st.divider()