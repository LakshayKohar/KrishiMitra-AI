import streamlit as st


def render_trend_charts(df):
    st.header("📈 Time-Series Trends")

    if df.empty:
        st.info("No time-series data available.")
        return

    chart_df = df.set_index("date")

    st.subheader("🌱 NDVI Trend")
    st.line_chart(chart_df["ndvi"])

    st.subheader("💧 NDWI Trend")
    st.line_chart(chart_df["ndwi"])

    st.subheader("🔥 MSI Trend")
    st.line_chart(chart_df["msi"])

    st.subheader("🌧 Rainfall Trend")
    st.line_chart(chart_df["rainfall"])

    st.subheader("🌡 Temperature Trend")
    st.line_chart(chart_df["temperature"])

    st.divider()