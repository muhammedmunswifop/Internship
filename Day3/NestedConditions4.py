"""4.Write a program to check whether a number is positive and even."""
number = int(input("Enter a number: "))
if number > 0:
    if number % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive but not even.")
else:
    print("The number is not positive.")