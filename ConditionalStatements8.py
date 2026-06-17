"""8.Write a program to check whether a character is a vowel or consonant.
"""
char = input("Enter a character: ").lower()
vowels = 'aeiou'
if char in vowels:
    print(char, "is a vowel.")
else:
    print(char, "is a consonant.")