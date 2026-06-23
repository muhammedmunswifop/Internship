"""2.Write a function to find the largest of three numbers."""
def largest():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    c = float(input("Enter the third number: "))
    if a >= b and a >= c:
        print("The largest number is:", a)
    elif b >= a and b >= c:
        print("The largest number is:", b)
    else:
        print("The largest number is:", c)

largest()