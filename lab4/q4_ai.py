# AI-assisted code generated using ChatGPT
# Experiment: Minkowski Distance

import pandas as pd
import numpy as np

df = pd.read_excel("Lab Session Data_final.xlsx", sheet_name="marketing_campaign")


def minkowski_distance(vector1, vector2, p):
    # AI-assisted implementation using NumPy vectorization
    vector1 = np.asarray(vector1)
    vector2 = np.asarray(vector2)

    return np.sum(
        np.abs(vector1 - vector2) ** p
    ) ** (1 / p)


numeric_df = df.select_dtypes(include=["int64", "float64"])

vector1 = numeric_df.iloc[0].to_numpy()
vector2 = numeric_df.iloc[1].to_numpy()

manhattan = minkowski_distance(vector1, vector2, 1)
euclidean = minkowski_distance(vector1, vector2, 2)

print("Manhattan Distance :", manhattan)
print("Euclidean Distance :", euclidean)
