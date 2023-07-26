# Data
import matplotlib.pyplot as plt
categories = ['Electronics', 'Clothing', 'Home Appliances']
revenue = [35000, 28000, 40000]
plt.bar(categories, revenue, color='skyblue')
plt.xlabel('Categories')
plt.ylabel('Revenue')
plt.title('Revenue by Category')
plt.show()