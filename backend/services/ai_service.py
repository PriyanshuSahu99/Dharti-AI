import google.generativeai as genai
from utils.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(
    "gemini-2.0-flash"
)


def explain_crop_recommendation(
    crop,
    confidence,
    temperature,
    humidity,
    rainfall,
    ph
):
    try:

        prompt = f"""
You are an agricultural expert.

Crop: {crop}
Confidence: {confidence}%

Temperature: {temperature}
Humidity: {humidity}
Rainfall: {rainfall}
pH: {ph}

Explain why this crop is suitable.
"""

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        print("GEMINI ERROR:", str(e))
        raise e