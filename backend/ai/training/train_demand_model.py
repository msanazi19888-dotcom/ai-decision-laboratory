from pathlib import Path

import joblib
import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

from ai.config.settings import SYNTHETIC_DATA_DIR


class DemandModelTrainer:
    """Train a demand forecasting model."""

    def __init__(self) -> None:
        self.dataset_path = SYNTHETIC_DATA_DIR / "sales_features.csv"
        self.model_path = SYNTHETIC_DATA_DIR / "demand_model.pkl"

    def load_dataset(self) -> pd.DataFrame:
        return pd.read_csv(self.dataset_path)

    def train(self) -> None:
        df = self.load_dataset()

        feature_columns = [
            "day_of_week",
            "day",
            "month",
            "year",
            "week_of_year",
            "is_weekend",
            "rolling_7_day_avg",
            "rolling_30_day_avg",
        ]

        X = df[feature_columns]
        y = df["future_quantity"]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42,
            shuffle=True,
        )

        model = RandomForestRegressor(
            n_estimators=100,
            random_state=42,
            n_jobs=-1,
        )

        model.fit(X_train, y_train)

        predictions = model.predict(X_test)

        mae = mean_absolute_error(y_test, predictions)
        rmse = mean_squared_error(y_test, predictions) ** 0.5
        r2 = r2_score(y_test, predictions)

        joblib.dump(model, self.model_path)

        print("\nModel Training Complete\n")
        print(f"MAE : {mae:.2f}")
        print(f"RMSE: {rmse:.2f}")
        print(f"R²  : {r2:.4f}")
        print(f"\nModel saved to:\n{self.model_path}")


if __name__ == "__main__":
    trainer = DemandModelTrainer()
    trainer.train()