from fastapi import APIRouter

from schemas import CropInput
from services.crop_service import recommend_crop
from services.climate_service import calculate_climate_score

router = APIRouter(
    prefix="/api/crop",
    tags=["Crop Recommendation"]
)


@router.post("/recommend")
def recommend(data: CropInput):

    # Crop Recommendation
    recommendations = recommend_crop(
        data.model_dump()
    )

    # Climate Score
    climate = calculate_climate_score(
        data.temperature,
        data.humidity,
        data.rainfall
    )

    # Response
    return {
        "recommendations": recommendations,
        "climate": climate
    }