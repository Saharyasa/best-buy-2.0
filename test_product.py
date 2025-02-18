import pytest
import sys
import os

# Add the parent directory of 'test_product.py' to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from products import Product

# Test that creating a normal product works
def test_creating_product():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.is_active() is True

# Test that creating a product with invalid details (empty name, negative price) raises an exception
def test_creating_product_invalid_details():
    with pytest.raises(ValueError, match="Product name cannot be empty."):
        Product("", price=1450, quantity=100)

    with pytest.raises(ValueError, match="Price cannot be negative."):
        Product("MacBook Air M2", price=-10, quantity=100)

    with pytest.raises(ValueError, match="Quantity cannot be negative."):
        Product("MacBook Air M2", price=1450, quantity=-5)

# Test that when a product reaches 0 quantity, it becomes inactive
def test_product_becomes_inactive():
    product = Product("Bose Earbuds", price=250, quantity=1)
    product.buy(1)  # Buying all stock
    assert product.is_active() is False

# Test that product purchase modifies the quantity and returns the right total cost
def test_buy_modifies_quantity():
    product = Product("Google Pixel 7", price=500, quantity=10)
    total_cost = product.buy(2)
    
    assert total_cost == 1000  # 2 * 500
    assert product.quantity == 8  # 10 - 2

# Test that buying more than available quantity raises an exception
def test_buy_too_much():
    product = Product("PS5", price=600, quantity=5)
    
    with pytest.raises(ValueError, match="Not enough stock available."):
        product.buy(10)
