#1. Loading Library
import pandas as pd

#2.Load Data into DataFrame
dfEmployee = pd.read_csv("data.csv")

#3. Display DataFrame
print(dfEmployee)

# take this dataset.  filter age >100. select name age city

filtered_df = dfEmployee[dfEmployee['Age'] > 100]

# Select Name, Age, and City columns
result = filtered_df[['Name', 'Age', 'City']]

result.to_csv("nithinsudulakunta/packages_pandas/proceed_data.csv")
