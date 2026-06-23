"""3.Write a function to check whether a number is even or odd."""
def even_odd():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(num, "is an even number.")
    else:
        print(num, "is an odd number.")

even_odd()