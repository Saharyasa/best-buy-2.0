import pytest
from products import Product, NonStockedProduct, LimitedProduct

def test_non_stocked_product():
    product = NonStockedProduct("Microsoft Windows License", 150)
    assert product.get_promotion() is None  # No promotion applied
    assert product.buy(3) == 450  # No stock restrictions
    assert product.show() == "Microsoft Windows License, Price: 150 (Non-stocked product)"

def test_limited_product():
    product = LimitedProduct("Shipping Fee", 5, quantity=10, max_purchase=2)
    assert product.quantity == 10
    assert product.buy(2) == 10  # Allowed
    with pytest.raises(ValueError):
        product.buy(3)  # Exceeds max purchase limit

    assert product.show() == "Shipping Fee, Price: 5, Quantity: 8, Max Purchase: 2"
