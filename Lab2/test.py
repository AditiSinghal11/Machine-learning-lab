import pandas as pd

file = "C:/Users/91971/Downloads/Lab Session Data.xlsx"

excel = pd.ExcelFile(file)

print(excel.sheet_names)