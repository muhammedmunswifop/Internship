"""10.Write a program to check whether a given day number (1-7) corresponds to a weekday or weekend."""
day = int(input("Enter a day number (1-7): "))
if day >= 1 and day <= 5:
    print("It's a weekday.")
else:
    print("It's a weekend.")