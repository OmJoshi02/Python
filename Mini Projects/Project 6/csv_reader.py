#Create a Python script that can read data from a CSV file and write it to an Excel file (and vice versa).

import pandas as pd

df = pd.read_csv("data.csv")
print(df)

#Writing data to excel
df.to_excel("exceldata.xlsx", index=False)

excel_data = pd.read_excel("exceldata.xlsx")
print("Excel data")