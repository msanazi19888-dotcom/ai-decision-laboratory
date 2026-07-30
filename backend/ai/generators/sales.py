from datetime import date, timedelta
import random
from typing import Dict, List

from ai.config.settings import RANDOM_SEED
from ai.config.sales_catalog import CATEGORY_DAILY_SALES
from ai.generators.products import ProductGenerator


class SalesGenerator:
    """Generates daily sales history for products."""

    def __init__(self) -> None:
        self.random = random.Random(RANDOM_SEED)
        self.products = ProductGenerator().generate_products()

    def _daily_sales(self, category: str) -> int:
        minimum, maximum = CATEGORY_DAILY_SALES[category]
        return self.random.randint(minimum, maximum)

    def generate_sales(
        self,
        number_of_days: int = 365,
    ) -> List[Dict]:

        sales = []

        start_date = date(2025, 1, 1)

        sale_id = 1

        for product in self.products:

            for day in range(number_of_days):

                current_date = start_date + timedelta(days=day)

                quantity = self._daily_sales(
                    product["category"]
                )

                sales.append(
                    {
                        "sale_id": f"SALE{sale_id:07d}",
                        "date": current_date.isoformat(),
                        "product_id": product["product_id"],
                        "product_name": product["product_name"],
                        "category": product["category"],
                        "quantity_sold": quantity,
                    }
                )

                sale_id += 1

        return sales


if __name__ == "__main__":

    generator = SalesGenerator()

    sales = generator.generate_sales()

    print(f"Generated {len(sales)} sales records\n")

    for row in sales[:10]:
        print(row)