class Employee:
    def __init__(self):
        print('Initializing employee')
        self.salary = 0
    
    def __del__(self):
        print('Destroying employee')

    def add_salary(self,val):
        self.salary += val
    
    def red_salary(self,val):
        self.salary -= val
    
if __name__ == '__main__':
    emp = Employee()
    print(emp.salary)
    emp.add_salary(50)
    print(emp.salary)
    emp.red_salary(25)
    print(emp.salary)
    del emp
    
    