"""24.Write a function using *args to find the largest value."""

def find_largest(*args):
    return max(args)

print("Largest value =", find_largest(10, 25, 5, 40, 15))
print("Largest value =", find_largest(100, 250, 75))