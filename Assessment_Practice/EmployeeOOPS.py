

# Task 2
# Design a Python program using Object-Oriented Programming concepts with the following requirements:
# Create a class Employee with:
# Instance variables:
# name
# employee_id
# basic_salary
# Create a method calculate_salary() that:
# Calculates the total salary by adding:
# basic_salary
# 20% of basic salary as HRA
# 10% of basic salary as bonus
# Returns the total salary
# Create another method display_details() that prints:
# Name: <name>
# Employee ID: <employee_id>
# Total Salary: <total_salary>

class Employee:
    def __init__(self, name, employee_id, basic_salary):
        self.name=name
        self.employee_id=employee_id
        self.basic_salary=basic_salary
    def calculate_salary(self):
        total_salary=self.basic_salary+ .2*self.basic_salary + .1*self.basic_salary
        return total_salary
    def display_details(self):
        print("Name:", self.name)
        print("Employee Id:", self.employee_id)
        print("Total Salary:", self.calculate_salary())
emp1=Employee("John", 101, 1000)
emp1.display_details()