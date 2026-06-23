"""3.Write a program to check if a person is eligible for a loan:
  Age ≥ 21 and salary ≥ 25,000."""
age = int(input("Enter your age: "))
salary = float(input("Enter your salary: "))   
if age >= 21:
    if salary >= 25000:
        print("You are eligible for a loan.")
    else:
        print("You are not eligible for a loan due to insufficient salary.")