import pandas as pd

df = pd.read_csv('SumeetS/data.csv')

print(df)

df.to_csv('SumeetS/written_data.csv')
