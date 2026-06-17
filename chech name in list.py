"""Check whether a name (Sample: "Alice") exists in a list of students (Sample:
["John", "Alice", "Bob"]).
"""
students = ["John", "Alice", "Bob"]
name = input("Enter a name to check: ")
if name in students:
    print(name,"is in the list of students.")
else:
    print(name ,"is not in the list of students.")
