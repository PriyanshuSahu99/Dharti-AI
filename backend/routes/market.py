from fastapi import APIRouter

router = APIRouter(
    prefix="/api/market",
    tags=["Market Intelligence"]
)

market_data = [
    {
        "crop": "Rice",
        "price": "₹2,450 / Quintal",
        "market": "Delhi Mandi",
        "trend": "📈 Rising",
        "profit": "High"
    },
    {
        "crop": "Wheat",
        "price": "₹2,180 / Quintal",
        "market": "Punjab Mandi",
        "trend": "📉 Falling",
        "profit": "Medium"
    },
    {
        "crop": "Cotton",
        "price": "₹6,900 / Quintal",
        "market": "Gujarat Market",
        "trend": "📈 Rising",
        "profit": "Very High"
    },
    {
        "crop": "Maize",
        "price": "₹2,050 / Quintal",
        "market": "MP Market",
        "trend": "➡ Stable",
        "profit": "Good"
    }
]


@router.get("/")
def get_market_data():
    return market_data