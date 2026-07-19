import pandas as pd

data = pd.read_excel(
    "C:/Users/91971/Downloads/Lab Session Data.xlsx",
    sheet_name="thyroid0387_UCI"
)

print("Data Types")
print(data.dtypes)

print("\nMissing Values")
print(data.isnull().sum())

print("\nNumeric Summary")
print(data.describe())

print("\nMean")
print(data.mean(numeric_only=True))

print("\nVariance")
print(data.var(numeric_only=True))

print("\nMinimum Values")
print(data.min(numeric_only=True))

print("\nMaximum Values")
print(data.max(numeric_only=True))

print("\nCategorical Columns")

for col in data.columns:
    if data[col].dtype == "object":
        print(col)