import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/api/weather"


def show_weather():

    st.title("🌦 Weather Intelligence")
    st.caption("Get live weather information for your city.")

    city = st.text_input(
        "Enter City",
        value="Delhi"
    )

    if st.button("🌦 Get Weather"):

        try:

            response = requests.get(
                f"{API_URL}/{city}",
                timeout=10
            )

            if response.status_code != 200:

                st.error("Unable to fetch weather.")
                st.code(response.text)
                return

            weather = response.json()

            st.success("Weather Retrieved Successfully")

            st.divider()

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "🌡 Temperature",
                    f"{weather['temperature']} °C"
                )

                st.metric(
                    "💧 Humidity",
                    f"{weather['humidity']} %"
                )

            with col2:

                st.metric(
                    "💨 Wind Speed",
                    f"{weather['wind_speed']} m/s"
                )

                st.metric(
                    "🌧 Rainfall",
                    f"{weather['rainfall']} mm"
                )

            st.divider()

            st.subheader("📍 City")

            st.info(weather["city"])

        except requests.exceptions.ConnectionError:

            st.error("Cannot connect to FastAPI backend.")

        except Exception as e:

            st.error(str(e))