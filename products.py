class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True  # By default, the product is active

    def get_quantity(self) -> float:
        return float(self.quantity)

    def is_active(self) -> bool:
        return self.active

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("Quantity to buy must be greater than 0.")
        if quantity > self.quantity:
            raise ValueError("Not enough stock available.")

        total_price = self.price * quantity
        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        return total_price


class NonStockedProduct(Product):
    """
    A product that does not track quantity (e.g., software license).
    The quantity is always zero.
    """
    def __init__(self, name: str, price: float):
        super().__init__(name, price, quantity=0)

    def get_quantity(self) -> float:
        return 0  # Non-stocked products always have zero quantity.

    def buy(self, quantity: int) -> float:
        return self.price * quantity  # No stock limitations.

    def show(self) -> str:
        return f"{self.name}, Price: {self.price} (Non-stocked product)"


class LimitedProduct(Product):
    """
    A product that has a maximum purchase limit per order.
    """
    def __init__(self, name: str, price: float, quantity: int, max_purchase: int):
        super().__init__(name, price, quantity)
        self.max_purchase = max_purchase

    def buy(self, quantity: int) -> float:
        if quantity > self.max_purchase:
            raise ValueError(f"Cannot purchase more than {self.max_purchase} per order.")

        return super().buy(quantity)

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Max Purchase: {self.max_purchase}"
