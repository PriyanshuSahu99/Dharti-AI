from fastapi import APIRouter

from services.ai_service import explain_crop_recommendation

router = APIRouter(
    prefix="/api/ai",
    tags=["AI"]
)


@router.post("/explain")
def explain(data: dict):

    try:

        result = explain_crop_recommendation(
            crop=data["crop"],
            confidence=data["confidence"],
            temperature=data["temperature"],
            humidity=data["humidity"],
            rainfall=data["rainfall"],
            ph=data["ph"]
        )

        return {
            "explanation": result
        }

    except Exception as e:

        return {
            "error": str(e)
        }