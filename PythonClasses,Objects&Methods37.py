"""37.Create a Car class with brand, model, and year attributes. Create three objects and display their information."""

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)


car1 = Car("Toyota", "Corolla", 2022)
car2 = Car("Honda", "City", 2021)
car3 = Car("Hyundai", "i20", 2023)


print("Car 1 Details:")
car1.display()

print("\nCar 2 Details:")
car2.display()

print("\nCar 3 Details:")
car3.display()