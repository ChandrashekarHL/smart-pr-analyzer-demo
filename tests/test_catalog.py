from shop.catalog import Product, by_sku


def test_by_sku_indexes_products():
    p = Product("A1", "Mug", 49_900)
    assert by_sku([p]) == {"A1": p}
