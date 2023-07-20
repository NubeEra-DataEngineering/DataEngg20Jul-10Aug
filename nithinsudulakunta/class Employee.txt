class Employee:
    def __init__(self, name, designation, basic_salary):
        self.name = name
        self.designation = designation
        self.basic_salary = basic_salary

    def __del__(self):
        print(f"{self.name} has been removed from the employee list.")

    def calculate_salary(self):
        return self.basic_salary

emp1 = Employee("John Doe", "Software Engineer", 50000)
emp2 = Employee("Jane Smith", "Data Analyst", 45000)

print(f"{emp1.name}'s basic salary: {emp1.calculate_salary()}")
print(f"{emp2.name}'s basic salary: {emp2.calculate_salary()}")