"""6.Write a function to find the factorial of a number."""
def factorial():
    num = int(input("Enter a number: "))
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    print("The factorial of", num, "is:", fact)

factorial()