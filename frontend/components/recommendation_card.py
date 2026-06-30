import streamlit as st


def recommendation_card(crop):
    """
    Displays a beautiful crop recommendation card.
    """

    confidence = float(crop["confidence"])

    st.markdown("---")

    st.subheader(f"🌾 {crop['crop']}")

    st.progress(confidence / 100)

    st.metric(
        "🎯 Confidence",
        f"{confidence:.1f}%"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.info(
            f"""
🌍 **Climate Score**

**{crop['climate_score']}/100**
"""
        )

        st.info(
            f"""
💧 **Water Requirement**

**{crop['water_requirement']}**
"""
        )

    with col2:

        st.info(
            f"""
📅 **Season**

**{crop['season']}**
"""
        )

        st.info(
            f"""
💰 **Expected Profit**

**{crop['expected_profit']}**
"""
        )

    st.success(
        f"📝 {crop['description']}"
    )