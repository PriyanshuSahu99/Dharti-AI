import os
import streamlit as st


def load_css():
    BASE_DIR = os.path.dirname(__file__)

    css_path = os.path.join(
        BASE_DIR,
        "..",
        "assets",
        "css",
        "style.css"
    )

    with open(css_path) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )