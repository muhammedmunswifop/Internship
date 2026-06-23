"""5.Write a program to calculate the factorial of a number using a for loop."""
n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
    factorial= factorial * i
print("The factorial of", n, "is:", factorial)