from fastapi import FastAPI
from pydantic import BaseModel

from optimizer import generate_recommendation


app = FastAPI(
    title="AI Cloud Infrastructure Optimizer",
    description=(
        "ML-powered infrastructure monitoring "
        "and optimization API."
    ),
    version="1.0.0"
)


class InfrastructureMetrics(BaseModel):

    cpu_usage: float
    memory_usage: float
    latency: float


@app.get("/")
def home():

    return {
        "status": "online",
        "service": "AI Cloud Infrastructure Optimizer"
    }


@app.post("/recommend")
def recommend(
    metrics: InfrastructureMetrics
):

    result = generate_recommendation(
        metrics.cpu_usage,
        metrics.memory_usage,
        metrics.latency
    )

    return result
