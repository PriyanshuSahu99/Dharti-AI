import os
from dotenv import load_dotenv

load_dotenv()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

print("Gemini Key Loaded:", GEMINI_API_KEY[:10] if GEMINI_API_KEY else "NONE")