
from fastapi import APIRouter, Request

router = APIRouter(tags=["Health"])


@router.get("/health")
def health_check(request: Request):
    model_loaded = getattr(request.app.state, "model", None) is not None

    return {
        "status": "ok" if model_loaded else "error",
        "model_loaded": model_loaded
    }
