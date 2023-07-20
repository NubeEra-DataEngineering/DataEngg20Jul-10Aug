import pandas as pd

df = pd.read_csv('Packages_Pandas/data.csv')

df = df[df["Age"] > 100]
df = df[["Name", "Age", "City"]]

print(df)
