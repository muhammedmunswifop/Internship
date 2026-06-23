"""21.Write a function with a default parameter to calculate shipping charges (default charge ₹50)."""

def calculate_shipping(total_amount, shipping_charge=50):
    return total_amount + shipping_charge

amount = float(input("Enter product amount: ₹"))

print("Final Amount (default shipping): ₹", calculate_shipping(amount))