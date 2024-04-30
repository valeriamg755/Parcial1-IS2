from product import Product
from user import User
from order import Order

class Main:
    def __init__(self):
        self.products = [
            Product("Laptop", 1000000),
            Product("Smartphone", 800000),
            Product("Headphones", 250000),
            Product("Mouse", 35000)
        ]
        self.users = []

    def register_user(self, username, email):
        new_user = User(username, email)
        self.users.append(new_user)
        return new_user

    def display_products(self):
        for product in self.products:
            print(product.name, product.price)


# Example:
if __name__ == "__main__":
    main_system = Main()

    # Display available products
    print("Available products:")
    main_system.display_products()

    # Register user
    user1 = main_system.register_user("Valeria", "valeria@example.com")
    print(f"User '{user1.username}' registered successfully.")

    # Add products to user's cart
    user1.add_to_cart(main_system.products[0])  # Adding Laptop to the cart
    user1.add_to_cart(main_system.products[2])  # Adding Headphones to the cart
    print("User's cart:")
    user1.view_cart()

    # Checkout
    order1 = Order(user1)
    order1.checkout()