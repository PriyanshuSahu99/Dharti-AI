import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/api/market"


def show_market():

    st.title("📈 Market Intelligence")
    st.caption("Real-time crop market insights and price trends")

    try:

        response = requests.get(API_URL, timeout=5)

        if response.status_code != 200:
            st.error("Unable to fetch market data.")
            return

        market_data = response.json()

        st.success("Latest Market Prices")

        st.divider()

        for item in market_data:

            with st.container(border=True):

                col1, col2 = st.columns([2, 1])

                with col1:

                    st.subheader(f"🌾 {item['crop']}")

                    st.write(f"**Market:** {item['market']}")
                    st.write(f"**Price:** {item['price']}")

                with col2:

                    st.metric(
                        "Trend",
                        item["trend"]
                    )

                    st.metric(
                        "Profit",
                        item["profit"]
                    )

    except requests.exceptions.ConnectionError:

        st.error("❌ Cannot connect to FastAPI Backend")

    except Exception as e:

        st.error(str(e))