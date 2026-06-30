from fastapi import FastAPI
from app.schemas import PredictionRequest, PredictionResponse
from app.model import predict_risk

app = FastAPI(title="Customer Risk API")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):

    risk, score = predict_risk(
        request.age,
        request.salary
    )

    return PredictionResponse(
        risk=risk,
        score=score
    )