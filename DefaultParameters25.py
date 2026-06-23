"""25.Write a function using **kwargs to display employee information."""

def display_employee(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_employee(
    name="Munswif",
    age=20,
    department="CSE",
    salary=50000
)