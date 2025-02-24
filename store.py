from typing import List


class Store:
    """Represents a store containing multiple products"""

    def __init__(self, products=None):
        if products is None:
            products = []
        self.products = products

    def add_product(self, product):
        """Adds a new product to the store"""
        self.products.append(product)

    def remove_product(self, product):
        """Removes a product from the store"""
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Returns the total quantity of all active products"""
        return sum(product.quantity for product in self.products if product.is_active())

    def get_all_products(self):
        """Returns a list of all active products"""
        return [product for product in self.products if product.is_active()]

    def get_product_by_name(self, product_name: str):
        """
        Finds and returns a product by name.

        :param product_name: Name of the product.
        :return: The Product object if found, otherwise None.
        """
        return next((p for p in self.products if p.name == product_name), None)

    def order(self, shopping_list: List[tuple]) -> float:
        """
        Processes an order given a shopping list of (Product, quantity).

        :param shopping_list: List of tuples (Product, quantity).
        :return: Total cost of the order.
        :raises ValueError: If a product is not found.
        """
        total_cost = 0.0
        for product, quantity in shopping_list:
            if product not in self.products:
                raise ValueError("Product not found in store.")
            total_cost += product.buy(quantity)
        return total_cost