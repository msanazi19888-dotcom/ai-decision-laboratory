from __future__ import annotations

from typing import Any


class DemandPredictor:
    def _fallback_prediction(self, payload: dict[str, Any]) -> float:
        r7 = float(payload.get("rolling_7_day_avg", 0))
        r30 = float(payload.get("rolling_30_day_avg", 0))
        weekend = 8 if int(payload.get("is_weekend", 0)) else 0
        month = int(payload.get("month", 0))
        seasonal_boost = 4 if month in (11, 12, 1) else 0

        prediction = (0.6 * r7) + (0.3 * r30) + weekend + seasonal_boost
        return round(max(prediction, 1.0), 2)

    def predict(self, payload: dict[str, Any]) -> float:
        return self._fallback_prediction(payload)