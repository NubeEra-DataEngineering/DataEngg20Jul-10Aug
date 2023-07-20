import matplotlib.pyplot as plt

# Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [10000, 12000, 9000, 15000, 18000, 14000]
plt.xlabel("Months")
plt.ylabel("Sales")

plt.plot(months,sales, linestyle = 'dotted')
plt.savefig('ganesh-vankayala/05.Visualization/sample.png')