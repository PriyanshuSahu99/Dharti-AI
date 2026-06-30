import streamlit as st

responses = {
    "rice": """
🌾 Rice grows best in warm and humid conditions.

Recommendations:
• Soil pH: 5.5 - 7.0
• Temperature: 20°C - 35°C
• High rainfall is beneficial.
""",

    "wheat": """
🌾 Wheat prefers cool weather.

Recommendations:
• Soil pH: 6.0 - 7.5
• Temperature: 15°C - 25°C
• Moderate irrigation.
""",

    "fertilizer": """
🧪 Fertilizer Tips

• Nitrogen → Leaf growth
• Phosphorus → Root development
• Potassium → Disease resistance
""",

    "water": """
💧 Irrigation Tips

Water early morning or evening.

Avoid overwatering to prevent root diseases.
"""
}


def show_chatbot():

    st.title("🤖 AI Farming Assistant")

    st.caption(
        "Ask questions related to farming, crops, fertilizers, or irrigation."
    )

    question = st.text_input(
        "Ask your question..."
    )

    if st.button("Ask AI"):

        if question == "":
            st.warning("Please enter a question.")
            return

        query = question.lower()

        answer = None

        for key in responses:

            if key in query:
                answer = responses[key]
                break

        if answer:

            st.success(answer)

        else:

            st.info(
                """
I don't know the answer yet.

Gemini AI integration is currently unavailable.
Future versions will provide AI-generated responses.
"""
            )