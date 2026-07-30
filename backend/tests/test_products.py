from ai.generators.products import ProductGenerator


def test_generate_products():
    generator = ProductGenerator()

    products = generator.generate_products()

    assert len(products) > 0

    first = products[0]

    assert "product_id" in first
    assert "product_name" in first
    assert "category" in first
    assert "unit_cost" in first
    assert "selling_price" in first
    assert "safety_stock" in first