"""34.Modify a global variable using the global keyword."""
count = 10

def update_count():
    global count   
    count = count + 5

print("Before function call:", count)

update_count()

print("After function call:", count)