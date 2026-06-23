"""7. Inventory Management System"""
class Product:
    def __init__(self, name, stock):
        self.name = name
        self.__stock = stock  

    def add_stock(self, quantity):
        self.__stock += quantity
        print(f"{quantity} items added.")

    def remove_stock(self, quantity):
        if quantity > self.__stock:
            print("Cannot remove stock. Insufficient stock available.")
        else:
            self.__stock -= quantity
            print(f"{quantity} items removed.")

    def get_stock(self):
        return self.__stock


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def view_stock(self):
        print("\nInventory Stock:")
        for product in self.products:
            print(f"{product.name}: {product.get_stock()}")



p1 = Product("Laptop", 10)

inventory = Inventory()
inventory.add_product(p1)

inventory.view_stock()

p1.add_stock(5)
p1.remove_stock(8)
p1.remove_stock(20)  

inventory.view_stock()