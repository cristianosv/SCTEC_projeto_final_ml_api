
from pathlib import Path

import joblib
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "model.joblib"

FEATURES = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)",
]

CLASS_NAMES = ["setosa", "versicolor", "virginica"]


def load_model():
    """Carrega o pipeline treinado e serializado."""
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Arquivo do modelo não encontrado: {MODEL_PATH}"
        )

    return joblib.load(MODEL_PATH)


def predict_species(model, flower_data: dict) -> dict:
    """Gera a previsão para uma flor."""
    input_data = pd.DataFrame(
        [[
            flower_data["sepal_length"],
            flower_data["sepal_width"],
            flower_data["petal_length"],
            flower_data["petal_width"],
        ]],
        columns=FEATURES,
    )

    predicted_class = int(model.predict(input_data)[0])

    return {
        "predicted_class": predicted_class,
        "predicted_species": CLASS_NAMES[predicted_class],
    }
