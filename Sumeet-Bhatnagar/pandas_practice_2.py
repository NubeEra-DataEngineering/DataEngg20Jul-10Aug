import pandas as pd

df = pd.read_csv('Packages_pandas/data.csv')

print(df.loc[df.Age > 100][['Name','Age','City']])
