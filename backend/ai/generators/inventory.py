import random
from typing import Dict, List

from ai.config.settings import RANDOM_SEED
from ai.generators.products import ProductGenerator
from ai.generators.suppliers import SupplierGenerator


WAREHOUSES = [
    "WH-01",
    "WH-02",
    "WH-03",
    "WH-04",
    "WH-05",
]


class InventoryGenerator:
    """Generates inventory records."""

    def __init__(self) -> None:
        self.random = random.Random(RANDOM_SEED)

        self.products = ProductGenerator().generate_products()
        self.suppliers = SupplierGenerator().generate_suppliers()

    def _find_supplier(self, category: str) -> Dict:
        candidates = [
            supplier
            for supplier in self.suppliers
            if supplier["category"] == category
        ]

        return self.random.choice(candidates)

    def generate_inventory(self) -> List[Dict]:

        inventory = []

        for index, product in enumerate(self.products, start=1):

            supplier = self._find_supplier(product["category"])

            reorder_point = product["safety_stock"]

            current_stock = self.random.randint(
                reorder_point,
                reorder_point * 4,
            )

            max_stock = reorder_point * 6

            inventory.append(
                {
                    "inventory_id": f"INV{index:06d}",
                    "product_id": product["product_id"],
                    "product_name": product["product_name"],
                    "category": product["category"],
                    "supplier_id": supplier["supplier_id"],
                    "supplier_name": supplier["supplier_name"],
                    "warehouse": self.random.choice(WAREHOUSES),
                    "current_stock": current_stock,
                    "reorder_point": reorder_point,
                    "max_stock": max_stock,
                }
            )

        return inventory


if __name__ == "__main__":

    generator = InventoryGenerator()

    inventory = generator.generate_inventory()

    print(f"Generated {len(inventory)} inventory records\n")

    for item in inventory[:5]:
        print(item)