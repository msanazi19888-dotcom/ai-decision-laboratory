from fastapi import APIRouter
from pydantic import BaseModel, Field

from ai.inference.predict import DemandPredictor

router = APIRouter(prefix="/api/v2", tags=["prediction"])

predictor = DemandPredictor()


class DemandPredictionRequest(BaseModel):
    day_of_week: int = Field(..., ge=0, le=6)
    day: int = Field(..., ge=1, le=31)
    month: int = Field(..., ge=1, le=12)
    year: int = Field(..., ge=2000, le=2100)
    week_of_year: int = Field(..., ge=1, le=53)
    is_weekend: int = Field(..., ge=0, le=1)
    rolling_7_day_avg: float = Field(..., ge=0)
    rolling_30_day_avg: float = Field(..., ge=0)


class DemandPredictionResponse(BaseModel):
    predicted_demand: float


@router.post("/predict-demand", response_model=DemandPredictionResponse)
def predict_demand(payload: DemandPredictionRequest):
    prediction = predictor.predict(
        day_of_week=payload.day_of_week,
        day=payload.day,
        month=payload.month,
        year=payload.year,
        week_of_year=payload.week_of_year,
        is_weekend=payload.is_weekend,
        rolling_7_day_avg=payload.rolling_7_day_avg,
        rolling_30_day_avg=payload.rolling_30_day_avg,
    )

    return DemandPredictionResponse(predicted_demand=prediction)