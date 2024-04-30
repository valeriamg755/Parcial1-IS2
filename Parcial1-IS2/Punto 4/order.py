class Order:
    def __init__(self, user):
        self.user = user
        self.products = user.cart
        self.total = sum(product.price for product in self.products)

    def checkout(self):
        # Here you would implement payment processing logic
        print(f"Total amount to be paid: ${self.total}")
        print("Payment processed successfully.")
        self.user.cart = []  # Empty the cart after successful checkout