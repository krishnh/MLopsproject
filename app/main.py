from fastapi import FastAPI
from app.schemas import PredictionRequest, PredictionResponse
from app.sagemaker_client import invoke_sagemaker

app = FastAPI(title="Customer Risk API")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):

    risk, score = invoke_sagemaker(
    age=request.age,
    salary=request.salary
    )

    return PredictionResponse(
        risk=risk,
        score=score
    )