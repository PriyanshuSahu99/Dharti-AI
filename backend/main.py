from fastapi import FastAPI

from routes.crop import router as crop_router
from routes.weather import router as weather_router
from routes.ai import router as ai_router
from routes.market import router as market_router

app = FastAPI(
    title="Dharti AI",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "status": "Running",
        "project": "Dharti AI"
    }


app.include_router(crop_router)
app.include_router(weather_router)
app.include_router(ai_router)
app.include_router(market_router)