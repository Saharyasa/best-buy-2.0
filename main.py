from products import Product, NonStockedProduct, LimitedProduct, SecondHalfPrice, PercentDiscount, ThirdOneFree
from store import Store


def start(store_obj):
    """
    Provides an interactive menu for the user to interact with the store.

    :param store_obj: The store instance.
    """
    while True:
        print("\n==== Best Buy Store ====")
        print("1. List all products")
        print("2. Show total stock quantity")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # List all available products
            print("\nAvailable Products:")
            for product in store_obj.get_all_products():
                print(product.show())

        elif choice == "2":
            # Show total quantity of all products in the store
            print(f"\nTotal stock quantity: {store_obj.get_total_quantity()}")

        elif choice == "3":
            # Make an order by selecting a product and quantity
            try:
                product_name = input("Enter product name: ")
                quantity = int(input("Enter quantity: "))

                # Find the product using the new method
                product = store_obj.get_product_by_name(product_name)

                if product:
                    total_cost = store_obj.order([(product, quantity)])
                    print(f"✅ Order successful! Total cost: ${total_cost:.2f}")
                else:
                    print("❌ Product not found! Try again.")

            except ValueError as e:
                print(f"⚠️ Error: {e}")

        elif choice == "4":
            # Exit the program
            print("👋 Exiting... Thank you for shopping at Best Buy!")
            break

        else:
            print("❌ Invalid choice! Please enter a number between 1 and 4.")


def main():
    # Setup initial stock of inventory
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=50),
        Product("Google Pixel 7", price=500, quantity=25),
        NonStockedProduct("Windows License", price=120),
        LimitedProduct("Shipping", price=10, quantity=1, max_purchase=1)
    ]

    # Create promotion catalog
    second_half_price = SecondHalfPrice("Second Half price!")
    third_one_free = ThirdOneFree("Third One Free!")
    thirty_percent = PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[2].set_promotion(third_one_free)
    product_list[1].set_promotion(thirty_percent)

    best_buy = Store(product_list)

    start(best_buy)

    # List all products in the store
    print("\n📦 Available Products:")
    for product in best_buy.get_all_products():
        print(product.show())


if __name__ == "__main__":
    main()