import pandas as pd
import numpy as np

data = pd.read_excel(
    "C:/Users/91971/Downloads/Lab Session Data.xlsx",
    sheet_name="thyroid0387_UCI"
)

data = data.replace({"t": 1, "f": 0, "M": 1, "F": 0, "?": 0})

for col in data.columns:
    data[col] = pd.factorize(data[col])[0]

v1 = data.iloc[0].values
v2 = data.iloc[1].values

cosine = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

print("Cosine Similarity =", cosine)