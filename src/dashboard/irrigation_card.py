import streamlit as st


def render_irrigation_card(report):
    st.header("💧 Irrigation Advisory")

    if "irrigation_advice" in report:
        st.info(report["irrigation_advice"])
    else:
        st.info("Run a fresh analysis to generate irrigation advice.")

    st.divider()