# Data
categories = ['Electronics', 'Clothing', 'Home Appliances']
revenue = [35000, 28000, 40000]

import matplotlib.pyplot as plt

# Create a bar chart using matplotlib
plt.bar(categories, revenue)

# Customize the chart (optional)
plt.xlabel('Categories')
plt.ylabel('Revenue')
plt.title('Revenue by Category')
plt.grid(True)

# Display the chart

plt.savefig('bar_chart_revenue.png')

plt.show()


