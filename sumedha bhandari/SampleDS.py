import matplotlib.pyplot as plt
categories = ['Electronics', 'Clothing', 'Home Appliances']
revenue = [35000, 28000, 40000]
plt.bar(categories, revenue, color = 'black', width = 0.5)
plt.xlabel("categories")
plt.ylabel("revenue")
plt.title("products and revenues")
plt.savefig("barchrt.png")

