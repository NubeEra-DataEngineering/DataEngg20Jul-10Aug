import matplotlib.pyplot as plt

# Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [10000, 12000, 9000, 15000, 18000, 14000]

plt.plot(months, sales)
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Sales per Month")
plt.savefig("linePlot.png")