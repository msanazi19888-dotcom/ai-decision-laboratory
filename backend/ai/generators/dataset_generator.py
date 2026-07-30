from pathlib import Path

import pandas as pd

from ai.config.settings import SYNTHETIC_DATA_DIR
from ai.generators.inventory import InventoryGenerator
from ai.generators.products import ProductGenerator
from ai.generators.sales import SalesGenerator
from ai.generators.suppliers import SupplierGenerator


class DatasetGenerator:
    """Generates and saves synthetic datasets."""

    def __init__(self) -> None:
        self.product_generator = ProductGenerator()
        self.supplier_generator = SupplierGenerator()
        self.inventory_generator = InventoryGenerator()
        self.sales_generator = SalesGenerator()

    # -----------------------------
    # Products
    # -----------------------------
    def generate_products_dataframe(self) -> pd.DataFrame:
        products = self.product_generator.generate_products()
        return pd.DataFrame(products)

    def save_products_dataset(self) -> Path:
        df = self.generate_products_dataframe()

        output_path = SYNTHETIC_DATA_DIR / "products.csv"
        output_path.parent.mkdir(parents=True, exist_ok=True)

        df.to_csv(output_path, index=False)
        return output_path

    # -----------------------------
    # Suppliers
    # -----------------------------
    def generate_suppliers_dataframe(self) -> pd.DataFrame:
        suppliers = self.supplier_generator.generate_suppliers()
        return pd.DataFrame(suppliers)

    def save_suppliers_dataset(self) -> Path:
        df = self.generate_suppliers_dataframe()

        output_path = SYNTHETIC_DATA_DIR / "suppliers.csv"
        output_path.parent.mkdir(parents=True, exist_ok=True)

        df.to_csv(output_path, index=False)
        return output_path

    # -----------------------------
    # Inventory
    # -----------------------------
    def generate_inventory_dataframe(self) -> pd.DataFrame:
        inventory = self.inventory_generator.generate_inventory()
        return pd.DataFrame(inventory)

    def save_inventory_dataset(self) -> Path:
        df = self.generate_inventory_dataframe()

        output_path = SYNTHETIC_DATA_DIR / "inventory.csv"
        output_path.parent.mkdir(parents=True, exist_ok=True)

        df.to_csv(output_path, index=False)
        return output_path

    # -----------------------------
    # Sales
    # -----------------------------
    def generate_sales_dataframe(self) -> pd.DataFrame:
        sales = self.sales_generator.generate_sales()
        return pd.DataFrame(sales)

    def save_sales_dataset(self) -> Path:
        df = self.generate_sales_dataframe()

        output_path = SYNTHETIC_DATA_DIR / "sales.csv"
        output_path.parent.mkdir(parents=True, exist_ok=True)

        df.to_csv(output_path, index=False)
        return output_path

    # -----------------------------
    # Generate Everything
    # -----------------------------
    def generate_all(self) -> None:
        products_path = self.save_products_dataset()
        suppliers_path = self.save_suppliers_dataset()
        inventory_path = self.save_inventory_dataset()
        sales_path = self.save_sales_dataset()

        print(f"✅ Products dataset saved to: {products_path}")
        print(f"✅ Suppliers dataset saved to: {suppliers_path}")
        print(f"✅ Inventory dataset saved to: {inventory_path}")
        print(f"✅ Sales dataset saved to: {sales_path}")


if __name__ == "__main__":
    DatasetGenerator().generate_all()