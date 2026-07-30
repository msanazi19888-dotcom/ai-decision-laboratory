from pathlib import Path

# ==========================
# Project Paths
# ==========================

AI_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = AI_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
SYNTHETIC_DATA_DIR = DATA_DIR / "synthetic"

# ==========================
# Dataset Configuration
# ==========================

DATASET_SIZE = 100_000

# ==========================
# Business Configuration
# ==========================

NUM_PRODUCTS = 500
NUM_SUPPLIERS = 40
NUM_WAREHOUSES = 5

# ==========================
# Random Seed
# ==========================

RANDOM_SEED = 42

# ==========================
# Product Categories
# ==========================

PRODUCT_CATEGORIES = [
    "Electronics",
    "Grocery",
    "Clothing",
    "Furniture",
    "Pharmacy",
    "Sports",
    "Books",
    "Office Supplies",
]
