import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel(
    "C:/Users/91971/Downloads/Lab Session Data.xlsx",
    sheet_name="thyroid0387_UCI"
)

data = data.replace({"t": 1, "f": 0, "M": 1, "F": 0, "?": 0})

for col in data.columns:
    data[col] = pd.factorize(data[col])[0]

sample = data.iloc[:20]

matrix = np.zeros((20, 20))

for i in range(20):
    for j in range(20):
        a = sample.iloc[i].values
        b = sample.iloc[j].values
        matrix[i][j] = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

plt.imshow(matrix)
plt.colorbar()
plt.title("Cosine Similarity Heatmap")
plt.show()