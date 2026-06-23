"""Check whether a user is eligible for voting (age > 18 and citizenship is True)."""
age = int(input("Enter your age: "))
citizenship = input("Are you a citizen? (yes/no): ")
if age > 18 and citizenship== "yes":
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
