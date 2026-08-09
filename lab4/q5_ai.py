# AI-assisted code generated using ChatGPT
# Experiment: Minkowski Distance for p = 1 to 10

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("Lab Session Data_final.xlsx", sheet_name="marketing_campaign")


def minkowski_distance(vector1, vector2, p):
    # AI-assisted implementation using NumPy
    vector1 = np.asarray(vector1)
    vector2 = np.asarray(vector2)

    return np.linalg.norm(vector1 - vector2, ord=p)


numeric_df = df.select_dtypes(include=["int64", "float64"])

vector1 = numeric_df.iloc[0].to_numpy()
vector2 = numeric_df.iloc[1].to_numpy()

p_values = range(1, 11)
distances = [
    minkowski_distance(vector1, vector2, p)
    for p in p_values
]

print("p\tDistance")

for p, distance in zip(p_values, distances):
    print(f"{p}\t{distance}")

plt.plot(list(p_values), distances, marker="o")
plt.xlabel("Value of p")
plt.ylabel("Minkowski Distance")
plt.title("Minkowski Distance for p = 1 to 10")
plt.grid(True)
plt.show()
