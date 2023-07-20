import pandas as pd

df = pd.read_csv('Packages_pandas/proceed_data.csv')

print(df[df['Age'] > 100][['Name', 'Age', 'City']])
