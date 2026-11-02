
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.routers.health import router as health_router
from src.routers.predict import router as predict_router
from src.services import load_model


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Executado durante a inicialização
    app.state.model = load_model()

    try:
        yield
    finally:
        # Liberar a referência ao modelo durante o encerramento
        app.state.model = None


app = FastAPI(
    title="Iris Classification API",
    description=(
        "API para classificação de espécies de flores "
        "utilizando Machine Learning."
    ),
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(health_router)
app.include_router(predict_router)
