import streamlit as st
import requests

WEATHER_API = "http://127.0.0.1:8000/api/weather/Delhi"


def show_dashboard():

    st.title("🌱 Dharti AI Dashboard")
    st.caption("Smart Agriculture Platform powered by AI")

    st.divider()

    # -------------------------
    # Weather
    # -------------------------

    try:

        weather = requests.get(
            WEATHER_API,
            timeout=5
        ).json()

        temperature = weather["temperature"]
        humidity = weather["humidity"]

    except:

        temperature = "--"
        humidity = "--"

    # -------------------------
    # Metrics
    # -------------------------

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "🌾 Crop Model",
        "Ready"
    )

    col2.metric(
        "🌦 Temperature",
        f"{temperature}°C"
    )

    col3.metric(
        "💧 Humidity",
        f"{humidity}%"
    )

    col4.metric(
        "📈 Market",
        "Active"
    )

    st.divider()

    # -------------------------
    # Feature Cards
    # -------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.info(
            """
### 🌾 Crop Recommendation

✔ Machine Learning Model

✔ Soil Analysis

✔ Climate Score

✔ Top 3 Crop Suggestions
"""
        )

    with col2:

        st.success(
            """
### 🌦 Weather Intelligence

✔ Live Weather

✔ Rainfall

✔ Temperature

✔ Humidity
"""
        )

    col3, col4 = st.columns(2)

    with col3:

        st.warning(
            """
### 📈 Market Intelligence

✔ Crop Prices

✔ Profit Analysis

✔ Price Trends

✔ Market Status
"""
        )

    with col4:

        st.error(
            """
### 🦠 Disease Detection

✔ Upload Leaf Image

✔ Disease Prediction

✔ Treatment Advice
"""
        )

    st.divider()

    st.subheader("🚀 Platform Status")

    st.progress(95)

    st.success("Dharti AI is operational and all core services are running.")

    st.divider()

st.subheader("🌍 About Dharti AI")

st.write("""
Dharti AI is an AI-powered smart agriculture platform designed to help farmers make informed decisions.

### Key Features

- 🌾 Crop Recommendation using Machine Learning
- 🌦 Live Weather Intelligence
- 📈 Market Price Analysis
- 🦠 Disease Detection
- 📄 PDF Report Generation
- 🤖 AI Agricultural Assistant

Developed using Streamlit, FastAPI, Scikit-learn, Python, and AI technologies.
""")

