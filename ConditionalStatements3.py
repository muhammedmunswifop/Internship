"""3.Write a program to find the larger of two numbers."""
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

if number1 > number2:
    print("The larger number is:", number1)
elif number2 > number1:
    print("The larger number is:", number2)
else:
    print("Both numbers are equal.")