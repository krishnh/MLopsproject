from pydantic import BaseModel


class PredictionRequest(BaseModel):
    age: int
    salary: float


class PredictionResponse(BaseModel):
    risk: str
    score: float