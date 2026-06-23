"""4.Write a program to calculate the sum of numbers from 1 to N."""
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n + 1):
    sum=sum+i
print("The sum of numbers from 1 to", n, "is:", sum)