class Employee:
    def __init__(self, emp_id,name):
        self.emp_id = emp_id
        self.name=name

    def salary(self,salary):
        self.salary=salary

    def __del__(self):
        print(f"Employee {self.name}  is being removed.")

employee1 = Employee(101, "rohan")
print(employee1.name)