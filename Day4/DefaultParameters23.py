"""23.Write a function using *args to calculate the sum of any number of values."""

def calculate_sum(*args):
    return sum(args)

print("Sum =", calculate_sum(10, 20, 30))
print("Sum =", calculate_sum(5, 15, 25, 35, 45))