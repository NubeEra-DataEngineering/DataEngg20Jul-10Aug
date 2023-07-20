import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [10000, 12000, 9000, 15000, 18000, 14000]


ax = plt.plot(months,sales)
plt.xlabel('Months')
plt.ylabel('Sales')
plt.title('Monthly Sales')
plt.show()