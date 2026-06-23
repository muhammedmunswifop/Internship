"""30.Write a function that accepts multiple marks using *args and returns the highest mark.  """

def highest_mark(*marks):
    return max(marks)

result = highest_mark(78, 85, 92, 67, 88)
print("Highest Mark:", result)