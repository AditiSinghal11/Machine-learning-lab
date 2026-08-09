# AI-assisted code generated using ChatGPT
# Experiment: Compare custom Minkowski distance with SciPy

import pandas as pd
import numpy as np
from scipy.spatial.distance import minkowski

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

p = 2

my_distance = minkowski_distance(vector1, vector2, p)
package_distance = minkowski(vector1, vector2, p)

print("My Function :", my_distance)
print("Scipy Function :", package_distance)
print("Results Match :", np.isclose(my_distance, package_distance))
