"""2. Employee Salary Management"""
class Employee :
    def __init__(self,employee_ID, name, salary):
          self.employee_ID=employee_ID
          self.name=name
          self.salary=salary

    def display(self):
         print("employee ID:", self.employee_ID)
         print("Name", self.name)
         print("Salary", self.salary)

    def salary_increment(self,increment):
         self.increment=increment
         self.salary =( self.salary + (self.salary*self.increment/100))
         print("new salary=",self.salary)

employee1 = Employee(100, "Manaf",50000)
employee1.display()
employee1.salary_increment(10)

         

