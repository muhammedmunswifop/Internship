"""35.Create two functions having variables with the same name and observe their scopes."""
def function1():
    value = 10
    print("Function1 value:", value)

def function2():
    value = 20
    print("Function2 value:", value)

function1()
function2()