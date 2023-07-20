class Employee:
	def __init__(self, salary):
		self.salary = salary
	def __del__(self):
		del self.salary

e = Employee(2000)
print(e.salary)
