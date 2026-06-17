"""4.Write a program to find the largest of three numbers."""
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))

if number1 >= number2 and number1 >= number3:
    print("The largest number is:", number1)
elif number2 >= number1 and number2 >= number3:
    print("The largest number is:", number2)
else:
    print("The largest number is:", number3)