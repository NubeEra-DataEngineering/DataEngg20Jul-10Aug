#1. Loading Library
import pandas as pd

#2.Load Data into DataFrame
dfEmployee = pd.read_csv("data.csv")

dfEmployee.to_csv("proceed_data.csv")
dfEmployee_filtered = dfEmployee[dfEmployee['Age'] > 100]
print(dfEmployee_filtered[['Name', 'Age','City']])