"""17.Write a function that accepts a list of numbers and returns the sum of all elements."""
def sum_of_elements(numbers):
    return sum(numbers)

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Sum of all elements:", sum_of_elements(numbers))