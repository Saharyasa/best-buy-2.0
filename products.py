from abc import ABC, abstractmethod

class Promotion(ABC):
    """Abstract base class for all promotions"""
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        """Apply promotion and return the discounted price"""
        pass

class PercentDiscount(Promotion):
    """Applies a percentage discount to the total price"""
    def __init__(self, name: str, percent: float):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity) -> float:
        discount = (self.percent / 100) * (product.price * quantity)
        return (product.price * quantity) - discount

class SecondHalfPrice(Promotion):
    """Buy one, get the second item at half price"""
    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product, quantity) -> float:
        full_price_items = quantity // 2 + quantity % 2
        half_price_items = quantity // 2
        return (full_price_items * product.price) + (half_price_items * product.price * 0.5)

class ThirdOneFree(Promotion):
    """Buy 2, get 1 free"""
    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product, quantity) -> float:
        payable_items = quantity - (quantity // 3)
        return payable_items * product.price

class Product:
    """Represents a product in the store"""
    def __init__(self, name: str, price: float, quantity: int):
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid product attributes")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.promotion = None  # New promotion attribute

    def set_promotion(self, promotion: Promotion):
        """Assigns a promotion to the product"""
        self.promotion = promotion

    def get_promotion(self):
        """Returns the current promotion of the product"""
        return self.promotion

    def is_active(self) -> bool:
        """Returns True if the product is available (quantity > 0)"""
        return self.quantity > 0

    def buy(self, quantity: int) -> float:
        """Handles product purchase with promotions"""
        if quantity > self.quantity:
            raise ValueError("Not enough stock available")
        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity
        self.quantity -= quantity
        return total_price

    def show(self):
        """Displays product details"""
        promo_text = f" (Promotion: {self.promotion.name})" if self.promotion else ""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}{promo_text}"

class NonStockedProduct(Product):
    """Represents a digital product or service with unlimited quantity"""
    def __init__(self, name: str, price: float):
        super().__init__(name, price, quantity=0)

    def is_active(self) -> bool:
        """Non-stocked products are always active"""
        return True

    def buy(self, quantity: int) -> float:
        """Allows unlimited purchase since it's not a physical product"""
        return self.price * quantity

    def show(self):
        return f"{self.name}, Price: {self.price} (Non-stocked product)"

class LimitedProduct(Product):
    """Represents a product with a max purchase limit per order"""
    def __init__(self, name: str, price: float, quantity: int, max_purchase: int):
        super().__init__(name, price, quantity)
        self.max_purchase = max_purchase

    def buy(self, quantity: int) -> float:
        """Restricts purchase to the max limit per order"""
        if quantity > self.max_purchase:
            raise ValueError("Cannot buy more than allowed quantity per order")
        return super().buy(quantity)

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Max Purchase: {self.max_purchase}"
