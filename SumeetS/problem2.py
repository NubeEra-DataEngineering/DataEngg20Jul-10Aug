class Employee:
  def __init__(self, first_name, last_name, title):
    self.first_name = first_name
    self.last_name = last_name
    self.title = title

  def add_salary(self, salary):
    self.salary = salary

  def __del__(self):
    print('Object destroyed')


employee1 = Employee("Sumeet","Sachdev", "Data Engineer")

print(employee1.title)