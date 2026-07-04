import streamlit as st


def render_growth_stage_card(report):
    st.header("📈 Growth Stage Detection")

    if "growth_stage" not in report:
        st.info("Run a fresh analysis to detect growth stage.")
        return

    growth_stage = report["growth_stage"]

    st.metric("Detected Stage", growth_stage["stage"])
    st.write(f"**Confidence:** {growth_stage['confidence']}")
    st.info(growth_stage["message"])

    if "stage_advice" in report:
        st.warning(report["stage_advice"])

    st.divider()