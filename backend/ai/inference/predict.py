from __future__ import annotations

from pathlib import Path
from typing import Any

import joblib


class DemandPredictor:
    def __init__(self) -> None:
        self.model_path = (
            Path(__file__).resolve().parents[1]
            / "data"
            / "synthetic"
            / "demand_model.pkl"
        )
        self.model = None

        if self.model_path.exists():
            try:
                self.model = joblib.load(self.model_path)
            except Exception:
                self.model = None

    def _build_features(self, payload: dict[str, Any]) -> list[list[float]]:
        return [[
            float(payload.get("day_of_week", 0)),
            float(payload.get("day", 0)),
            float(payload.get("month", 0)),
            float(payload.get("week_of_year", 0)),
            float(payload.get("is_weekend", 0)),
            float(payload.get("rolling_7_day_avg", 0)),
            float(payload.get("rolling_30_day_avg", 0)),
        ]]

    def _fallback_prediction(self, payload: dict[str, Any]) -> float:
        r7 = float(payload.get("rolling_7_day_avg", 0))
        r30 = float(payload.get("rolling_30_day_avg", 0))
        weekend = 8 if int(payload.get("is_weekend", 0)) else 0
        month = int(payload.get("month", 0))
        seasonal_boost = 4 if month in (11, 12, 1) else 0

        prediction = (0.6 * r7) + (0.3 * r30) + weekend + seasonal_boost
        return round(max(prediction, 1.0), 2)

    def predict(self, payload: dict[str, Any]) -> float:
        if self.model is None:
            return self._fallback_prediction(payload)

        features = self._build_features(payload)
        prediction = self.model.predict(features)[0]
        return round(float(prediction), 2)