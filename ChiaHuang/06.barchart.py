import matplotlib.pyplot as plt

# Data
categories = ['Electronics', 'Clothing', 'Home Appliances']
revenue = [35000, 28000, 40000]

plt.bar(categories, revenue)

plt.xlabel('Categories')
plt.ylabel('Revenue')
plt.title('Bar Chart')

plt.show()