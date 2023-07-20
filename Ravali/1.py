class Employee:
    def __init__(self, emp_id, emp_name, emp_salary):
        self.emp_id = emp_id
        self.emp_salary = emp_salary

    def employee_info(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Salary: ${self.emp_salary:.2f}")


employee1 = Employee(101, 50000.50)
employee1.employee_info()






