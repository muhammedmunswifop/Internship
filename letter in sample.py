"""Check whether a character (Sample: "p") exists in a string (Sample: "python").
"""
a= input("Enter a string: ")
letter = input("Enter a character to check: ")
if letter in a:
    print(letter,"is in the string.")
else:
    print(letter,"is not in the string.")