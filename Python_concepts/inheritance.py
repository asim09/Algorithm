class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def show_details(self):
        super().show_details()
        print(f"Department: {self.department}")

class Developer(Employee):
    def __init__(self, name, salary, programming_lang):
        super().__init__(name, salary)
        self.programming_lang = programming_lang

    def show_details(self):
        super().show_details()
        print(f"Programming Language: {self.programming_lang}")

# Usage
m1 = Manager("Alice", 90000, "Sales")
d1 = Developer("Bob", 80000, "Python")

m1.show_details()
# Name: Alice, Salary: 90000
# Department: Sales

d1.show_details()
# Name: Bob, Salary: 80000
# Programming Language: Python
