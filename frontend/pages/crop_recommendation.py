import streamlit as st
import requests

from components.recommendation_card import recommendation_card

# -------------------------------------
# API URLs
# -------------------------------------

CROP_API = "http://127.0.0.1:8000/api/crop/recommend"
WEATHER_API = "http://127.0.0.1:8000/api/weather"


def show_crop_recommendation():

    st.title("🌾 Smart Crop Recommendation")
    st.caption(
        "AI-powered crop recommendation using live weather and soil information."
    )

    st.divider()

    # =====================================
    # LOCATION
    # =====================================

    st.subheader("📍 Farm Location")

    col_city, col_btn = st.columns([3, 1])

    with col_city:
        city = st.text_input(
            "Enter City",
            value="Delhi"
        )

    with col_btn:

        st.write("")
        st.write("")

        if st.button("🌦 Fetch Weather", use_container_width=True):

            try:

                with st.spinner("Fetching Live Weather..."):

                    response = requests.get(
                        f"{WEATHER_API}/{city}",
                        timeout=10
                    )

                if response.status_code == 200:

                    weather = response.json()

                    st.session_state["temperature"] = weather["temperature"]
                    st.session_state["humidity"] = weather["humidity"]
                    st.session_state["rainfall"] = weather["rainfall"]
                    st.session_state["wind_speed"] = weather["wind_speed"]
                    st.session_state["weather_loaded"] = True

                    st.success("✅ Weather Updated Successfully")

                else:

                    st.error("Unable to fetch weather.")

            except Exception as e:

                st.error(f"Error: {e}")

    # =====================================
    # WEATHER DASHBOARD
    # =====================================

    if st.session_state.get("weather_loaded", False):

        st.divider()

        st.subheader("🌦 Current Weather")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "🌡 Temperature",
            f"{st.session_state['temperature']} °C"
        )

        c2.metric(
            "💧 Humidity",
            f"{st.session_state['humidity']} %"
        )

        c3.metric(
            "🌧 Rainfall",
            f"{st.session_state['rainfall']} mm"
        )

        c4.metric(
            "💨 Wind Speed",
            f"{st.session_state['wind_speed']} m/s"
        )

    else:

        st.info("👆 Fetch live weather before analyzing your farm.")

    st.divider()

    col1, col2 = st.columns(2)

    # =====================================
    # SOIL INFORMATION
    # =====================================

    with col1:

        st.subheader("🌱 Soil Information")

        N = st.number_input("Nitrogen (N)", 0.0, 150.0, 90.0)
        P = st.number_input("Phosphorus (P)", 0.0, 150.0, 42.0)
        K = st.number_input("Potassium (K)", 0.0, 250.0, 43.0)

        ph = st.slider(
            "Soil pH",
            0.0,
            14.0,
            6.5,
            0.1
        )

    # =====================================
    # WEATHER DATA
    # =====================================

    with col2:

        st.subheader("🌦 Weather Data")

        temperature = st.number_input(
            "Temperature (°C)",
            value=float(st.session_state.get("temperature", 20.8)),
            disabled=True
        )

        humidity = st.slider(
            "Humidity (%)",
            0,
            100,
            int(st.session_state.get("humidity", 82)),
            disabled=True
        )

        rainfall = st.number_input(
            "Rainfall (mm)",
            value=float(st.session_state.get("rainfall", 202.0)),
            disabled=True
        )

    st.divider()

    # =====================================
    # ANALYZE
    # =====================================

    if st.button("🚀 Analyze Farm", use_container_width=True):

        if not st.session_state.get("weather_loaded", False):

            st.warning("⚠ Please fetch live weather first.")

            st.stop()

        payload = {

            "N": N,
            "P": P,
            "K": K,
            "temperature": temperature,
            "humidity": humidity,
            "ph": ph,
            "rainfall": rainfall

        }

        try:

            with st.spinner("🤖 AI is analyzing your farm..."):

                response = requests.post(
                    CROP_API,
                    json=payload,
                    timeout=15
                )

            if response.status_code != 200:

                st.error("Backend Error")

                st.code(response.text)

                return

            result = response.json()

            recommendations = result["recommendations"]

            climate = result["climate"]

            st.success("✅ Analysis Completed Successfully")

            st.divider()

            # =====================================
            # CLIMATE SCORE
            # =====================================

            st.subheader("🌍 Climate Suitability")

            score = climate["score"]

            st.progress(score / 100)

            if score >= 90:

                st.success(f"🌿 Excellent Climate ({score}/100)")

            elif score >= 75:

                st.info(f"🌾 Good Climate ({score}/100)")

            else:

                st.warning(f"⚠ Poor Climate ({score}/100)")

            for reason in climate["reasons"]:

                st.write(reason)

            st.divider()

            # =====================================
            # RECOMMENDATIONS
            # =====================================

            st.subheader("🏆 Top 3 Recommended Crops")

            st.write("Crop recommendation received successfully.")

        except requests.exceptions.ConnectionError:

            st.error("❌ Cannot connect to the FastAPI backend.")

        except Exception as e:

            st.error(f"Unexpected Error: {e}")