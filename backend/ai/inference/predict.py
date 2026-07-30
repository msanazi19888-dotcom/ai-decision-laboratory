from pathlib import Path

import joblib
import pandas as pd

from ai.config.settings import SYNTHETIC_DATA_DIR


class DemandPredictor:
    """Load a trained demand model and make predictions."""

    def __init__(self) -> None:
        self.model_path = SYNTHETIC_DATA_DIR / "demand_model.pkl"
        self.model = joblib.load(self.model_path)

    def predict(
        self,
        *,
        day_of_week: int,
        day: int,
        month: int,
        year: int,
        week_of_year: int,
        is_weekend: int,
        rolling_7_day_avg: float,
        rolling_30_day_avg: float,
    ) -> float:
        features = pd.DataFrame(
            [
                {
                    "day_of_week": day_of_week,
                    "day": day,
                    "month": month,
                    "year": year,
                    "week_of_year": week_of_year,
                    "is_weekend": is_weekend,
                    "rolling_7_day_avg": rolling_7_day_avg,
                    "rolling_30_day_avg": rolling_30_day_avg,
                }
            ]
        )

        prediction = self.model.predict(features)
        return round(float(prediction[0]), 2)


if __name__ == "__main__":
    predictor = DemandPredictor()

    prediction = predictor.predict(
        day_of_week=4,
        day=15,
        month=7,
        year=2025,
        week_of_year=29,
        is_weekend=0,
        rolling_7_day_avg=72,
        rolling_30_day_avg=68,
    )

    print(f"\nPredicted demand: {prediction} units")