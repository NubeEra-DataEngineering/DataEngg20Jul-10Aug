import pandas as pd 
df=pd.read_csv("data.csv")
df=df[df["Age"] >100]
df1 = df[['Name', 'Age','City']]
df1.to_csv("filtered_data.csv")