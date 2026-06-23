"""26.Write a function using **kwargs to display student information."""

def display_student_info(**kwargs):
    print("Student Information:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_student_info(
    name="Muhammed Munswif",
    age=19,
    course="B.Tech CSE",
    college="CUSAT"
)