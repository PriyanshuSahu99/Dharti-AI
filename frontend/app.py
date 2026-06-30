import streamlit as st

# Components
from components.sidebar import sidebar

# Pages
from pages.dashboard import show_dashboard
from pages.crop_recommendation import show_crop_recommendation

# Utils
from utils.style import load_css

from pages.market import show_market

from pages.report import show_report

from pages.disease import show_disease

from pages.chatbot import show_chatbot

from pages.weather import show_weather

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Dharti AI",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------
# Load Custom CSS
# -------------------------------
load_css()

# -------------------------------
# Sidebar Navigation
# -------------------------------
page = sidebar()

# -------------------------------
# Route Pages
# -------------------------------

if page == "🏠 Dashboard":
    show_dashboard()

elif page == "🌾 Crop Recommendation":
    show_crop_recommendation()

elif page == "🌦 Weather Intelligence":
    show_weather()

elif page == "📈 Market Intelligence":
    show_market()

elif page == "🌿 Disease Detection":
    show_disease()

elif page == "🤖 AI Assistant":
    show_chatbot()

elif page == "📄 Reports":
    show_report()