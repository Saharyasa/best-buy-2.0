class Product:
    def __init__(self, name: str, price: float, quantity: int):
        """
        Initializes a Product with a name, price, and quantity.

        :param name: Name of the product.
        :param price: Price of the product.
        :param quantity: Available quantity.
        :raises ValueError: If the name is empty or price/quantity is negative.
        """
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
        """
        Returns the available quantity of the product as a float.
        """
        return float(self.quantity)

    def set_quantity(self, quantity: int):
        """
        Updates the product's quantity. If quantity reaches 0, the product is deactivated.

        :param quantity: New quantity value.
        :raises ValueError: If the quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """
        Returns whether the product is active or not.
        """
        return self.active

    def activate(self):
        """
        Activates the product.
        """
        self.active = True

    def deactivate(self):
        """
        Deactivates the product (sets it to inactive).
        """
        self.active = False

    def show(self) -> str:
        """
        Returns a formatted string representation of the product.
        """
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def __repr__(self):
        return self.show()

    def buy(self, quantity: int) -> float:
        """
        Processes a purchase of the product.

        :param quantity: Number of units to buy.
        :return: Total price for the purchase.
        :raises ValueError: If the quantity is not greater than 0 or exceeds available stock.
        """
        if quantity <= 0:
            raise ValueError("Quantity to buy must be greater than 0.")
        if quantity > self.quantity:
            raise ValueError("Not enough stock available.")

        total_price = self.price * quantity
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()

        return total_price
