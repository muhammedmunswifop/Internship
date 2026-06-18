"""36.Create a Student class with name and age attributes. Create two objects and display their details."""
# Create a Student class
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


student1 = Student("Rahul", 20)
student2 = Student("Anjali", 19)


print("Student 1 Details:")
student1.display()

print("\nStudent 2 Details:")
student2.display()