"""27.Write a function that accepts both positional and keyword arguments."""

def student_details(name, age, **kwargs):
    print("Name:", name)
    print("Age:", age)

    for key, value in kwargs.items():
        print(f"{key}: {value}")

student_details(
    "Muhammed Munswif", 
    19, 
    course="B.Tech CSE", 
    college="CUSAT"
)