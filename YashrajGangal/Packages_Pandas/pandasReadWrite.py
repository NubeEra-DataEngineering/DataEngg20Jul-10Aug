import pandas

df = pandas.read_csv("data.csv")

print(df)

df.to_csv("proceed_data.csv")