"""7.Write a program to classify a person as:
  Child (<13)
  Teenager (13-19)
  Adult (20-59)
  Senior Citizen (60+)
  """
age = int(input("Enter your age: "))
if age < 13:
    print("You are a Child.")   
if age >= 13:
    if age <= 19:
        print("You are a Teenager.")
if age >= 20:
    if age <= 59:
        print("You are an Adult.")
if age >= 60:
    print("You are a Senior Citizen.")