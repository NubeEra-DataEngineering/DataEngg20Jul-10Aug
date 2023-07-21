import matplotlib.pyplot as plt

# Data
categories = ['Electronics', 'Clothing', 'Home Appliances']
revenue = [35000, 28000, 40000]

plt.bar(categories, revenue, width=0.2)
plt.xlabel("Categories")
plt.ylabel("Revenues")
plt.savefig("revenuesChart.png")