import pandas as pd

df = pd.read_csv('ganesh-vankayala/data.csv')

df_filtered = df[df["Age"] > 100]
df_filtered = df_filtered[['Name', "Age", "City"]]

df_filtered.to_csv('ganesh-vankayala/output.csv')

