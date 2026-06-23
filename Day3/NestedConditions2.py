"""2.Write a program to check whether a student passed:
  Marks ≥ 40 in all subjects."""
subject1 = int(input("Enter marks for subject 1: "))
subject2 = int(input("Enter marks for subject 2: "))
subject3 = int(input("Enter marks for subject 3: "))
if subject1 >= 40:
    if subject2 >= 40:
        if subject3 >= 40:
            print("The student has passed.")
        else:
            print("The student has failed.")
