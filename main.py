from products import Product, NonStockedProduct, LimitedProduct
from store import Store

def main():
    # Setup initial stock of inventory
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=50),
        Product("Google Pixel 7", price=500, quantity=25),
        NonStockedProduct("Windows License", price=120),
        LimitedProduct("Shipping", price=10, quantity=1, max_purchase=1)
    ]

    best_buy = Store(product_list)

    # List all products in the store
    print("\n📦 Available Products:")
    for product in best_buy.get_all_products():
        print(product.show())

if __name__ == "__main__":
    main()
