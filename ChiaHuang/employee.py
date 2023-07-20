class employee:
    def __init__(self, name, salary, title):
        self.name = name
        self.salary = salary
        self.title = title

def modify_salary(self, new_salary):
    self.salary = new_salary

e1 = employee("abc", 0, "engineer")
print(e1.name + " " + e1.title + " " + str(e1.salary))
