import pandas as pd

df = pd.read_csv('SumeetS/data.csv')

new_df = df[df['Age'] > 100]
new_df = new_df[['Name', 'Age', 'City']]

print(new_df)

new_df.to_csv('SumeetS/filtered_data.csv')
