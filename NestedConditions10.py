"""10.Write a program to check whether a number lies between 50 and 100"""
number = int(input("Enter a number: "))
if number > 50:
    if number < 100:
        print("The number lies between 50 and 100.")
else:
    print("The number is not between 50 and 100.")