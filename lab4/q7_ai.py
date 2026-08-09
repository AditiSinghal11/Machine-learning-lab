# AI-assisted code generated using ChatGPT
# Experiment: Dot Product and Euclidean Norm

import pandas as pd
import numpy as np

df = pd.read_excel("Lab Session Data_final.xlsx", sheet_name="marketing_campaign")


def dot_product(vector1, vector2):
    # AI-assisted implementation using NumPy
    return np.dot(vector1, vector2)


def euclidean_norm(vector):
    # AI-assisted implementation using NumPy
    return np.linalg.norm(vector)


numeric_df = df.select_dtypes(include=["int64", "float64"])

vector1 = numeric_df.iloc[0].to_numpy()
vector2 = numeric_df.iloc[1].to_numpy()

my_dot = dot_product(vector1, vector2)

my_norm1 = euclidean_norm(vector1)
my_norm2 = euclidean_norm(vector2)

print("Dot Product :", my_dot)

print("\nEuclidean Norm (Vector1) :", my_norm1)
print("Euclidean Norm (Vector2) :", my_norm2)
