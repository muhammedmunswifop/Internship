"""19.Write a function that accepts a product price and discount percentage and returns the final amount"""
def final_amount(price, discount_percentage):
    discount = (price * discount_percentage) / 100
    return price - discount

# Example
price = float(input("Enter product price: "))
discount = float(input("Enter discount percentage: "))

print("Final amount:", final_amount(price, discount))