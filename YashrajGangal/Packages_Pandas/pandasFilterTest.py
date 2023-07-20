import pandas

dfEmployees = pandas.read_csv("data.csv")

dfEmployees = dfEmployees[dfEmployees["Age"] > 100]

dfEmployees = dfEmployees[["Name", "Age", "City"]]

dfEmployees.to_csv("filteredData.csv", index=False)