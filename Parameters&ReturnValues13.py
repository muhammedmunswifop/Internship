"""13.Write a function that accepts a number and returns its multiplication table."""
def multiplication(num):
    for i in range(1, 11):
      a= num * i
      print(num, "x", i, "=", a)

number=int(input("enter the number:"))
multiplication(number)