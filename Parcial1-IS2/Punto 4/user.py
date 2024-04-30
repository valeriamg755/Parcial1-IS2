class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.cart = []

    def add_to_cart(self, product):
        self.cart.append(product)

    def remove_from_cart(self, product):
        if product in self.cart:
            self.cart.remove(product)

    def view_cart(self):
        for product in self.cart:
            print(product.name, product.price)