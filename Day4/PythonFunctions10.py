"""10.Write a function to check whether a string is a palindrome."""
def palindrome():
    str = input("Enter a string: ")
    reversed_str = str[::-1]
    if str == reversed_str:
        print(str, "is a palindrome.")
    else:
        print(str, "is not a palindrome.")

palindrome()