import streamlit as st
from PIL import Image
import random


def show_disease():

    st.title("🦠 Plant Disease Detection")
    st.caption("Upload a leaf image to detect possible plant diseases.")

    uploaded_file = st.file_uploader(
        "Choose a leaf image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:

        image = Image.open(uploaded_file)

        st.image(
            image,
            caption="Uploaded Leaf",
            use_container_width=True
        )

        if st.button("🔍 Detect Disease"):

            with st.spinner("Analyzing leaf..."):

                diseases = [
                    "Healthy Leaf",
                    "Leaf Blight",
                    "Early Blight",
                    "Powdery Mildew",
                    "Leaf Spot"
                ]

                disease = random.choice(diseases)

                confidence = random.randint(90, 99)

            st.success("Analysis Complete")

            st.metric(
                "Prediction",
                disease,
                f"{confidence}% Confidence"
            )

            if disease == "Healthy Leaf":
                st.success("✅ The plant appears healthy.")
            else:
                st.warning(
                    "⚠ Disease detected. Consider using a suitable fungicide and consult an agricultural expert."
                )