import matplotlib.pyplot as plt
categories = ['Electronics', 'Clothing', 'Home Appliances']
revenue = [35000, 28000, 40000]
plt.bar(categories, revenue, color ='maroon',
        width = 0.4)
 
plt.xlabel("Categories")
plt.ylabel("Revenue")
plt.title("Revenue by Categories")
plt.show()