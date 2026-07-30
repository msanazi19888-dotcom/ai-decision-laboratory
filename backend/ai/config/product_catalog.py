"""
Product Catalog Configuration

This module contains static business data used by the ProductGenerator.
It separates business configuration from generation logic.
"""

CATEGORY_RULES = {
    "Electronics": {
        "cost": (100, 1000),
        "markup": (1.2, 1.6),
        "safety_stock": (20, 60),
    },
    "Grocery": {
        "cost": (1, 20),
        "markup": (1.1, 1.4),
        "safety_stock": (100, 300),
    },
    "Clothing": {
        "cost": (15, 150),
        "markup": (1.5, 2.5),
        "safety_stock": (40, 120),
    },
    "Furniture": {
        "cost": (200, 3000),
        "markup": (1.3, 2.0),
        "safety_stock": (10, 40),
    },
    "Pharmacy": {
        "cost": (5, 100),
        "markup": (1.2, 1.8),
        "safety_stock": (50, 150),
    },
    "Sports": {
        "cost": (20, 500),
        "markup": (1.3, 2.0),
        "safety_stock": (20, 80),
    },
    "Books": {
        "cost": (5, 60),
        "markup": (1.4, 2.0),
        "safety_stock": (30, 120),
    },
    "Office Supplies": {
        "cost": (2, 80),
        "markup": (1.3, 1.8),
        "safety_stock": (50, 200),
    },
}

CATEGORY_NAMES = {
    "Electronics": [
        "Wireless Mouse",
        "Bluetooth Speaker",
        "USB-C Charger",
        "Laptop Stand",
        "Noise Cancelling Headphones",
        "Smart Watch",
    ],
    "Grocery": [
        "Basmati Rice",
        "Olive Oil",
        "Black Tea",
        "Pasta Pack",
        "Cereal Box",
        "Tomato Sauce",
    ],
    "Clothing": [
        "Cotton T-Shirt",
        "Denim Jeans",
        "Hoodie",
        "Running Shorts",
        "Winter Jacket",
        "Casual Shirt",
    ],
    "Furniture": [
        "Office Chair",
        "Wooden Desk",
        "Coffee Table",
        "Bookshelf",
        "Bed Frame",
        "Storage Cabinet",
    ],
    "Pharmacy": [
        "Vitamin C Tablets",
        "Pain Relief Gel",
        "Cough Syrup",
        "Antiseptic Spray",
        "Allergy Pills",
        "First Aid Kit",
    ],
    "Sports": [
        "Yoga Mat",
        "Dumbbell Set",
        "Football",
        "Tennis Racket",
        "Gym Gloves",
        "Water Bottle",
    ],
    "Books": [
        "Novel",
        "Notebook",
        "Programming Guide",
        "Business Book",
        "Children's Story",
        "Study Manual",
    ],
    "Office Supplies": [
        "Notebook Pack",
        "Ballpoint Pens",
        "Printer Paper",
        "Stapler",
        "Desk Organizer",
        "Sticky Notes",
    ],
}

DEFAULT_RULES = {
    "cost": (10, 100),
    "markup": (1.2, 2.0),
    "safety_stock": (20, 100),
}