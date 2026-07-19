import pandas as pd

data = pd.read_excel(
    "C:/Users/91971/Downloads/Lab Session Data.xlsx",
    sheet_name="Purchase data"
)

data["Category"] = ""

for i in range(len(data)):
    if data.loc[i, "Payment (Rs)"] > 200:
        data.loc[i, "Category"] = "RICH"
    else:
        data.loc[i, "Category"] = "POOR"

print(data[["Candies (#)", "Mangoes (Kg)", "Milk Packets (#)", "Payment (Rs)", "Category"]])