"""8.Write a program to determine the highest score among four students using nested if statements."""
score1 = float(input("Enter the score of student 1: "))
score2 = float(input("Enter the score of student 2: "))
score3 = float(input("Enter the score of student 3: "))
score4 = float(input("Enter the score of student 4: "))
if score1 >= score2:
    if score1 >= score3:
        if score1 >= score4:
            print("The highest score is:", score1)
        else:
            print("The highest score is:", score4)
    else:
        if score3 >= score4:
            print("The highest score is:", score3)
        else:
            print("The highest score is:", score4)
else:
    if score2 >= score3:
        if score2 >= score4:
            print("The highest score is:", score2)
        else:
            print("The highest score is:", score4)
    else:
        if score3 >= score4:
            print("The highest score is:", score3)
        else:
            print("The highest score is:", score4)