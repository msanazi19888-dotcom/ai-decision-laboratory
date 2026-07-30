from pathlib import Path

import pandas as pd

from ai.config.settings import SYNTHETIC_DATA_DIR


class FeatureBuilder:
    """Build machine-learning features from sales history."""

    def __init__(self) -> None:
        self.sales_path = SYNTHETIC_DATA_DIR / "sales.csv"

    def load_sales(self) -> pd.DataFrame:
        """Load the generated sales dataset."""
        df = pd.read_csv(self.sales_path)
        df["date"] = pd.to_datetime(df["date"])
        return df

    def build(self) -> pd.DataFrame:
        """Create ML features and the forecasting target."""
        df = self.load_sales()

        # Calendar features
        df["day_of_week"] = df["date"].dt.dayofweek
        df["day"] = df["date"].dt.day
        df["month"] = df["date"].dt.month
        df["year"] = df["date"].dt.year
        df["week_of_year"] = df["date"].dt.isocalendar().week.astype(int)
        df["is_weekend"] = (df["day_of_week"] >= 5).astype(int)

        # Sort by product and time
        df = df.sort_values(["product_id", "date"]).reset_index(drop=True)

        # Rolling features
        df["rolling_7_day_avg"] = (
            df.groupby("product_id")["quantity_sold"]
            .transform(lambda x: x.rolling(window=7, min_periods=1).mean())
        )

        df["rolling_30_day_avg"] = (
            df.groupby("product_id")["quantity_sold"]
            .transform(lambda x: x.rolling(window=30, min_periods=1).mean())
        )

        # Forecast target: next day's sales
        df["future_quantity"] = (
            df.groupby("product_id")["quantity_sold"].shift(-1)
        )

        # Remove rows where target is missing
        df = df.dropna(subset=["future_quantity"]).reset_index(drop=True)

        return df

    def save(self) -> Path:
        """Save the engineered features to CSV."""
        df = self.build()

        output_path = SYNTHETIC_DATA_DIR / "sales_features.csv"
        output_path.parent.mkdir(parents=True, exist_ok=True)

        df.to_csv(output_path, index=False)
        return output_path


if __name__ == "__main__":
    builder = FeatureBuilder()
    output = builder.save()
    print(f"✅ Features dataset saved to: {output}")