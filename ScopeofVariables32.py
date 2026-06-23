"""32.Create a local variable and demonstrate that it cannot be accessed outside the function."""
def show_age():
    age = 20 
    print("Age inside function:", age)

show_age()
print(age) #show error