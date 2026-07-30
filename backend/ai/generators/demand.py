from datetime import datetime
import random

from ai.config.settings import RANDOM_SEED
from ai.config.demand_catalog import (
    PROMOTION_MULTIPLIER,
    PROMOTION_PROBABILITY,
    SEASON_MULTIPLIERS,
    WEEKDAY_MULTIPLIERS,
)


class DemandGenerator:
    """Adjusts daily demand based on business factors."""

    def __init__(self):
        self.random = random.Random(RANDOM_SEED)

    def _season(self, date: datetime) -> str:

        month = date.month

        if month in (12, 1, 2):
            return "Winter"

        if month in (3, 4, 5):
            return "Spring"

        if month in (6, 7, 8):
            return "Summer"

        return "Autumn"

    def adjust_quantity(
        self,
        quantity: int,
        date: datetime,
    ) -> int:

        result = quantity

        season = self._season(date)
        result *= SEASON_MULTIPLIERS[season]

        weekday = date.weekday()
        result *= WEEKDAY_MULTIPLIERS[weekday]

        promotion = False

        if self.random.random() < PROMOTION_PROBABILITY:
            result *= PROMOTION_MULTIPLIER
            promotion = True

        return max(0, round(result)), promotion