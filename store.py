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
