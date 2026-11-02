
from fastapi.testclient import TestClient

from src.main import app


def test_health_check():
    """Verifica se a API está funcionando e se o modelo foi carregado."""

    with TestClient(app) as client:
        response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "ok"
    assert data["model_loaded"] is True


def test_predict_setosa():
    """Verifica se a API classifica corretamente um exemplo de setosa."""

    flower = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2,
    }

    with TestClient(app) as client:
        response = client.post("/predict", json=flower)

    assert response.status_code == 200

    data = response.json()

    assert data["predicted_class"] == 0
    assert data["predicted_species"] == "setosa"


def test_predict_invalid_input():
    """Verifica se a API rejeita valores inválidos."""

    flower = {
        "sepal_length": -1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2,
    }

    with TestClient(app) as client:
        response = client.post("/predict", json=flower)

    assert response.status_code == 422
