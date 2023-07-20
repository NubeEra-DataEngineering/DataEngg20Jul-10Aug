import pandas as pd

df = pd.read_csv('Packages_pandas/data.csv')

filtered_df = df[df['Age'] > 100]
selected_columns = filtered_df[['Name', 'Age', 'City']]

print(selected_columns)
