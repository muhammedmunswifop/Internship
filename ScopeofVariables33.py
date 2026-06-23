"""33.Demonstrate the difference between local and global variables."""
name = "Munswif"

def show_variables():
    age = 20

    print("Inside function:")
    print("Global variable:", name)
    print("Local variable:", age)

show_variables()

print("\nOutside function:")
print("Global variable:", name)
