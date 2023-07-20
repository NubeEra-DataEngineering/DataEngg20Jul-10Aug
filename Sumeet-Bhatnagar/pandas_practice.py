import pandas as pd

df = pd.read_csv('Packages_pandas/data.csv')

# print(df)

df.to_csv('./tmp123.csv')