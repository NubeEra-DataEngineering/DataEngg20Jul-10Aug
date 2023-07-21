import pandas as pd
from matplotlib import pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [10000, 12000, 9000, 15000, 18000, 14000]

plt.xlabel('Months')
plt.ylabel('Sales')
plt.title('Trends from Last 6 Months')
plt.plot(months, sales)

plt.show()

plt.savefig('sample.png')