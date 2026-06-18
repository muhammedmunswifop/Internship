"""9.Write a function to reverse a string"""
def reverse_string():
    string = input("Enter a string: ")
    reversed_string = string[::-1]
    print("The reversed string is:", reversed_string)

reverse_string()