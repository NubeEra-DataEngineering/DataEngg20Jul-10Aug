#1. Loading Library
import pandas as pd

#2.Load Data into DataFrame
dfEmployee = pd.read_csv("data.csv")

#3. Display DataFrame
print(dfEmployee)

#4. Writing into CSV file
dfEmployee.to_csv("proceed_data.csv")
