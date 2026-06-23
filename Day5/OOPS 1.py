"""1. School Student Management System"""
class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def display_details(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grade:", self.grade)

    def update_grade(self, new_grade):
        self.grade = new_grade
        print("Grade updated successfully!")

student1 = Student(101, "Rahul", 15, "A")

student1.display_details()

student1.update_grade("A+")

print("\nAfter Grade Update:")
student1.display_details()