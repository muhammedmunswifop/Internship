"""8.Write a function to count the number of vowels in a string."""
def vowel():
    string = input("Enter a string: ")
    char = 'aeiouAEIOU'
    count = 0
    for str in string:
        if str in char:
            count =count + 1
    print("The number of vowels in the string is:", count)

vowel()