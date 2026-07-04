import streamlit as st


def render_final_advisory_card(report):
    st.header("🤖 Final AI Advisory")

    if "final_advisory" not in report:
        st.info("Run a fresh analysis to generate final advisory.")
        return

    advisory = report["final_advisory"]
    priority = advisory["priority"]

    if priority == "Low":
        st.success(f"Priority: {priority}")

    elif priority == "Medium":
        st.warning(f"Priority: {priority}")

    elif priority == "High":
        st.error(f"Priority: {priority}")

    else:
        st.error(f"🚨 Priority: {priority}")

    st.write(advisory["summary"])

    st.subheader("Recommended Actions")

    for action in advisory["actions"]:
        st.write(f"• {action}")

    st.divider()