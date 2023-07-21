import pandas as pd
from matplotlib import pyplot as plt


categories = ['Electronics', 'Clothing', 'Home Appliances']
electronics = [35000, 28000, 40000]

plt.xlabel('Catgories')
plt.ylabel('Sales')
plt.title('Sales from Each Categories')
plt.bar(categories, electronics, color=['blue', 'red', 'green'])



plt.savefig('SumeetS/bar.png')