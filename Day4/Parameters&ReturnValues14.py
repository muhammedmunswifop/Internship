"""14.Write a function that accepts a student's marks in 5 subjects and returns the total and average."""
def calculate_marks():
    marks = []
    
    for i in range(5):
        mark = float(input(f"Enter mark for subject {i+1}: "))
        marks.append(mark)
    
    total = sum(marks)
    average = total / 5
    
    return total, average

total, average = calculate_marks()

print("Total Marks:", total)
print("Average Marks:", average)
