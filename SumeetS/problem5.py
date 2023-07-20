import pandas as pd
from matplotlib import pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [10000, 12000, 9000, 15000, 18000, 14000]

plt.plot(months, sales)

plt.savefig('SumeetS/sample.png')