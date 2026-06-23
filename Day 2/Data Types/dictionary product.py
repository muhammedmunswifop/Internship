"""Create a dictionary of 5 products and their prices (Sample: {"Laptop": 1200,
"Mouse": 25, "Keyboard": 75, "Monitor": 300, "Headphones": 150})
and print the product with the highest price."""
products = {
    "Laptop": 1200,
    "Mouse": 25,
    "Keyboard": 75,
    "Monitor": 300,
    "Headphones": 150,
}
highestprice = max(products, key=products.get)
highestvalue = products[highestprice]
print("Product with the highest price:", highestprice)
print("Price:", highestvalue)