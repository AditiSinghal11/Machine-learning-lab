import pandas as pd

data = pd.read_excel(
    "C:/Users/91971/Downloads/Lab Session Data.xlsx",
    sheet_name="thyroid0387_UCI"
)

numeric = data.select_dtypes(include=["int64", "float64"])

normalized = (numeric - numeric.min()) / (numeric.max() - numeric.min())

print(normalized.head())