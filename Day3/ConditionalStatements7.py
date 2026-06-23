"""7.Write a program to calculate grades based on marks:
  90+ → A
  80-89 → B
  70-79 → C
  Below 70 → D"""

marks = float(input("Enter your marks: "))
if marks >= 90:
    print("Your grade is: A")
elif marks >= 80:
    print("Your grade is: B")
elif marks >= 70:
    print("Your grade is: C")
else:
    print("Your grade is: D")
