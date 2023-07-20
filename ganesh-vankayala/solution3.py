import pandas as pd

df = pd.read_csv('ganesh-vankayala/data.csv')

print(df)

df.to_csv('ganesh-vankayala/output.csv')

