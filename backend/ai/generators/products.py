import random
from typing import Dict, List

from ai.config.settings import (
    NUM_PRODUCTS,
    PRODUCT_CATEGORIES,
    RANDOM_SEED,
)

from ai.config.product_catalog import (
    CATEGORY_RULES,
    CATEGORY_NAMES,
    DEFAULT_RULES,
)


class ProductGenerator:
    """Generates realistic product data."""

    def __init__(self) -> None:
        self._rng = random.Random(RANDOM_SEED)

    def _choose_category(self) -> str:
        if not PRODUCT_CATEGORIES:
            raise ValueError("PRODUCT_CATEGORIES cannot be empty.")
        return self._rng.choice(PRODUCT_CATEGORIES)

    def _get_rules(self, category: str) -> Dict[str, tuple]:
        return CATEGORY_RULES.get(category, DEFAULT_RULES)

    def _choose_product_name(self, category: str, product_number: int) -> str:
        names = CATEGORY_NAMES.get(category, [f"{category} Item"])
        base_name = self._rng.choice(names)
        return f"{base_name} {product_number:03d}"

    def generate_product(self, product_number: int) -> Dict[str, object]:
        category = self._choose_category()
        rules = self._get_rules(category)

        unit_cost = round(self._rng.uniform(*rules["cost"]), 2)
        markup = self._rng.uniform(*rules["markup"])
        selling_price = round(unit_cost * markup, 2)
        safety_stock = self._rng.randint(*rules["safety_stock"])

        return {
            "product_id": f"P{product_number:05d}",
            "product_name": self._choose_product_name(category, product_number),
            "category": category,
            "unit_cost": unit_cost,
            "selling_price": selling_price,
            "safety_stock": safety_stock,
        }

    def generate_products(self) -> List[Dict[str, object]]:
        return [
            self.generate_product(product_number)
            for product_number in range(1, NUM_PRODUCTS + 1)
        ]


if __name__ == "__main__":
    generator = ProductGenerator()
    products = generator.generate_products()

    print(f"Generated {len(products)} products\n")

    for product in products[:5]:
        print(product)