import pandas as pd
import matplotlib.pyplot as plt

s3_data_path = f's3://bkt-taniya-assignment/data.csv'

df = pd.read_csv(s3_data_path)

cities = df['City']
salaries = df['Salary']

# Create a bar plot for City vs. Salary

plt.bar(cities, salaries)
plt.xlabel('City')
plt.ylabel('Salary')
plt.title('Salary by City')
plt.show()