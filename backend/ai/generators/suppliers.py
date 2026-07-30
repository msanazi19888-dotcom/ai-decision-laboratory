import random
from typing import Dict, List

from ai.config.settings import (
    PRODUCT_CATEGORIES,
    RANDOM_SEED,
)

from ai.config.supplier_catalog import (
    SUPPLIER_CATALOG,
    COUNTRIES,
)


class SupplierGenerator:
    """Generates realistic supplier data."""

    def __init__(self):
        self.random = random.Random(RANDOM_SEED)

    def generate_supplier(
        self,
        supplier_number: int,
        category: str,
    ) -> Dict[str, object]:

        supplier_name = self.random.choice(
            SUPPLIER_CATALOG[category]
        )

        return {
            "supplier_id": f"S{supplier_number:05d}",
            "supplier_name": supplier_name,
            "category": category,
            "country": self.random.choice(COUNTRIES),
            "lead_time_days": self.random.randint(2, 21),
            "reliability": round(
                self.random.uniform(0.85, 0.99),
                2,
            ),
        }

    def generate_suppliers(self) -> List[Dict[str, object]]:

        suppliers = []

        supplier_number = 1

        for category in PRODUCT_CATEGORIES:

            for _ in SUPPLIER_CATALOG[category]:

                suppliers.append(
                    self.generate_supplier(
                        supplier_number,
                        category,
                    )
                )

                supplier_number += 1

        return suppliers


if __name__ == "__main__":

    generator = SupplierGenerator()

    suppliers = generator.generate_suppliers()

    print(f"Generated {len(suppliers)} suppliers\n")

    for supplier in suppliers:
        print(supplier)