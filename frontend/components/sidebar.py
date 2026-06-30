import streamlit as st


def sidebar():

    st.sidebar.image(
        "https://img.icons8.com/color/96/plant-under-sun.png",
        width=70
    )

    st.sidebar.title("🌱 DHARTI AI")

    page = st.sidebar.radio(
        "",
        [
            "🏠 Dashboard",
            "🌾 Crop Recommendation",
            "🌦 Weather Intelligence",
            "📈 Market Intelligence",
            "🌿 Disease Detection",
            "🤖 AI Assistant",
            "📄 Reports"
        ]
    )

    st.sidebar.divider()

    st.sidebar.success("System Status")

    st.sidebar.write("🟢 Backend Connected")

    st.sidebar.write("🟢 AI Model Loaded")

    return page