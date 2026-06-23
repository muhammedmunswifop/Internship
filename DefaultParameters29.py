"""29.Write a function that prints user profile details using **kwargs.
"""
def user_profile(**kwargs):
    print("User Profile Details:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

user_profile(
    name="Muhammed Munswif",
    age=19,
    course="B.Tech CSE",
    college="CUSAT"
)