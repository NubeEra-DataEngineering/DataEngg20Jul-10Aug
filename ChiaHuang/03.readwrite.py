import pandas as pd

df = pd.read_csv('Packages_Pandas/data.csv')

print(df)

df.to_csv('Packages_Pandas/write_data.csv')
