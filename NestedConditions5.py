"""5.Write a program to determine admission eligibility based on:
  Marks ≥ 75
  Attendance ≥ 80%"""
marks = float(input("Enter your marks: "))
attendance = float(input("Enter your attendance percentage: "))
if marks>= 75:
    if attendance >= 80:
        print("You are eligible for admission.")
    else:
        print("You are not eligible for admission due to insufficient attendance.")