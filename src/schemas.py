
from pydantic import BaseModel, Field


class FlowerInput(BaseModel):
    sepal_length: float = Field(gt=0, le=10)
    sepal_width: float = Field(gt=0, le=10)
    petal_length: float = Field(gt=0, le=10)
    petal_width: float = Field(gt=0, le=10)


class PredictionOutput(BaseModel):
    predicted_class: int = Field(ge=0, le=2)
    predicted_species: str
