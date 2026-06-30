import streamlit as st


def hero():

    st.markdown(
        """
        <div style="
            background:linear-gradient(90deg,#2E7D32,#43A047);
            padding:30px;
            border-radius:20px;
            color:white;
        ">

        <h1>🌱 DHARTI AI</h1>

        <h3>Climate Smart Farming Platform</h3>

        <p>
        AI-powered decision support system helping farmers
        adapt to climate change through crop recommendation,
        weather intelligence and market prediction.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )