# import library
import pandas as pd
# Load data into dataframe
dfemployee=pd.read_csv("data.csv")
# Display dataframe
print(dfemployee)
# Writing into csv file
dfemployee.to_csv("proceed_data.csv")