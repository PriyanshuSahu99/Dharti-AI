import os
import joblib
import pandas as pd

from data.crop_info import CROP_INFO

# ----------------------------------------------------
# Load Trained Model
# ----------------------------------------------------

BASE_DIR = os.path.dirname(__file__)

MODEL_PATH = os.path.abspath(
    os.path.join(
        BASE_DIR,
        "..",
        "models",
        "crop_model.pkl"
    )
)

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(
        f"Model not found at: {MODEL_PATH}"
    )

model = joblib.load(MODEL_PATH)


# ----------------------------------------------------
# Default Crop Information
# ----------------------------------------------------

DEFAULT_INFO = {
    "season": "Information Coming Soon",
    "water_requirement": "Unknown",
    "climate_score": 80,
    "expected_profit": "Not Available",
    "description": "Crop information will be added in future updates."
}


# ----------------------------------------------------
# Crop Recommendation Function
# ----------------------------------------------------

def recommend_crop(data: dict):

    # Convert input to DataFrame
    input_df = pd.DataFrame([data])

    # Predict probabilities
    probabilities = model.predict_proba(input_df)[0]

    # Crop names
    classes = model.classes_

    # Top 3 recommendations
    top_predictions = sorted(
        zip(classes, probabilities),
        key=lambda x: x[1],
        reverse=True
    )[:3]

    recommendations = []

    for crop, probability in top_predictions:

        # Get crop information
        info = CROP_INFO.get(
            crop.lower(),
            DEFAULT_INFO
        )

        recommendations.append(
            {
                "crop": crop.title(),
                "confidence": round(probability * 100, 2),

                "season": info["season"],

                "water_requirement": info["water_requirement"],

                "climate_score": info["climate_score"],

                "expected_profit": info["expected_profit"],

                "description": info["description"]
            }
        )

    return recommendations