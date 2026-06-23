"""20.Write a function that accepts two numbers and returns both quotient and remainder."""
def quotient_remainder(a, b):
    q = a // b
    r = a % b
    print("Quotient:", q)
    print("Remainder:", r)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
quotient_remainder(num1, num2)

