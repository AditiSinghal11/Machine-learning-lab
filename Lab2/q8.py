import pandas as pd

data = pd.read_excel(
    "C:/Users/91971/Downloads/Lab Session Data.xlsx",
    sheet_name="thyroid0387_UCI"
)

data = data.replace("?", pd.NA)

for col in data.columns:

    if data[col].dtype == "object":
        data[col] = data[col].fillna(data[col].mode()[0])

    else:
        data[col] = data[col].fillna(data[col].median())

print(data.head())