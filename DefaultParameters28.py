"""28.Write a function that calculates the average of any number of values using *args."""

def average(*args):
    if len(args) == 0:
        return 0
    return sum(args) / len(args)

print(average(10, 20, 30, 40))  
print(average(5, 15, 25))       