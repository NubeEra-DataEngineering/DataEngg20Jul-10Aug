# Data
import matplotlib.pyplot as plt

categories = ['Electronics', 'Clothing', 'Home Appliances']
revenue = [35000, 28000, 40000]

plt.xlabel("Categories")
plt.ylabel("Revenue")
plt.bar(categories, revenue)
plt.savefig('ganesh-vankayala/06.Visualization_BarChart/sample.png')