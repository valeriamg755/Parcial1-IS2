
class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, name, quantity):
        if name in self.products:
            print("Product already exists in inventory. Updating quantity...")
            self.products[name] += quantity
        else:
            self.products[name] = quantity
            print("Product added to inventory.")

    def update_product(self, name, quantity):
        if name in self.products:
            self.products[name] = quantity
            print("Product quantity updated in inventory.")
        else:
            print("Product does not exist in inventory.")

    def remove_product(self, name):
        if name in self.products:
            del self.products[name]
            print("Product removed from inventory.")
        else:
            print("Product does not exist in inventory.")

    def generate_report(self):
        print("Inventory:")
        for product, quantity in self.products.items():
            print(f"{product}: {quantity}")

# Main function
def main():
    inventory = Inventory()

    while True:
        print("\n1. Add product\n2. Update product\n3. Remove product\n4. Generate report\n5. Exit")
        option = input("Select an option: ")

        if option == "1":
            name = input("Enter the product name: ")
            quantity = int(input("Enter the product quantity: "))
            inventory.add_product(name, quantity)
        elif option == "2":
            name = input("Enter the product name to update: ")
            quantity = int(input("Enter the new product quantity: "))
            inventory.update_product(name, quantity)
        elif option == "3":
            name = input("Enter the product name to remove: ")
            inventory.remove_product(name)
        elif option == "4":
            inventory.generate_report()
        elif option == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid option. Please select a valid option.")

if __name__ == "__main__":
    main()
