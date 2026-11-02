
from fastapi import APIRouter, HTTPException, Request

from src.schemas import FlowerInput, PredictionOutput
from src.services import predict_species

router = APIRouter(tags=["Predictions"])


@router.post("/predict", response_model=PredictionOutput)
def predict(flower: FlowerInput, request: Request):
    model = getattr(request.app.state, "model", None)

    if model is None:
        raise HTTPException(
            status_code=503,
            detail="Modelo não está disponível."
        )

    try:
        return predict_species(
            model,
            flower.model_dump()
        )
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail="Não foi possível gerar a previsão."
        ) from exc
