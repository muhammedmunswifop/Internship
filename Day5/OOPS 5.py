"""5. Shopping Cart System"""

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(product.name, "added to cart.")

    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                print(product_name, "removed from cart.")
                return
        print(product_name, "not found in cart.")

    def calculate_total(self):
        total = sum(product.price for product in self.products)
        return total

    def display_cart(self):
        print("\nProducts in Cart:")
        for product in self.products:
            print(f"{product.name} - ₹{product.price}")
        print("Total = ₹", self.calculate_total())


p1 = Product("Laptop", 50000)
p2 = Product("Mouse", 1000)

cart = Cart()

cart.add_product(p1)
cart.add_product(p2)

cart.display_cart()