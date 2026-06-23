"""3.Write a program to print the multiplication table of a given number."""
number = int(input("Enter a number: "))
for i in range(1, 11):
    a= number * i
    print(number, "x", i, "=", a)
