import json
import streamlit as st


def render_download_button(report):
    report_json = json.dumps(report, indent=4)

    st.download_button(
        label="⬇ Download JSON Report",
        data=report_json,
        file_name="krishimitra_analysis_report.json",
        mime="application/json"
    )