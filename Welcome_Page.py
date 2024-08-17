import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# MCQ Validation Site! 👋")

st.sidebar.success("Select a Scenario")

st.markdown(
    """
    Select a scenario for the questions you want to validate!!!
"""
)
